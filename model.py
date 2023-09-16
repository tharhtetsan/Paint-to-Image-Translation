import tensorflow as tf
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np

class myModel():
    def __init__(self):
        self.OUTPUT_CHANNELS = 3
        self.IMG_WIDTH = 256
        self.IMG_HEIGHT = 256
        self.generator = self.Generator()
        self.discriminator = self.Discriminator()

        self.generator_optimizer =  tf.keras.optimizers.Adam(2e-4,beta_1= 0.5)
        self.discriminator_optimizer = tf.keras.optimizers.Adam(2e-4,beta_1 = 0.5)
        


    def downsample(self, filters,size,apply_batchnorm = True):
        initializer = tf.random_normal_initializer(0.,0.02)
    
        result = tf.keras.Sequential()
    
        result.add(tf.keras.layers.Conv2D(filters,size,strides = 2, padding='same',
                                     kernel_initializer = initializer,use_bias =False))
    
        if apply_batchnorm:
            result.add(tf.keras.layers.BatchNormalization())
        
        result.add(tf.keras.layers.LeakyReLU())
        
        
        return result

    def upsample(self,filters,size,apply_dropout=False):
        initializer = tf.random_normal_initializer(0.,0.02)
        
        result = tf.keras.Sequential()
        
        result.add(tf.keras.layers.Conv2DTranspose(filters, size, strides=2,padding = 'same',
                                                kernel_initializer = initializer, use_bias = False)
                )
        
        if apply_dropout:
            result.add(tf.keras.layers.Dropout(0.5))
        
        result.add(tf.keras.layers.ReLU())
        
        return result


    def Generator(self):
        inputs = tf.keras.layers.Input(shape=[self.IMG_WIDTH,self.IMG_HEIGHT,self.OUTPUT_CHANNELS]) # (bs, 256,256, 3)
        
        down_stack = [
            self.downsample( 64, 4, apply_batchnorm = False), # (bs, 128,128, 64)
            self.downsample(128,4),  # (bs, 64, 64, 128)
            self.downsample(256,4),  # (bs, 32, 32, 256)
            self.downsample(512,4),  # (bs, 16, 16, 512)
            self.downsample(512,4),  # (bs, 8, 8, 512)
            self.downsample(512,4),  # (bs, 4, 4, 512)
            self.downsample(512,4),  # (bs, 2, 2, 512)
            self.downsample(512,4),  # (bs, 1, 1, 512)
        ]
        
        
        up_stack = [
            self.upsample(512,4, apply_dropout = True), # (bs, 2,2, 1024)
            self.upsample(512,4, apply_dropout = True), # (bs, 4,4, 1024)
            self.upsample(512,4, apply_dropout = True), # (bs, 8,8, 1024)
            self.upsample(512,4), # (bs, 16,16, 1024)
            self.upsample(256,4), # (bs, 32, 32, 512)
            self.upsample(128,4), # (bs,64, 64, 256)
            self.upsample(64,4),  # (bs, 128, 128, 128)
        ]
        
        
        initializer = tf.random_normal_initializer(0.,0.02)
        last = tf.keras.layers.Conv2DTranspose(self.OUTPUT_CHANNELS, 4,
                                            strides = 2,
                                            padding = 'same',
                                            kernel_initializer = initializer,
                                            activation = 'tanh') #(bs, 256,256, 3)
        
        x = inputs
        
        
        #Downsampling through the model
        skips = []
        for down in down_stack:
            x = down(x)
            skips.append(x)
            
        skips = reversed(skips[:-1])
        
        #Upsampling and establishing the skip connections
        for up,skip in zip(up_stack,skips):
            x = up(x)
            x = tf.keras.layers.Concatenate()([x,skip])
            
        x = last(x)
        
        return tf.keras.Model(inputs=inputs,outputs= x)



    def Discriminator(self):
        initializer = tf.random_normal_initializer(0., 0.02)
        
        inp = tf.keras.layers.Input(shape = [256,256,3], name = 'input_image')
        tar = tf.keras.layers.Input(shape = [256,256,3], name = 'target_image')
        
        x = tf.keras.layers.concatenate([inp,tar]) # (bs, 256,256, channels*2)
        
        down1 = self.downsample(64,4, False)(x)  # (bs, 128,128,64)
        down2 = self.downsample(128,4)(down1)    # (bs, 64,64, 128)
        down3 = self.downsample(256,4)(down2)    # (bs, 32,32,256)
        
        zero_pad1 = tf.keras.layers.ZeroPadding2D()(down3) # (bs, 34,34, 256)
        
        conv = tf.keras.layers.Conv2D(512, 4, strides = 1,
                                    kernel_initializer = initializer,
                                    use_bias = False)(zero_pad1) #(bs,31,31,512)
        
        batchnorm1 = tf.keras.layers.BatchNormalization()(conv)
        
        leaky_relu = tf.keras.layers.LeakyReLU()(batchnorm1)
        
        zero_pad2 = tf.keras.layers.ZeroPadding2D()(leaky_relu) #(bs, 33,33,512)
        
        
        last = tf.keras.layers.Conv2D(1,4, strides=1,
                                    kernel_initializer = initializer)(zero_pad2)# (bs, 30, 30, 1)
        
        
        return tf.keras.Model(inputs = [inp,tar],outputs= last)


    def loadModel(self,model_path):

        checkpoint = tf.train.Checkpoint(generator_optimizer=self.generator_optimizer,
                                discriminator_optimizer=self.discriminator_optimizer,
                                generator=self.generator,
                                discriminator=self.discriminator)
        latest = tf.train.latest_checkpoint(model_path)
        checkpoint.restore((latest))
        print("[+] Model is successfully loaded [+]")


    def model_predict(self):
        img_path = "captured.png"
        image = tf.io.read_file(img_path)
        image = tf.image.decode_jpeg(image)
        image = tf.cast(image, tf.float32)

        image = tf.image.resize(image, [256,256],
                                        method = tf.image.ResizeMethod.NEAREST_NEIGHBOR)

        image = (image/127.5)-1
        data_input = tf.expand_dims(image,0)
        output = self.generator(data_input, training=True)
        output_image = output[0]* 0.5 + 0.5
        return output_image


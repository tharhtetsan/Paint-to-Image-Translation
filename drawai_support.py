
import sys
from PIL import ImageGrab
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import paint
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
from tkinter import filedialog
import cv2
import PIL
import PIL.Image
from model import myModel
import numpy as np


def init(top, gui, *args, **kwargs):
    global w, top_level, root,model
    w = gui
    top_level = top
    root = top
    model = myModel()
    

def btn_generate():
    paint.btn_saveImage()
    output_image = model.model_predict()
    np_image =  output_image.numpy()*255.0
    cv2.imwrite("output.jpg",np_image)

    cv_image = cv2.imread("output.jpg")
    cv_image = cv2.resize(cv_image, (542,382))
    pil_image = PIL.Image.fromarray(cv_image)
    tk_image = Pil_imageTk.PhotoImage(image=pil_image)
    w.Frame2_img.configure(image=tk_image)
    w.Frame2_img._image_cache = tk_image
    sys.stdout.flush()

def btn_loadmodel():
    model_path = filedialog.askdirectory()
    model_path = model_path.strip()
    #model.generator.summary()
    #model.discriminator.summary()
    model.loadModel(model_path)
    w.txt_modelPath.delete(0, 'end')
    w.txt_modelPath.insert(0,model_path)




def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None





if __name__ == '__main__':
    import drawai
    drawai.vp_start_gui()





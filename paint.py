import sys
import PIL
import PIL.Image
from PIL import ImageGrab
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
from tkinter import filedialog
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import cv2


class pen(object):


    def __init__(self):

        self.old_x = None
        self.old_y = None
        self.eraser_on = False
        self.color =  'black'
        self.background_img = None
        self.line_width =  2.0
        self.frame1_canvas = w.frame1_canvas
        self.frame1_canvas.bind("<Button-1>",self.xy)
        self.frame1_canvas.bind("<B1-Motion>", self.addLine)
        root.bind("<Control-s>", self.save)
    
    def xy(self,event):
        self.old_x, self.old_y = event.x, event.y
    
    def addLine(self,event):
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.frame1_canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle='round', smooth=True, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
    
    def save(self,event):
        x=root.winfo_rootx()+self.frame1_canvas.winfo_x()+10
        y=root.winfo_rooty()+self.frame1_canvas.winfo_y()+66
        
        x1=x+w.frame1_canvas.winfo_width()
        y1=y+w.frame1_canvas.winfo_height()
        im = ImageGrab.grab((x, y, x1, y1))
        im.save("captured.png")


def init(top, gui, *args, **kwargs):
    global w, top_level, root,p
    w = gui
    top_level = top
    root = top
    p = pen()

def btn_16xBrush():
    p.eraser_on = False
    p.line_width = 16.0
    sys.stdout.flush()

def btn_2xBrush():
    p.eraser_on = False
    p.line_width = 2.0
    sys.stdout.flush()

def btn_4xBrush():
    p.eraser_on = False
    p.line_width = 4.0
    sys.stdout.flush()

def btn_8xBrush():
    p.eraser_on = False
    p.line_width = 8.0
    sys.stdout.flush()


def btn_earseON():
    p.eraser_on = True


def btn_obj_road():
    p.color = "#804080"
    sys.stdout.flush()

def btn_obj_platform():
    p.color = "#F423E8"
    sys.stdout.flush()

def btn_obj_tree():
    p.color = "#6B8E23"
    sys.stdout.flush()

def btn_obj_board():
    p.color = "#DCDC00"
    sys.stdout.flush()

def btn_obj_pole():
    p.color = "#999999"
    sys.stdout.flush()

def btn_obj_people():
    p.color = "#DC143C"
    sys.stdout.flush()

def btn_obj_cycle():
    p.color = "#770B21"
    sys.stdout.flush()



def btn_obj_btn_building():
    p.color = "#464646"
    sys.stdout.flush()

def btn_obj_car():
    p.color = "#0000BE"
    sys.stdout.flush()

def btn_obj_steel():
    p.color = "#000000"
    sys.stdout.flush()

def btn_obj_gress():
    p.color = "#98FB98"
    sys.stdout.flush()

def btn_Clear():
    print('drawai_support.btn_Clear')
    p.frame1_canvas.delete('all')
    sys.stdout.flush()

def btn_saveImage():
    x=root.winfo_rootx()+p.frame1_canvas.winfo_x()+10
    y=root.winfo_rooty()+p.frame1_canvas.winfo_y()+66
    
    x1=x+p.frame1_canvas.winfo_width()
    y1=y+p.frame1_canvas.winfo_height()
    im = ImageGrab.grab((x, y, x1, y1))
    im.save("captured.png")

    sys.stdout.flush()


def btn_pickImage():

    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpg files", "*.png"), ("all files", "*.*")))
    filename = filename.strip()

    load_img = cv2.imread(filename)
    cv_image = cv2.cvtColor(load_img, cv2.COLOR_BGR2RGB)
    cv_image = cv2.resize(cv_image, (542,382))
    pil_image = PIL.Image.fromarray(cv_image)
    p.background_img = Pil_imageTk.PhotoImage(image=pil_image)

    w.txt_imagePath.delete(0, 'end')
    w.txt_imagePath.insert(0,filename)
    w.frame1_canvas.create_image(0,0, image=p.background_img, anchor='nw')   
    sys.stdout.flush()





"""
Road 	804080
platform F423E8
Car 	0000BE
Tree 6B8E23
Board DCDC00
Pole 999999
People DC143C
Cycle 770B21
building 464646
other 000000
gress 98FB98
"""
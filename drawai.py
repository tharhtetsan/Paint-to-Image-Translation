
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

import drawai_support,paint



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = copyright_cloudsourceai (root)
    drawai_support.init(root, top)
    root.resizable(False, False)
    paint.init(root, top)
    root.mainloop()

w = None

def destroy_copyright_cloudsourceai():
    global w
    w.destroy()
    w = None

class copyright_cloudsourceai:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1222x700+279+124")
        top.minsize(120, 1)
        top.maxsize(1924, 1041)
        top.resizable(1, 1)
        top.title("copyright@cloudsourceai")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                label="File")
        self.sub_menu.add_command(
                command=paint.btn_saveImage,
                label="Save")
        self.sub_menu.add_command(
                command=paint.btn_Clear,
                label="Clear")
        self.sub_menu1 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                label="Brush Size")
        self.sub_menu1.add_command(
                command=paint.btn_2xBrush,
                label="2x")
        self.sub_menu1.add_command(
                command=paint.btn_4xBrush,
                label="4x")
        self.sub_menu1.add_command(
                command=paint.btn_8xBrush,
                label="8x")
        self.sub_menu1.add_command(
                command=paint.btn_16xBrush,
                label="16x")
        self.sub_menu1.add_command(
                command=paint.btn_earseON,
                label="Eraser")




        self.sub_menu12 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                label="Object")
        self.sub_menu12.add_command(
                command=paint.btn_obj_road,
                label="Road")
        self.sub_menu12.add_command(
                command=paint.btn_obj_platform,
                label="Platform")
        self.sub_menu12.add_command(
                command=paint.btn_obj_car,
                label="Car")
        self.sub_menu12.add_command(
                command=paint.btn_obj_tree,
                label="Tree")
        self.sub_menu12.add_command(
                command=paint.btn_obj_board,
                label="Board")
        self.sub_menu12.add_command(
                command=paint.btn_obj_pole,
                label="Pole")
        self.sub_menu12.add_command(
                command=paint.btn_obj_people,
                label="People")
        self.sub_menu12.add_command(
                command=paint.btn_obj_cycle,
                label="Cycle")
        self.sub_menu12.add_command(
                command=paint.btn_obj_btn_building,
                label="Building")
        self.sub_menu12.add_command(
                command=paint.btn_obj_steel,
                label="Steel")
        self.sub_menu12.add_command(
                command=paint.btn_obj_gress,
                label="Gress")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.008, rely=0.097, relheight=0.556, relwidth=0.45)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.frame1_canvas = tk.Canvas(self.Frame1,bg='white')#
        self.frame1_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)
        
        #self.frame1_canvas.pack()
        #self.frame1_canvas.pack(fill='both')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.532, rely=0.097, relheight=0.556, relwidth=0.45)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Frame2_img = ttk.Label(self.Frame2)
        self.Frame2_img.place(relx=0, rely=0, relheight=1, relwidth=1)



        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.818, rely=0.944, height=20, width=200)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''copyright@cloudsourceai''')

        self.txt_imagePath = tk.Entry(top)
        self.txt_imagePath.place(relx=0.008, rely=0.709, height=30
                , relwidth=0.347)
        self.txt_imagePath.configure(background="white")
        self.txt_imagePath.configure(disabledforeground="#a3a3a3")
        self.txt_imagePath.configure(font="TkFixedFont")
        self.txt_imagePath.configure(foreground="#000000")
        self.txt_imagePath.configure(highlightbackground="#d9d9d9")
        self.txt_imagePath.configure(highlightcolor="black")
        self.txt_imagePath.configure(insertbackground="black")
        self.txt_imagePath.configure(selectbackground="blue")
        self.txt_imagePath.configure(selectforeground="white")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.36, rely=0.709, height=34, width=117)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#808080")
        self.Button1.configure(command=paint.btn_pickImage)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family Bahnschrift -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Pick Image''')

        self.txt_modelPath = tk.Entry(top)
        self.txt_modelPath.place(relx=0.008, rely=0.791, height=30
                , relwidth=0.347)
        self.txt_modelPath.configure(background="white")
        self.txt_modelPath.configure(disabledforeground="#a3a3a3")
        self.txt_modelPath.configure(font="TkFixedFont")
        self.txt_modelPath.configure(foreground="#000000")
        self.txt_modelPath.configure(highlightbackground="#d9d9d9")
        self.txt_modelPath.configure(highlightcolor="black")
        self.txt_modelPath.configure(insertbackground="black")
        self.txt_modelPath.configure(selectbackground="blue")
        self.txt_modelPath.configure(selectforeground="white")

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.466, rely=0.361, height=64, width=57)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#b90746")
        self.Button3.configure(background="#808080")
        self.Button3.configure(command=drawai_support.btn_generate)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family Arial -size 23 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''>''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.229, rely=0.0, height=50, width=611)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI Historic} -size 20 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Drawing to Image Translation AI''')

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.359, rely=0.791, height=34, width=117)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#808080")
        self.Button1_1.configure(command=drawai_support.btn_loadmodel)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family Bahnschrift -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Load Model''')

if __name__ == '__main__':
    vp_start_gui()






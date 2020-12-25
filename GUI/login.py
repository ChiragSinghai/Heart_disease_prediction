from tkinter import *
import tkinter
from PIL import ImageTk,Image
class login():
    def __init__(self,master):
        self.master=master
        self.image_path="heart1.jpg"
        self.bg_image=ImageTk.PhotoImage(file=self.image_path)
        self.window_configuration()
    def window_configuration(self):
        self.master.title("Doctor strange")
        self.master_label=Label(image=self.bg_image)
        self.master_label.pack(fill=BOTH,expand=True)
        self.master.bind('<Configure>',self.resizer)
        self.master.geometry("400x400+0+0")
    def resizer(self,event):
        height=event.height
        width=event.width
        self.bg_image=Image.open(self.image_path)
        self.resized_bg = self.bg_image.resize((width, height), Image.ANTIALIAS)
        self.new_bg = ImageTk.PhotoImage(self.resized_bg)
        self.master_label['image']=self.new_bg


root=Tk()
obj=login(root)






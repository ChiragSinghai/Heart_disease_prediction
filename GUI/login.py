from tkinter import *
import tkinter
from PIL import ImageTk,Image
class login():
    def __init__(self,master):
        self.master=master
        self.image_path="heart7.jpg"
        self.bg_image=ImageTk.PhotoImage(file=self.image_path)
        self.window_configuration()
        self.design()
    def window_configuration(self):
        self.master.title("Doctor strange")
        self.master_label=Label(image=self.bg_image)
        self.master_label.pack(fill=BOTH,expand=True)
        self.master_label.bind('<Configure>',self.resizer)
        self.master.geometry("600x600+0+0")
    def resizer(self,event):
        height=event.height
        width=event.width
        self.bg_image=Image.open(self.image_path)
        self.resized_bg = self.bg_image.resize((width, height), Image.ANTIALIAS)
        self.new_bg = ImageTk.PhotoImage(self.resized_bg)
        self.master_label['image']=self.new_bg

    def design(self):
        #b1d1f7
        self.frame=Frame(self.master,bg='#b1d1f7')
        self.frame.place(relx=0.42,rely=0.2,relwidth=0.4,relheight=0.6)
        self.sign_in_frame=Frame(self.frame,bg='#b1d1f7')
        self.sign_in_frame.place(relx=0.3,rely=0.2,relwidth=0.4,relheight=0.15)
        self.sign_in_button=Button(self.sign_in_frame,text=' Sign-in ',command=self.sign_in,font=("times new roman",16,"bold"))
        self.sign_in_button.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
        self.sign_up_frame=Frame(self.frame,bg='#b1d1f7')
        self.sign_up_frame.place(relx=0.3,rely=0.65,relwidth=0.4,relheight=0.15)
        self.sign_up_button=Button(self.sign_up_frame,text=' Sign-up ',font=("times new roman",16,"bold"))
        self.sign_up_button.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9)
        self.sign_in_button.bind('<Enter>',self.animate)
        self.sign_in_button.bind('<Leave>',self.animate)
        self.sign_up_button.bind('<Enter>',self.animate)
        self.sign_up_button.bind('<Leave>',self.animate)

    def animate(self,event):
        parent=event.widget
        frameParentName = parent.winfo_parent()
        frameParent = parent._nametowidget(frameParentName)
        if str(event.type)=='Enter':
            frameParent.config(bg='white')
            parent.config(bg='#b1d1f7')
        else:
            frameParent.config(bg='#b1d1f7')
            parent.config(bg='white')
    def del_frame(self):
        self.frame.destroy()
    def sign_in(self):
        self.del_frame()
        
    def sign_up(self):
        pass
        

root=Tk()
obj=login(root)






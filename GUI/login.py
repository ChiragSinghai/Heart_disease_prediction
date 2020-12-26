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
        
        
        self.sign_in_button=Button(self.frame,text=' Sign-in ',font=("times new roman",20,"bold"))
        self.sign_in_button.place(relx=0.3,rely=0.2,relwidth=0.4,relheight=0.15)
        self.sign_up_button=Button(self.frame,text=' Sign-up ',font=("times new roman",20,"bold"))
        self.sign_up_button.place(relx=0.3,rely=0.65,relwidth=0.4,relheight=0.15)
        #self.username_label=Label(self.master,text='Username',bg='black',fg='white')
        #self.username_label.place(relx=0.42,rely=0.2,relwidth=0.1,relheight=0.05)
        self.sign_in_button.bind('<Enter>',self.animate)
    def animate(self,event):
        event.widget.pack(pady=5)
        event.widget.config(bg='red')
    


root=Tk()
obj=login(root)






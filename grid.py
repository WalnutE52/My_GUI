
from cProfile import label
from email.mime import image
import random
from tkinter import *
from tkinter import messagebox
from turtle import width

from setuptools import Command

class Application(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        #Using grid to achieve the login interface
        self.label01 = Label(self, text="Username")
        self.label01.grid(row = 0, column=0)
        v1 = StringVar()
        self.entry01 = Entry(self,textvariable=v1)
        self.entry01.grid(row=0,column=1)
        Label(self,text="Username is your mobile number").grid(row=0,column=2)
        Label(self,text="Password").grid(row=1,column=0)
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2,show="*")
        self.entry02.grid(row=1,column=1)
        Button(self,text="Login", command = self.login).grid(row=2,column=1,sticky="EW")
        Button(self,text="Exit", command = root.destroy).grid(row=2,column=2,sticky="W")    
        
    def login(self):
        if self.entry01.get() == "123456789" and self.entry02.get() == "12345":
            messagebox.showinfo("Walnuts", "Login successfully!")
        else:
            messagebox.showinfo("Walnut", "Wrong username or password")
        
if __name__  == '__main__':
    root = Tk()
    root.geometry("800x800+200+300")
    root.title("Canvas")
    app = Application(master=root)
    root.mainloop()


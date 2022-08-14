from cProfile import label
from curses import window
from tkinter import *
from tkinter import messagebox
from turtle import back, title
import webbrowser

from setuptools import Command

class Application(Frame):
    """a classic GUI programm"""
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
       #RatioButton; Checkbutton
       self.v = StringVar()
       self.v.set("F")
       
       self.r1 = Radiobutton(self,text = "Female", value = "F", variable=self.v)
       self.r2 = Radiobutton(self,text = "Male", value = "M", variable=self.v)
       self.r1.pack(side = "left")
       self.r2.pack(side="left")
       
       Button(self, text = "Comfirm", command=self.comfirm).pack(side="left")
       
    def comfirm(self):
        messagebox.showinfo("Test", "The Gender is: "+self.v.get())
    
        
        
        
        
        
if __name__ == '__main__':
    
    root = Tk()
    root.geometry("800x800+200+300")
    root.title("A classic GUI program")
    app = Application(master = root)

    root.mainloop()




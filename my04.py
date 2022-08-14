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
       self.w1 = Text(root, width=40,height=12,bg = "grey")
       self.w1.pack()
       self.w1.insert(1.0,"0123456789\nabcdefghijklmn")
       self.w1.insert(2.3, "Life is a box of chocolate")
       
       Button(self, text = "Repeat Insert Text", command = self.insertText).pack(side="left")
       Button(self, text = "Return Text", command=self.returnText).pack(side="left")
       Button(self, text = "Add Image", command=self.addImage).pack(side="left")
       Button(self, text = "Add Widget", command=self.addWidget).pack(side="left")
       Button(self, text = "Tag Control Text", command=self.testTag).pack(side="left")
       
    def insertText(self):
        #INSERT means insert text at the mouse position
        self.w1.insert(INSERT, "eason")
        #END means insert text at the end position
        self.w1.insert(END, '\nend')
        
    def returnText(self):
        print(self.w1.get(1.2,1.6))
        self.w1.insert(1.8,"eason")
        print("All content: \n"+self.w1.get(1.0,END))
    
    def addImage(self):
        #global photo    # set photo to global variable, if it is local variable, photo object will be destroyed, the window cannot display the image
        self.photo = PhotoImage(file = "test.gif")
        self.w1.image_create(END, image=self.photo) 
    
    def addWidget(self):
        b1 = Button(self.w1,text = "Walnut")
        self.w1.window_create(INSERT, window = b1)
    def testTag(self):
        self.w1.delete(1.0,END)
        self.w1.insert(INSERT, "GOOD GOOD study! Day Day up\n Walnut forever!!!!!\njasoidfoasdoadjaoik\nGoogle")
        self.w1.tag_add("tagName",1.0,1.9)
        self.w1.tag_config("tagName", background="blue",foreground="white")
        
        self.w1.tag_add("google",4.0,4.6)
        self.w1.tag_config("google", foreground="green",underline=True)
        self.w1.tag_bind("google","<Button-1>", self.webshow)
        
    def webshow(self,event):
        webbrowser.open("https://www.google.com/")
        
        
        
        
        
if __name__ == '__main__':
    
    root = Tk()
    root.geometry("800x800+200+300")
    root.title("A classic GUI program")
    app = Application(master = root)

    root.mainloop()




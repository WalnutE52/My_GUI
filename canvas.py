from cProfile import label
from curses import window
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
        #generate canvas
        self.canvas = Canvas(self, width=600, height=600, bg = "red")
        self.canvas.pack()
        # draw lines
        line = self.canvas.create_line(10,10,20,20,45,60)
        #draw rectangle
        rect = self.canvas.create_rectangle(60,60, 100,100)
        ##draw circle
        oval = self.canvas.create_oval(60,60,100,100)
        
        global photo
        photo = PhotoImage(file = "test.gif")
        self.canvas.create_image(100,200,image = photo)
        
        Button(self, text = "Draw Random 10 Graphs", command=self.tenGraph).pack()
    def tenGraph(self):
        for i in range(10):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["height"])/2)
            x2 = x1 + random.randrange(int(self.canvas["width"])/2)
            y2 = x2 + random.randrange(int(self.canvas["height"])/2)
            self.canvas.create_rectangle(x1,y1,x2,y2)
            
        
if __name__  == '__main__':
    root = Tk()
    root.geometry("800x800+200+300")
    root.title("Canvas")
    app = Application(master=root)
    root.mainloop()


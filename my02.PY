from cProfile import label
from time import sleep
from tkinter import *
from tkinter import messagebox
from turtle import title

class Application(Frame):
    """a classic GUI programm"""
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        # Button 
        self.btn01 = Button(self)
        self.btn01["text"] = "click to send a flower"
        self.btn01.pack()
        self.btn01["command"] = self.GiveFlower
        
        self.btnQuit = Button(self, text = "exit", command = root.destroy)
        self.btnQuit.pack()
        
        #Label
        self.label01 = Label(self, text="Walnuts", width = 10, height = 2,
                             bg = "black", fg = "white")
        self.label01.pack()
        self.label02 = Label(self, text="Eason", width = 10, height = 2,
                             bg = "black", fg = "white", font = ("Arial",30))
        self.label02.pack()
        
        # image
        global photo    # set photo to global variable, if it is local variable, photo object will be destroyed, the window cannot display the image
        photo = PhotoImage(file = "test.gif")
        self.label03 = Label(self, image = photo)
        self.label03.pack()
        
        self.label04 = Label(self,text = "Test\nfor\multiple lines ", borderwidth=1, relief="solid",justify="right")
        self.label04.pack()
    def GiveFlower(self):
        messagebox.showinfo("giveflower", "Give u 99 flowers")

if __name__ == '__main__':
    
    root = Tk()
    root.geometry("800x800+200+300")
    root.title("A classic GUI program")
    app = Application(master = root)

    root.mainloop()




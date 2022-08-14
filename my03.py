from cProfile import label
from tkinter import *
from tkinter import messagebox
from turtle import title

from setuptools import Command

class Application(Frame):
    """a classic GUI programm"""
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
       """Create login component"""
       #user name label
       self.label01 = Label(self, text = "Username")
       self.label01.pack()
       self.label01.setvar("admin")
       
       #Combnine the StringVar with the specific component
       #The content of component change with the change of the content of StringVar
       v1 = StringVar()
       self.entry01 = Entry(self,textvariable=v1)
       self.entry01.pack()
       
       self.label02 = Label(self, text = "Password")
       self.label02.pack()
       
       #Combnine the StringVar with the specific component
       #The content of component change with the change of the content of StringVar
       v2 = StringVar()
       self.entry02 = Entry(self,textvariable=v2,show = "*")
       self.entry02.pack()

    
       self.botton = Button(root, text="Login",command = self.login)
       self.botton.pack()
        
   
        
  
    def login(self):
        #It should search in the database in fact
        #simple test
        username = self.entry01.get()
        pwd = self.entry02.get()
        print("Go compare with the database")
        print("Username: "+ username)
        print("Password: "+pwd )
        if username == "eason" and pwd == "555":
            
            messagebox.showinfo("Walnuts", "Login successfully! Welcome to Study!")
        else:
            messagebox.showinfo("Walnuts", "Login Failed! Wrong Username or Passwprd")
          

if __name__ == '__main__':
    
    root = Tk()
    root.geometry("800x800+200+300")
    root.title("A classic GUI program")
    app = Application(master = root)

    root.mainloop()




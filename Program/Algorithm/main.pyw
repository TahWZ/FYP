import sys
from tkinter import *
from interface.home import Home
from interface.about import About
from interface.report import Report
from interface.instructions import Instruction
import interface.login
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

#====================( Main )====================
class Main:
    #====================( Functions )====================
    def __init__(self, root):
        #================( Root Reference )================
        self.root = root
        self.photo = ImageTk.PhotoImage(Image.open(os.getcwd()+'/images/logo.png'))
        #====================( Frames )====================
        self.frame_main = Frame(root)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        self.get_tabs()
        #====================( Widgets )====================
        #Label
        button_logout = Button(self.frame_main, text="Logout", width = 10,command=lambda: self.logout())
        lab_1 = Label(self.frame_main, image = self.photo, width = 150, height = 150)
        
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Row 0
        lab_1.pack()
        #Row 1
        self.tabControl.pack()
        self.frame_main.pack()
        #End
        button_logout.pack()
        
    def get_tabs(self):
        #Tab 1
        tab = ttk.Frame(self.tabControl)
        self.tabControl.add(tab, text='Main algorithm')
        frame = Frame(tab)
        Home(frame)
        frame.pack()
        #Tab 2
        tab = ttk.Frame(self.tabControl)
        self.tabControl.add(tab, text='Reports')
        frame = Frame(tab)
        Report(frame)
        frame.pack()
        #Tab 3
        tab = ttk.Frame(self.tabControl)
        self.tabControl.add(tab, text='About us')
        frame = Frame(tab)
        About(frame)
        frame.pack(expand=True)
        #Tab 4
        tab = ttk.Frame(self.tabControl)
        self.tabControl.add(tab, text='Instructions')
        frame = Frame(tab)
        Instruction(frame)
        frame.pack(expand=True)
    
    def logout(self):
        msgBox = messagebox.askquestion('Logout','Are you sure you want to Logout?',icon = 'warning')
        if msgBox == 'yes':
            self.frame_main.destroy()
            interface.login.Login(self.root)

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    root.resizable(False,False)
    main_root = interface.login.Login(root)
    root.title('Prediction software')
    root.mainloop()
    
    


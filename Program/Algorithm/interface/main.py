import sys
from tkinter import *
# sys.path.append('interface')
import login
from home import Home
from about import About
from report import Report
from tkinter import ttk
#from PIL import ImageTK, Image

#====================( Main )====================
class Main:
    #====================( Functions )====================
    def __init__(self, root):
        self.pred = 0
        self.train = 0
        #================( Root Reference )================
        self.root = root
        #====================( Frames )====================
        self.frame_main = Frame(root)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        self.get_tabs()
        #====================( Widgets )====================
        #Label
        button_logout = Button(self.frame_main, text="Logout", width = 10,command=lambda: self.logout())
        lab_1 = Label(self.frame_main, text="Logo", bg = "black", fg = "white", width = 80, height = 10)
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Row 0
        lab_1.pack(fill=BOTH)
        #Row 1
        button_logout.pack()
        #End
        self.tabControl.pack()
        self.frame_main.pack()
        
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

    def get_results(self):
        tab = ttk.Frame(self.tabControl)
        frame = Frame(tab)
        self.pred, self.train = Home(frame).get_results()
        return self.pred,self.train
    
    def logout(self):
        self.frame_main.destroy()
        login.Login(self.root)
    

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    Main(root)
    root.title('Prediction software')
    root.mainloop()


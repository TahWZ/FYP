import sys
from tkinter import *
#sys.path.append('interface')
from home import Home
from about import About
from report import Report
from tkinter import ttk
#from PIL import ImageTK, Image

#====================( Main )====================
class Main:
    #====================( Functions )====================
    def __init__(self, root):
        #====================( Frames )====================
        self.frame_main = Frame(root)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        self.get_tabs()
        #====================( Widgets )====================
        #Label
        lab_1 = Label(self.frame_main, text="Logo", bg = "black", fg = "white", width = 80, height = 10)
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Row 0
        lab_1.pack(fill=BOTH)
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

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    Main(root)
    root.title('Prediction software')
    root.mainloop()


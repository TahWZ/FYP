import sys
from tkinter import *
#sys.path.append('interface')
from home import Home
from about import About
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
        tab = ttk.Frame(self.tabControl)
        self.tabControl.add(tab, text='Main algorithm')
        #Tab 1
        frame = Frame(tab)
        Home(frame)
        frame.pack()
        tab = ttk.Frame(self.tabControl)
        self.tabControl.add(tab, text='About us')
        #Tab 2
        frame = Frame(tab)
        About(frame)
        frame.pack(expand=True)

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    Main(root)
    root.title('Prediction software')
    root.mainloop()


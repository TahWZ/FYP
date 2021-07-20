from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

#====================( Class )====================
class Result():
    #====================( Functions )====================
    def __init__(self, result, res):
        #====================( Main Frame )====================
        self.frame_main = LabelFrame(result, text="Result", padx = 10, pady = 10)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        tab_table = ttk.Frame(self.tabControl)
        tab_chart = ttk.Frame(self.tabControl)
        self.tabControl.add(tab_table, text='Table View')
        self.tabControl.add(tab_chart, text='Chart View')
        #====================( Frames )====================
        frame_table = Frame(tab_table)
        #====================( Widgets )====================
        #Button
        '''
        @Attributes
        text: The displayed text
        state: DISABLED/ENABLED
        padx: Performs padding on x-axis (*.px)
        pady: Performs padding on y-axis (*.px)
        command: Function to execute
        '''
        but_cv_chart = Button(tab_chart, text="Show chart", command=lambda: self.chart())
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        but_cv_chart.pack()
        self.tabControl.grid(row = 0, column = 1)
        self.frame_main.pack(fill=BOTH, pady = 10)

    def chart(self):
        a = ['a','b','c','d']
        b = [[90,20],20,21,22]
        ypos = np.arange(len(a))
        plt.xticks(ypos, b)
        plt.bar(ypos,a)
        plt.show()

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    sm = Result(root, [])
    root.mainloop()

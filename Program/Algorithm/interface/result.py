from tkinter import *
from tkinter import ttk
import home
import numpy as np
import matplotlib.pyplot as plt

#====================( Class )====================
class Result():
    #====================( Functions )====================
    def __init__(self, result, fs_res, pred_res, train_res):
        #================( Root Reference )================
        self.root = result
        #====================( Main Frame )====================
        self.frame_main = LabelFrame(result, text="Result", padx = 10, pady = 10)
        self.backbutton = Frame(result)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        tab_table = ttk.Frame(self.tabControl)
        tab_chart = ttk.Frame(self.tabControl)
        self.tabControl.add(tab_table, text='Table View')
        self.tabControl.add(tab_chart, text='Chart View')
        #====================( Frames )====================
        self.frame_table = Frame(tab_table)
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
        button_goback = Button(self.backbutton, text = "Go Back", width = 10, command = lambda: self.back())
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        but_cv_chart.pack()
        button_goback.pack()
        self.backbutton.pack()
        self.table()
        self.frame_table.pack()
        self.tabControl.grid(row = 0, column = 1)
        self.frame_main.pack(fill=BOTH, pady = 10)

    def table(self):
        lst = [['DT','lR','MLP','NB'],[90,20,21,22],[60,70,100,89]]
        
        for j in range(len(lst[0])):
            entry = Entry(self.frame_table, bg='light gray')
            entry.grid(row=0, column=j)
            entry.insert(END,lst[0][j])
        for i in range(1,len(lst)):
            for j in range(len(lst[0])):
                entry = Entry(self.frame_table)
                entry.grid(row=i, column=j)
                entry.insert(END,lst[i][j])
        

    def chart(self):
        name = ['DT','lR','MLP','NB']
        temp1 = [90,20,21,22]
        temp2 = [60,70,100,89]
        ypos = np.arange(len(name))
        #plt.legend(labels=["a","b"])
        plt.subplot(1,2,1) #row, column, position
        plt.xticks(ypos, name)
        plt.title('AUC-score')
        plt.xlabel('Model')
        plt.ylabel('Score')
        plt.bar(ypos,temp1,color='blue')
        plt.subplot(1,2,2) #row, column, position
        plt.xticks(ypos, name)
        plt.title('F1-score')
        plt.xlabel('Model')
        plt.ylabel('Score')
        plt.bar(ypos,temp2,color='orange')
        plt.show()
    
    def back(self):
        self.frame_main.destroy()
        self.backbutton.destroy()
        home.Home(self.root)

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    sm = Result(root, [])
    root.mainloop()

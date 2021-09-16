from tkinter import *
from tkinter import ttk
from pathlib import Path 
import interface.result as r
from tkinter import messagebox
#====================( Class )====================
class SM():
    #====================( Functions )====================
    def __init__(self, fs, pred_res, train_res):
        #====================( Variables )====================
        self.root = fs
        self.datasets = []
        self.pred_res = pred_res
        self.train_res = train_res
        for _ in range(len(train_res["uploads"])):
            selections = []
            for _ in range(3): #Three feature selection methods
                selections.append(IntVar())
            self.datasets.append(selections)
        #====================( Main Frame )====================
        self.frame_main = LabelFrame(fs, text="Feature selection menu", padx = 10, pady = 10)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        self.get_tabs(train_res['uploads'])
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
        but_sm_run = Button(self.frame_main, text="Run", command = lambda: self.result())#, command=lambda: self.remove())
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        self.tabControl.pack()
        self.frame_main.pack(fill=BOTH, pady = 10)
        but_sm_run.pack()

    def get_tabs(self,uploads):
        i = 0
        #--------------------( Loop )--------------------
        for f in uploads:
            tab = ttk.Frame(self.tabControl)
            self.tabControl.add(tab, text=Path(f).name)
            #Frame
            frame = Frame(tab)
            #Top
            top_1 = Label(frame, text="Feature selection", width = 20, bg = "light grey", anchor = W)
            top_1.grid(sticky="W", row = 0, column = 1)
            top_2 = Label(frame, text="Select", bg = "light grey", anchor = W)
            top_2.grid(sticky="W", row = 0, column = 2)
            #Metric
            self.get_metrics(frame, i)
            #End
            frame.grid(row = 0, column = 1)
            i += 1
    
    def get_metrics(self, frame, i):
        j = 1
        for fs in ['All','CFS','RFE']:
            #Label
            lab = Label(frame, text=fs)
            #Checkbutton
            cb = Checkbutton(frame, variable=self.datasets[i][j-1])
            lab.grid(sticky="W", row = j, column = 1)
            cb.grid(row = j, column = 2)
            j+=1

    #====================( Transition )====================
    def result(self):
        result = []
        for i,selections in enumerate(self.datasets):
            result.append([])
            for s in selections:
                if s.get() == 1:
                    result[i].append(True)
                else:
                    result[i].append(False)
        if self.validate(result):
            self.frame_main.destroy()
            self.fs_res = {'result' : result}
            r.Result(self.root,self.fs_res,self.pred_res,self.train_res)
            return {
                "result" : self.result
    }

    def validate(self, result):
        for i, r in enumerate(result):
            if True not in r:
                if i == 0:
                    ord_ind = "st"
                elif i == 1: 
                    ord_ind = "nd"
                elif i == 2:
                    ord_ind = "rd"
                else:
                    ord_ind = "th"
                error_msg = "Please select at least one option for the " + str(i+1) + ord_ind + " dataset"
                messagebox.showerror("An error occured",error_msg)
                return False
        else:
            return True

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    sm = SM(root, [0,{"uploads" : ['D:/Computer Science/Python/test1.py','D:/Computer Science/Python/test2.py']}])
    root.mainloop()

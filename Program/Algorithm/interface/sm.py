from tkinter import *
from tkinter import ttk

#====================( Class )====================
class SM():
    #====================( Functions )====================
    def __init__(self, sm, res):
        #====================( Variables )====================
        self.datasets = []
        for _ in range(len(res[1]["uploads"])):
            dataset = []
            for _ in range(5):
                dataset.append(IntVar())
            self.datasets.append(dataset)
        #====================( Main Frame )====================
        self.frame_main = LabelFrame(sm, text="Software metric selection menu", padx = 10, pady = 10)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        self.get_tabs(res[1]["uploads"])
        #====================( Widgets )====================
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        self.tabControl.grid(row = 0, column = 1)
        self.frame_main.pack(fill=BOTH, pady = 10)

    def get_tabs(self,uploads):
        i = 0
        #--------------------( Loop )--------------------
        for f in uploads:
            tab = ttk.Frame(self.tabControl)
            self.tabControl.add(tab, text='Temp')
            #Frame
            frame = Frame(tab)
            #Top
            top_1 = Label(frame, text="Software Metric", width = 20, bg = "light grey", anchor = W)
            top_1.grid(sticky="W", row = 0, column = 1)
            top_2 = Label(frame, text="Select", bg = "light grey", anchor = W)
            top_2.grid(sticky="W", row = 0, column = 2)
            #Metric
            self.get_metrics(frame, i, self.read_file(f))
            #End
            frame.grid(row = 0, column = 1)
            i += 1
    
    def get_metrics(self, frame, i, metrics):
        j = 1
        for m in metrics:
            #Label
            lab = Label(frame, text="Decision Tree")
            #Checkbutton
            cb = Checkbutton(frame, variable=self.datasets[i][j-1])
            lab.grid(sticky="W", row = j, column = 1)
            cb.grid(row = j, column = 2)
            j+=1

    def read_file(self,f):
        return [1,2,3,4,5]

    def result(self):
        base = []
        for b in self.base:
            base.append(b.get())
        return {
            "base" : base
    }


#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    sm = SM(root, [0,{"uploads" : [1,2,3,4,5]}])
    root.mainloop()

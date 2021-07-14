from tkinter import *
from tkinter import ttk

#====================( Class )====================
class HomePred():
    #====================( Functions )====================
    def __init__(self, home):
        #====================( Variables )====================
        self.base = []
        for _ in range(5):
            self.base.append(IntVar())
        #====================( Main Frame )====================
        self.frame_main = LabelFrame(home, text="Prediction settings", padx = 10, pady = 10)
        #====================( Notebook )====================
        self.tabControl = ttk.Notebook(self.frame_main)
        #====================( Tabs )====================
        tab_base = ttk.Frame(self.tabControl)
        tab_ensemble = ttk.Frame(self.tabControl)
        self.tabControl.add(tab_base, text='Base')
        self.tabControl.add(tab_ensemble, text='Ensemble')
        #====================( Frames )====================
        frame_base = Frame(tab_base)
        #====================( Widgets )====================
        #--------------------( Tab 1 )--------------------
        #Label
        t1_lab1 = Label(frame_base, text="Decision Tree")
        t1_lab2 = Label(frame_base, text="Multi-Layer Perceptron")
        t1_lab3 = Label(frame_base, text="Logistic Regression")
        t1_lab4 = Label(frame_base, text="Naive Bayes")
        t1_lab5 = Label(frame_base, text="Complement Naive Bayes")

        #Checkbutton
        t1_cb1 = Checkbutton(frame_base, variable=self.base[0])
        t1_cb2 = Checkbutton(frame_base, variable=self.base[1])
        t1_cb3 = Checkbutton(frame_base, variable=self.base[2])
        t1_cb4 = Checkbutton(frame_base, variable=self.base[3])
        t1_cb5 = Checkbutton(frame_base, variable=self.base[4])
        #--------------------( Tab 2 )--------------------
        #--------------------( Others )--------------------

        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #--------------------( Tab 1 )--------------------
        #Top
        t1_labt1 = Label(frame_base, text="Base predictors", width = 20, bg = "light grey", anchor = W)
        t1_labt1.grid(sticky="W", row = 0, column = 1)
        t1_labt2 = Label(frame_base, text="Select", bg = "light grey", anchor = W)
        t1_labt2.grid(sticky="W", row = 0, column = 2)
        #Row 1
        t1_lab1.grid(sticky="W", row = 1, column = 1)
        t1_cb1.grid(row = 1, column = 2)
        #Row 2
        t1_lab2.grid(sticky="W", row = 2, column = 1)
        t1_cb2.grid(row = 2, column = 2)
        #Row 3
        t1_lab3.grid(sticky="W", row = 3, column = 1)
        t1_cb3.grid(row = 3, column = 2)
        #Row 4
        t1_lab4.grid(sticky="W", row = 4, column = 1)
        t1_cb4.grid(row = 4, column = 2)
        #Row 5
        t1_lab5.grid(sticky="W", row = 5, column = 1)
        t1_cb5.grid(row = 5, column = 2)
        #End
        frame_base.grid(row = 0, column = 1)
        #--------------------( Tab 2 )--------------------
        #--------------------( Others )--------------------
        self.tabControl.grid(row = 0, column = 1)
        self.frame_main.pack(side=LEFT, fill=BOTH, pady = 10)

    def get(self):
        base = []
        for b in self.base:
            base.append(b.get())
        return {
            "base" : base
        }


#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    home_train = HomePred(root)
    root.mainloop()

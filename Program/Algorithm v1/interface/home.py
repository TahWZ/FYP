import sys
from tkinter import *
import interface.result
import interface.fs
from interface.home_train import HomeTrain
from interface.home_pred import HomePred
from tkinter import messagebox

#====================( Class )====================
class Home:

    #====================( Functions )====================
    def __init__(self, root):
        #================( Root Reference )================
        self.root = root
        #====================( Frames )====================
        self.frame_1 = Frame(root)
        self.frame_2 = Frame(root)
        self.frame_3 = Frame(root)
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
        but_start = Button(self.frame_3, text="Start", width = 10, command=lambda: self.start())
        but_quit = Button(self.frame_3, text="Exit", width = 10, command=lambda: self.exit())
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Row 0
        #lab_1.pack(fill=BOTH)
        #Row 1 (Windows)
        self.home_pred = HomePred(self.frame_2)
        self.home_train = HomeTrain(self.frame_2)
        #Row 2
        but_start.pack(side = LEFT)
        but_quit.pack(side = RIGHT)
        #End
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
    
    #====================( Transition )====================
    def start(self):
        home_pred_res = self.home_pred.result()
        if home_pred_res: #Validation check on model selection
            home_train_res = self.home_train.result()
            if home_train_res: #Validation check on training settings
                interface.fs.SM(self.root,home_pred_res,home_train_res)
                self.frame_1.destroy()
                self.frame_2.destroy()
                self.frame_3.destroy()

    def exit(self):
        msgBox = messagebox.askquestion('Exit Application','Are you sure you want to exit this application',icon = 'warning')
        if msgBox == 'yes':
            self.root.quit()


#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    Home(root)
    root.mainloop()

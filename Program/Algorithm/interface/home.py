import sys
from tkinter import *
import result
import fs
from home_train import HomeTrain
from home_pred import HomePred
#from PIL import ImageTK, Image

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
        #Label
        #lab_1 = Label(frame_1, text="Logo", bg = "black", fg = "white", width = 80, height = 10)

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
        but_quit = Button(self.frame_3, text="Exit", width = 10, command=root.quit)
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
    
    def start(self):
        # fs.SM(self.root,[0,
        #     {
        #         "uploads" : ['D:/Computer Science/Python/test1.py','D:/Computer Science/Python/test2.py']
        #     }]
        #     ,
        # self.home_pred.result(),
        # self.home_train.result()
        # )
        fs.SM(self.root,[0,{}],self.home_pred.result(),self.home_train.result())
        self.frame_1.destroy()
        self.frame_2.destroy()
        self.frame_3.destroy()


#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    Home(root)
    root.mainloop()

import sys
from tkinter import *
import interface.result
import interface.fs
from interface.home_train import HomeTrain
from interface.home_pred import HomePred
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
        # import os
        # import re
        # test_file_path = os.getcwd() + '/datasets/NASA/CM1.arff.txt'
        # test_file_path2 = os.getcwd() + '/datasets/NASA/JM1.arff.txt'
        # test_file_path = os.getcwd() + '\\test1.py'
        # test_file_path = re.sub(r'\\','/',test_file_path)
        # test_file_path2 = os.getcwd() + '\\test2.py'
        # test_file_path2 = re.sub(r'\\','/',test_file_path2)
        home_pred_res = self.home_pred.result()
        home_train_res = self.home_train.result()
        # home_train_res['uploads'] = [test_file_path, test_file_path2]
        interface.fs.SM(self.root,home_pred_res,home_train_res)
        self.frame_1.destroy()
        self.frame_2.destroy()
        self.frame_3.destroy()


#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    Home(root)
    root.mainloop()

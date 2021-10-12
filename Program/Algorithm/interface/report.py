#import sys
from tkinter import *
#from tkinter import messagebox
from interface.report_pdf import PDF
#from home_train import HomeTrain
#from home_pred import HomePred
#from PIL import ImageTK, Image

#====================( Users )====================
#users = [['hi','hi']]

#====================( Class )====================
class Report:
    #====================( Functions )====================
    def __init__(self, root):
        #====================( Frames )====================
        self.frame_main = LabelFrame(root, text="Reports", padx = 10, pady = 10)
        #====================( Widgets )====================
        #Label
        lab_1 = Label(self.frame_main, text="PDF1")
        lab_2 = Label(self.frame_main, text="PDF2")

        #Button
        '''
        @Attributes
        text: The displayed text
        state: DISABLED/ENABLED
        padx: Performs padding on x-axis (*.px)
        pady: Performs padding on y-axis (*.px)
        command: Function to execute
        '''
        but_view1 = Button(self.frame_main, text="View", width = 10, command=lambda: self.view(r"\test.pdf"))
        but_view2 = Button(self.frame_main, text="View", width = 10, command=lambda: self.view(r"\test.pdf"))
        self.pdf = None
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #PDF files
        lab_1.grid(row=0, column=1) #Username
        but_view1.grid(row=0, column = 2)
        lab_2.grid(row=1, column=1) #Password
        but_view2.grid(row=1, column = 2, pady = 10)
        #End
        self.frame_main.pack()

    def create_view(self, filename):
        self.view_ = Frame(self.frame_main)
        self.pdf = PDF(self.view_, filename)
        self.view_.grid(row=3, column= 1, columnspan = 2)

    def view(self, filename):
        # If there is no exisiting pdf (create a new frame)
        if self.pdf is None:
            self.create_view(filename)
        else:
            # Resets the pdf view if there is an exisiting pdf
            self.pdf.reset_view()
            self.create_view(filename)
            

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    Report(root)
    root.mainloop()

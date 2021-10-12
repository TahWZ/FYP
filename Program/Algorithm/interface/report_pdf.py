#import sys
import os
from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf
#from home_train import HomeTrain
#from home_pred import HomePred
#from PIL import ImageTK, Image

#====================( Users )====================
#users = [['hi','hi']]

#====================( Class )====================
class PDF:
    #====================( Functions )====================
    def __init__(self, root, filename):
        # Parent directory of current file
        path = os.path.abspath(os.path.join(os.path.dirname(__file__),"reports"))
        #====================( Frames )====================
        self.frame_main = LabelFrame(root, text="Report view", padx = 10, pady = 10)
        #====================( Widgets )====================
        #Label
        lab_1 = Label(self.frame_main, text="Report: Test")

        #PDF
        self.v1 = pdf.ShowPdf()
        self.v2 = self.v1.pdf_view(self.frame_main, pdf_location = path+ filename,width = 70, height = 50)

        #Button
        '''
        @Attributes
        text: The displayed text
        state: DISABLED/ENABLED
        padx: Performs padding on x-axis (*.px)
        pady: Performs padding on y-axis (*.px)
        command: Function to execute
        '''
        but_quit = Button(self.frame_main, text="Exit", width = 10, command=lambda: root.destroy())
        
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Row 0-1 (Input fields)
        self.v2.pack()
        #Row 2
        but_quit.pack()
        #End
        self.frame_main.pack()

    def reset_view(self):
        # https://stackoverflow.com/questions/68753733/tkinter-skip-through-pdfs-in-gui
        # Destroys the old frame
        self.v1.frame.destroy()
        # Clear the image list (removes the concatenation of the two pdfs)
        self.v1.img_object_li.clear()

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    PDF(root)
    root.mainloop()

from tkinter import *
from tkinter.filedialog import askopenfilename
#from PIL import ImageTK, Image

#====================( Class )====================
class HomeTrain():
    #====================( Functions )====================
    def __init__(self, home):
        #====================( Variables )====================
        #====================( Frames )====================
        self.frame_main = LabelFrame(home, text="Training settings", padx = 10, pady = 10)
        #self.frame_ud = LabelFrame(self.frame_main)
        #====================( Widgets )====================
        #Label
        lab_1 = Label(self.frame_main, text="Training/Test")
        lab_2 = Label(self.frame_main, text="Upload dataset")
        lab_3 = Label(self.frame_main, text="Prediction file name")
        lab_4 = Label(self.frame_main, text="Prediction file path")
        #lab_2_1 = Label(self.frame_ud, text="Name", width = 50, anchor=W, bg="light grey")
        #lab_2_2 = Label(self.frame_ud, text="Remove", width = 20, anchor=W, bg="light grey")

        #Button
        '''
        @Attributes
        text: The displayed text
        state: DISABLED/ENABLED
        padx: Performs padding on x-axis (*.px)
        pady: Performs padding on y-axis (*.px)
        command: Function to execute
        '''
        but_ud_remove = Button(self.frame_main, text="Remove selected files")
        but_ud_upload = Button(self.frame_main, text="Upload", command=lambda: self.upload())

        #Entry
        '''
        @Additional functions
        .insert(,): To insert text in the input field
        .get(): To retrieve the input value
        @Attributes
        width: The width size
        bg: background colour
        fg: foreground colour
        borderwidth: the border's width size
        '''
        self.ent_tt = Entry(self.frame_main, width=10) #Training/Test
        self.ent_pfn = Entry(self.frame_main, width=20)#Prediction file name
        self.ent_pfp = Entry(self.frame_main, width=20)#Prediction file path

        #Listbox
        self.lb_upload = Listbox(self.frame_main, width=40)

        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Row 0
        lab_1.grid(sticky="W", row = 0, column = 1)
        self.ent_tt.grid(sticky="W", row = 0, column = 2)
        #Row 1
        lab_2.grid(sticky="W", row = 1, column = 1)
        #Row 2
        #self.frame_ud.grid(sticky="W", row = 2, column = 1, padx=10, pady=10)
        #lab_2_1.grid(sticky="W", row = 0, column = 1)
        #lab_2_2.grid(sticky="W", row = 0, column = 2)
        self.lb_upload.grid(row = 2, column = 1, columnspan = 2)
        #Row 3
        but_ud_remove.grid(row = 3, column = 1, pady = 10)
        but_ud_upload.grid(row = 3, column = 2, pady = 10)
        #Row 4
        lab_3.grid(sticky="W", row = 4, column = 1)
        self.ent_pfn.grid(sticky="W", row = 4, column = 2)
        #Row 5
        lab_4.grid(sticky="W", row = 5, column = 1)
        self.ent_pfp.grid(sticky="W", row = 5, column = 2)
        self.frame_main.grid(row = 0, column = 0)

    def upload(self):
        filename = askopenfilename()
        test = Label(self.frame_ud, text=filename)
        test.grid(sticky="W", row=2, column=1)

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    home_train = HomeTrain(root)
    root.mainloop()

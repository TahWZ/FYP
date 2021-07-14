from tkinter import *
from tkinter.filedialog import askopenfilenames

#====================( Class )====================
class HomeTrain():
    #====================( Functions )====================
    def __init__(self, home):
        #====================( Frames )====================
        self.frame_main = LabelFrame(home, text="Training settings", padx = 10, pady = 10)
        #====================( Widgets )====================
        #Label
        lab_1 = Label(self.frame_main, text="Training/Test")
        lab_2 = Label(self.frame_main, text="Upload dataset")
        lab_3 = Label(self.frame_main, text="Prediction file name")
        lab_4 = Label(self.frame_main, text="Prediction file path")

        #Button
        '''
        @Attributes
        text: The displayed text
        state: DISABLED/ENABLED
        padx: Performs padding on x-axis (*.px)
        pady: Performs padding on y-axis (*.px)
        command: Function to execute
        '''
        but_ud_remove = Button(self.frame_main, text="Remove selected files", command=lambda: self.remove())
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
        self.ent_tt = Entry(self.frame_main, width=5) #Training/Test
        self.ent_pfn = Entry(self.frame_main, width=20)#Prediction file name
        self.ent_pfp = Entry(self.frame_main, width=20)#Prediction file path

        #Listbox
        self.lb_upload = Listbox(self.frame_main, width=40, selectmode="multiple")
        sb_upload  = Scrollbar(self.frame_main)
        self.lb_upload.config(yscrollcommand = sb_upload.set)
        sb_upload.config(command = self.lb_upload.yview)

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
        self.lb_upload.grid(row = 2, column = 1, columnspan = 2)
        sb_upload.grid(sticky=N+S+W, row = 2, column = 3)
        #Row 3
        but_ud_remove.grid(row = 3, column = 1, pady = 10)
        but_ud_upload.grid(row = 3, column = 2, pady = 10)
        #Row 4
        lab_3.grid(sticky="W", row = 4, column = 1)
        self.ent_pfn.grid(sticky="W", row = 4, column = 2)
        #Row 5
        lab_4.grid(sticky="W", row = 5, column = 1)
        self.ent_pfp.grid(sticky="W", row = 5, column = 2)
        #End
        self.frame_main.pack(side = RIGHT, fill=BOTH, pady = 10)

    def upload(self):
        filenames = askopenfilenames()
        for f in filenames:
            self.lb_upload.insert(self.lb_upload.size()+1, f)

    def remove(self):
        sel = self.lb_upload.curselection()
        for i in reversed(sel):
            self.lb_upload.delete(i)

    def get(self):
        filenames = []
        for i in range(self.lb_upload.size()):
            filenames.append(self.lb_upload.get(i))
        return {
            "tt": self.ent_tt.get(),
            "uploads" : filenames,
            "pfn": self.ent_pfn.get(),
            "pfp": self.ent_pfp.get()
        }


#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    home_train = HomeTrain(root)
    root.mainloop()

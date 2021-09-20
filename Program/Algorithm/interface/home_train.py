from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox
from interface.tooltip import CreateToolTip

#====================( Class )====================
class HomeTrain():
    #====================( Functions )====================
    def __init__(self, home):
        #====================( Frames )====================
        self.frame_main = LabelFrame(home, text="Training settings", padx = 10, pady = 10)
        #====================( Widgets )====================
        #Label
        lab_1 = Label(self.frame_main, text="Feature reduction")
        lab_2 = Label(self.frame_main, text="Upload dataset")
        lab_3 = Label(self.frame_main, text="Prediction file name")
        lab_4 = Label(self.frame_main, text='K Fold')

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
        self.ent_tt = Entry(self.frame_main, width=5) #Feature reduction
        CreateToolTip(self.ent_tt, "The number of features to reduce from the feature selection algorithm (1-20)")
        self.ent_pfn = Entry(self.frame_main, width=20)#Prediction file name
        CreateToolTip(self.ent_pfn, "The name of the output csv file")
        self.ent_kfold = Entry(self.frame_main, width = 5) # K Fold
        CreateToolTip(self.ent_kfold, "The number of folds in K-fold cross-validation (2-20)")

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
        lab_4.grid(sticky='W', row = 1, column = 1)
        self.ent_kfold.grid(sticky='W', row = 1, column = 2)
        #Row 2
        lab_2.grid(sticky="W", row = 2, column = 1)
        #Row 3
        self.lb_upload.grid(row = 3, column = 1, columnspan = 2)
        sb_upload.grid(sticky=N+S+W, row = 3, column = 3)
        #Row 4
        but_ud_remove.grid(row = 4, column = 1, pady = 10)
        but_ud_upload.grid(row = 4, column = 2, pady = 10)
        #Row 5
        lab_3.grid(sticky="W", row = 5, column = 1)
        self.ent_pfn.grid(sticky="W", row = 5, column = 2)
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

    #====================( Transition )====================
    def result(self):
        if self.validate():
            filenames = []
            for i in range(self.lb_upload.size()):
                filenames.append(self.lb_upload.get(i))
            return {
                "tt": self.ent_tt.get(),
                "kfold" : self.ent_kfold.get(),
                "uploads" : filenames,
                "pfn": self.ent_pfn.get()
            }
        else:
            return False
    
    def validate(self):
        if not self.ent_tt.get().isdigit(): #Check feature reduction
            messagebox.showerror("An error occured","Invalid value for feature reduction")
            return False
        elif int(self.ent_tt.get()) > 20 or int(self.ent_tt.get()) < 1:
            messagebox.showerror("An error occured","Feature reduction value should be between 1 and 20")
            return False
        elif not self.ent_kfold.get().isdigit(): #Check k-fold input
            messagebox.showerror("An error occured","Invalid value for k-fold")
            return False
        elif int(self.ent_kfold.get()) > 20 or int(self.ent_kfold.get()) < 2: 
            messagebox.showerror("An error occured","Number of folds should be between 2 and 20")
            return False
        elif self.lb_upload.size() == 0: #Check uploaded dataset
            messagebox.showerror("An error occured","Please upload at least one dataset")
            return False
        elif self.ent_pfn == "": #Check prediction file name
            messagebox.showerror("An error occured","Please enter a filename for the result")
            return False
        else:
            return True


#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    home_train = HomeTrain(root)
    root.mainloop()

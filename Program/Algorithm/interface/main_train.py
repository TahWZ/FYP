from tkinter import *
from tkinter.filedialog import askopenfilename
#from PIL import ImageTK, Image

#====================( Start )====================
root = Tk()
main_train = LabelFrame(root, text="Training settings", padx = 10, pady = 10)

#====================( Variables )====================


#====================( Frames )====================
frame_ud = LabelFrame(main_train)

#====================( Widgets )====================
#Label
lab_1 = Label(main_train, text="Training/Test")
lab_2 = Label(main_train, text="Upload dataset")
lab_3 = Label(main_train, text="Prediction file name")
lab_4 = Label(main_train, text="Prediction file path")
lab_2_1 = Label(frame_ud, text="Name")
lab_2_2 = Label(frame_ud, text="Remove")

#Button
'''
@Attributes
text: The displayed text
state: DISABLED/ENABLED
padx: Performs padding on x-axis (*.px)
pady: Performs padding on y-axis (*.px)
command: Function to execute
'''
but_ud_remove = Button(main_train, text="Remove selected files")
but_ud_upload = Button(main_train, text="Upload", command=askopenfilename)

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
ent_tt = Entry(main_train, width=10) #Training/Test
ent_pfn = Entry(main_train, width=20)#Prediction file name
ent_pfp = Entry(main_train, width=20)#Prediction file path
#====================( Functions )====================
#def train_get():

#====================( Display )====================
'''
@Functions
.pack(padx, pady)
.grid(row, column, columnspan)
'''
#Row 0
lab_1.grid(row = 0, column = 1)
ent_tt.grid(row = 0, column = 2)
#Row 1
lab_2.grid(row = 1, column = 1)
#Row 2
frame_ud.grid(row = 2, column = 1, padx=10, pady=10)
lab_2_1.grid(row = 0, column = 1)
lab_2_2.grid(row = 0, column = 2)
#Row 3
but_ud_remove.grid(row = 3, column = 1)
but_ud_upload.grid(row = 3, column = 2)
#Row 4
lab_3.grid(row = 4, column = 1)
ent_pfn.grid(row = 4, column = 2)
#Row 5
lab_4.grid(row = 5, column = 1)
ent_pfp.grid(row = 5, column = 2)

#====================( Main )====================
main_train.grid(row = 0, column = 0)
root.mainloop()

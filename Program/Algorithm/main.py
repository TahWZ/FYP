import sys
from tkinter import *
sys.path.append('interface')
from home_train import HomeTrain
from home_pred import HomePred
#from PIL import ImageTK, Image

#====================( Start )====================
root = Tk()
#====================( Frames )====================
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
#====================( Widgets )====================
#Label
lab_1 = Label(frame_1, text="Logo", bg = "black", fg = "white", width = 80, height = 10)

#Button
'''
@Attributes
text: The displayed text
state: DISABLED/ENABLED
padx: Performs padding on x-axis (*.px)
pady: Performs padding on y-axis (*.px)
command: Function to execute
'''
but_start = Button(frame_3, text="Start", width = 10)
but_quit = Button(frame_3, text="Exit", width = 10, command=root.quit)

#====================( Functions )====================
#====================( Display )====================
'''
@Functions
.pack(padx, pady)
.grid(row, column, columnspan)
'''
#Row 0
lab_1.pack(fill=BOTH)
#Row 1 (Windows)
home_pred = HomePred(frame_2)
home_train = HomeTrain(frame_2)
#Row 2
but_start.pack(side = LEFT)
but_quit.pack(side = RIGHT)
#End
frame_1.pack()
frame_2.pack()
frame_3.pack()

#====================( Main )====================
root.mainloop()

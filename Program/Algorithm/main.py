from tkinter import *
#from PIL import ImageTK, Image

#====================( Start )====================
root = Tk()

#====================( Widgets )====================

#Label
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Hello World!")

#Button
'''
@Attributes
text: The displayed text
state: DISABLED/ENABLED
padx: Performs padding on x-axis (*.px)
pady: Performs padding on y-axis (*.px)
command: Function to execute
'''
myButton = Button(root, text="Click Me!")
b_quit = Button(root, text="Exit", command=root.quit)

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
e = Entry(root, width=50)

#Radio
'''
@Attributes
text: The displayed text
variable: Variable which stores the value
value: Value to be stored
'''
r = IntVar()
#r.get()



#====================( Functions )====================

#====================( Frames )====================
frame = LabelFrame(root, text="This is my Frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

#====================( Display )====================
'''
@Functions
.pack(padx, pady)
.grid(row, column, columnspan)
'''
myLabel1.grid(row = 0, column = 1)
myLabel2.grid(row = 0, column = 2)

#====================( Main )====================
root.mainloop()

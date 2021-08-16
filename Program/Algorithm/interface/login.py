import sys
from tkinter import *
#from home_train import HomeTrain
#from home_pred import HomePred
#from PIL import ImageTK, Image

#====================( Class )====================
class Login:
    #====================( Functions )====================
    def __init__(self, root):
        #====================( Frames )====================
        self.frame_main = LabelFrame(root, text="Login page", padx = 10, pady = 10)
        #====================( Widgets )====================
        #Label
        lab_1 = Label(self.frame_main, text="Username")
        lab_2 = Label(self.frame_main, text="Password")

        #Button
        '''
        @Attributes
        text: The displayed text
        state: DISABLED/ENABLED
        padx: Performs padding on x-axis (*.px)
        pady: Performs padding on y-axis (*.px)
        command: Function to execute
        '''

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
        self.ent_usr = Entry(self.frame_main, width=20) #Username
        self.ent_pwd = Entry(self.frame_main, width=20) #Password
        
        but_login = Button(self.frame_main, text="Login", width = 10, command=lambda: self.get())
        but_quit = Button(self.frame_main, text="Exit", width = 10, command=lambda: root.quit)
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Row 0-1 (Input fields)
        lab_1.grid(row=0, column=1) #Username
        self.ent_usr.grid(row=0, column = 2)
        lab_1.grid(row=0, column=1) #Password
        self.ent_pwd.grid(row=1, column = 2, pady = 10)
        #Row 2
        but_login.grid(row=2, column = 1)
        but_quit.grid(row=2, column = 2)
        #End
        self.frame_main.pack()

    def get(self):
        return [self.home_pred.result(),self.home_train.result()] 

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    Login(root)
    root.mainloop()

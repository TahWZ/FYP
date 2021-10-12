#import sys
from tkinter import *
import webbrowser
from PIL import ImageTk, Image
import os

#from home_train import HomeTrain
#from home_pred import HomePred
#from PIL import ImageTK, Image

#====================( Class )====================
class About:
    #====================( Functions )====================
    def __init__(self, root):
        #====================( Frames )====================
        self.frame_main = Frame(root)
        self.desc = "We are a group of 3 students from Monash University that have been tasked with building prediction models for software modules that are capable of handling the problem of dataset imbalance. As such, we have made the decision to develop this program." 
        self.desc2 = "Our aim is to create a program which lets the user upload their desired software datasets, and then give them the option of choosing which prediction models they would like to use against their datasets. Further details about the program will be explained in the next section."
        #====================( Widgets )====================
        #Label
        #Who we are
        top_1 = Label(self.frame_main, text="About Us", font=('Helvetica', 16, 'bold'))
        text_1 = Label(self.frame_main, text=self.desc, font=('Helvetica', 11), wraplength = 475, justify = LEFT)

        #Objective
        top_2 = Label(self.frame_main, text="Objective", font=('Helvetica', 16, 'bold'))
        text_2 = Label(self.frame_main, text=self.desc2, font=('Helvetica', 11), wraplength = 475, justify = LEFT)

        #Bind 
        #label.bind("<Button-1>", lambda e:open_url(url))

        # Information
        names = ['Jason','Tah','Ethan']
        # emails = ['jtoh0003@student.monash.edu','wtah0001@student.monash.edu','ehor0005@student.monash.edu']
        emails =['jtoh0003','wtah0001','ehor0005']
        stickies = ['NW','N','NE']

        # Parent directory of current file
        path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

        # Images
        # img1 = Image.open(path + '/images/placeholder.png')
        img1 = Image.open(path + '/images/jason.JPG')
        resized_image= img1.resize((100,100), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(resized_image)
        panel1 = Label(self.frame_main, image = img1)
        panel1.image = img1
        panel1.grid(row=0,column=0,sticky=NW)

        # img2 = Image.open(path + '/images/placeholder.png')
        img2 = Image.open(path + '/images/tah.JPG')
        resized_image= img2.resize((100,100), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(resized_image)
        panel2 = Label(self.frame_main, image = img2)
        panel2.image = img2
        panel2.grid(row=0,column=0,sticky=N)

        # img3 = Image.open(path + '/images/placeholder.png')
        img3 = Image.open(path + '/images/ethan.JPG')
        resized_image= img3.resize((100,100), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(resized_image)
        panel3 = Label(self.frame_main, image = img3)
        panel3.image = img3
        panel3.grid(row=0,column=0,sticky=NE)

        for i in range(len(names)):
            name = Label(self.frame_main, text=names[i], font=('Helvetica', 11),justify = LEFT)
            email = Label(self.frame_main, text=emails[i], font=('Helvetica', 11),justify = LEFT)
            name.grid(row=1,column=0,sticky=stickies[i])
            email.grid(row=2,column=0,sticky=stickies[i])
        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Rows
        # top_1.pack(anchor = 'w')
        # text_1.pack(anchor = 'w')
        # top_2.pack(anchor = 'w')
        # text_2.pack(anchor = 'w')
        top_1.grid(row=3,column=0,sticky=W)
        text_1.grid(row=4,column=0,sticky=W)
        top_2.grid(row=5,column=0,sticky=W)
        text_2.grid(row=6,column=0,sticky=W)
        # End
        self.frame_main.pack(expand = True)

    def open_url(url):
        webbrowser.open_new_tab(url)
            

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    About(root)
    root.mainloop()

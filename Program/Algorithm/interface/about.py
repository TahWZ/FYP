import sys
from tkinter import *
import webbrowser

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
        self.desc3 = "Before running the algorithm within the program. Users are required to upload at least one of their desired software datasets. Then, they can also select the prediction models they wish to use on their datasets. After that, the program takes them to a screen which lets them decide whether they want to include additional algorithms which optimize the selection of software metrics. Once that is done, the algorithm runs in the background, and then takes the user to the results screen, at which they can choose to view the results of the prediction algorithms in table view as well as chart view."
        #====================( Widgets )====================
        #Label
        #Who we are
        top_1 = Label(self.frame_main, text="About Us", font=('Helvetica', 16, 'bold'))
        text_1 = Label(self.frame_main, text=self.desc, font=('Helvetica', 11), wraplength = 475, justify = LEFT)

        #Objective
        top_2 = Label(self.frame_main, text="Objective", font=('Helvetica', 16, 'bold'))
        text_2 = Label(self.frame_main, text=self.desc2, font=('Helvetica', 11), wraplength = 475, justify = LEFT)

        #Summary
        top_3 = Label(self.frame_main, text="How the Program Works", font=('Helvetica', 16, 'bold'))
        text_3 = Label(self.frame_main, text=self.desc3, font=('Helvetica', 11), wraplength = 475, justify = LEFT)

        #Bind 
        #label.bind("<Button-1>", lambda e:open_url(url))

        #====================( Display )====================
        '''
        @Functions
        .pack(padx, pady)
        .grid(row, column, columnspan)
        '''
        #Rows
        top_1.pack(anchor = 'w')
        text_1.pack(anchor = 'w')
        top_2.pack(anchor = 'w')
        text_2.pack(anchor = 'w')
        top_3.pack(anchor = 'w')
        text_3.pack(anchor = 'w')
        #End
        self.frame_main.pack(expand = True)

    def open_url(url):
       webbrowser.open_new_tab(url)
            

#====================( Main )====================
if __name__=='__main__':
    root = Tk()
    About(root)
    root.mainloop()

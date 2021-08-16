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
        #====================( Widgets )====================
        #Label
        #Who we are
        top_1 = Label(self.frame_main, text="Who we are", font=('Helvetica', 18, 'bold'))
        text_1 = Label(self.frame_main, text="-", justify = LEFT)

        #Objective
        top_2 = Label(self.frame_main, text="Objective", font=('Helvetica', 18, 'bold'))
        text_2 = Label(self.frame_main, text="-", justify = LEFT)

        #Summary
        top_3 = Label(self.frame_main, text="Summary", font=('Helvetica', 18, 'bold'))
        text_3 = Label(self.frame_main, text="-", justify = LEFT)

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

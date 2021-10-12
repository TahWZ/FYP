from tkinter import *

class Instruction:
    def __init__(self,root):
        self.frame_main = Frame(root)

        self.desc = "Before running the algorithm within the program. Users are required to upload at least one of their desired software datasets. Then, they can also select the prediction models they wish to use on their datasets. After that, the program takes them to a screen which lets them decide whether they want to include additional algorithms which optimize the selection of software metrics. Once that is done, the algorithm runs in the background, and then takes the user to the results screen, at which they can choose to view the results of the prediction algorithms in table view as well as chart view."

        top = Label(self.frame_main, text="How the Program Works", font=('Helvetica', 16, 'bold'))
        text = Label(self.frame_main, text=self.desc, font=('Helvetica', 11), wraplength = 475, justify = LEFT)

        top.pack(anchor = 'w')
        text.pack(anchor = 'w')

        self.frame_main.pack(expand = True)

if __name__=='__main__':
    root = Tk()
    Instruction(root)
    root.mainloop()

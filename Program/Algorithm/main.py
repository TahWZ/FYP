import sys
from tkinter import *
sys.path.append('interface')
from home import Home
#from PIL import ImageTK, Image

#====================( Main )====================
root = Tk()
Home(root)
root.title('Prediction software')
root.mainloop()

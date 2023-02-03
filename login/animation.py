from tkinter import *
import time
import os
root = Tk()

frameCnt = 50
frames = [PhotoImage(file='images/emasb.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
class Gif():
    
    def update(ind):

        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0      
        root.after(100, ind)
        label = Label(root)
        label.configure(image=frame)
        label.pack()
        root.after(0, 0)
        root.mainloop()

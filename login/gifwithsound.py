import tkinter as tk
import customtkinter as cstk
import time
import os
from PIL import ImageTk, Image

class GifWSound(cstk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        self.button = cstk.CTkButton(self, text="GifSound", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)


    def gifWSound(ind):
        frameCnt = 50
        frames = [cstk.CTkImage(file='images/emasb.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
        frame = frames[ind]
        ind += 1
        topup = cstk.CTkToplevel()
        topup.geometry("500x350")
        topup.title('Sounded Gif')
        topup.resizable(False, False)
        if ind == frameCnt:
            ind = 0
        label_img = cstk.CTkLabel(master=topup,
                            text='',
                            image=frame)
        label_img.place(relx=0.5, rely=0.5, anchor=cstk.CENTER)
        
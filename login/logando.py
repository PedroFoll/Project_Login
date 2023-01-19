import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.geometry('700x400')
janela.title('Sistema de login')
janela.resizable(False, False)


img= ctk.CTkImage('images\eumoleton.png')
label_img = ctk.CTkLabel(master=janela, image=img)

janela.mainloop()
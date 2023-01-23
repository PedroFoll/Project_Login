import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.geometry('700x400')
janela.title('Sistema de login')
janela.resizable(False, False)

""" campo_0 = ctk.CTkLabel(master=janela, text="Teste 000")
campo_0.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

campo_1 = ctk.CTkLabel(master=janela, text="Teste 001")
campo_1.place(relx=0.5, rely=0.6, anchor=ctk.CENTER) """

campo_0 = ctk.CTkLabel(master=janela,
                    text='Teste 001',
                    width=120,
                    height=25,
                    fg_color=("blue"),
                    corner_radius=8)
campo_0.place(relx=0.1, rely=0.1, anchor=ctk.CENTER)

espaco_0 = ctk.CTkEntry(master=janela,
                               placeholder_text="Login",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
espaco_0.place(relx=0.28, rely=0.1, anchor=ctk.CENTER)

campo_1 = ctk.CTkLabel(master=janela,
                    text='Teste 002',
                    width=120,
                    height=25,
                    fg_color=("blue"),
                    corner_radius=8)
campo_1.place(relx=0.1, rely=0.2, anchor=ctk.CENTER)

espaco_1 = ctk.CTkEntry(master=janela,
                            placeholder_text="Senha",
                            show='*',
                            width=120,
                            height=25,
                            border_width=2,
                            corner_radius=10)
espaco_1.place(relx=0.28, rely=0.2, anchor=ctk.CENTER)


img= ctk.CTkImage(Image.open('images/eumoleton.png'),size=(350,400))
label_img = ctk.CTkLabel(master=janela,
                            text='',
                            image=img,)
label_img.place(relx=0.8, rely=0.5, anchor=ctk.CENTER)
janela.mainloop()
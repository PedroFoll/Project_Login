import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.geometry('700x400')
janela.title('Sistema de login')
janela.resizable(False, False)
def botao1_event():
    print('botão pressionado')
botao2_event=botao1_event

img= ctk.CTkImage(Image.open('images/eumoleton.png'),size=(350,400))
label_img = ctk.CTkLabel(master=janela,
                            text='',
                            image=img,)

label_img.place(relx=0.8, rely=0.5, anchor=ctk.CENTER)

campo_0 = ctk.CTkLabel(master=janela,
                    text='Teste 001',
                    width=180,
                    height=40,
                    fg_color=("blue"),
                    corner_radius=8)
campo_0.place(relx=0.132, rely=0.1, anchor=ctk.CENTER)

espaco_0 = ctk.CTkEntry(master=janela,
                               placeholder_text="Login",
                               width=180,
                               height=40,
                               border_width=2,
                               corner_radius=10)
espaco_0.place(relx=0.40, rely=0.1, anchor=ctk.CENTER)

campo_1 = ctk.CTkLabel(master=janela,
                    text='Teste 002',
                    width=180,
                    height=40,
                    fg_color=("blue"),
                    corner_radius=8)
campo_1.place(relx=0.132, rely=0.24, anchor=ctk.CENTER)

espaco_1 = ctk.CTkEntry(master=janela,
                            placeholder_text="Senha",
                            show='*',
                            width=180,
                            height=40,
                            border_width=2,
                            corner_radius=10)
espaco_1.place(relx=0.40, rely=0.24, anchor=ctk.CENTER)

botao1 = ctk.CTkButton(master=janela,
                        text="Entrar",
                        width=180,
                        height=40,
                        border_width=2,
                        corner_radius=10,
                        command=botao1_event)
botao1.place(relx=0.26, rely=0.45, anchor=ctk.CENTER)

botao2 = ctk.CTkButton(master=janela,
                        text='Registrar-se',
                        width=90,
                        height=20,
                        fg_color='transparent',
                        command=botao2_event)
botao2.place(relx=0.26, rely=0.35, anchor=ctk.CENTER)


janela.mainloop()
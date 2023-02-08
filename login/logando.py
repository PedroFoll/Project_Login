from telaregistro import ExampleApp

import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
#Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('theme/acid_purple.json')

janela = ctk.CTk()
janela.geometry('700x400')
janela.title('Sistema de login')
janela.resizable(False, False)
def botao1_event():
    import animation
    animation.ImageLabel.load()
def botao2_event():
    ExampleApp.create_toplevel()
    

img= ctk.CTkImage(Image.open('images/eumoleton.png'),size=(350,400))
imagem_pedro = ctk.CTkLabel(master=janela,
                            text='',
                            image=img,)

imagem_pedro.place(relx=0.8, rely=0.5, anchor=ctk.CENTER)

campo_0 = ctk.CTkLabel(master=janela,
                    text='Usuário',
                    width=180,
                    height=40,
                    fg_color=(["#9932CC", "#8A2BE2"]),
                    text_color= (["#F8F8FF", "#BEBEBE"]),
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
                    text='Senha',
                    width=180,
                    height=40,
                    fg_color=(["#9932CC", "#8A2BE2"]),
                    text_color= (["#F8F8FF", "#BEBEBE"]),
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
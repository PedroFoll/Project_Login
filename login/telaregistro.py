import tkinter as tk
import customtkinter as cstk
from models import login_model

class ExampleApp(cstk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        self.button = cstk.CTkButton(self, text="Tela de Registro", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)

    

    def create_toplevel():
        topup = cstk.CTkToplevel()
        topup.geometry("500x350")
        topup.title('Tela de Registro')
        topup.resizable(False, False)

        def send_register():            
            if (ru1.get()==""or
                ru2.get()==""):
                print('Empty input')
            else:
                login_model.login_treino.db_model(nome = ru1.get(), senha=ru2.get())
                print(ru1.get())
        
        # create label on CTkToplevel window
        ra0 = cstk.CTkLabel(topup, 
                                        text="Usuário",
                                        fg_color=(["#9932CC", "#8A2BE2"]),
                                        text_color= (["#F8F8FF", "#BEBEBE"]),
                                        corner_radius=8,
                                        width=140,
                                        height=30,)
        ra0.place(relx=0.180, rely=0.1, anchor=cstk.CENTER)
        ra1 = cstk.CTkLabel(topup, 
                                        text="Senha",
                                        fg_color=(["#9932CC", "#8A2BE2"]),
                                        text_color= (["#F8F8FF", "#BEBEBE"]),
                                        corner_radius=8,
                                        width=140,
                                        height=30,)
        ra1.place(relx=0.180, rely=0.2, anchor=cstk.CENTER)

        ru1 = cstk.CTkEntry(topup,                                
                               placeholder_text="Insira seu Username",
                               width=140,
                               height=30,
                               border_width=2,
                               corner_radius=10)
        ru1.place(relx=0.480, rely=0.1, anchor=cstk.CENTER)

        ru2 = cstk.CTkEntry(topup,                                
                               placeholder_text="Informe sua senha",
                               width=140,
                               height=30,
                               border_width=2,
                               corner_radius=10)
        ru2.place(relx=0.480, rely=0.2, anchor=cstk.CENTER)


        registro1 = cstk.CTkButton(master=topup,
                        text="Registrar-se",
                        width=180,
                        height=40,
                        border_width=2,
                        corner_radius=10,
                        command=send_register)
        registro1.place(relx=0.26, rely=0.45, anchor=cstk.CENTER) 
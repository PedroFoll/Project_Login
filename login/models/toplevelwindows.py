import tkinter
import customtkinter as ctk


class ExampleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        self.button = ctk.CTkButton(self, text="Tela de Registro", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)

    def create_toplevel():
        topup = ctk.CTkToplevel()
        topup.geometry("500x350")
        topup.title('Tela de Registro')
        topup.resizable(False, False)


        # create label on CTkToplevel window
        register_username = ctk.CTkLabel(topup, 
                                        text="Usuário",
                                        fg_color=("blue"),
                                        corner_radius=8,
                                        width=140,
                                        height=30,)
        register_username.place(relx=0.180, rely=0.1, anchor=ctk.CENTER)
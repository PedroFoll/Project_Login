import tkinter
import customtkinter as cstk
import tripleTdb


class ExampleApp(cstk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        self.button = cstk.CTkButton(self, text="Tela de Registro", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)

    def create_toplevel():
        registro1_event = print("Registrado")
        topup = cstk.CTkToplevel()
        topup.geometry("500x350")
        topup.title('Tela de Registro')
        topup.resizable(False, False)
        
        # create label on CTkToplevel window
        register_username = cstk.CTkLabel(topup, 
                                        text="Usuário",
                                        fg_color=(["#9932CC", "#8A2BE2"]),
                                        text_color= (["#F8F8FF", "#BEBEBE"]),
                                        corner_radius=8,
                                        width=140,
                                        height=30,)
        register_username.place(relx=0.180, rely=0.1, anchor=cstk.CENTER)

        registro1 = cstk.CTkButton(master=topup,
                        text="Registrar-se",
                        width=180,
                        height=40,
                        border_width=2,
                        corner_radius=10,
                        command=registro1_event)
        registro1.place(relx=0.26, rely=0.45, anchor=cstk.CENTER)
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

window = ctk.CTk()

class Application():
    def __init__(self):
        self.window = window
        self.theme()
        self.main_window()
        self.login_window()
        window.mainloop()
    
    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def main_window(self):
        window.geometry("700x410")
        window.title("Login System")
        window.iconbitmap("password_code.ico")
        window.resizable("False", "False")

    def login_window(self):
        # Login window image
        img = PhotoImage(file="login.png")
        label_img = ctk.CTkLabel(master=window, image=img, text="").place(x=25, y=75)

        label_tt = ctk.CTkLabel(master=window, text='Make login to acces your manager \npasswords', font=('Roboto', 18, 'bold'), text_color='#1F538D').place(x=25, y=10)

        # Frame
        login_frame = ctk.CTkFrame(master=window, width=320, height=260)
        login_frame.pack(side=RIGHT, padx=25, pady=10)

        # Frame widgets
        label = ctk.CTkLabel(master=login_frame, text='Login', font=('Roboto', 20, 'bold'), text_color= ('white') ).place(x=134, y=10)

        # User label
        entry_user = ctk.CTkEntry(master=login_frame, placeholder_text='User', width=280).place(x=20, y=60)

        # Password label
        entry_password = ctk.CTkEntry(master=login_frame, placeholder_text='Password', width=280, show='*').place(x=20, y=110)

        def login_user():
            msg = messagebox.showinfo(title="Status of enrollment", message="Congratulation user enrolled success!")

        # Login button
        login_button = ctk.CTkButton(master=login_frame, text='LOGIN', width=280, command=login_user).place(x=20, y=160)

        # Register span
        register_span = ctk.CTkLabel(master=login_frame, text="If you don't have an account").place(x=20, y=210)
        
        def register_window():
            # Remove frame login
            login_frame.pack_forget()
            
            # Creating enrollment window
            rg_frame = ctk.CTkFrame(master=window, width=320, height=260)
            rg_frame.pack(side=RIGHT, padx=25, pady=10)
            label = ctk.CTkLabel(master=rg_frame, text='Make your register', font=('Roboto', 20, 'bold'), text_color= ('white') ).place(x=75, y=10)
            # span = ctk.CTkLabel(master=rg_frame, text="Fill labels correctly.", text_font=('Roboto', 10), text_color="gray").place(x=25, y=35)

            entry_user = ctk.CTkEntry(master=rg_frame, placeholder_text='User', width=280).place(x=20, y=60)
            email_user = ctk.CTkEntry(master=rg_frame, placeholder_text='Email', width=280).place(x=20, y=100)
            entry_password = ctk.CTkEntry(master=rg_frame, placeholder_text='Password', width=280, show='*').place(x=20, y=140)
            confirm_password = ctk.CTkEntry(master=rg_frame, placeholder_text='Confirm password', width=280, show='*').place(x=20, y=180)

            def back_to_login():
                rg_frame.pack_forget()
                login_frame.pack(side=RIGHT, padx=25, pady=10)

            back_button = ctk.CTkButton(master=rg_frame, text='Back', width=100, command=back_to_login).place(x=50, y=220)
            
            def save_user():
                msg = messagebox.showinfo(title="Status of enrollment", message="Congratulation user enrolled success!")
            
            save_button = ctk.CTkButton(master=rg_frame, text='Register', width=100, fg_color="green", hover_color="#014B05", command=save_user).place(x=170, y=220)

        register_button = ctk.CTkButton(master=login_frame, fg_color='green', hover_color='#2D9334', text="Sign Up", width=110, command=register_window).place(x=190, y=210)

if __name__ == "__main__":
    Application()

import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("700x410")
window.title("Login Sytem")
window.iconbitmap("password_code.ico")
window.resizable("False", "False")

# Login window image
img = PhotoImage(file="login.png")
label_img = customtkinter.CTkLabel(master=window, image=img, text="")
label_img.place(x=25, y=75)

label_tt = customtkinter.CTkLabel(master=window, text='Make login to acces your manager \npasswords', font=('Roboto', 18, 'bold'), text_color='#1F538D')
label_tt.place(x=25, y=10)

# Frame
frame = customtkinter.CTkFrame(master=window, width=350, height=406)
frame.pack(side=RIGHT)

# Frame widgets
label = customtkinter.CTkLabel(master=frame, text='Login', font = ('Roboto', 20, 'bold'), text_color= ('white') )
label.place(x=25, y=10)

# User
entry_user = customtkinter.CTkEntry(master=frame, placeholder_text='User', width=300)
entry_user.place(x=25, y=105)

# Password
entry_password = customtkinter.CTkEntry(master=frame, placeholder_text='Password', width=300)
entry_password.place(x=25, y=155)

# Button
button = customtkinter.CTkButton(master=frame, text='LOGIN', width=300)
button.place(x=25, y=205)

window.mainloop()

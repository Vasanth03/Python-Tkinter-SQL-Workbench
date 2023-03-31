#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:36:44 2023

@author: vasanthdhanagopal
"""

import tkinter as tk
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="waitforit",
    database="Onego"
)

# Create cursor object
mycursor = mydb.cursor()

# Create login window
def login_window():
    login = tk.Toplevel()
    login.title("Welcome Back")
    login.geometry("300x200")
    login.config(bg="#4876FF")
    login.resizable(0, 0)  

    # Create login form
    username_label = tk.Label(login, text="Username",fg="black")
    username_label.place(x=50,y=20)
    username_entry = tk.Entry(login)
    username_entry.place(x=50,y=50)

    password_label = tk.Label(login, text="Password",fg="black")
    password_label.place(x=50,y=90)
    password_entry = tk.Entry(login, show="*")
    password_entry.place(x=50,y=120)

    # Check user credentials
    def check_credentials():
        username = username_entry.get()
        password = password_entry.get()

        mycursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username, password))
        user = mycursor.fetchall()

        if user:
            login.destroy()
            import Onego
                       
        else:
            tk.messagebox.showerror("Error", "Invalid username or password.")

    login_button = tk.Button(login, text="Login", command=check_credentials,fg="black")
    login_button.place(x=110,y=160)

# Create registration window
def registration_window():
    registration = tk.Toplevel()
    registration.title("Welcome to Onego")
    registration.geometry("300x450")
    registration.config(bg="#EEEE00")
    registration.resizable(0, 0)  

    # Create registration form
    username_label = tk.Label(registration, text="Username",fg="black")
    username_label.place(x=50,y=20)
    username_entry = tk.Entry(registration)
    username_entry.place(x=50,y=50)

    password_label = tk.Label(registration, text="Password",fg="black")
    password_label.place(x=50,y=90)
    password_entry = tk.Entry(registration, show="*")
    password_entry.place(x=50,y=120)
    

    nationality_label = tk.Label(registration, text="Nationality:",fg="black")
    nationality_label.place(x=50, y=160)
    nationality_var = tk.StringVar(root) 
    nationality_var.set("Indian")
    nationality_dropdown = tk.OptionMenu(registration, nationality_var, "Indian", "Foreigner")
    nationality_dropdown.place(x=150,y=160)

    # Aadhaar or Passport Label and Input Field
    id_labela = tk.Label(registration, text="Aadhaar Number:") 
    id_labela.place(x=50, y=210)
    id_labela_entry = tk.Entry(registration)
    id_labela_entry.place(x=50,y=240)
    
    id_label1 = tk.Label(registration, text="(or)") 
    id_label1.place(x=150, y=280)
    
    
    id_labelb = tk.Label(registration, text="Passport Number:") 
    id_labelb.place(x=50, y=310)
    id_labelb_entry = tk.Entry(registration)
    id_labelb_entry.place(x=50,y=340)

    # Add user to database
    def add_user():
        username    = username_entry.get()
        password    = password_entry.get()
        nationality = nationality_var.get()
        idindian    = id_labela_entry.get()
        idforeigner = id_labelb_entry.get()

        mycursor.execute("INSERT INTO users (username, password, nationality, idindian, idforeigner) \
                         VALUES (%s, %s, %s, %s, %s)",\
                         (username, password,nationality,idindian,idforeigner))
        mydb.commit()

        registration.destroy()

    register_button = tk.Button(registration, text="Register", command=add_user)
    register_button.place(x=110,y=400)

# Create main window after login
# import Draft18 as dft
# welcome_label = tk.Label(dft)
# welcome_label.pack()

# def main_window(username):
#     import Onego as og
#     return og.redirect("Onego.py")
    #main = tk.Toplevel()
    #main.title("Main")
    #main.geometry("300x200")

    #welcome_label = tk.Label(main, text=f"Welcome, {username}!")
    #welcome_label.pack()

# Create root window with login and registration buttons
root = tk.Tk()
root.title("Ride Wide")
root.geometry("300x200")
root.config(bg="#43CD80")
root.resizable(0,0)


login_button = tk.Button(root, text="Login",command=login_window)
login_button.place(x=125,y=50)


register_button = tk.Button(root, text="Register",command=registration_window)
register_button.place(x=115,y=110)

root.mainloop()

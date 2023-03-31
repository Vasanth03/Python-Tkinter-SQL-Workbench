#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:40:44 2023

@author: vasanthdhanagopal
"""

# Modules used in the program
import tkinter as tk
import mysql.connector
from tkinter import ttk 
import requests
from PIL import Image, ImageTk
from tkmacosx import Button

#  Window Creation
wd = tk.Tk()
wd.title('One Go')            # Title of the window   
wd.geometry('900x750')        # setting the size of the window
wd.resizable(0, 0)            # This is to prevent from resizing the window
wd.config(bg="cornflowerblue")

############################  USER DETAILS ####################################
# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='waitforit',
    database='Onego'
)

# Create a users table
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer_Details (
        No INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(30) NOT NULL,
        Mobile_No VARCHAR(30) NOT NULL,
        Age VARCHAR(30),
        Gender VARCHAR(30), 
        Nationality VARCHAR(30) NOT NULL, 
        Ref_Code VARCHAR(30), 
        Source VARCHAR(30) NOT NULL,
        Destination VARCHAR(30) NOT NULL, 
        Insurance VARCHAR(30)
    )
''')

conn.commit()

def save_details():
    # Get the user input
    Name        = e1.get()
    Mobile_No   = e2.get()
    Age         = e3.get()
    Gender      = Gender_selected.get()
    Nationality = e5.get()
    Ref_Code    = e5_1.get()
    Source      = pickeds.get()
    Destination = pickedd.get()
    Insurance   = Insurance_selected.get()
    
    # Save the user details to the MySQL database
    cursor = conn.cursor()
    sql = "INSERT INTO Customer_Details (Name, Mobile_No, Age, Gender, Nationality, Ref_Code,  \
           Source, Destination, Insurance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (Name, Mobile_No, Age, Gender, Nationality, Ref_Code,Source, Destination, Insurance)
    cursor.execute(sql, val)
    conn.commit()
    
    # Clear the form
    # e1.delete(0, "end")
    # e2.delete(0, "end")
    # e3.delete(0, "end")
    # Gender_selected.delete(0, "end")
    # e5.delete(0, "end")
    # e5_1.delete(0, "end")
    # pickeds.delete(0, "end")
    # pickedd.delete(0, "end")
    # Insurance_selected.delete(0, "end")

################################ CAB BOOKING ##################################
# Label Intro
lb00    = tk.Label(wd,text="Hi"  , font=("Times", "25", "bold italic"),bg = "gold",relief='sunken')  
lb01    = tk.Label(wd,text="Welcome Onboard !", font=("Times", "25", "bold italic"),bg = "gold",relief='sunken')
lb02    = tk.Label(wd,text="Version 2.1.1"  , font=("Times", "15"),bg='peach puff')  
lb03    = tk.Label(wd,text="Copyright OneGo © 2023. All rights Reserved."  , font=("Times", "15"),bg='peach puff')  


 
lb0     = tk.Label(wd,text="Customer Information", width=30,fg="white",bg = "dark green",font=("Times", "15", "bold italic"),relief='ridge')  
lb1     = tk.Label(wd,text="Name",font=('Calibri',15),bg = "white") 
lb2     = tk.Label(wd,text="Mobile_No",font=('Calibri',15),bg = "white")
lb3     = tk.Label(wd,text="Age",font=('Calibri',15),bg = "white")
lb4     = tk.Label(wd,text="Gender",font=('Calibri',15),bg = "white")
lb5     = tk.Label(wd,text="Nationality",font=('Calibri',15),bg = "white")
lb5_1   = tk.Label(wd,text="Ref_Code",font=('Calibri',15),bg = "white")

lb6     = tk.Label(wd,text="Booking Details", width=25,fg="white",bg = "dark green",font=("Times", "15", "bold italic"),relief='ridge')  
lb7     = tk.Label(wd,text="Source",font=('Calibri',15),bg = "white") 
lb8     = tk.Label(wd,text="Destination",font=('Calibri',15),bg = "white")
lb8_0   = tk.Label(wd,text="Distance",font=('Calibri',15),bg = "white")
lb8_00  = tk.Label(wd,text="km",font=('Calibri',15),bg = "white")
lb8_1   = tk.Label(wd,text="Insurance",font=('Calibri',15),bg = "white")

lb9     = tk.Label(wd,text="Charges", width=30,fg="white",bg = "dark green",font=("Times", "15", "bold italic"),relief='ridge') 
#lb10   = tk.Label(wd,text="Base Charge",font=('Calibri',15))
lb10_1  = tk.Label(wd,text="@ Cab Type",font=('Calibri',9),bg = "white")
lb11    = tk.Label(wd,text="Rs./-",font=('Calibri',13),bg = "white") 
#lb12   = tk.Label(wd,text="Charge/Dist",font=('Calibri',15))
lb12_1  = tk.Label(wd,text="@ 18Rs/km",font=('Calibri',9),bg = "white")
lb13    = tk.Label(wd,text="Rs./-",font=('Calibri',13),bg = "white")
#lb14   = tk.Label(wd,text="GST & HST",font=('Calibri',15))
lb14_1  = tk.Label(wd,text="@ 5%",font=('Calibri',9),bg = "white")
lb15    = tk.Label(wd,text="Rs./-",font=('Calibri',13),bg = "white") 
#lb16_1 = tk.Label(wd,text="Conversion",font=('Calibri',15)) 
#lb16_2 = tk.Label(wd,text="Charge",font=('Calibri',15)) 
lb16_3  = tk.Label(wd,text="@ 1%",font=('Calibri',9),bg = "white")
lb17    = tk.Label(wd,text="Rs./-",font=('Calibri',13),bg = "white")
#lb18   = tk.Label(wd,text="Total Charge*",font=('Calibri',15))
lb18_1  = tk.Label(wd,text="*Toll Parking if any are extra.",font=('Calibri',"11","italic"),bg = "white")
lb19    = tk.Label(wd,text="Rs./-",font=('Calibri',13),bg = "white")

lb20    = tk.Label(wd, text="Currency Conversion", width=25,fg="white",bg = "dark green",font=("Times", "15", "bold italic"),relief='ridge') 

lb21    = tk.Label(wd, text="Geographical Map", width=22,fg="white",bg = "dark green",font=("Times", "15", "bold italic"),relief='ridge') 

#lb22    = tk.Label(wd, text="Emergency Call : 1800 0000 1234", width=30,bg = "orange red",font=("Times", "15", "bold italic")) 



#Placement
lb00.place(x=465,y=20)
lb01.place(x=380,y=70)
lb02.place(x=710,y=720)
lb03.place(x=330,y=720)



lb0.place(x=50,y=170)
lb1.place(x=50,y=210)
lb2.place(x=50,y=250)
lb3.place(x=50,y=290)
lb4.place(x=50,y=330)
lb5.place(x=50,y=370)
lb5_1.place(x=50,y=410)

lb6.place(x=380, y=170)
lb7.place(x=380, y=210)
lb8.place(x=380, y=250)
lb8_0.place(x=380, y=290)
lb8_00.place(x=560, y=290)
lb8_1.place(x=380, y=410)

lb9.place(x=50, y=450)
#lb10.place(x=50,y=490)
lb10_1.place(x=50,y=512)
lb11.place(x=240,y=495)
#lb12.place(x=50,y=530)
lb12_1.place(x=50,y=552)
lb13.place(x=240,y=535)
#lb14.place(x=50,y=570)
lb14_1.place(x=50,y=592)
lb15.place(x=240,y=575)
#lb16_1.place(x=50,y=610)
#lb16_2.place(x=50,y=630)
lb16_3.place(x=50,y=635)
lb17.place(x=240,y=615)
#lb18.place(x=50,y=660)
lb18_1.place(x=50,y=695)
lb19.place(x=240,y=665)


lb20.place(x=380,y=450)

lb21.place(x=665,y=170)

#lb22.place(x=630,y=620)
#lb22    = tk.Label(wd, text="Emergency Call : 1800 0000 1234", width=30,bg = "orange red",font=("Times", "15", "bold italic")) 

B22 = Button(wd,text='Emergency Call : 1800 0000 1234',width=230,bg = "orange red",font=("Times", "15", "bold italic"),command=save_details).place(x=640,y=620)


#Entry Intro
name_var = tk.StringVar()
e1=tk.Entry(wd,width=15,textvariable=name_var)
e1.place(x=150,y=210)
#mob_var = tk.StringVar()
#e2=tk.Entry(wd,width=15,textvariable=mob_var)
#e2.place(x=150,y=250)
age_var = tk.StringVar()
e3=tk.Entry(wd,width=15,textvariable=age_var)
e3.place(x=150,y=290)
nat_var = tk.StringVar()
e5=tk.Entry(wd,width=15,textvariable=nat_var)
e5.place(x=150,y=370)
ref_var = tk.StringVar()
e5_1=tk.Entry(wd,width=15,textvariable=ref_var)
e5_1.place(x=150,y=410)


def mask_phone_number(entry):
    phone_number = entry.get()
    if len(phone_number) > 3:
        masked_phone_number = "*" * (len(phone_number) - 3) + phone_number[-3:]
        entry.delete(0, tk.END)
        entry.insert(0, masked_phone_number)

# Create the entry widget for the phone number
mob_var = tk.StringVar()
e2 = tk.Entry(wd, show="*",width=15,textvariable=mob_var)
e2.place(x=150,y=250)
# Bind the function to the entry widget so that it's called whenever the user types in the entry box
e2.bind("<KeyRelease>", lambda event: mask_phone_number(e2))



# e7=tk.Entry(wd,width=15)
# e7.place(x=405,y=235)
dist_var = tk.StringVar()
e8_0=tk.Entry(wd,width=8,textvariable=dist_var)
e8_0.place(x=470,y=290)


#e10=tk.Entry(wd,width=6)
#e10.place(x=170,y=490)
# e12=tk.Entry(wd,width=6)
# e12.place(x=170,y=530)
# e15=tk.Entry(wd,width=6)
# e15.place(x=170,y=570)
# e16=tk.Entry(wd,width=6)
# e16.place(x=170,y=610)
# e18=tk.Entry(wd,width=6)
# e18.place(x=170,y=660)



#Radio Button
Gender_selected = tk.StringVar()
Gender_selected.set('M')
R4_1=tk.Radiobutton(wd,text='M',value='M', fg='White', font=("Times", "13", "bold italic"),bg='cornflowerblue',variable=Gender_selected)
R4_1.place(x=150,y=330)
R4_2=tk.Radiobutton(wd,text='F',value='F',fg='White',font=("Times", "13", "bold italic"),bg='cornflowerblue',variable=Gender_selected)
R4_2.place(x=195,y=330)
R4_3=tk.Radiobutton(wd,text='Trans',fg='White',font=("Times", "13", "bold italic"),bg='cornflowerblue',value='Trans',variable=Gender_selected)
R4_3.place(x=235,y=330)

Cabtype_selected = tk.StringVar()
Cabtype_selected.set("Standard        [4Persons]")
R4_1=tk.Radiobutton(wd,text="Standard        [4Persons]",fg='White',bg = "cornflowerblue",value="Standard        [4Persons]",font=("Times","15","bold italic"),variable=Cabtype_selected)
R4_1.place(x=380,y=330)
R4_2=tk.Radiobutton(wd,text="Prime Sedan  [4Persons/Bag]",fg='White',bg = "cornflowerblue",value="Prime Sedan  [4Persons/Bag]",font=("Times","15","bold italic"),variable=Cabtype_selected)
R4_2.place(x=380,y=350)
R4_2=tk.Radiobutton(wd,text="Prime SUV    [6Persons]" ,fg='White',bg = "cornflowerblue",value="Prime SUV    [6Persons]",font=("Times","15","bold italic"),variable=Cabtype_selected)
R4_2.place(x=380,y=370)

Insurance_selected = tk.StringVar()
Insurance_selected.set("Y")
R8_1=tk.Radiobutton(wd,text='Y',value='Y',fg='White',font=("Times", "13", "bold italic"),bg = "cornflowerblue",variable=Insurance_selected)
R8_1.place(x=470,y=410)
R8_2=tk.Radiobutton(wd,text='N',value='N',fg='White',font=("Times", "13", "bold italic"),bg = "cornflowerblue",variable=Insurance_selected)
R8_2.place(x=510,y=410)



#Combo Box
pickeds = tk.StringVar()
pickedd = tk.StringVar()
citys = ttk.Combobox(wd,textvariable=pickeds,width=10)
cityd = ttk.Combobox(wd,textvariable=pickedd,width=10)
citys['values']=('Chennai','Coimbatore','Kanyakumari','Kodaikanal','Madurai','Ooty','Pondicherry','Rameswaram','Salem','Thanjavur','Theni','Thoothukudi','Tiruchirappalli','Tirunelveli')
citys.place(x=470,y=210)
cityd['values']=('Chennai','Coimbatore','Kanyakumari','Kodaikanal','Madurai','Ooty','Pondicherry','Rameswaram','Salem','Thanjavur','Theni','Thoothukudi','Tiruchirappalli','Tirunelveli')
cityd.place(x=470,y=250)


# Button
B1 = Button(wd,text='Ride Now',width=200,bg = "orange",font=("Times", "15", "bold italic"),command=save_details).place(x=655,y=550)


######################### CHARGE CALCULATIONS  ################################
# 1. Base Charges
def base_charges():
    if Cabtype_selected.get() == "Standard        [4Persons]":
        basecharges = 500
    elif Cabtype_selected.get() == "Prime Sedan  [4Persons/Bag]":
        basecharges = 700
    else:
        basecharges = 1000
        
    result_base_charges.configure(text="" + str(basecharges))
    
    #Placing the value inside the entry box
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,basecharges)
    t1.config(state='disabled')
   
Base_button  = tk.Button(wd, text="Base Charge",  command=base_charges,font=("Monospace", 12)).place(x=50, y =490)
result_base_charges = tk.Label(wd, text="",bg='cornflowerblue')
result_base_charges.place(x=170,y=490)
t1=tk.Text(wd,width=8,height=1,state="disabled")
t1.place(x=170,y=495)


# 2. Distance Charges
def dist_charges():
    dist = int(dist_var.get())
    distcharge = 18 * dist 
    result_dist_charges.configure(text="" + str(distcharge))
    
    #Placing the value inside the entry box
    t2.config(state='normal')
    t2.delete('1.0', tk.END)
    t2.insert(tk.END,distcharge)
    t2.config(state='disabled')
   
Dist_button  = tk.Button(wd, text="Charge/Dist" ,  command=dist_charges, font=("Monospace", 12)).place(x=50, y =530)
result_dist_charges = tk.Label(wd, text="",bg='cornflowerblue')
result_dist_charges.place(x=170,y=530)
t2=tk.Text(wd,width=8,height=1,state="disabled")
t2.place(x=170,y=535)


# 3. Tax(GST & HST) Charges
def tax_charges():
    if Cabtype_selected.get() == "Standard        [4Persons]":
        basecharges = 500
    elif Cabtype_selected.get() == "Prime Sedan  [4Persons/Bag]":
        basecharges = 700
    else:
        basecharges = 1000
            
    dist = int(dist_var.get())
    distcharge = 18 * dist
    taxcharge = int((distcharge + basecharges) * 0.05)
    result_tax_charges.configure(text="" + str(taxcharge))
    
    #Placing the value inside the entry box
    t3.config(state='normal')
    t3.delete('1.0', tk.END)
    t3.insert(tk.END,taxcharge)
    t3.config(state='disabled')
   
Tax_button   = tk.Button(wd, text="GST & HST" ,    command=tax_charges, font=("Monospace", 12)).place(x=50, y =570)
result_tax_charges = tk.Label(wd, text="",bg='cornflowerblue')
result_tax_charges.place(x=170,y=570)
t3=tk.Text(wd,width=8,height=1,state="disabled")
t3.place(x=170,y=575)


# 4. Conversion Charges
def conv_charges():
    conv = int(wd.amount_entry.get())
    convcharges = 0.01 * conv
    result_conv_charges.configure(text="" + str(convcharges),bg='cornflowerblue')
    
    #Placing the value inside the entry box
    t4.config(state='normal')
    t4.delete('1.0', tk.END)
    t4.insert(tk.END,convcharges)
    t4.config(state='disabled')
   
Conv_button  = tk.Button(wd, text="Conv Charge" ,command=conv_charges, font=("Monospace", 12)).place(x=50, y =610)
result_conv_charges = tk.Label(wd, text="",bg='cornflowerblue')
result_conv_charges.place(x=170,y=610)
t4=tk.Text(wd,width=8,height=1,state="disabled")
t4.place(x=170,y=615)

# 5. Total Charges
def total_charges():
    if Cabtype_selected.get() == "Standard        [4Persons]":
        basecharges = 500
    elif Cabtype_selected.get() == "Prime Sedan  [4Persons/Bag]":
        basecharges = 700
    else:
        basecharges = 1000
            
    dist = int(dist_var.get())
    distcharge = 18 * dist
    
    taxcharge = int((distcharge + basecharges) * 0.05)
        
    if Insurance_selected.get() == "Y":
        Insurcharge = 5
    else:
        Insurcharge = 0
        
    codelist = ['V1A2A7S8','D13H14K19A20','S3A4H9W10','I15V16N21A22','N5T6I11N12','Y17A18G23A24']    
    if ref_var.get() in codelist:
        Refdisc = 100
    else:
        Refdisc = 0
  
    totalcharges = (basecharges + distcharge + taxcharge + Insurcharge) - Refdisc
    result_total_charges.configure(text="" + str(totalcharges))
    
    #Placing the value inside the entry box
    t5.config(state='normal')
    t5.delete('1.0', tk.END)
    t5.insert(tk.END,totalcharges)
    t5.config(state='disabled')
   
Total_button = tk.Button(wd, text="Total Charge*" ,command=total_charges, font=("Monospace", 12)).place(x=50, y=660)
result_total_charges = tk.Label(wd, text="",bg='cornflowerblue')
result_total_charges.place(x=170,y=660)
t5=tk.Text(wd,width=8,height=1,state="disabled")
t5.place(x=170,y=665)

# ListBox
# lb22=tk.Listbox(wd)
# lb22.place(x=650,y=220,width=220,height=200)

###############################################################################


################################# Clock #######################################

import time
def digital_clock(): 
   time1 = time.strftime("%I:%M:%S %p")
   clock.config(text=time1) 
   clock.after(1000, digital_clock)
   
clock = tk.Label(wd,font=('times',14,'bold'),bg='black',fg='Yellow') 
clock.place(x=440, y=120)
digital_clock()
###############################################################################


############################ Data and Time ####################################

import datetime as dt
date = dt.datetime.now()
label = tk.Label(wd, text=f"{date:%A, %B %d, %Y}", font=('times',14,'bold'),bg='black',fg='Yellow')
label.place(x=405,y=140)
###############################################################################


########################### Currency Convertor ################################

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
 
    def convert(self, from_currency, to_currency, amount): 
        #initial_amount = amount 
        if from_currency != 'USD' :
            amount = amount / self.currencies[from_currency]
 
        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount
    

# GUI class
class GUI(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        #self.title('ONE GO')
        #self.geometry('900x600')
        #self.resizable(0, 0)            

        self.currency_converter = converter
        
        # creating the labels and entry widgets
        self.from_label = tk.Label(wd, text="From", bg='white',font=("Monospace", 15),relief = "groove")

        self.from_label.place(x=380, y=490)
        self.from_var = tk.StringVar(wd)
        self.from_var.set("INR")
        
        self.from_dropdown = tk.OptionMenu(wd, self.from_var, *self.currency_converter.currencies.keys())
        self.from_dropdown.place(x=520, y=490)
        
        self.amount_label = tk.Label(wd, text="Home Currency",bg='white',font=("Monospace", 15),relief = "groove")
        self.amount_label.place(x=380, y=590)
        
        self.amount_entry = tk.Entry(wd,width=6)
        self.amount_entry.place(x=520, y=590)
        
        self.to_label = tk.Label(wd, text="To",bg='white',font=("Monospace", 15),relief = "groove")
        self.to_label.place(x=380, y=540)
        self.to_var = tk.StringVar(wd)
        self.to_var.set("USD")
        
        self.to_dropdown = tk.OptionMenu(wd,self.to_var, *self.currency_converter.currencies.keys())
        self.to_dropdown.place(x=520, y=540)
        
        self.converted_label = tk.Label(wd, text="", bg='cornflowerblue')
        self.converted_label.place(x=475, y=670)
        
        self.convert_button = tk.Button(wd, text="Converted Amt" ,bg='white', font=("Monospace", 15),relief = "groove",command=self.convert)
        self.convert_button.place(x =420, y =630)


    def convert(wd):
        from_currency = wd.from_var.get()
        to_currency = wd.to_var.get()
        amount = float(wd.amount_entry.get())
        converted_amount = wd.currency_converter.convert(from_currency, to_currency, amount)
        wd.converted_label.config(text=str(converted_amount))

###############################################################################




########################### Weather Updation ##################################
def get_weather(city):
       # Unique OpenWeatherMap API key
       api_key      = 'c0e4d6f99e947f7abd25878c34555904'
       url1         = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
       response     = requests.get(url1)
       weather_data = response.json()

       # Extract the relevant weather information
       description  = weather_data['weather'][0]['description'].title()
       temperature  = weather_data['main']['temp']
       humidity     = weather_data['main']['humidity']
       wind_speed   = weather_data['wind']['speed']

       # Display the weather information in the GUI
       weather_label.config(text=f'{description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h',bg='white')


# Create the input field and submit button
#city_entry = tk.Entry(wd, font=('Arial', 14))
#city_entry.pack(pady=10)
submit_button = Button(wd, text='Weather @ Destination',fg="white",bg = "dark green",font=("Times", "15", "bold italic"),highlightbackground='#3E4149', command=lambda: get_weather(cityd.get()))
submit_button.place(x=660,y=25)

# Create the label to display the weather information
weather_label = tk.Label(wd, font=('Constantia','16','bold italic'),fg='saddlebrown', bg='cornflowerblue',justify='left')
weather_label.place(x=660,y=65)    
###############################################################################



# ################################ App Icon ###################################
load = Image.open("/Users/vasanthdhanagopal/Desktop/Soft Logic Systems/Codethon/Final Project/Images/CWS.png")
render = ImageTk.PhotoImage(load)
wd.iconphoto(False, render)
###############################################################################



################################ Image Insertion ##############################

#Load the image using PIL
image = Image.open('/Users/vasanthdhanagopal/Desktop/Soft Logic Systems/Codethon/Final Project/Images/frt.png')
photo = ImageTk.PhotoImage(image)

# Create a canvas to display the image
canvas = tk.Canvas(wd, width=240, height=130,relief='raised')
canvas.place(x=50,y=15)

# Set the image as the background of the canvas
canvas.create_image(1, 1, anchor=tk.NW, image=photo)


image2 = Image.open('/Users/vasanthdhanagopal/Desktop/Soft Logic Systems/Codethon/Final Project/Images/mapsimage2.png')
photo2 = ImageTk.PhotoImage(image2)

# Create a canvas to display the image
canvas2 = tk.Canvas(wd, width=220, height=200,relief='raised')
canvas2.place(x=640,y=220)

# # Set the image as the background of the canvas
canvas2.create_image(1, 1, anchor=tk.NW, image=photo2)

# #Define the PhotoImage Constructor by passing the image file
# img= ImageTk.PhotoImage(file='/Users/vasanthdhanagopal/Desktop/Soft Logic Systems/Codethon/Project/vasan1.png', master= wd)
# img_label= tk.Label(wd,image=img)

# #define the position of the image
# img_label.place(x=0, y=0)

###############################################################################        
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    wd = GUI(converter)
    wd.mainloop()
        



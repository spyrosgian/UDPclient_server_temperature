# Importing necessary Python packages:
import socket
import sys
from tkinter import *

# Creating temperature server-client interface

def clear():
    txt1.delete(0, END)
    txt2.config(state = NORMAL)
    txt2.delete(0, END)
    txt2.config(state = DISABLED)
    txt3.config(state = NORMAL)
    txt3.delete(0, END)
    txt3.config(state = DISABLED)

def convert():
    # Taking Centigrade temperature from interface:
    dataclient = txt1.get()
    
    # Deleting previous status message.
    txt3.config(state = NORMAL)
    txt3.delete(0, END)
    txt3.config(state = DISABLED)

    # Defining clent constants:
    SERVER = "localhost"
    PORT = 5000
    ADDR = (SERVER, PORT)
    FORMAT = "utf-8"

    # Checking if users input is a positive number:
    if dataclient.isdigit():
        # Creating client socket:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
                # Sending Centigrafe temperature to server: 
                client.sendto(dataclient.encode(FORMAT), ADDR)
                # Receiving (coverted) Fahrenheit temperature from server:
                dataserver = client.recv(8192).decode(FORMAT)
                # Printing received Fahrenheit temperature to interface:
                txt2.config(state = NORMAL)
                txt2.insert(END, dataserver)
                txt2.config(state = DISABLED)
        except socket.error:
                txt3.config(state = NORMAL)
                txt3.insert(END, "Server not available.")
                txt3.config(state = DISABLED)  
        finally:
                client.close
    else:
        # Presenting message if server is not available:
        clear()
        txt3.config(state = NORMAL)
        txt3.insert(END, "Input not an integer.")
        txt3.config(state = DISABLED)


def exit():
    sys.exit()

#Creating root instance and defining properties:
intface = Tk()
intface.title("Temperature Conversion")
intface.geometry("300x250")
intface.resizable(False, False)

#Creating and placing interface labels:
lbl1 = Label(text = "Temperature Converion",
        bg = "red", font = ("Normal", 12, "bold"),
        bd = 2, relief = "raised")
lbl1.place(x = 0, y = 0,
        width = 300, height = 50)

lbl2 = Label(text = "Centigrade",
        bg = "cyan", font = ("Normal", 12, "bold"),
        bd = 2, relief = "raised")
lbl2.place(x = 0, y = 50,
        width = 200, height = 50)

lbl3 = Label(text = "Fahrenheit",
        bg = "cyan", font = ("Normal", 12, "bold"),
        bd = 2, relief = "raised")
lbl3.place(x = 0, y = 100, 
        width = 200, height = 50)

lbl4 = Label(text = "Status",
        bg = "cyan", font = ("Normal", 12, "bold"),
        bd = 2, relief = "raised")
lbl4.place(x = 0, y = 200, 
        width = 100, height = 50)

#Creating interface text inputs:
txt1 = Entry(bg = "yellow3", bd = 2, relief = "solid",
        font = ("Normal", 12), justify = "center")
txt1.place(x = 200, y = 50,
        width = 100, height = 50)

txt2 = Entry(bd = 2, relief = "solid",
        font = ("Normal", 12), justify = "center")
txt2.place(x = 200, y = 100,
        width = 100, height = 50)
txt2.config(state = DISABLED) 

txt3 = Entry(bd = 2, relief = "solid",
        font = ("Normal", 12), justify = "center")
txt3.place(x = 100, y = 200,
        width = 200, height = 50)
txt3.config(state = DISABLED)  

#Creating interface buttons:
btn1 = Button(text = "Done",
        bg = "Orange", font = ("Normal", 12, "bold"),
        bd = 2, relief = "raised",
        command = exit)
btn1.place(x = 200, y = 150,
        width = 100, height = 50)

btn2 = Button(text = "Clear",
        bg = "Orange", font = ("Normal", 12, "bold"),
        bd = 2, relief = "raised",
        command = clear)
btn2.place(x = 0, y = 150,
        width = 100, height = 50)

btn3 = Button(text = "Convert",
        bg = "Orange", font = ("Normal", 12, "bold"),
        bd = 2, relief = "raised",
        command = convert)
btn3.place(x = 100, y = 150,
        width = 100, height = 50) 

intface.mainloop()
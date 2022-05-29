from fileinput import filename
import tkinter as tk
from tkinter import StringVar, filedialog, Text
import os
from pubchemscrape import *
import csv

root = tk.Tk()
inventory = []

if os.path.isfile('save.csv'):
    with open('save.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            inventory.append(row)
    

def saveData():
    with open('save.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for chemical in inventory:
            writer.writerow(chemical)

def findInfo(cas, mass, quantity, unit):
    attributeList = find_chem_info(cas)
    attributeList.insert(1, cas)
    quantityMassStr = quantity + "x" + mass
    attributeList.insert(2, quantityMassStr)
    attributeList.insert(3, unit)
    inventory.append(attributeList)
    saveData()

print(inventory)
canvas = tk.Canvas(root, height=300, width=500, bg="#263D42")
canvas.pack() 

frame = tk.Frame(root, bg="#263D42")
frame.place(relwidth=0.95, relheight=0.9, relx=0.025, rely=0.025)

openFile = tk.Label(frame, text="CAS Number", bg="white", fg="#263D42")
openFile.grid(row=0, column=0, padx= 5, pady= 5)

casNumber = tk.Entry(frame, bg="white", fg="#263D42")
casNumber.grid(row=0, column=1, padx= 5, pady= 5)

massLabel = tk.Label(frame, text= "Mass", bg="white", fg="#263D42")
massLabel.grid(row=1, column=0, padx= 5, pady= 5)

massEntry = tk.Entry(frame, bg="white", fg="#263D42")
massEntry.grid(row=1, column=1, padx= 5, pady= 5)

quantityLabel = tk.Label(frame, text= "Quantity", bg="white", fg="#263D42")
quantityLabel.grid(row=2, column=0, padx= 5, pady= 5)

quantityEntry = tk.Entry(frame, bg="white", fg="#263D42")
quantityEntry.grid(row=2, column=1, padx= 5, pady= 5)

value = StringVar()
value.set("g")
unitOptions = tk.OptionMenu(frame, value, "g", "mL", "kg")
unitOptions.grid(row=1, column=2, padx=5, pady=5)

openFile = tk.Button(frame, text="Enter", padx=10, pady=5, 
                    fg="white", bg="#263D42", command= lambda: findInfo(casNumber.get(), massEntry.get(), quantityEntry.get(), value.get()))
openFile.grid(row=3, column=1, padx= 5, pady= 5)

root.mainloop()

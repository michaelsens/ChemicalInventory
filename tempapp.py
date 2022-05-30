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
    print(inventory)
    
def saveData():
    with open('save.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for chemical in inventory:
            writer.writerow(chemical)

def compareChemicals(chemicalOne, chemicalTwo):
    for idx, chem in enumerate(chemicalOne):
        print(idx)
        if idx == 2:
            massOne = chemicalOne[idx].split("x")[1]
            massTwo = chemicalTwo[idx].split("x")[1]
            if massOne != massTwo: return False
        elif chemicalOne[idx] != chemicalTwo[idx]: return False
    return True

def addChemical(chemical):
    inInventory = False
    for listChemical in inventory:
        if(compareChemicals(chemical, listChemical)):
            quantityInv = listChemical[2].split("x")
            quantityInv[0] = str(int(chemical[2].split("x")[0]) + int(quantityInv[0]))
            quantityInv = "x".join(quantityInv)
            listChemical[2] = quantityInv
            inInventory = True
    if not inInventory: inventory.append(chemical)

def findInfo(cas, mass, quantity, unit, state):
    attributeList = find_chem_info(cas)
    attributeList.insert(1, cas)
    quantityMassStr = quantity + "x" + mass
    attributeList.insert(2, quantityMassStr)
    attributeList.insert(3, unit)
    attributeList.insert(4, state)
    addChemical(attributeList)
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

stateValue = StringVar()
stateValue.set("solid")
stateOptions = tk.OptionMenu(frame, stateValue, "solid", "liquid", "gas")
stateOptions.grid(row=2, column=2, padx=5, pady=5, sticky="W")

value = StringVar()
value.set("g")
unitOptions = tk.OptionMenu(frame, value, "g", "mL", "kg")
unitOptions.grid(row=1, column=2, padx=5, pady=5, sticky="W")

enterButton = tk.Button(frame, text="Enter", padx=10, pady=5, 
                    fg="#263D42", bg="white", command= lambda: findInfo(casNumber.get(), massEntry.get(), quantityEntry.get(), value.get(), stateValue.get()))
enterButton.grid(row=2, column=3, padx= 5, pady= 5, sticky="E")

root.mainloop()

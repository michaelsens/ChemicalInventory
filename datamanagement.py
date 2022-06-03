from fileinput import filename
import os

import attr
from pubchemscrape import *
import csv

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

def compareChemicals(chemicalOne, chemicalTwo):
    for idx, chem in enumerate(chemicalOne):
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
    saveData()

def findInfo(cas, mass, quantity, unit, state):
    attributeList = find_chem_info(cas)
    attributeList.insert(1, cas)
    quantityMassStr = quantity + "x" + mass
    attributeList.insert(2, quantityMassStr)
    attributeList.insert(3, unit)
    attributeList.insert(4, state)
    addChemical(attributeList)
    return attributeList
    

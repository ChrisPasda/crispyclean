import pandas as pd
import xlwings as xw
import numpy as np
pd.set_option('display.precision',100)

counter = 0
list1 = []
list2 = []
list3 = []


PATH = 'F:\Programmieren\mdm.xlsx'
wb = xw.Book(PATH)
sheetGeräte = wb.sheets['Geräte Pool-Vergabe']
sheetBank = wb.sheets['MDM Bank']
sheetService = wb.sheets['MDM Service']

#print(type(sheetGeräte))


df = sheetGeräte['A1:T1520'].options(pd.DataFrame, index=True, header = True).value
af = sheetBank['A8:D1256'].options(pd.DataFrame, index=True, header = True).value

df = df.set_index(["Nachname"])

df = df.drop("Pool",0)

df = df.reset_index()

pf = df.loc[:, "Nachname"]
cf = df.loc[:, 'IMEI-Nummer']
gf = af.loc[:, 'IMEI']

def search(list1):
    for item in list1:
        if '354200072240011' != item:
            print('nicht Vorhanden')



def saveAsExcel(list, Name):

   name = pd.DataFrame(list)

   writer = pd.ExcelWriter(Name, engine='xlsxwriter')

   name.to_excel(writer, sheet_name='Sheet1')

   writer.save()

def checkImei(cf,gf):
   global counter
   for rowD in cf:
       for rowA in gf:
           if (rowD == rowA and len(str(rowD)) > 5):
               list1.append(rowD)
               counter += 1
   c = np.array(list1)
   return c


def nameToList(pf):
    for row in pf:
        list2.append(row)
    c = np.array(list2)
    return c

def imeiToList(cf):
    for row in cf:
        list3.append(row)
    c = np.array(list3)
    return c

def check(list):
    for index, row in enumerate(list):
        for index, cell in enumerate(row):
            print(cell)
Namen = []

#print(len(checkImei(cf,gf)))
nameToList(pf)
imeiToList(cf)
list4 = np.array([list(a) for a in zip(list3, list2)])


print(list4)

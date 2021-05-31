from tkinter import *
import Image

while(1):

   menu = int(input('Was möchten Sie tun\n'
                     ' 1.Bild einlesen\n'
                     ' 2.Bild analysieren\n'
                     ' 3.Daten filtern\n'
                     ' 4.Daten in Excelliste speichern\n'
                     ' 5.exit\n'))
   if menu == 1:
       image = input('Dateinamen eingeben: ')
       saveImage = input('Unter welchem Namen soll das neue Bild gespeichert werden? ')
       Image.scaleImage(image, saveImage)
   elif menu == 2:
       c = Image.imageToString(image)
       for item in c:
           print(item)
   elif menu == 3:
       tupelList = Image.filterImage(c)
       print(c)
       Image.appendToList(tupelList)
   elif menu == 5:
       break

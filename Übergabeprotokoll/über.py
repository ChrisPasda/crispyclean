try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import webbrowser
import PIL.ImageGrab
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def openSide():
   name = input("Bitte geben Sie den Namen ein: ")
   side = ('http://e111spwmve2164b:81/dkb-intern/telefonbuch/phonebookSearch.do?command=searchFromHeader&&searchWords='+name)
   webbrowser.open(side)

def screenshot():
   im = PIL.ImageGrab.grab()
   im.show()
   save_path = "C:\\Users\\Chris\\github\\crispyclean\\übergabe\\snap.jpg"
   im.save(save_path)

def imageToString():
    image = 'snap.jpg'
    c = pytesseract.image_to_string(Image.open(image))
    return c

def filterImage(image):
    startV = 'Vorname '
    endV = ''

    startN = 'Nachname:*'
    endN  = ''

    startP = ' PE '
    endP = ''


    resultName = re.findall('%s(.*)%s' % (startV, endV), image)
    resultNachname = re.findall('%s(.*)%s' % (startN,endN), image)
    resultPE = re.findall('%s(.*)%s' % (startP,endP), image)

    name = str(resultName[0])
    pe = str(resultPE[0])
    pe = pe.split(',')[0]
    nachname = resultNachname[0].replace("* ","")

    #print(resultNachname)

    print(name)
    print(nachname)
    print(pe)




if __name__ == '__main__':

    #screenshot()
    text = imageToString()
    filterImage(text)

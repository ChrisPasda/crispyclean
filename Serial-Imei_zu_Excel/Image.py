try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import numpy as np
import cv2
import re
import pandas as pd   #pandas for handleing excelfile
from pandas import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

myList = []

def scaleImage(image, saveImage):
    img = cv2.imread(image,0)
    img = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)  #resize image for better accuracy
    #img = cv2.blur(img,(1,1))
    img = cv2.bilateralFilter(img,9,75,75)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(saveImage,img)

def imageToString(image):
    c = pytesseract.image_to_string(Image.open(image))
    return c

def filterImage(stringImage):
    print(stringImage)
    startS = '#:'
    endS = ''

    startI = 'MEID:'
    endI  = ''

    resultSerial = re.findall('%s(.*)%s' % (startS, endS), stringImage)
    resultImei = re.findall('%s(.*)%s' % (startI,endI), stringImage)
    print(resultSerial)
    print(resultImei)
    #resultImei.remove('Numbers')
    tupelList = zip(resultSerial,resultImei)
    print(tupelList)
    return tupelList

def importToExcel(tupelList):

    df = pd.DataFrame(tupelList)
    writer = ExcelWriter('Seriennummern.xlsx')  #define writer as name for the excelfile
    df.to_excel(writer,'Ipads',index=False)   #write data to excel with no index
    writer.save()

def appendToList(tupelList):
    myList.append(tupelList)

def returnList():
    return myList

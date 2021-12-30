import csv
import os
import re

import cv2
import pytesseract
from pdf2image import convert_from_path
from PIL import ImageFile
from pytesseract import Output

import cv2
from PIL import Image


class OCR:
    def __init__(self,image_location):
        self.image= image_location

    def mark_region_around_characters(self):
        image = cv2.imread(self.image)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        img_h,img_w,_ = image.shape
        img_boxes = pytesseract.image_to_boxes(image)

        for b in img_boxes.splitlines():
            b = b.split(' ')
            x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
            image = cv2.rectangle(image,(x,img_h-y),(w,img_h-h),(0,0,255),1)
        
        return image

    def mark_region_around_roi(self,roi=[]):
        # need to provide roi in array of tuples where [(x,y),[w,h])
        image = cv2.imread(self.image)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        if roi != []:
            for r in roi:
                image = cv2.rectangle(image,r[0],r[1], color=(255,0,255), thickness=1)
        
        return image

    def find(self,*argv,**kwargs):
        # in the args you could specific things you want to find:
        #current functions are:
        #dates
        #total price

        image = cv2.imread(self.image)
        text = str(pytesseract.image_to_string(image,config = kwargs['config']))

        data = {}
        for arg in argv:
            if arg == 'dates':
                dates = re.findall(r'\d+[/.-]\d+[/.-]\d+',text)
                data['dates'] = dates
            elif arg == 'total_price':
                total_price = re.findall(r'\$\s?[0-9,]+\.[0-9]{1,2}',text)
                if total_price != []:
                    total_price = [float(re.sub(r'[$,]',"",price)) for price in total_price]
                    data['total_price'] = max(total_price)
            
        data['text'] = str(pytesseract.image_to_string(image, config='--psm 6'))
        return data

dir_path =os.path.dirname(os.path.realpath(__file__))
pdf_path = os.path.join(dir_path,'sample.pdf')
image_location = os.path.join(dir_path,'images/sample1.jpg')

o = OCR(image_location)
text = o.find('dates','total_price',config='--psm 6')
print(text)

# i = o.mark_region_around_characters()

# cv2.imshow('Result',i)
# cv2.waitKey(0)

# roi = [[(45,472),(107,588)],
#        [(117,476),(294,588)],
#        [(436,479),(550,592)],
#        [(619,479),(707,587)],
#        ]

# i = o.mark_region_around_roi(roi=roi)

# cv2.imshow('Result',i)
# cv2.waitKey(0)













    
    








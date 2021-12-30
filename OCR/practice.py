import csv
import os
import re

import cv2
import pytesseract
from matplotlib import pyplot as plt
from pdf2image import convert_from_path
from PIL import ImageFile
from pytesseract import Output

dir_path =os.path.dirname(os.path.realpath(__file__))
pdf_path = os.path.join(dir_path,'sample.pdf')
image_location = os.path.join(dir_path,'sample.png')




import cv2
from PIL import Image


# def mark_region(image_path):
    
#     im = cv2.imread(image_path)

#     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (9,9), 0)
#     thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

#     # Dilate to combine adjacent text contours
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
#     dilate = cv2.dilate(thresh, kernel, iterations=4)

#     # Find contours, highlight text areas, and extract ROIs
#     cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = cnts[0] if len(cnts) == 2 else cnts[1]

#     img_h,img_w,img_z = im.shape

#     line_items_coordinates = []
#     for c in cnts:
#         area = cv2.contourArea(c)
#         x,y,w,h = cv2.boundingRect(c)

#         # if y >= 600 and x <= 1000:
#         #     if area > 10000:
#         line_items_coordinates.append([(x,y), (w,h)])

#         # if y >= 2400 and x<= 2000:
#         #     im = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=1)
#         #     line_items_coordinates.append([(x,y), (2200, y+h)])

#     im = cv2.rectangle(im, (45,472),(107,588), color=(255,0,255), thickness=1)
#     im = cv2.rectangle(im, (117,476),(294,588), color=(255,0,255), thickness=1)
#     im = cv2.rectangle(im, (436,479),(550,592), color=(255,0,255), thickness=1)
#     im = cv2.rectangle(im, (619,479),(707,587), color=(255,0,255), thickness=1)


    

#     return im, line_items_coordinates

# image,cor = mark_region(image_location)

# cv2.imshow('Result',image)
# cv2.waitKey(0)




# pdfs = pdf_path
# pages = convert_from_path(pdfs,350)

# i=1
# for page in pages:
#     image_name = "Page_" + str(i) + ".jpg"
#     page.save(image_name,"JPEG")
#     i = i + 1

# def mark_region(image_path):
#     image = cv2.imread(image_path)
#     image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#     img_h,img_w,img_z = image.shape
#     img_boxes = pytesseract.image_to_boxes(image)

#     for b in img_boxes.splitlines():
#         print(b)

    # data = pytesseract.image_to_data(image,output_type=Output.DICT)

    # print(data['text'])

# image = mark_region(image_location)

#     for b in img_boxes.splitlines():
#         b = b.split(' ')
#         x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#         image = cv2.rectangle(image,(x,img_h-y),(w,img_h-h),(0,0,255),1)
    
#     return image

# image = mark_region(image_location)


# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Akash.Chauhan1\AppData\Local\Tesseract-OCR\tesseract.exe'

#load the original image
image = cv2.imread(image_location)

text = str(pytesseract.image_to_string(image, config='--psm 6'))
print(text)

dates = re.findall(r'\d+[/.-]\d+[/.-]\d+',text)
total_price = re.findall(r'\$\s?[0-9,]+\.[0-9]{1,2}',text)

print(total_price)
print(dates)

# get co-ordinates to crop the image
# c = cor[1]
# print(c)
roi = [[(45,472),(107,588),'text','Sample'],
       [(117,476),(294,588),'text2','Sample2'],
       [(436,479),(550,592),'text3','Sample3'],
       [(619,479),(707,587),'text4','Sample4'],
       ]




my_data = []
# # cropping image img = image[y0:y1, x0:x1]
for r in roi:
    img = image[r[0][1]:r[1][1], r[0][0]:r[1][0]] 

# pytesseract image to string to get results
    text = str(pytesseract.image_to_string(img, config='--psm 6'))
    my_data.append(text.splitlines())

print(my_data)
cleaned_data = []

for data in my_data:
    cleaned_data.append([d for d in data if d != ''])

print(cleaned_data)

final_data_array = []

for i,data in enumerate(cleaned_data,0):

    final_data_array.append([data[i] for data in cleaned_data])

for f in final_data_array:
    print(f)


with open('sample.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerows((final_data_array))
    








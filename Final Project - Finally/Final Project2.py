# Digital Commons Ingest Processing

#This code will perform a series of actions to process and prepare outsourced digitization work for ingest into the institutional repository.

#Starts at a parent folder [Box level, typically] and is reading sub-folders [item level]
#Establish logging library
# Start a timer
#Convert TIFF files into JPG files within each sub-folder
#Convert JPGs within each sub-folder into a PDF
#Create a new folder at the parent folder level called "ingest_[parent_folder_name]_[date]"
#Copy all PDFs from the sub-folders into "ingest_[parent_folder_name]"
#Run OCR on each PDF in Ingest Folder using PyTesseract: https://pypi.org/project/pytesseract/.

#LOGGING
import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#TIMER
import time
start_time_Guru99 = time.time()
print("Time elapsed after some level wait...")
print("The start time is", start_time_Guru99)
time.sleep(1)

#CONVERT TIF TO JPG
import os
from os import listdir
from PIL import Image

i = 1

folder_dir = "/Users/ab_home/Desktop/Sample_Combined_Files"
for images in os.listdir(folder_dir):

    if(images.endswith(".tif")):
        img_tif = Image.open(images)
        rgb = img_tif.convert("RGB")
        img_filename = os.path.splitext(images)[0]
        rgb.save("/Users/ab_home/Desktop/Sample_Combined_Files/" + img_filename + '.jpg')
        # rgb.save("/Users/ab_home/Desktop/Sample_Combined_Files/" + str(i) + '.jpg')
        # i = i + 1

#RUN OCR ON JPG
import pytesseract
import cv2

folder_dir = "/Users/ab_home/Desktop/Sample_Combined_Files"
for images in os.listdir(folder_dir):

    if(images.endswith(".jpg")):
        image = cv2.imread(images)
        text = pytesseract.image_to_string(image)
        print(text)

#COMBINE
import os
import img2pdf

try:
    list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(
        "/Users/ab_home/Desktop/Sample_Combined_Files/", x)),
                        os.listdir("/Users/ab_home/Desktop/Sample_Combined_Files/") ) )

    with open("../../../Desktop/Sample_Combined_Files/output.pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in list_of_files if i.endswith(".jpg")]))

except:
    print("Something Went Wrong!")
else:
    print("All is well!")

#
# import os
# from PIL import Image # pip install pillow
#
# output_dir = './pdfs'
# source_dir = './images'
#
# for file in os.listdir("/Users/ab_home/Desktop/Sample_Combined_Files"):
#     if file.split('.')[-1] in ('.jpg'):
#         image = Image.open(file)
#         image_converted = image.convert('RGB')
#         image_converted.save(os.path.join('/Users/ab_home/Desktop/Sample_Combined_Files', '{0}.pdf'.format(file.split('.')[-2])))
#         # image_converted.save(os.path.join('/Users/ab_home/Desktop/Sample_Combined_Files', '{0}.pdf'.format(file.split('.')[-2])))
# from PyPDF2 import PdfMerger
# import os
#
# pdf = PdfMerger()
#
# for file in os.listdir("/Users/ab_home/Desktop/Sample_Combined_Files"):
#     if file.endswith(".pdf"):
#         pdf.append(file)
#
# pdf.write("/Users/ab_home/Desktop/Sample_Combined_Files/output.pdf")
# pdf.close()
# print("Merge complete!")

import glob

files = glob.glob('/Users/ab_home/Desktop/Sample_Combined_Files/*.jpg', recursive=True)

for f in files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

end_time_Guru99 = time.time()
print("The end time is", end_time_Guru99)


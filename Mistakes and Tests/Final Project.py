# Digital Commons Ingest Processing

#This code will perform a series of actions to process and prepare outsourced digitization work for ingest into the institutional repository.

#Starts at a parent folder [Box level, typically] and is reading sub-folders [item level]
#Establish logging library
# Start a timer
#Convert TIFF files into JPG files within each sub-folder
# try-except block
#Convert JPGs within each sub-folder into a PDF
# try-except block
#Transfer the name of the sub-folder onto the PDF file
# try-except block
#Create a new folder at the parent folder level called "ingest_[parent_folder_name]_[date]"
# try-except block
#Copy all PDFs from the sub-folders into "ingest_[parent_folder_name]"
# try-except block
#Run OCR on each PDF in Ingest Folder using PyTesseract: https://pypi.org/project/pytesseract/.
#Generate a CSV file with the names of each PDF and total number of pages within each PDF
# try-except block

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
end_time_Guru99 = time.time()
print("The end time is", end_time_Guru99)
print("Time elapsed in this example code: ", end_time_Guru99 - start_time_Guru99)

import os
from os import listdir
from PIL import Image

i = 1

folder_dir = "/Users/ab_home/Desktop/Sample_Combined_Files"
for images in os.listdir(folder_dir):

    if(images.endswith(".tif")):
        img_tif = Image.open(images)
        rgb = img_tif.convert("RGB")
        rgb.save("/Users/ab_home/Desktop/Sample_Combined_Files/" + str(i) + '.jpg')
        i = i + 1

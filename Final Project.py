# Digital Commons Ingest Processing

## This code will perform a series of actions to process and prepare outsourced digitization work for ingest into the institutional repository.

#Starts at a parent folder [Box level, typically] and is reading sub-folders [item level]
#Convert TIFF files into JPG files within each subfolder
#Convert JPGs within each folder into a PDF
#Transfer the name of the folder onto the PDF file
#Create a new folder at the parent folder level called "ingest_[parent_folder_name]"
#Copy all PDFs from the sub-folders into "ingest_[parent_folder_name]"
#Generate a CSV file with the names of each PDF and total number of pages within each PDF


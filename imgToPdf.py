from PIL import Image
from io import BytesIO
from pathlib import Path
from PyPDF2 import PdfMerger

# Specify the folder where the images are stored
image_folder = Path('namegoeshere') # path name here

# Create a list of all the image files in the folder
image_files = sorted(image_folder.glob('*.[jp][pn]g'))

# Prompts the user for the name of the PDF file
pdf_filename = input("Please name your new PDF file(no spaces or extensions): ") + ".pdf"


# Create a new PDF file
pdf_file = PdfMerger()


# Loop through all the image files and add them to the PDF
for image_file in image_files:
# Open the image and convert it to RGB format
    image = Image.open(image_file).convert('RGB')

# Create an in-memory PDF file and save the image to it
    pdf_bytes = BytesIO()
    image.save(pdf_bytes, format='PDF')
    pdf_bytes.seek(0)

    # Add the PDF bytes to the PDF file
    pdf_file.append(pdf_bytes)

# Save the PDF file
pdf_file.write(pdf_filename)

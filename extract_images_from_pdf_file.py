import fitz
import shutil
from pathlib import Path
import os
 
def extract_images_from_pdf_file(filepath):

    base_name = Path(filepath).stem

    pdf_file = fitz.open(filepath)
    image_list = pdf_file[0].get_images()
    
    for image_index, img in enumerate(image_list):
        xref = img[0]
        base_image = pdf_file.extract_image(xref)

        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        if not os.path.exists(f"./extracted_images/{base_name}"):
            os.makedirs(f"./extracted_images/{base_name}")
        
        try:
            with open(f'./extracted_images/{base_name}/{image_index}.{image_ext}', mode='wb') as file:
                file_out = file.write(image_bytes)
        except Exception as e:
            try:
                shutil.rmtree(f"./extracted_images/{base_name}")
            except OSError as e:
                print("Error: %s : %s" % (f"./extracted_images/{base_name}", e.strerror))

        

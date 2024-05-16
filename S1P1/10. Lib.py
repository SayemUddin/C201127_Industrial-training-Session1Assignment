from my_package.file1 import func
from my_package.file2 import square

print(func("Ifty"))
print(square(32))



pip install pytesseract
import pytesseract
from PIL import Image


image_path = "ifty.png"

# Open the image
image = Image.open(image_path)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)

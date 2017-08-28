from PIL import Image
import pytesser


image = Image.open('test.jpg')

print pytesser.image_file_to_string('test.jpg')
print pytesser.image_to_string(image)
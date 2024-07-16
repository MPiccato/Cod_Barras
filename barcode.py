import barcode
from PIL import Image #No encuentro esta librería
from barcode import ImageWriter

number = input("Ingresa el producto para generar el código de barrasÑ ")
barcode_format = barcode.get_barcode_class("upc")
my_barcode = barcode_format(number, writer = ImageWriter())
my_barcode.save('generated_barcode')

from PIL import Image
Image.open('generated_barcode.png')
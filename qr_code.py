#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:23:32 2020

@author: jeanwolf

Para mas info sobre insertar texto en el documento
https://recursospython.com/guias-y-manuales/anadir-texto-imagen-pillow/
"""
import pyqrcode
from PIL import Image, ImageDraw, ImageFont
# import os, sys
import xlrd

#-----------------------------
# Abrimos el fichero excel
document = xlrd.open_workbook("data/name.xlsx")

# Leer las celdas del libro de nombres 
Hoja1 = document.sheet_by_index(0)
contenido_celda = Hoja1.cell_value(2,2)
tex1 = Hoja1.cell_value(1,0)
tex2 = Hoja1.cell_value(1,1)

print(tex2)

# crear QR en formato PNG
big_code = pyqrcode.create(contenido_celda, error='L', version=9, mode='binary')
big_code.png('imagen/code.png', scale=5, module_color=[0, 0, 0, 128], background=None)


image = Image.open("imagen/cdertificado_ICOMOS_Virtual.png")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("font/CASLFS__.TTF", 103)

draw.text((500, 700), tex1, font=font, fill="black")
draw.text((300, 1000), tex2, font=font, fill="blue")
image.save("imagen/marte2.png")





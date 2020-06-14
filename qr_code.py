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
# import xlrd

#-----------------------------
# Abrimos el fichero excel
document = xlrd.open_workbook("data/ICOMOS Virtual.xlsx")

# Leer las celdas del libro de nombres 
Hoja1 = document.sheet_by_index(0)
# contenido_celda = Hoja1.cell_value(2,2)
tex1 = Hoja1.cell_value(1,2)
tex2 = Hoja1.cell_value(1,11)
tex3 = Hoja1.cell_value(1,8)
tex4 = Hoja1.cell_value(1,10)
print(tex2)
print("---------------")
# crear QR en formato PNG
big_code = pyqrcode.create(tex4, error='L', version=9, mode='binary')
big_code.png('imagen/code.png', scale=5, module_color=[0, 0, 0, 128], background=[0xFF, 0xFF, 0xFF])


image = Image.open("imagen/cdertificado_ICOMOS_Virtual.png")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("font/AGaramond-Semibold.otf", 73)
font1 = ImageFont.truetype("font/AGaramond-Semibold.otf", 32)

draw.text((775, 580), tex1, font=font, fill="black")
draw.text((775, 890), tex3, font=font, fill="green")
draw.text((1395, 953), tex2, font=font1, fill="black")
image.save("imagen/marte2.png")

    


# # __________________________________________________________________

# # Training: Python and GOES-R Imagery: Script 1
 
# # Required modules
# import cv2
# import numpy as np


# img1 = cv2.imread('imagen/python.png')
# gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# #bgr_gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# bgr_gray = np.stack((gray,) * 3, axis=-1)

# img2 = cv2.imread('imagen/house.png')
# tamaño1 = cv2.resize(bgr_gray, (320,280))
# tamaño2 = cv2.resize(img2, (320,280))
# dst = cv2.addWeighted(tamaño1, 0.7, tamaño2, 0.5, 0)
# cv2.imshow('mezcla',dst)
# cv2.waitKey(0)



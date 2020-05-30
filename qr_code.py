#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:23:32 2020

@author: jeanwolf
"""
# pyqrcode; Image y PIL son las dependencias requeridas
# pyqrcode genera los QR
# Image convierte un png a JPG

import pyqrcode
from PIL import Image
import os, sys
import xlrd

#Abrimos el fichero excel
document = xlrd.open_workbook("data/planets.xlsx")
 
#Podemos guardar cada una de las hojas por separado
Hoja1 = document.sheet_by_index(0)
contenido_celda = Hoja1.cell_value(1,2)
# conversatorio = "par"
# pio = contenido_celda, conversatorio 
# print(contenido_celda )
#-----------------------------

# crear QR
# url =  pyqrcode.create(contenido_celda, error='L', version=8, mode='binary')
# url.svg('imagen/code.svg', scale=16)

# crear PNG
big_code = pyqrcode.create(contenido_celda, error='L', version=10, mode='binary')
big_code.png('imagen/code.png', scale=10, module_color=[0, 0, 0, 128], background=[0xFF, 0xFF, 0xFF])

# convertir PNG a JPG
im = Image.open('imagen/code.png')
rgb_im = im.convert('RGB')
rgb_im.save('imagen/code.jpg', quality=95)

#---------------------------------------------------


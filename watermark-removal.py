#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:15:43 2020

@author: oyewunmi
"""
# importing necessary packages
from skimage import io
import numpy as np
import pdf2image
# from PIL import Image
import os

def select_pixel2(r,g,b):
    print(r, g, b)
    if r > 175 and r < 250 and g > 175 and g < 250 and b > 175 and b < 250:
        return True
    else:
        return False

def handle(imgs):
    for  i in range(imgs.shape[0]):
        for j in range(imgs.shape[1]):
            if select_pixel2(imgs[i][j][0],imgs[i][j][1],imgs[i][j][2]):
                imgs[i][j][0] =  imgs[i][j][1] = imgs[i][j][2] = 255
    return imgs

save_dir = os.getcwd()
# path to pdf file
file = 'test.pdf'

# converting to image using pdf2image
file_images = pdf2image.convert_from_path(file)
for image in file_images:
    image = np.array(image)
    # print(image.shape)
    image = handle(image)
    io.imsave(save_dir +'.jpg', image)

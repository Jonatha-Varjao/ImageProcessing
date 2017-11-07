# -*- coding: utf-8 -*-
from PIL import Image
import sys
sys.path.append('../OtsuBinarization')
from otsu import *
# COUNTOR EXTRACTION BASED ON MORPHOLOGICAL TRANSFORM 
# ORIGINAL IMAGE - EROSED IMAGE -> GIVES ME THE COUNTOR



def getPixel(image, coord ):
    try:
        p = image.getpixel(coord)
        return p
    except IndexError as e:
        return 0
    else:
        return 0

# STRUCTURING ELEMENT NEIGBOORHOOD 4
def elementoEstruturante_4(image, coord):
    p2 = getPixel( image, (coord[0]-1,coord[1]) )
    p4 = getPixel( image, (coord[0],coord[1]-1) )
    p5 = getPixel( image, (coord[0],coord[1]) ) 
    p6 = getPixel( image, (coord[0],coord[1]+1) )
    p8 = getPixel( image, (coord[0]+1,coord[1]) )    

    if p2 and p4 and p5 and p6 and p8 > 128:
        return 255
    else:
        return 0

# STRUCTURING ELEMENT NEIGBOORHOOD 8
def elementoEstruturante_8(image, coord):
    p1 = getPixel( image, (coord[0]-1,coord[1]-1) ) 
    p2 = getPixel( image, (coord[0]-1,coord[1])   )
    p3 = getPixel( image, (coord[0]-1,coord[1]+1) )
    p4 = getPixel( image, (coord[0]  ,coord[1]-1) )
    p5 = getPixel( image, (coord[0]  ,coord[1])   ) 
    p6 = getPixel( image, (coord[0]  ,coord[1]+1) )
    p7 = getPixel( image, (coord[0]+1,coord[1]-1) )
    p8 = getPixel( image, (coord[0]+1,coord[1])   )
    p9 = getPixel( image, (coord[0]+1,coord[1]+1) )    
    
    if p1 and p2 and p3 and p4 and p5 and p6 and p7 and p8 and p9 > 128:
        return 255
    else:
        return 0

# FUNCTION THAT RETURNS EROSED IMAGE
def imageErosion(image, elemento):
    new_Image = Image.new("L",image.size,0)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            coord = i,j
            if elemento     == 4:
                new_Image.putpixel( coord, elementoEstruturante_4( image, coord) )    
            elif elemento   == 8 :
                new_Image.putpixel( coord, elementoEstruturante_8( image, coord) )    
    
    return new_Image

# FUNCTION THAT RETURNS COUNTOR : ORIGINAL - EROSED
def contourExtraction(image,imageErodida):
    new_Image = Image.new("L",image.size,0)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            coord = i,j
            contorno = image.getpixel(coord) - imageErodida.getpixel(coord)
            new_Image.putpixel( coord, contorno )    

    return new_Image


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("compile assim 'python 'extraction.py' 'imagem' '4 ou 8' ")
        exit()
    else:
            #IMAGEM COLORIDA
        if Image.open(sys.argv[1]).mode == 'RGB':
            #RGB -> GRAYSCALE
            imageGray =  RGB_to_GrayScale(Image.open(sys.argv[1]))
            imageGray.show()
            vizinhanca      = int(sys.argv[2])
            OtsuValue       = otsuBinarization(imageGray)
            #BINARIZANDO ATRAVES DO METODO OTSU
            imagemOriginal  =  limiarizacao(imageGray, OtsuValue)
            #EROSAO
            imagemErodida   = imageErosion(imagemOriginal, vizinhanca)
            imagemOriginal.show()
            imagemErodida.show()
            #EXTRACAO DE CONTORNO
            contourExtraction(imagemOriginal, imagemErodida).show()
        elif Image.open(sys.argv[1]).mode == 'L':
            #IMAGEM EM ESCALA DE CINZA
            vizinhanca      = int(sys.argv[2])
            imageGray       = Image.open(sys.argv[1])
            OtsuValue       = otsuBinarization(imageGray)
            #BINARIZANDO ATRAVES DO METODO OTSU
            imagemOriginal  =  limiarizacao(imageGray, OtsuValue)
            imagemErodida   = imageErosion(imagemOriginal, vizinhanca)
            imagemOriginal.show()
            imagemErodida.show()
            #EXTRACAO DE CONTORNO
            contourExtraction(imagemOriginal, imagemErodida).show()
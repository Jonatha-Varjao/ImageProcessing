# -*- coding: utf-8 -*-
from PIL import Image
import sys

def rotation(image, grau):
    #PRIMEIRO SETAR A NOVAS LINHAS E COLUNAS
    #CRIAR A NOVA IMAGEM BASEADA NAS LINHAS E COLUNAS


    return image

def translation(image, grau):
    return image

def soma(imageOne, imageTwo):
    image = imageOne + imageTwo
    return image

def sub(imageOne, imageTwo):
    image = imageOne - imageTwo
    return image

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print(" compile assim 'python arithmetic.py 'imagem' 'grau' ")
        exit()
    else :
        rotation = float(sys.argv[2])
        img = Image.open(sys.argv[1])
        img.show()
        #img = rotation(img,rotation)
        
        img.rotate(2).show()
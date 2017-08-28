# -*- coding: utf-8 -*-
from PIL import Image
import sys

#testar as interpolações usando numpy
#import numpy as np

#TODO Usar OO



#Interpolação por vizinho por 2 redução (numero de colunas par)
def Vizinho(img, factor):
    size = img.size
    n_X = int(size[0] * factor)
    n_Y = int(size[1] * factor)
    n_img = Image.new("L",(n_X, n_Y))
    
    for i in range(n_X):
        for j in range(n_Y):
            p = (int(i/factor), int(j/factor))
            n_img.putpixel((i,j), img.getpixel(p))
    return n_img
    
def Bilinear(img, factor):
    size = img.size
    n_X = int(size[0] * factor)
    n_Y = int(size[1] * factor)
    n_img = Image.new("L",(n_X, n_Y))


# MAIN passando a foto pelo CLI
if __name__ == "__main__":

    if len(sys.argv) < 4:
        print(" 'python Interplation.py 'imagem' 'fator' 'imagemSaida' 'tipo'")
        # tipo -> 1 = Vizinho, 2 = Bilinear
        exit()
    else :
        #RECEBENDO O FATOR DE REDUÇÃO AMPLIAÇÃO
        size = float(sys.argv[2])
        #INTERPOLACAO VIZINHO
        if sys.argv[4] == '1':
            img = Image.open(sys.argv[1])
            img.show()
            a = Vizinho(img, size)
            a.show()
            a.save(sys.argv[3])
        #INTERPOLACAO BILINEAR
        elif sys.argv[4] == '2' :
            img = Image.open(sys.argv[1])
            img.show()
            a = Bilinear(img,size)
            a.show()
            a.save(sys.argv[3])
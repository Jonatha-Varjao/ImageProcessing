# -*- coding: utf-8 -*-
from PIL import Image
import sys

#testar as interpolações usando numpy
#import numpy as np

#TODO Usar OO


#Interpolação por vizinho por 2 redução (numero de colunas par)
def interpolacaoVizinho(img, factor):
    size = img.size
    n_X = int(size[0] * factor)
    n_Y = int(size[1] * factor)
    n_img = Image.new("L",(n_X, n_Y))
    #REDUÇÃO 
    if factor <= 1:
        for i in range(n_X):
            for j in range(n_Y):
                p = (int(i/factor), int(j/factor))
                n_img.putpixel((i,j), img.getpixel(p))

        return n_img
    #AUMENTO
    else :
        for i in range(n_X):
            for j in range(n_Y):
                p = (int(i/factor), int(j/factor))
                n_img.putpixel((i,j), img.getpixel(p))

        return n_img
        print("AMPLIACAO")

def InterpolacaoBilinear(img, factor):
    print("a")

# MAIN passando a foto pelo CLI
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Faltando path/to/image.png")
        exit()

    img = Image.open(sys.argv[1])
    img.show()
    #RECEBENDO O FATOR DE REDUÇÃO AMPLIAÇÃO
    size = float(sys.argv[2])
    
    a = interpolacaoVizinho(img, size)
    a.show()
    a.save(sys.argv[3])
    
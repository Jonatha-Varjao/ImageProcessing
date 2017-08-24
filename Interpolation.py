# -*- coding: utf-8 -*-
from PIL import Image
import sys

#testar as interpolações usando numpy
#import numpy as np

#TODO Usar OO


#Interpolação por vizinho por 2 redução (numero de colunas par)
def interpolacaoVizinho(img, factor):
    size = img.size
    nwidth = int(size[0] * factor)
    nheight = int(size[1] * factor)

    n_img = Image.new("L",(nwidth, nheight))

    for i in range(nwidth):
        for j in range(nheight):
            p = (int(i/factor), int(j/factor))
            n_img.putpixel((i,j), img.getpixel(p))

    return n_img



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

    
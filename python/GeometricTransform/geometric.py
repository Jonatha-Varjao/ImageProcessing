# -*- coding: utf-8 -*-
from PIL import Image
import sys

def translation(image,new_x,new_y):
    new = Image.new("L",(image.size[0]+new_y,image.size[1]+new_y))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = (i,j)
            new.putpixel((i+new_x,j+new_y), image.getpixel(p)) 
    return new


def reflexao(image, eixo):
    
    x = lambda x: x
    y = lambda y: y
    
    if "x" in eixo:
        x = lambda x: image.size[0] -1 -x
    else: 
        y = lambda y: image.size[1] -1 -y

    newImage = Image.new("L", image.size)

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            newImage.putpixel( (x(i), y(j) ), image.getpixel( (i,j) ) )

    return newImage



# MAIN passando a foto pelo CLI
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("compile assim 'python geometric.py 'imagem' 'opcao' ")
        exit()
    else :
        # TRANSLAÇÃO
        if sys.argv[2] == '1':           
            print("compile assim 'python geometric.py 'imagem' 'opcao' 'X,Y' ")
            image = Image.open(sys.argv[1])
            options = sys.argv[3]
            opt = options.split(',')
            print(opt)
            #translation(image, int(opt[0]), int(opt[1])).save("Trans"+sys.argv[1])
        # REFLEXAO
        elif sys.argv[2] == '2' :
            print("compile assim 'python Interplation.py 'imagem' 'opcao' 'X ou Y' ")
            image = Image.open(sys.argv[1])
            reflexao(image, sys.argv[3]).save("Reflex"+sys.argv[1])
        # ROTACAO
        elif sys.argv[2] == '3' :
            pass
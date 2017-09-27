# -*- coding: utf-8 -*-
from PIL import Image
import sys
import math

def translation(image,new_x,new_y):
    size = image.size
    size = size[0] + abs(new_x) , size[1] + abs(new_y)
    print(size)
    new = Image.new("L",(size))
    # X e Y pos
    if new_x >= 0 and new_y >= 0:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i+new_x,j), image.getpixel(p)) 
        return new
    # X negativo , Y negativo
    if new_x < 0 and new_y < 0:
        print("X and Y < 0")
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i,j+ abs(new_y)), image.getpixel(p)) 
        return new
    # X negativo, Y positivo
    if new_x < 0 and new_y > 0: 
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i,j), image.getpixel(p)) 
        return new  
    # X pos , Y neg
    else:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i + abs(new_x), j + abs(new_y)), image.getpixel(p)) 
        return new  
        
        
def reflexao(image, eixo):    
    x = lambda x: x
    y = lambda y: y    
    
    if "x" in eixo:
        x = lambda x: image.size[0] -1 -x
    elif "y" in eixo: 
        y = lambda y: image.size[1] -1 -y

    newImage = Image.new("L", image.size)

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            newImage.putpixel( (x(i), y(j) ), image.getpixel( (i,j) ) )

    return newImage

# TODO
#  CISALHAMENTO HORIZONTAL EIXO X 
#def shear(image, valor):
#    size = image.size
#    size = int( image.size[0] + image.size[0]*valor ), image.size[1]
#    print(size)
#    newImage = Image.new("L", size)
#    print(newImage)
     
#    for i in range(image.size[0]):
#        for j in range(image.size[1]):
#            p = i + int(image.size[0]*valor)
#            newImage.putpixel((i, j),  p  )
#    return newImage

# MAIN passando a foto pelo CLI
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("compile assim 'python geometric.py 'imagem' 'opcao' ")
        exit()
    else :
        # TRANSLAÇÃO
        if sys.argv[2] == '1' :           
            if len(sys.argv) < 4:
                print("compile assim 'python geometric.py 'imagem' 'opcao' 'X,Y' ")
                exit()
            else:
                opt = sys.argv[3].split(',')
                translation(Image.open(sys.argv[1]), int(opt[0]), int(opt[1])).save("Trans"+sys.argv[1])
        # REFLEXAO
        elif sys.argv[2] == '2' :
            if len(sys.argv) < 4:
                print("compile assim 'python Interplation.py 'imagem' 'opcao' 'X ou Y' ")
                exit()
            else :
                reflexao(Image.open(sys.argv[1]), sys.argv[3]).save("Reflex"+sys.argv[1])
        # CISALHAMENTO
        #elif sys.argv[2] == '3' :
        #    if len(sys.argv) < 4:
        #        print("compile assim 'python Interplation.py 'imagem' 'valor' ")
        #        exit()
        #    else:
        #        valor = float(sys.argv[3])
        #        shear(Image.open(sys.argv[1]), valor).save("Shear"+sys.argv[1])
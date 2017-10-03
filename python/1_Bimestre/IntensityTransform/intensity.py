# -*- coding: utf-8 -*-
from PIL import Image
import sys

def limiarizacao(img, treshould):
    newImage = Image.new("L", (img.size[0],img.size[1]) )
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = (i,j)
            if img.getpixel(p) > treshould:
                newImage.putpixel((i,j), 255)
            else:
                newImage.putpixel((i,j), 0)  
            
    return newImage


def powerLaw(img, y):
    newImage = Image.new("L", (img.size[0],img.size[1]) )
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = (i,j)
            a = float(img.getpixel(p))/255
            a2 = pow(a,y)
            p =  a2* 255
            newImage.putpixel((i,j), int(p))                       
    return newImage


# MAIN passando a foto pelo CLI
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("compile assim 'python intesity.py 'imagem' 'opcao' ")
        exit()
    else :
         # LIMIARIZACAO
        if sys.argv[2] == '1':  
            treshould = abs(int(sys.argv[3]))
            limiarizacao(Image.open(sys.argv[1]), treshould ).save("Limiarizacao"+sys.argv[1])
        # POWERLAW
        elif sys.argv[2] == '2':
            y = float(sys.argv[3])
            print(y)
            powerLaw(Image.open(sys.argv[1]), y).save("PowerLaw"+sys.argv[1])
        
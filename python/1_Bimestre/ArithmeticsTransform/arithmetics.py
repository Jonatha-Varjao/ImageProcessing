# -*- coding: utf-8 -*-
from PIL import Image
from decimal import Decimal 
import sys
#TODO OBJECT ORIENTED
#adicionando o path do script de interpolação
sys.path.insert(0, 'C:\Users\jonat\Documents\GitClones\ImageProcessing\python\Interpolation')
# importando as funções de interpolação
from interpolation import *
import time


#Imagens tem que ser do mesmo tamanho, caso contrário usar interpolaçãoBi                                                                                                                                                        }
def transformArit(imageOne, imageTwo):
    start = time.time()
    soma(imageOne, imageTwo).save("Soma.jpg") 
    sub(imageOne, imageTwo).save("Subtracao.jpg") 
    mult(imageOne, imageTwo).save("Multiplicacao.jpg") 
    div(imageOne, imageTwo).save("Divisao.jpg")  
    
    print("Time taken = {0:.5f}".format(time.time() - start))

def sizeTeste(imageOne, imageTwo):
    # M = N             matriz[m,n]
    if imageOne.size[0] == imageTwo.size[0] and imageOne.size[1] == imageTwo.size[1] :
        return transformArit(imageOne,imageTwo)
    elif imageOne.size[0] < imageTwo.size[0] :
        #interpolo a primeira
        print("imageOne < imageTwo")
        Xa,Ya = imageOne.size[0],imageOne.size[0]
        Xb,Yb = imageTwo.size[0],imageTwo.size[1]
        FatorMult =  float(Xb)/float(Xa), float(Yb)/float(Ya)
        print(FatorMult)
        
        Xa,Ya = FatorMult[0]*Xa, FatorMult[1]*Ya        
        imgInterpolada = Bilinear(imageOne,(FatorMult[0]))
        imgInterpolada.save("Bi"+sys.argv[1])
        
        return transformArit(imgInterpolada, imageTwo )
        
    else:
        print("imageOne > imageTwo")
        #interpolo a segunda
        Xa,Xb = imageOne.size[0],imageTwo.size[0]
        Ya,Yb = imageOne.size[1],imageTwo.size[1]
        
        FatorMult =  float(Xa)/float(Xb), float(Ya)/float(Yb)
        print(FatorMult)
        
        Xb,Yb = FatorMult[0]*Xb, FatorMult[1]*Yb
        imgInterpolada = Bilinear(imageTwo,(FatorMult[0]))
        imgInterpolada.save("Bi"+sys.argv[2])

        return transformArit(imgInterpolada, imageOne)
            

def soma(imageOne, imageTwo):
    newImage = Image.new("L", imageOne.size)
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            p = (i, j)
            newImage.putpixel((i,j), imageOne.getpixel(p) + imageTwo.getpixel(p))
    return newImage

def sub(imageOne, imageTwo):
    newImage = Image.new("L", imageOne.size)
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            p = (i, j)
            newImage.putpixel((i,j), imageOne.getpixel(p) - imageTwo.getpixel(p))
    return newImage

def div(imageOne, imageTwo):
    newImage = Image.new("L", imageOne.size)
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            p = (i, j)
            if imageTwo.getpixel(p) == 0:
                   newImage.putpixel((i,j), imageOne.getpixel(p))
            else:
               
                newImage.putpixel((i,j), imageOne.getpixel(p) / imageTwo.getpixel(p))
    return newImage

def mult(imageOne, imageTwo):
    newImage = Image.new("L", imageOne.size)
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            p = (i, j)
            newImage.putpixel((i,j), imageOne.getpixel(p) * imageTwo.getpixel(p))
    return newImage




if __name__ == "__main__":

    if len(sys.argv) < 3:
        print(" compile assim 'python arithmetic.py 'imagem1' 'imagem2'")
        exit()
    #SOMA
    else :
        imageOne = Image.open(sys.argv[1])
        imageTwo = Image.open(sys.argv[2])        
        sizeTeste(imageOne, imageTwo)
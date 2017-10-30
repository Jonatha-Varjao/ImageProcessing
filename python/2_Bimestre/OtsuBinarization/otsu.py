# -*- coding: utf-8 -*-
# TRESHOULDING A GRAYSCALE IMAGE AND RGB IMAGE (256) TO A BINARY IMAGE USING OTSU METHOD
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


def RGB_to_GrayScale(image):
    new_image = Image.new("L",(image.size),0)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            m = float((p[0] + p[1] + p[2])/ 3)            
            new_image.putpixel((i,j),  int(m) )            
    
    return new_image
    
def getQtdPixelsAntes(indice, hist):
    soma = 0
    for i in range(0,indice+1):
        soma = soma + hist[i]
    
    if soma == 0:
        soma = 1
    
    return soma

def getQtdPixelsDepois(indice, hist):
    soma = 0
    for i in range(indice,len(hist)):
        soma = soma + hist[i]
    
    if soma == 0 :
        soma = 1
    
    return soma

def getWeightBackground(indice, hist ,qtdPixels):
    weight = 0
    for i in range(indice):
        weight = weight + hist[i]
    
    return float(weight) / float(qtdPixels)

def getWeightForeground(indice, hist ,qtdPixels):
    weight = 0
    for i in range(indice, len(hist)):
        weight = weight + hist[i]
    
    return float(weight)/float(qtdPixels)

def getMeanBackground(indice, hist):
    if indice == 0 : return 0
    mean = 0
    for i in range(indice+1):
        mean =  mean + (i * hist[i])
        
    return float(mean)/float(getQtdPixelsAntes(indice, hist))

def getMeanForeground(indice, hist):
    if indice == 0 : return 0
    mean = 0
    for i in range(indice, len(hist)):
        mean =  mean + (i * hist[i])
    
    return float(mean)/float(getQtdPixelsDepois(indice, hist))

def getVarianceBackground(indice, hist, mean):
    variance = 0
    for i in range(0,indice+1):
        variance =  variance + (pow((i - mean),2) * hist[i])
    
    return float(variance)/float(getQtdPixelsAntes(indice, hist))

def getVarianceForeground(indice, hist, mean):
    variance = 0
    for i in range(indice,len(hist)):
        variance =  variance + (pow((i - mean),2) * hist[i])
    
    return float(variance)/float(getQtdPixelsDepois(indice, hist))

def otsuBinarization(image):
    hist            = image.histogram()
    qtdPixels       = image.size[0]*image.size[1]
    Variacao        = []
    
    for i in range(len(hist)):
        # TAKING WEIGHT
        Wb              =   getWeightBackground (i, hist, qtdPixels)
        Wf              =   getWeightForeground (i+1, hist, qtdPixels)
        # TAKING MEAN
        Mb              =   getMeanBackground   (i, hist)
        Mf              =   getMeanForeground   (i, hist)
        # CLASS VARIANCE
        Vb              =   getVarianceBackground(i, hist, Mb)
        Vf              =   getVarianceForeground(i, hist, Mf)
        Variacao.insert(i, float((Wb*Vb)+(Wf*Vf)))
       
    print min(Variacao)
    print Variacao.index(min(Variacao))
    
    return Variacao.index(min(Variacao))


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("compile assim 'python 'otsu.py' 'imagem' ")
        exit()
    else:
        if Image.open(sys.argv[1]).mode == 'RGB':
            #transormar em cinza 
            imageGray =  RGB_to_GrayScale(Image.open(sys.argv[1]))
            imageGray.show()
            OtsuValue = otsuBinarization(imageGray)
            limiarizacao(imageGray,OtsuValue).show()
        elif Image.open(sys.argv[1]).mode == 'L':    
            imageGray = Image.open(sys.argv[1])
            imageGray.show()
            print imageGray
            OtsuValue = otsuBinarization(imageGray)
            limiarizacao(imageGray, OtsuValue).show()
        else :
            print("Imagem não suportada")  
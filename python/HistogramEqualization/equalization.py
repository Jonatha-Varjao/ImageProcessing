# -*- coding: utf-8 -*-
from PIL import Image
from matplotlib import pyplot as plt
import sys
from itertools import izip_longest   

def escalaCinza(image):
    new_image = Image.new("L",(image.size[0],image.size[1]))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            m = (p[0] + p[1] + p[2])/3
            new_image.putpixel((i,j),(m))
    return new_image

def histogramGraph(image):
    x,y = image.size
    colors = image.getcolors(x*y)
    for idx, c in enumerate(colors):
        plt.bar(idx, c[0], color="black")
    return plt.savefig("./histogram/histogram"+sys.argv[1])

def returnFrequencia(image):
    
    qtdPixels = image.size[0]*image.size[1]
    list2 = image.histogram()
    PrRk = [ (float(list2[i])/float(qtdPixels),i) for i in range(256) ]    
    #print PrRk
    freqEq = []   
    for i in range(256):
        #print i
        #print PrRk[i][0]
        if i == 0:
            freqEq.append(255*PrRk[i][0])
            pass
        else:
            freqEq.append(255*PrRk[i][0] + freqEq[i-1])
    #print freqEq

    new_image = Image.new("L",(image.size))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            m = freqEq[p]
            new_image.putpixel((i,j), int(m) )
    return new_image
    


if __name__ == "__main__":
    

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("compile assim 'python 'equalization.py' 'imagem' ")
        exit()
    
    image = Image.open(sys.argv[1])
    # RECEBER UMA IMAGEM RGB TRANSFORMA PARA CINZA 
    if image.mode == "RGB":
        escalaCinza(image).show()
        print(escalaCinza(image))
    else:
        histogramGraph(image)
        imageEqualizada = returnFrequencia(image)
        sys.argv[1]= "Equalizada"+sys.argv[1]
        imageEqualizada.save(sys.argv[1])
        histogramGraph(imageEqualizada)
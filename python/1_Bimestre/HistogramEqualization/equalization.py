# -*- coding: utf-8 -*-
# HISTOGRAM EQUALIZATION 
from PIL import Image
from matplotlib import pyplot as plt
import sys

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
        else:
            freqEq.append( 255*(PrRk[i][0]) + freqEq[i-1] )
    #print freqEq

    new_image = Image.new("L",(image.size))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            m = round(freqEq[p])
            new_image.putpixel((i,j), int(m) )
    return new_image

def contrastStrech(image):
    list = image.getcolors()
    c =  list[0][1] 
    d =  list[len(list) - 1][1]
    #print('{} {}'.format(c,d))

    new_image = Image.new("L",(image.size))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = ( image.getpixel((i,j)) - c ) * (float(255)/float((d-c)))
            round(p)
            if p < 0:
                p = 0
                
            new_image.putpixel( (i,j), int(p) )
            
    return new_image

    

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("compile assim 'python 'equalization.py' 'imagem' ")
        exit()
    # RECEBER UMA IMAGEM RGB TRANSFORMA PARA CINZA 
    elif sys.argv[2] == '1' :
        image = Image.open(sys.argv[1])
        if image.mode == "RGB":
            image = escalaCinza(image)
            sys.argv[1] = "Cinza"+sys.argv[1]
            image.save(sys.argv[1])
            histogramGraph(image)
            sys.argv[1]= "Equalizada"+sys.argv[1]
            image = returnFrequencia(image)
            image.save(sys.argv[1])
            histogramGraph(image)
            
        else:
            histogramGraph(image)
            imageEqualizada = returnFrequencia(image)
            sys.argv[1]= "Equalizada"+sys.argv[1]
            imageEqualizada.save(sys.argv[1])
            histogramGraph(imageEqualizada)
    
    elif sys.argv[2] == '2':
        image = contrastStrech(Image.open(sys.argv[1]))
        sys.argv[1]= "ConstantStretch"+sys.argv[1]
        image.save(sys.argv[1])
        histogramGraph(image)

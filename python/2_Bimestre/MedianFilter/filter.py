# -*- coding: utf-8 -*-
# MEDIAN FILTER 3X3 MASK
from PIL import Image
import sys

def returnSomaVizin(image, coord ):
    try:
        p = image.getpixel(coord)
        return p
    except IndexError as e:
        return 0
    else:
        return 0
#3x3
def maskMedia(image, coord):
    p1 = returnSomaVizin( image, (coord[0]-1,coord[1]-1) ) 
    p2 = returnSomaVizin( image, (coord[0]-1,coord[1]) )
    p3 = returnSomaVizin( image, (coord[0]-1,coord[1]+1) )
    p4 = returnSomaVizin( image, (coord[0],coord[1]-1) )
    p5 = returnSomaVizin( image, (coord[0],coord[1]) ) 
    p6 = returnSomaVizin( image, (coord[0],coord[1]+1) )
    p7 = returnSomaVizin( image, (coord[0]+1,coord[1]-1) )
    p8 = returnSomaVizin( image, (coord[0]+1,coord[1]) )
    p9 = returnSomaVizin( image, (coord[0]+1,coord[1]+1) )
    pMedia = round((p1+p2+p3+p4+p5+p6+p7+p8+p9)/9)
    
    return pMedia
#15x15



def medianFilter(image):    
    new_image = Image.new("L",(image.size),0)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pMedia = maskMedia(image, (i,j))            
            new_image.putpixel((i,j), int(pMedia))
            #print("p1:{}  p2:{}  p3:{} p4:{}  p5:{}  p6:{} p7:{} p8:{}  p9:{} pMedia {} ".format(p1,p2,p3,p4,p5,p6,p7,p8,p9,pMedia))
    return new_image
    
    

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("compile assim 'python 'filter.py' 'imagem' ")
        exit()
    else:
        medianFilter(Image.open(sys.argv[1])).save("FiltroMedio"+sys.argv[1])
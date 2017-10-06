# -*- coding: utf-8 -*-
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

def maskHorizontal(image, coord):
    p1 = returnSomaVizin( image, (coord[0]-1,coord[1]-1) ) 
    p2 = returnSomaVizin( image, (coord[0]-1,coord[1]) )
    p3 = returnSomaVizin( image, (coord[0]-1,coord[1]+1) )
    p7 = returnSomaVizin( image, (coord[0]+1,coord[1]-1) )
    p8 = returnSomaVizin( image, (coord[0]+1,coord[1]) )
    p9 = returnSomaVizin( image, (coord[0]+1,coord[1]+1) )
    pMedia = ((-p1) + (-2*p2) + (-p3) + p7 + (2*p8) + p9)
    
    return pMedia

def maskVertical(image, coord):
    p1 = returnSomaVizin( image, (coord[0]-1,coord[1]-1) ) 
    p3 = returnSomaVizin( image, (coord[0]-1,coord[1]+1) )
    p4 = returnSomaVizin( image, (coord[0],coord[1]-1) )
    p6 = returnSomaVizin( image, (coord[0],coord[1]+1) )
    p7 = returnSomaVizin( image, (coord[0]+1,coord[1]-1) )
    p9 = returnSomaVizin( image, (coord[0]+1,coord[1]+1) )
    pMedia = ( (-p1) + p3 + (-2*p4) + (2*p6) + (-p7) + p9)
    
    return pMedia


def sobelFilter(image, filter):
    new_image = Image.new("L",(image.size),0)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            cood = i,j
            if filter == 1:
                pMedia = maskHorizontal(image,cood)
            elif filter == 2:
                pMedia = maskVertical(image,cood)
                        
            new_image.putpixel((i,j), int(pMedia))
            #print("p1:{}  p2:{}  p3:{} p4:{}  p5:{}  p6:{} p7:{} p8:{}  p9:{} pMedia {} ".format(p1,p2,p3,p4,p5,p6,p7,p8,p9,pMedia))
    return new_image


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("compile assim 'python 'sobel.py' 'imagem' ")
        exit()
    else:
        sobelFilter(Image.open(sys.argv[1]), int(sys.argv[2]) ).save("Sobel"+sys.argv[2]+sys.argv[1])
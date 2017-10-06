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

def mask1(image, coord):
    p2 = returnSomaVizin( image, (coord[0]-1,coord[1]) )
    p4 = returnSomaVizin( image, (coord[0],coord[1]-1) )
    p5 = returnSomaVizin( image, (coord[0],coord[1]) ) 
    p6 = returnSomaVizin( image, (coord[0],coord[1]+1) )
    p8 = returnSomaVizin( image, (coord[0]+1,coord[1]) )
    pMedia = p2 + p4 + (p5*-4) + p6 + p8
    
    return pMedia

def mask2(image, coord):
    p1 = returnSomaVizin( image, (coord[0]-1,coord[1]-1) ) 
    p2 = returnSomaVizin( image, (coord[0]-1,coord[1]) )
    p3 = returnSomaVizin( image, (coord[0]-1,coord[1]+1) )
    p4 = returnSomaVizin( image, (coord[0],coord[1]-1) )
    p5 = returnSomaVizin( image, (coord[0],coord[1]) ) 
    p6 = returnSomaVizin( image, (coord[0],coord[1]+1) )
    p7 = returnSomaVizin( image, (coord[0]+1,coord[1]-1) )
    p8 = returnSomaVizin( image, (coord[0]+1,coord[1]) )
    p9 = returnSomaVizin( image, (coord[0]+1,coord[1]+1) )
    pMedia = (p1 + p2 + p3 + p4 + (p5*-8) + p6 + p7 + p8 + p9)
    
    return pMedia

def mask3(image, coord):
    p2 = returnSomaVizin( image, (coord[0]-1,coord[1]) )
    p4 = returnSomaVizin( image, (coord[0],coord[1]-1) )
    p5 = returnSomaVizin( image, (coord[0],coord[1]) ) 
    p6 = returnSomaVizin( image, (coord[0],coord[1]+1) )
    p8 = returnSomaVizin( image, (coord[0]+1,coord[1]) )
    pMedia = (-p2) + (-p4) + (p5 *4) + (-p6) + (-p8)
    
    return pMedia

def mask4(image, coord):
    p1 = returnSomaVizin( image, (coord[0]-1,coord[1]-1) ) 
    p2 = returnSomaVizin( image, (coord[0]-1,coord[1]) )
    p3 = returnSomaVizin( image, (coord[0]-1,coord[1]+1) )
    p4 = returnSomaVizin( image, (coord[0],coord[1]-1) )
    p5 = returnSomaVizin( image, (coord[0],coord[1]) ) 
    p6 = returnSomaVizin( image, (coord[0],coord[1]+1) )
    p7 = returnSomaVizin( image, (coord[0]+1,coord[1]-1) )
    p8 = returnSomaVizin( image, (coord[0]+1,coord[1]) )
    p9 = returnSomaVizin( image, (coord[0]+1,coord[1]+1) )
    pMedia = (-p1) + (-p2) + (-p3) + (-p4) + (p5*8) + (-p6) + (-p7) + (-p8) + (-p9)
    
    return pMedia



def laplacianFilter(image, filter):
    new_image = Image.new("L",(image.size),0)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            cood = i,j
            if filter == 1:
                pMedia = mask1(image,cood)
            elif filter == 2:
                pMedia = mask2(image,cood)
            elif filter == 3:
                pMedia = mask3(image,cood)
            elif filter == 4:
                pMedia = mask4(image,cood)
            
            new_image.putpixel((i,j), int(pMedia))
            #print("p1:{}  p2:{}  p3:{} p4:{}  p5:{}  p6:{} p7:{} p8:{}  p9:{} pMedia {} ".format(p1,p2,p3,p4,p5,p6,p7,p8,p9,pMedia))
    return new_image


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("compile assim 'python 'laplacian.py' 'imagem' 'Tipo Filtro: 1 2 3 4' ")
        exit()
    else:
        laplacianFilter(Image.open(sys.argv[1]), int(sys.argv[2])).save("Laplacian"+sys.argv[1])
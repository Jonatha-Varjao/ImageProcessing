# -*- coding: utf-8 -*-
# INTERPOLATION METHODS : NEIGHBOORHOOD AND BILINEAR
from PIL import Image
import sys

#testar as interpolações usando numpy
#import numpy as np

#TODO Usar OO



def Vizinho(img, factor):
    size = img.size
    n_X = int(size[0] * factor)
    n_Y = int(size[1] * factor)
    n_img = Image.new("L",(n_X, n_Y))
    #LOOP ACESSANDO OS PIXELS DA NOVA IMAGEM
    for i in range(n_X):
        for j in range(n_Y):
            p = (int(i/factor), int(j/factor))
            n_img.putpixel((i,j), img.getpixel(p))
    return n_img
    
def Bilinear(img, factor):
    size = img.size
    n_X = int(size[0] * factor)    
    n_Y = int(size[1] * factor)
    n_img = Image.new("L",(n_X, n_Y))
    #REDUCAO
    if factor < 1:
        #PEGAR A RELACAO DE VIZINHA DO PIXEL ATUAL
        for i in range(n_X):
            for j in range(n_Y):
                if i == n_X-1: #CHEGUEI NO LIMITE NO I, LOGO N ADD O I+1
                    p = (int(i/factor),int(j/factor))
                    b, c, d = (p[0], p[1]+1), (p[0]-1, p[1]), (p[0]-1, p[1]+1)
                    a,b,c,d = img.getpixel(p), img.getpixel(b), img.getpixel(c), img.getpixel(d)                    
                    p = (a+b+c+d)/4
                    n_img.putpixel((i,j), p)
                elif j == n_Y-1: #CHEGUEI NO LIMITE DO J, LOGO N ADD O J+1
                    p = (int(i/factor),int(j/factor))                    
                    if i == 0:  # primira linha n posso pegar i-1
                        b, c, d = (p[0], p[1]-1), (p[0]+1, p[1]), (p[0]+1, p[1]-1)
                        a,b,c,d = img.getpixel(p), img.getpixel(b), img.getpixel(c), img.getpixel(d)                    
                        p = (a+b+c+d)/4
                    else:
                        b, c, d = (p[0], p[1]-1), (p[0]+1, p[1]-1), (p[0]+1, p[1])
                        a,b,c,d = img.getpixel(p), img.getpixel(b), img.getpixel(c), img.getpixel(d)                    
                        p = (a+b+c+d)/4
                    n_img.putpixel((i,j), p)                    
                else:
                    p = (int(i/factor),int(j/factor))             
                    b, c, d = (p[0], p[1]+1), (p[0]+1, p[1]), (p[0]+1, p[1]+1)
                    a,b,c,d = img.getpixel(p), img.getpixel(b), img.getpixel(c), img.getpixel(d)                    
                    p = (a+b+c+d)/4
                    n_img.putpixel((i,j), p)
        return n_img
    #AMPLIACAO
    else:
        for i in range (n_X):
            for j in range (n_Y):
                #tratamento da borda i                
                if i == n_X-1: 
                    if j % 2 == 0: # setar img original
                        p  = (int(i/factor),int(j/factor))
                        a1 = (p[0],p[1])
                        a1 = img.getpixel(a1)
                        n_img.putpixel((i,j), a1)
                    else:          #a = Lpassado + Lfuturo / 2
                        p = (int(i/factor),int(j/factor))
                        if j == n_Y-1: 
                            a1,a2 = (p[0],p[1]-1), (p[0],p[1])
                            a1,a2 = img.getpixel(a1), img.getpixel(a2)
                            a = (a1+a2)/2
                            n_img.putpixel((i,j), a)
                            
                        else:
                            a1,a2 = (p[0],p[1]), (p[0],p[1]+1)
                            a1,a2 = img.getpixel(a1), img.getpixel(a2)
                            a = (a1+a2)/2
                            n_img.putpixel((i,j), a)                        

                #tratamento da borda j                
                elif j == n_Y-1:
                    p  = (int(i/factor),int(j/factor))
                    if j % 2 == 0: # setar img original
                        a1 = (p[0],p[1])
                        a1 = img.getpixel(a1)
                        n_img.putpixel((i,j), a1)
                        
                    else:          #a = Lpassado + Lfuturo / 2
                        a1,a2 = (p[0],p[1]-1), (p[0],p[1])
                        a1,a2 = img.getpixel(a1), img.getpixel(a2)
                        a = (a1+a2)/2
                        n_img.putpixel((i,j), a)                
                #i par
                elif i % 2 == 0 : 
                    
                    if j % 2 == 0: # setar pixel da img original
                        p  = (int(i/factor),int(j/factor))
                        a1 = (p[0],p[1])
                        a1 = img.getpixel(a1)
                        n_img.putpixel((i,j), a1)
                    else:  #j impar logo a = Lpassado + Lfuturo / 2                       
                        
                        p = (int(i/factor),int(j/factor))                                   
                        a1,a2 = (p[0],p[1]), (p[0],p[1]+1)

                        a1,a2 = img.getpixel(a1), img.getpixel(a2)
                        a = (a1+a2)/2
                        n_img.putpixel((i,j), a)

                else: #i impar
                    if j % 2 == 0: #a = cima + baixo / 2
                        p  = (int(i/factor),int(j/factor))
                        a1,a2 = (p[0],p[1]),(p[0]+1,p[1])
                        a1,a2 = img.getpixel(a1),img.getpixel(a2)
                        a = (a1+a2)/2
                        n_img.putpixel((i,j), a)
                    else:
                        p  = (int(i/factor),int(j/factor))
                        a1,a2,a3,a4 = (p[0],p[1]),(p[0]+1,p[1]),(p[0],p[1]+1),(p[0]+1,p[1]+1)
                        a1,a2,a3,a4 = img.getpixel(a1),img.getpixel(a2),img.getpixel(a3),img.getpixel(a4)
                        a = (a1+a2+a3+a4)/4
                        n_img.putpixel((i,j), a)
                        
        return n_img

# MAIN passando a foto pelo CLI
if __name__ == "__main__":

    if len(sys.argv) < 5:
        print("compile assim 'python Interplation.py 'imagem' 'fator' 'imagemSaida' 'tipo'")
        # tipo -> 1 = Vizinho, 2 = Bilinear
        exit()
    else :
        #RECEBENDO O FATOR REDUÇÃO/AMPLIAÇÃO
        size = float(sys.argv[2])
        #INTERPOLACAO VIZINHO
        if sys.argv[4] == '1':
            img = Image.open(sys.argv[1])
            img.show()
            a = Vizinho(img, size)
            a.show()
            a.save(sys.argv[3])
        #INTERPOLACAO BILINEAR
        elif sys.argv[4] == '2' :
            img = Image.open(sys.argv[1])
            img.show()
            b = Bilinear(img,size)
            b.show()
            b.save(sys.argv[3])
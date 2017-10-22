# -*- coding: utf-8 -*-
# LABELLING METHODO USING UNION-FIND ARRAYS
from PIL import Image, ImageDraw

import sys
import math, random
from itertools import product
from ufarray import *

def BinarizarImagem(image):
    new_image = Image.new("RGB",(image.size[0],image.size[1]))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            p = image.getpixel((i,j))
            m = (p[0] + p[1] + p[2])/3
            if m > 127:
                new_image.putpixel((i,j),(255,255,255))
            else:
                new_image.putpixel((i,j),(0,0,0))
    return new_image

def Rotulacao(img):
    img = img.convert('L')
    matrizPixel = img.load()
    width, height = img.size
 
    # Instacia da minha estrutura UNION FIND / dicionario das labels
    uf = UFarray()
    labels = {}
    colors = {}
 
    for y, x in product(range(height), range(width)):
 
        #
        # Condicoes de vizinhas dos meu pixeis:
        #
        #   -------------
        #   | a | b | c |
        #   -------------
        #   | d | e |   |
        #   -------------
        #   |   |   |   |
        #   -------------
        #
        # Se o meu pixel for 'e'
        # a, b, c, e d sao meus vizinhos de interesse
        # 255 branco, 0 = preto
        # pixeis brancos sao ignorados
 
        # Pixel branco, ignoro
        if matrizPixel[x, y] == 255:
            pass
 
        # Se o pixel b for preto :
        # a,c,e sao seus vizinhos, logo fazem parte da mesma regiao
        # e como e é vizinho de d, assumo que b = e = d
        
        elif y > 0 and matrizPixel[x, y-1] == 0:
            labels[x, y] = labels[(x, y-1)]
 
        # Se o pixel c for preto :
        #    b é seu vizinho, mas a e d não
        #    logo checo a label de 'a' e 'd'
        elif x+1 < width and y > 0 and matrizPixel[x+1, y-1] == 0:
 
            c = labels[(x+1, y-1)]
            labels[x, y] = c
 
            # Se a for petro:
            #    logo a e c estão na mesma regiao
            #    adiciono na união (c,a)
            if x > 0 and matrizPixel[x-1, y-1] == 0:
                a = labels[(x-1, y-1)]
                uf.union(c, a)
 
            # Se d for petro:
            #    logo d e c estão na mesma região
            #    adiciona na união (c,d)
            elif x > 0 and matrizPixel[x-1, y] == 0:
                d = labels[(x-1, y)]
                uf.union(c, d)
 
        # Se a for preto:
        #    sabemos que c e b sao brancos
        #    d is a's neighbor, so they already have the same label
        #    lgoo seto a label a em e
        elif x > 0 and y > 0 and matrizPixel[x-1, y-1] == 0:
            labels[x, y] = labels[(x-1, y-1)]
 
        # Se o d for preto:
        #    logo a,b,c são brancos
        #    logo seto a label d em e
        elif x > 0 and matrizPixel[x-1, y] == 0:
            labels[x, y] = labels[(x-1, y)]
 
        # toda minha vizinhança é branca
        # logo o pixel atual recebe uma nova label
        else: 
            labels[x, y] = uf.criaLabel()
 
   
    # Elimino as equivalencias
    uf.flatten()
    
   

    # Crio nova imagem e uma matriz dessa imagem
    saida_img = Image.new("RGB", (width, height))
    outmatrizPixel = saida_img.load()

    for (x, y) in labels:
 
        # Busco o label da região em que o ponto atual pertence
        component = uf.find(labels[(x, y)])

        # Associo cor random com a regiao
        if component not in colors: 
            colors[component] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

        #Pinto as regioes
        outmatrizPixel[x, y] = colors[component]
    print("Regiões: "+str(len(colors)))
    return saida_img
 
def main():
    
    
    img = Image.open(sys.argv[1])
    #img.show()
    img = BinarizarImagem(img)      
    #img.show()
    img.save("Binarizada"+sys.argv[1])
    img = Rotulacao(img)
    #img.show()
    img.save("Rotulada"+sys.argv[1])
if __name__ == "__main__": main()
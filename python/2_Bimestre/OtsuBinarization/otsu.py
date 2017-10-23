# OTSU METHOD FOR TRESHOULDING A GRAYSCALE IMAGE (256) TO A BINARY IMAGE
from PIL import Image
import sys

'''
def getIndex(image, coord ):
    try:
        p = image.getpixel(coord)
        return coord
    except IndexError as e:
        return 256
    else:
        return 256
'''

def getQtdPixelsAntes(indice, hist):
    soma = 0
    for i in range(0,indice+1):
        soma = soma + hist[i]
    return soma

def getQtdPixelsDepois(indice, hist):
    soma = 0
    for i in range(indice,len(hist)):
        soma = soma + hist[i]
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
    
    print len(Variacao)
    print min(Variacao)
    print Variacao.index(min(Variacao))
    


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("compile assim 'python 'otsu.py' 'imagem' ")
        exit()
    else:
        otsuBinarization(Image.open(sys.argv[1]))
        #otsuBinarization(Image.open(sys.argv[1]).convert("L"))
        print Image.open(sys.argv[1])
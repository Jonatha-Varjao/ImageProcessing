from PIL import Image
import sys

def getIndex(image, coord ):
    try:
        p = image.getpixel(coord)
        return coord
    except IndexError as e:
        return 256
    else:
        return 256

def getQtdPixelsAntes(indice, hist):
    soma = 0
    for i in range(0,indice):
        soma = soma + hist[i]
    print soma
    return soma

def getQtdPixelsDepois(indice, hist):
    soma = 0
    for i in range(indice,256):
        soma = soma + hist[i]
    print soma
    return soma

def getWeightBackground(indice, hist ,qtdPixels):
    weight = 0
    for i in range(indice):
        weight = weight + hist[i]
    return float(weight) / float(qtdPixels)

def getWeightForeground(indice, hist ,qtdPixels):
    weight = 0
    for i in range(indice, 256):
        weight = weight + hist[i]
    return float(weight)/float(qtdPixels)

def getMeanBackground(indice, hist):
    mean = 0
    for i in range(indice, 256):
        mean =  mean + (indice * hist[i])
    
    return float(mean)/float(getQtdPixelsAntes(indice, hist))
    
    pass


def getMeanForeground(indice, hist):
    pass

def otsuBinarization(image):
    hist                    = image.histogram()
    qtdPixels               = image.size[0]*image.size[1]
    PrRk                    = [(i, hist[i]) for i in range(256)]
    soma                    = 0
    qtdPixelsAtuaisAntes    = 0
    qtdPixelsAtuaisDepois   = 0
    
    for i in range(256):
        qtdPixelsAtuaisAntes =  qtdPixelsAtuaisAntes + hist[i]
        soma            =   soma + PrRk[i][1] 
        Wb              =   getWeightBackground(i, hist, qtdPixels)
        Wf              =   getWeightForeground(i+1, hist, qtdPixels)

    print Wb
    print Wf       
        

    
    

    pass

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("compile assim 'python 'otsu.py' 'imagem' ")
        exit()
    else:
        otsuBinarization(Image.open(sys.argv[1]))
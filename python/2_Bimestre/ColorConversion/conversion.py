# -*- coding: utf-8 -*-
from PIL import Image
import sys
from math import acos,sqrt

# COLOR SYSTEM CONVERSION  RGB -> CMY -> CMYK -> HSV

def RGB_to_CMY(R,G,B):
    C = 1 - R/float(255)
    M = 1 - G/float(255)
    Y = 1 - B/float(255)
    return (C,M,Y)

def RGB_to_HSV(R,G,B):
    R,G,B = R/float(255), G/float(255), B/float(255)
   
    Max = max(R,G,B)
    Min = min(R,G,B)
    Delta = Max - Min
    

    if Delta == 0:
        H = 0
    elif Max == R:
        H = 60 * ( ((G-B)/float(Delta)) % 6  ) 
    elif Max == G:
        H = 60 * ( ((B-R)/float(Delta)) + 2  ) 
    elif Max == B:
        H = 60 * ( ((R-G)/float(Delta)) + 4  ) 

    if Max == 0:
        S = 0
    else:
        S = Delta/Max
    
    V = Max
    return (H,S,V)

def RGB_to_CMYK(R,G,B):
    K = 1 - max(R/float(255) , G/float(255), B/float(255))
    C = (1 - R/float(255) - K )/float(1 - K)
    M = (1 - G/float(255) - K)/float(1 - K)
    Y = (1 - B/float(255) - K)/float(1 - K)
    
    return (C,M,Y,K)

def CMY_to_CMYK(C,M,Y):
    K = min(C,M,Y)
    C = (C-K)/float(1-K)
    M = (M-K)/float(1-K)
    Y = (Y-K)/float(1-K)
    
    return (C,M,Y,K)

def CMY_to_RGB(C,M,Y):
    R = 255 * (1 - C)
    G = 255 * (1 - M)
    B = 255 * (1 - Y)
    
    return (R,G,B)

def CMY_to_HSV(C,M,Y):
    R,G,B = CMY_to_RGB(C,M,Y)
    H,S,V = RGB_to_HSV(R,G,B)
    return (H,S,V)

def CMYK_to_CMY(C,M,Y,K):
    C = min(1, (C*(1-K)+K) )
    M = min(1, (M*(1-K)+K) )
    Y = min(1, (Y*(1-K)+K) )
    
    return (C,M,Y)

def CMYK_to_RGB(C,M,Y,K):
    R = 255 * (1-C) * (1-K)
    G = 255 * (1-M) * (1-K)
    B = 255 * (1-Y) * (1-K)
    
    return (R,G,B)

def CMYK_to_HSV(C,M,Y,K):
    R,G,B = CMYK_to_RGB(C,M,Y,K)
    H,S,V = RGB_to_HSV(R,G,B)

    return (H,S,V)

def HSV_to_RGB(H,S,V):
    if 0 <= H <=360 and 0 <= S <= 100 and 0<= V <=100:
        C = (V/float(100)) * (S/float(100))
        
        X = C*(1 - abs(((H / float(60)) % 2) - 1))
        m = (V/float(100)) -C
        
        if 0 <= H < 60:
            r,g,b = C,X,0
        elif 60<= H < 120:
            r,g,b = X,C,0
        elif 120<= H < 180:
            r,g,b = 0,C,X
        elif 180<= H < 240:
            r,g,b = 0,X,C
        elif 240<= H < 300:
            r,g,b = X,0,C
        elif 300<= H < 360:
            r,g,b = C,0,X
        
        R,G,B = (r+m)*255, (g+m)*255, (b+m)*255

        return (round(R),round(G),round(B))

    else:
        print("Informe H S V válidos")

def HSV_to_CMY(H,S,V):
    
    R,G,B = HSV_to_RGB(H,S,V)
    return RGB_to_CMY(R,G,B)

def HSV_to_CMYK(H,S,V):
    R,G,B = HSV_to_RGB(H,S,V)
    
    return RGB_to_CMYK(R,G,B)
    

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("compile assim 'python 'conversion.py' 'Sistema' '(pixels)' ")
        print("RGB  -> (R,G,B)")
        print("HSV  -> (H,S,V) 0 < H < 360, 0 < S < 100, 0 < V < 100")
        print("CMYK -> (C,M,Y,K)")
        exit()
    elif sys.argv[1] == 'RGB':
        RGB = sys.argv[2].split(",")
        c,m,y   = RGB_to_CMY  ( int(RGB[0]), int(RGB[1]), int(RGB[2]))
        C,M,Y,K = RGB_to_CMYK ( int(RGB[0]), int(RGB[1]), int(RGB[2]))
        H,S,V   = RGB_to_HSV ( int(RGB[0]), int(RGB[1]), int(RGB[2]) )
        print("RGB -> CMY")
        print("Cian: {} Magenta: {} Yellow: {} ".format(c,m,y))
        print("RGB -> CMYK")
        print("Cian: {} Magenta: {} Yellow: {} Black: {}".format(C,M,Y,K) )
        print("RGB -> HSV")
        print("H: {} º  S: {} %  V: {} %".format(H, round(S*100,2) , round(V*100,2)))
    elif sys.argv[1] == 'CMY':
        CMY = sys.argv[2].split(",")
        C,M,Y,K =   CMY_to_CMYK ( float(CMY[0]), float(CMY[1]), float(CMY[2]))
        R,G,B   =   CMY_to_RGB  ( float(CMY[0]), float(CMY[1]), float(CMY[2]))
        H,S,V   =   CMY_to_HSV  ( float(CMY[0]), float(CMY[1]), float(CMY[2]))
        print("CMY -> RGB")
        print("R: {} G: {} B: {}".format(int(round(R)),int(round(G)),int(round(B))))
        print("CMY -> CMYK")
        print("Cian: {} Magenta: {} Yellow: {} Black: {}".format(C,M,Y,K) )
        print("CMY -> HSV")
        print("H: {} º  S: {} %  V: {} %".format(H, round(S*100,2) , round(V*100,2)))

    elif sys.argv[1] == 'CMYK':
        CMYK = sys.argv[2].split(",")
        #print CMYK
        C,M,Y = CMYK_to_CMY ( float(CMYK[0]), float(CMYK[1]), float(CMYK[2]), float(CMYK[3]) )
        R,G,B = CMYK_to_RGB ( float(CMYK[0]), float(CMYK[1]), float(CMYK[2]), float(CMYK[3]) )
        H,S,V = CMYK_to_HSV ( float(CMYK[0]), float(CMYK[1]), float(CMYK[2]), float(CMYK[3]) )
        print("CMYK -> RGB")
        print("R: {} G: {} B: {}".format(int(round(R)),int(round(G)),int(round(B))))
        print("CMYK -> CMY")
        print("Cian: {}   Magenta: {}  Yellow: {}".format(C,M,Y))
        print("CMYK -> HSV")
        print("H: {} º  S: {} %  V: {} %".format(H, round(S*100,2) , round(V*100,2)))
    elif sys.argv[1] == 'HSV':
        HSV     = sys.argv[2].split(",")
        #print HSV
        R,G,B   = HSV_to_RGB( float(HSV[0]), float(HSV[1]), float(HSV[2]) )
        C,M,Y   = HSV_to_CMY( float(HSV[0]), float(HSV[1]), float(HSV[2]) )
        c,m,y,k = HSV_to_CMYK( float(HSV[0]), float(HSV[1]), float(HSV[2]) )
        print("HSV -> RGB")
        print("R: {}  G: {}  B: {}".format(round(R),round(G),round(B)))
        print("HSV -> CMY")
        print("Cian: {} Magenta: {} Yellow: {}".format(C,M,Y) )
        print("HSV -> CMYK")
        print("Cian: {} Magenta: {} Yellow: {} Black: {}".format(c,m,y,k) )
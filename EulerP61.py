#Euler project P61
import math
#generate a four digit triangle number
nTri = 1
tri = 1
answer = False
while(answer == False):
    while tri < 10000:
        tri = nTri * (nTri + 1) / 2
        strTri = str(tri)
        nTri += 1
        if len(strTri)!=6:
            continue
        #print(tri)
        #generate a four digit Square number and check if the first
        #two digits match the last two of Tri
        nSqr = 1
        sqr = 1
        while (sqr < 10000):
            sqr = nSqr * nSqr
            strSqr = str(sqr)
            nSqr += 1
            if len(strSqr) != 4:
                continue
            #print("sqr: " + strSqr)
            if (strSqr[0:2] == strTri[2:4]):
                #print(sqr)
                #now reapeat but with square number as the seed and
                #pentagonal as the next number

                nPen = 1
                pen = 1
                while (pen < 10000):
                    pen = nPen * ( 3 * nPen - 1) / 2
                    strPen = str(pen)
                    nPen += 1
                    #print("pen: " + strPen)
                    if len(strPen) != 6:
                        continue
                    
                    if (strPen[0:2] == strSqr[2:4]):
                        #print(pen)
                        #hexagonal
                        nHexa = 1
                        hexa = 1
                        while (hexa < 10000):
                            hexa = nHexa * ( 2 * nHexa - 1)
                            strHexa = str(hexa)
                            nHexa += 1
                            if len(strHexa) != 4:
                                continue
                            if (strHexa[0:2] == strPen[2:4]):

                            #Heptagonal    
                                nHep = 1
                                hep = 1
                                while (hep < 10000):
                                    hep = nHep * ( 5 * nHep - 3) / 2
                                    strHep = str(hep)
                                    nHep += 1
                                    if len(strHep) != 6:
                                        continue
                                    if (strHep[0:2] == strHexa[2:4]):
                                        
                                        #octogonal
                                    
                                        nOcta = 1
                                        octa = 1
                                        while (octa < 10000):
                                            octa = nOcta * ( 3 * nOcta - 2)
                                            strOcta = str(octa)
                                            nOcta += 1
                                            if len(strOcta) != 4:
                                                continue
                                            if (strOcta[0:2] == strHep[2:4]):
                                                print("oct: " + strOcta)
                                                numbers = [tri, sqr, pen, hexa, hep, octa]
                                                print("answer:")
                                                print(sum(numbers))
                                                print(numbers)
                                                print(strTri)
                                                if (strOcta[2:4] == strTri[0:2]):
                                                    answer = True
                            
        
        
        
    
    

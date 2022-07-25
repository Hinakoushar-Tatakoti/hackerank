import random
import math 


def degenerateTriangle(x1, y1, x2, y2, x3, y3):
    ab=(x1-y1)
    t1 =abs((x1-x2)^2 +(y1-y2)^2)
    bc=math.sqrt(t1)
    t2=abs((x2-x3)^2 +(y2-y3)^2)
    ac=math.sqrt(t2)
    if ((ab+bc)>ac) & ((bc+ac)>ab) & ((ab+ac)>bc): return True
 
def area(x1, y1, x2, y2, x3, y3):
  return abs((x1*(y2-y3)+(x2*(y3-y1))+(x3*(y1-y2)))/2.0)
 

def isInside(x1, y1, x2, y2, x3, y3, xp, yp,xq,yq):
    if not degenerateTriangle(x1, y1, x2, y2, x3, y3):
        return 0
    A = area (x1, y1, x2, y2, x3, y3)
        ## fpr point p

    A1p = area (xp, yp, x2, y2, x3, y3)
    A2p = area (x1, y1, xp, yp, x3, y3)
    A3p = area (x1, y1, x2, y2, xp, yp)

## point q
    A1q = area (xq, yq, x2, y2, x3, y3)
    A2q = area (x1, y1, xq, yq, x3, y3)
    A3q = area (x1, y1, x2, y2, xq, yq)
    if(A == A1p + A2p + A3p) & (A == A1q + A2q + A3q):
        return 3
    elif (A == A1p + A2p + A3p):
        if not (A == A1q + A2q + A3q):
            return 1
    elif (A == A1q + A2q + A3q):
        if not (A == A1p + A2p + A3p):
            return 2
    else:
        return 4
    

if __name__=='__main__':
    # Driver code
    #print(isInside(0, 0, 2, 0, 4, 0, 2, 0,4,0))
    print(isInside(3, 1, 7, 1, 5, 5, 5, 2,6,3))
    #print(isInside(3, 1, 7, 1, 5, 5, 1, 1,2,2))

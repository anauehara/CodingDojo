#Resposta

def flores(t,r,p):
    angle = 360 / p
    for i in range(p):
        arc2(t,r,angle)
        t.lt(180 - angle)
        arc2(t,r,angle)
        t.lt(180)

def flores_compostas(t,r,p,n):
    for i in range(n):
        flores(t,r,p)
        t.lt(360 / (p * n))


flores_compostas(4,50,30)
flores(50,60,40,50)
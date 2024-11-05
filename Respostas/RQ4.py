#Resposta

def formas(t,n,l):
    ang_int = (180 * (n - 2)) / n
    ang_tri = ang_int / 2
    ang_cen = 180 - ang_int
    raio = (math.sin(ang_tri/180 * math.pi) * l )/ math.sin(ang_cen/180 * math.pi)
    t.lt(ang_cen / 2)
    for i in range(n):
        t.fd(raio)
        t.rt(180 - ang_tri)
        t.fd(l)
        t.rt(180 - ang_tri)
        t.fd(raio)
        t.rt(180)
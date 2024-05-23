#1
'''def sahe(m,n) :
    sahe = m*n/2
    return sahe
print(sahe(3,4))
'''
#2
'''def sil(soz) :
    netice = ""
    evvelki_herf = ""
    for herf in soz :
        if herf != evvelki_herf :
            netice += herf
            evvelki_herf = herf
    return netice

print(sil("iiimtaaaahaaan"))
'''
#3
'''def eded(eded) :
    reqemler = ['0','1','2','3','4','5','6','7','8','9']
    olmayan_reqemler = []
    for reqem in reqemler :
        if reqem not in str(eded) :
            olmayan_reqemler.append(reqem)
    return f"Ededin icinde {olmayan_reqemler} yoxdur"
    

print(eded(8305614820608024402))
'''

#5
'''def bolunen(eded) :
    cem = 0
    for reqem in str(eded) :
        cem += int(reqem)
    if eded%cem == 0 :
        return f"{eded} ededi {cem} ededine qaliqsiz bolunur"
    return f"{eded} ededi {cem} ededine qaliqsiz bolunmur"
print(bolunen(134))'''

#16

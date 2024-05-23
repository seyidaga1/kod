#1
'''def sahe(katet1,katet2) :
    sahe = (katet1*katet2)/2
    return sahe

print(sahe(3,4))
'''
#2
'''def myfunc(soz) :
    yeni_soz = ""
    evvelki_herf = ""
    for i in range(0,len(soz)) :
        if soz[i] != evvelki_herf :
            yeni_soz+=soz[i]
        evvelki_herf = soz[i]
    return yeni_soz
print(myfunc("imtaaaahaaann"))'''




#3
'''def eded(eded) :
    reqemler = ["1","2","3","4","5","6","7","8","9","0"]
    olmayan_reqemler = []
    for i in reqemler :
        if i not in str(eded) :
            olmayan_reqemler.append(i)
    return(f"Ədədin içində {olmayan_reqemler} rəqəmi yoxdur ")
print(eded(8305614820608024402))'''


#4
'''def nomre(nomre) :
    emsal = 1
    if nomre[0:2] == "10" or "77" or "90" or "99" :
        emsal+=3
    if nomre[3] == nomre[4] :
        emsal+=4
    if nomre[6] == nomre[7] == nomre[8] :
        emsal +=5
    elif nomre[6] == nomre[8] :
        emsal+=4
    return(emsal*60)
print(f"Nomrenin qiymeti : {nomre("90-CB-505")} AZN")'''

#5
'''def bolunen(eded) :
    cem=0
    for i in str(eded) :
        cem+=int(i)
    if eded%cem == 0 :
        return(f"Bəli, {eded} ədədi {cem} ədədinə bölünür. ")
    else :
        return(f"Xeyr, {eded} ədədi {cem} ədədinə bölünmür. ")


print(bolunen(134))'''

#6
'''def addim(n):
    dovr = 0
    while len(str(n)) > 1:
        hasil = 1
        for i in str(n):
            hasil *= int(i)
        n = hasil
        dovr += 1
    return dovr

print(addim(82))'''

#7
'''i=1
while i<100 :
    if i%3 == 0 and i%5 == 0 :
        print(i)
    i+=1
'''

#8
'''
eded = int(input("Eded : "))
for i in range(1,eded) :
    if i%2 == 0 :
        print(i)
        i+=2
'''
#9
'''siyahi = [2,2,4,3,6,9,6,1,5,1] 
yeni = []
for i in siyahi :
    if i<=3 :
        yeni.append(i)
print(yeni)
'''
#10
'''siyahi =  [136,135,125,119,146,133,118,106,138,136,127,120] 
minimum = min(siyahi)
maximum = max(siyahi)

ay1 = siyahi.index(minimum)+1
ay2 = siyahi.index(maximum)+1
print(f"{ay1}-ci aydaki mehsulu {ay2}-ci ayda satsaq daha cox gelir elde ederik")
'''
#11
'''for i in range(1,6) :
    print(str(i)*i) '''

#12
'''fibonacci = [0, 1]
while fibonacci[-1] < 100:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
if fibonacci[-1]>100 :
    fibonacci.pop()
print(fibonacci)'''

#13
'''sum = 0
while True :
    
    a = input("Eded :")
    if a == "=" :
        print(sum)
        sum = 0
    else :
        sum +=float(a)
        print("cem ucun '=' duymesine basin")'''

#14
'''a=input("cumle :")
siyahi = a.split(" ")
print(siyahi[-1])'''

#15
'''siyahi = []
while True :
    a= input("eded(sonlandirmaq ucun '=' basin) : ")
    if a == "=" :
        break
    else :
        siyahi.append(int(a)**2)
print(siyahi)
'''
#16
'''s = 0
for i in range(100,200) :
    if i%3 == 0 and i%5 !=0 :
        s+=1
print(s)
'''
#17
'''saitler = ['a','ı','o','u','e','ə','i','ö','ü']
cumle = str(input("Cumle : \n"))
s = 0
for herf in cumle :
    herf = herf.lower()
    if herf in saitler :
        s += 1
print(s)
'''

#18 tam deyil

'''
def check():
    reqemler = "1234567890"
    eded = input("eded : ")
    if len(eded) == 9:
        for reqem in reqemler:
            if reqem not in eded:
                return reqem
        return("+")
    else:
        return ("Ededin uzunlugu 9 reqemden ibaret olmalidir")

print(check())
'''

#19
'''
a = str(input("cumle : "))
sozler = a.split(" ")

print(sozler)
cumle = []
for soz in sozler :
    soz = soz[::-1]
    cumle = soz.append()
print(cumle)'''
#?

#20
'''def qisa(cumle):
    sozler = cumle.split()  
    en_qisa = sozler[0]  
    for soz in sozler:
        if len(soz) < len(en_qisa):
            en_qisa = soz 
    return en_qisa


cumle = input("Cümle : ")
print("En qisa soz:", qisa(cumle))
'''

#21
'''
def uzun(cumle):
    sozler = cumle.split()  
    en_uzun = sozler[0]  
    for soz in sozler:
        if len(soz) > len(en_uzun):
            en_uzun = soz 
    return en_uzun


cumle = input("Cümle : ")
print("En uzun soz:", uzun(cumle))
'''

#22

'''cumle = str(input("Cumle : "))
sozler = cumle.split(" ")
print(len(sozler))'''

#23
'''cumle = str(input("Cumle : "))
sozler = cumle.split(" ")
for soz in sozler :
    if len(soz) == 4 :
        print(soz)'''

#24
'''cumle = str(input("Cumle : "))
sozler = cumle.split(" ")
for soz in sozler :
    if soz[0].lower() == "a" and soz[-1].lower() == "m" :
        print(soz)'''

#25
'''cumle = str(input("Cumle : "))
sozler = cumle.split(" ")
s = 0
for soz in sozler :
    if soz.endswith('lar') :
        s+=1
print(s)'''

#26
'''cumle = str(input("Cumle : "))
sozler = cumle.split(" ")
print(len(sozler))'''

#27
'''
def myFunction(word):
    indexes = []
    for i in range(len(word)):
        if word[i].isupper():
            indexes.append(i)
    return indexes

print(myFunction("HeLlo WorD")) 
'''

#28
'''
def isogram(word) :
    istifade_olunmus_herfler = []
    for letter in word :
        if letter not in istifade_olunmus_herfler :
            istifade_olunmus_herfler.append(letter)
        else :
            return False
    return True

print(isogram("abc"))'''

#29
'''
def convert(word) :
    upper = []
    lower = []
    i = 0
    for letter in word :
        if letter.isupper() :
            upper.append(letter)
        else :
            lower.append(letter)
    if len(upper)<len(lower) :
        for element in upper :
            element.lower()
            i+=1
        
    else :
        for element in lower :
            element.upper()
            i+=1
    return i
print(convert("abCBA"))'''

#30
'''
def armstrong(number) :
    length = len(number)
    s= 0
    for i in number :
        s+= int(i)**length

    if int(number) == s :
        return True
    else :
        return False

print(armstrong("153"))
'''
#31

'''def palindrom(number) :
    number = str(number)
    if len(number) == 4 :
        if number == number[::-1] :
            return "Palindrom"
        else : 
            return "not Palindrom"
    else :
        return "Not 4 digits"


print(palindrom(2332))'''


#32
'''def myfunc(number) :
    number = str(number)
    min = 0
    if len(number) == 5 and int(number)>0:
        for i in number :
            if int(i)<=min :
                return False
            min = int(i)
        return True
    return "Not 5 digits"


print(myfunc(15589))'''




#33
'''def eded(eded) :
    if len(str(eded)) == 4:
        for i in str(eded) :
            if eded % int(i) != 0 :
                return "Eded butun reqemlerine bolunmur"
    else :
        return "Eded 4 reqemli olmalidir"
    return "Eded butun reqemlerine bolunur"


print(eded(12345))'''

#34
'''def eded(eded) :
    eded1 = ''
    if len(str(eded)) == 4:
        for i in str(eded) :
            if int(i)%2 != 0 :
                eded1+=i
    else :
        return "Eded 4 reqemli olmalidir"
    return eded1


print(eded(1024))'''

#35
'''def eded(eded) :
    istifade_olunmus_reqemler = []
    for i in str(eded) :
        if i not in istifade_olunmus_reqemler :
            istifade_olunmus_reqemler.append(i)
        else :
            return "NO"
    return "YES"
print(eded(1223))'''

#36

'''def dayaqNoqtesi(list):
    for a in range(1,len(list)):
        if sum(list[:a]) == sum(list[a+1:]):
            return list[a]
print(dayaqNoqtesi([3,1,5,2,4,6,-1]))'''

#37
'''def fib(eded) :
    siyahi = [1,1]
    while siyahi[-1] + siyahi[-2] < eded :
        yeni_hedd = siyahi[-1] +siyahi[-2]    
        siyahi.append(yeni_hedd)
    return siyahi

print(fib(3))
'''

#38

'''def myFunction(word,list) :
    new_word = ""
    for letter in word :
        if letter not in list :
            new_word+="-"
        else :
            new_word+=letter
    return new_word


print(myFunction("apple", ["r", "t", "e"]))'''

#39
'''def myfunc(n) :
    product = 1
    for i in range(1,n) :
        if i%7 == 0 :
            product*=i
    return product

n = int(input("eded :"))
print(myfunc(n))'''

#40
'''def myfunc(n) :
    list = []
    for i in range(1,n) :
        if str(i).endswith("3") :
            list.append(i)
    return list

n = int(input("eded :"))
print(myfunc(n))'''

#41
'''def myfunc(m,n) :
    siyahi = []
    for i in range(m,n) :
        if i%6 != 0 :
            siyahi.append(i)
    return siyahi

m = int(input("Ilk eded : "))
n = int(input("Son eded :"))
print(myfunc(m,n))'''

#42

'''cumle = str(input("Cumle :"))
cumle = cumle.split()
s = 0
for word in cumle :
    if len(word) == 4 :
        s+=1
print(s)'''

#44
'''import math
eded = int(input("Eded : "))
print(math.factorial(eded))'''

#45
'''def myFunction(word) :
    max = 0
    max1 =""
    for letter in word :
        if word.count(letter)==max :
            if letter not in max1 :
                max = word.count(letter)
                max1 += letter
                
        elif word.count(letter)>max :
            max = word.count(letter)
            max1 = letter
    return max,max1
print(myFunction("balloon"))'''

#46
'''def list(list) :
    s= 0
    for i in list :
        s+=i
    return s

print(list([1, 2, 3, 5, 5]))'''

#47
'''def myFunction(list1,list2) :
    new_list = list1+list2
    return new_list

print(myFunction([True, False], [False, True]))'''

#48

'''def myFunction(cumle) :
    cumle = cumle.split(' ')

    sozler = {}
    for soz in cumle :
        soz = soz.lower().strip(",.?!")
        if soz not in sozler :
            sozler[soz] = 1
        else :
            sozler[soz] +=1
    
    maximum = max(sozler,key=sozler.get)
    return maximum,sozler[maximum]

print(myFunction("Bu cümlədə bu sözü ən çox istifadə edirəm, bu sözü çox istifadə edirəm."))
'''

#49
'''
def myFunction(eded) :
    s = 0 
    for i in str(eded) :
        s+=int(i)
    return(s)


print(myFunction(12345))'''

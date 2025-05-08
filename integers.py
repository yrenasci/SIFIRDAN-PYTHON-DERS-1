#integers, float ve type fonksiyonları
#MATEMATİKSEL İŞLEMLER



#TOPLAMA : " + "
#ÇIKARMA : " - "
#ÇARPMA :  " * "
#BÖLME : " / "
#ÜS ALMA : " ** "
#TAM SAYI BÖLMESİ : " // "
#MUTLAK DEĞER     : " abs "
#YUVARLAMA   : " round "


sayi1 = 5
sayi2 = 3.5
sayi3 = 6 ** 100 #6'nın 100. kuvveti " ** : kuvvet"
sayi4 = 22 / 5 #22 bölü 7 " / :bölme"
sayi5 = 5.5421 #yuvarlama yapılacak

print(sayi1)
print(type(sayi1)) #sayi1'e tam sayı yazdığımız için sonuca integer yani "tam sayı" olarak sonuç verir
print(type(sayi2)) #sayi2'e sayı yazdığımız için sonuca float yani "sayi" olarak sonuç verir
print(sayi3) #direkt sonucu verir
print(sayi4)
print(3 + 5) #toplama
print(5 -8) #çıkarma
print(8 * 5) #çarpma
print(8 / 7) #bölme
print(2 ** 5) #üs alma
print(abs(2 - 9)) #mutlak değer
print(round(8 / 5)) #yuvarlama
print(85 // 4) #tam sayısını alma
print(round(sayi5)) #direkt sayı5'i en yakına tam sayıya yuvarladı
print(round(sayi5,3)) #virgülden sonraki 3 basamaklı sayı


#İŞLEM ÖNECELİĞİ
print(3 * 5 + 8) #23
print(3 + 5 * 6) #33
print((3 + 2) * 5 )



#KARŞILAŞTIRMA OPERETÖRLERİ
#BÜYÜKTÜR : " > "
#KÜÇÜKTÜR : " < "
#EŞİTTİR : " == "
#BÜYÜK EŞİT : " >= "
#KÜÇÜK EŞİT : " <= "
#EŞİT DEĞİL : " ! "

a = 5
b = 9
c = 10

print( a == 5) #a int 5'e eşit mi? --> TRUE
print(a > b) #a int'i b int'inden büyük mü? --> FALSE
print(b < c) #b int'i c int'inden küçük mü? --> TRUE
print( a + b > c) #a ve b intlerinin toplamı c'den büyük mü? --> TRUE
print(a >= 5) #a int'i 5'ten büyük eşit mi? --> TRUE    

y = 5
k = y
y = 9
print(k) #tekrar 5 yazmasının sebebi belleğe öncelikle y=5 yazdığım içindi diğer değerinin bir anlamı yoktur!


#STING VE INTERLARI BİRBİRİNE ÇEVİRME

sayi10 = "100"
sayi11 = 100
print(type(sayi10))
print(type(sayi11))
print(sayi10 == sayi11) #sayi10 = yazı ile yazılan yüz ama sayi11 sayı ile yazılan bir 100 o yüzden -->FALSE
j = int(3.5)
print(j) #ondalıklı yazılmasına rağmen sadece tam sayı alınır.
h = round(-4.8)
print(h) #-5e yubarlar

i = 1
i = 1 +5
print(i) #6

g = 5
g += 5
print(g)

z = 8
z **= 2
print(z)
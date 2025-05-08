mesaj = "Merhaba"
mesaj2 = "Dünya!"

print(mesaj + mesaj2)
print(mesaj + " " + mesaj2)

print(mesaj2[0]) #Bu kod mesajın 0. karakterini yazdır anlamına gelir. Python saymaya her zaman "0" dan başlar. Buna da "index" denir.
print(mesaj[5])
print(mesaj[-3]) #sondan 3. harifi yazdır.
print(mesaj2[0:4]) #0. karakterle 4.karakter arasını yazdır fakat 0 dahil, 4 dahil değildir.
print(mesaj2[ : :2 ]) #0. karakter alınır sonra 2'şerli olarak devam eder.
print(mesaj[2: : 3]) #2. karakterden başla sonra 3'erli yazmaya devam et.
print(mesaj[ : : -1]) #Tersten yazar
print(mesaj.upper()) #Tüm karakterler büyük harflerle yazılır

mesaj = mesaj.upper() #Depolama özelliğiyle mesaja "Hepsi Büyük" komutu verdim.
print(mesaj)

mesaj2 = mesaj2.lower() #Depolama özelliği ile mesaja "Hepsi Küçük" komutu verdim
print(mesaj2)

mesaj2 = mesaj2.capitalize() #sadece baş harfi büyütür.
print(mesaj2)

mesaj3 = "Hello"
mesaj4 = "World!"

print(mesaj3.startswith("he")) #Bir listede "he" ile başlayan var mı yok mu diye arayan string'tir. false verdi
print(mesaj3.startswith("He")) #True dedi
print(mesaj.endswith("a")) #false
print(mesaj.endswith("A")) #true

print(len(mesaj)) #stringin kaç karakterden oluştuğunu gösterir.
print(len(mesaj + mesaj2)) #toplam karakter sayısını yazar
print(mesaj3 * 10) #yan yana 10 kere yazmak

isim = "Kerem"
yas = "23"
print("{} , {} yaşındadır".format(isim,yas)) #1. değişken 1. kümeye ve 2.değişken de 2.kümeye yazılır

isim1 = "Yaren"
mesaj5 = "Naber"

print("{}, {} özledim".format(isim1,mesaj5)) 

print(f"{isim} {isim1} dedi")

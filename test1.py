# print("Merhaba Dünya")

# ----

# Örnek 2: <isim alarak merhaba demek>
# isim = input ('İsminizi Girin: ')
# print("Merhaba "+ isim)

# ----




# ----

# Örnek4: Girilen iki sayının ortalamasını bulma
# sayi1 = input('1. sayı : ')
# sayi2 = input('2. sayı : ')
# ortalama=(int(sayi1)+int(sayi2))/2
# print("Ortalama: {0}" .format(ortalama))


# vize = input('Vize Notunuz : ')
# final = input('Final Notunuz : ')
# endeks=(float(vize)*0.3)+(float(final)*0.7)
# print("Ortalama :{0} ".format(endeks))




# ort = input('Lütfen ortalamanızı Giriniz: ')
# if(int(ort)>=50):
#     print("Geçtiniz")
# else:
#     print("Kaldınız")




# Bir sayının tek mi çift mi olduğunu hesaplama
# sayi = input('Sayı: ')
# if(int(sayi)%2==0):
#     print("Sayı Çifttir.")
# else:
#         print("Sayı Tektir.")




# sayi = input ('Sayı: ')
# if(int(sayi)<0) :
#     print("Sayı Negatiftir.")
# elif(int(sayi)>0) :
#     print("Sayı Pozitiftir.")
# else:
#     print("Sayı Sıfır")
# 

# ----
# ----
# ----


boy = float(input("Boy(m): "))
kilo = float(input("Kilo(kg):"))

endeks = kilo/(boy*boy)

if endeks <=18:
 print("\n Zayıf VKİ:{}" .format(endeks)) 
elif endeks > 18 and endeks <=25 :
   print("\n Normal VKİ:{}" .format(endeks))
elif endeks > 25 and endeks <=30 :
     print("\n obez VKİ:{}" .format(endeks))
elif endeks > 30 :
    print("\n Ciddi Obez VKİ:{}" .format(endeks))

# https://www.fulbright.org.tr/


# a = """Burada
# birkaç satırlı bir
# değişken görüyorsunuz!"""
# print(a)

# a = "Merhaba Dünya!"
# print(a[5])   # e harfini verir

# b = "Merhaba Dünya!"
# print(b[2:5])

# a = "Merhaba Dünya!"
# print(len(a))

# txt = "Akdeniz Bölgesinde dağlar denize paraleldir"
# x = "paralel" in txt
# print(x)
# y = "paralel" not in txt
# print(y)

# yas1 = 36
# yas = 45
# metin = "Benim adım Murat, ve ben {} yaşındayım!"
# print(metin.format(yas1))

# adet = 3
# urun = 567
# fiyat = 49.95
# siparis = "Ben {} parça {} numaralı üründen {} TL karşılığında alacağım."
# print(siparis.format(adet, urun, fiyat))


# txt = 'Ankara\'nın'
# print(txt)

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33
# 
# if b > a:
#   print("b, a'dan büyüktür")
# else:
#       print("b, a'dan büyük değildir.")

# deger1 = "Hello"
# deger2 = 15
# deger3 = ""
# deger4 = 0 
# 
# print(bool(deger1))
# print(bool(deger2))
# print(bool(deger3))
# print(bool(deger4))


# x = 200
# print(isinstance(x, int))
# print("Merhaba Dünya")

# ----

# # Örnek 2: <isim alarak merhaba demek>
# isim = input ('İsminizi Girin: ')
# print("Merhaba "+ isim)

# ----

# örnek3: iki sayıyı toplama
# sayi1 = input('1. sayı : ')
# sayi2 = input('2. sayı : ')
# toplam= float(sayi1)+float(sayi2)
# print("Toplam: {0}" .format(toplam))

# ----

# # Örnek4: Girilen iki sayının ortalamasını bulma
# sayi1 = input('1. sayı : ')
# sayi2 = input('2. sayı : ')
# ortalama=(int(sayi1)+int(sayi2))/2
# print("ortalama:{0}" .format(ortalama))

# ----

# # Vize final notu
# vize = input ('lütfen vize notunuzu giriniz:')
# final = input('lütfen final notunuzu giriniz:')
# ortalama = (float(vize) *0.3) + (float (final)*0.7))
# print ("ort. notunuz:{0}" . format (Ortalama))

# ----

# # vize = input('Vize Notunuz : ')
# # final = input('Final Notunuz : ')
# # ortalama=(float(vize)*0.3)+(float(final)*0.7)
# # print("Ortalama :{0} ".format(ortalama))

# ----

# y1 = input('1. Yazılı : ')
# y2 = input('2. Yazılı : ')
# y3 = input('3. Yazılı : ')
# ortalama= (float(y1)+float(y2)+float(y3))/3
# print ("Ortalama :{0} ".format(ortalama))

# ----

# ort = input('Lütfen ortalamanızı Giriniz: ')
# if(int(ort)>=50):
#     print("Geçtiniz")
# else:
#     print("Kaldınız")

# ----

# Bir sayının tek mi çift mi olduğunu hesaplama
# sayi = input('Sayı: ')
# if(int(sayi)%2==0):
#     print("Sayı Çifttir.")
# else:
#         print("Sayı Tektir.")

# ----

#Girilen sayının pozitif negatiflik değeri

# sayi = input ('Sayı: ')
# if(int(sayi)<0) :
#     print("Sayı Negatiftir.")
# elif(int(sayi)>0) :
#     print("Sayı Pozitiftir.")
# elif(int(sayi)== 0) :
#     print("Sayı Sıfır")

# ----
# ----
# ----



# Boy kilo endeksi

# boy = float(input("Boy(m): "))
# kilo = float(input("Kilo(kg):"))
# 
# endeks = kilo /(boy*boy)
# 
# if endeks <=18:
#      print("\n Zayıf VKİ:{}" .format(endeks))
# elif endeks > 18 and endeks <=25 :
#         print("\n Normal VKİ:{}" .format(endeks))
# elif endeks > 25 and endeks <=30 :
#           print("\n Obez VKİ:{}" .format(endeks))
# elif endeks > 30 :
#          print("\n Ciddi Obez VKİ:{}" .format(endeks))


# liste = ["elma", "muz", "ayva"]
# liste[-1] = "mandalina"
# for x in liste:
#     print(x)


# liste = ["elma", "muz", "kiraz"]
# if "elma" in liste
#    print("Evet, elma listede var!")


# liste = ["elma", "muz", "kiraz"]
# print(len(liste))

# liste = ["elma", "muz", "kiraz"]
# liste.append("kavun")
# print(liste)


# liste1 = ["elma", "muz", "kiraz", "kavun"]
# liste2 = ["domates","biber","salatalık"]
# 
# for x in liste2:
#     liste1.append(x)
# 
# print(liste1)

# ornTuple = ("muz", "elma", "kiraz")
# print(ornTuple)


# x =("muz","elma","kiraz")
# y = list(x)
# y[1] = "kivi"
# x = tuple(y)
# 
# print(x)

# ornekSet = {"elma", "muz", "kiraz"}
# 
# print("armut" in ornekSet) #listede yoksa false, varsa true der.


# ornekSet = {"elma", "muz", "kiraz"}
# ornekSet.update(["portakal", "mango", "üzüm"])
# print(ornekSet)

# otomobil = {
#   "uretici": "Renault",
#   "model": "Clio",
#   "yil": 2009
# }
# otomobil["yil"] = 2020;
# print(otomobil);


# otomobil = {
#   "uretici": "Ford",
#   "model": "Mustang",
#   "yil": 1969
# }
# if "model" in otomobil:
#   print("Evet; model, otomobil sözlüğünün bir anahtarıdır")
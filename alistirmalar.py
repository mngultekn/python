# for x in range (*);
# for y in range (*)
#   print(x+y)

# for {*} in range (x):
# for {*} in range (y):
# 
#   print("x+y")

# for x in range (6):
#     for y in range (6):
#         if(x==y):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print("\n")     


# sayac=0
# sayi=input('Sayı: ')
# for i in range(2,int(sayi)):
#     if(int(sayi)%i==0):
#         sayac+=1
#         break
#     if(sayac!=0):
#         print("Sayı Asal Sayı Değildir.")
#     else:
#          print("Sayı Asal Sayıdır.")

 
# def daireAlan(yaricap):
#     alan = float(yaricap) * float(yaricap)*3.14
#     print ("Alan :",alan)
#     return alan
#  
# r = input("Yarıçapı Gir :")
#  
# daireAlan(r)


from random import randint

def oyun():
    rand=randint(1, 100)
    sayac=0
 
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))
        break
    
def zorluk_belirle():
    while True:
        zorluk = input("Oyun Zorluk Seviyesini Seçiniz.(Kolay/Zor)").lower()
        if zorluk == "kolay":
            return 10
        elif zorluk == "zor":
            return 5
        else:
            print("Geçersiz giriş, lütfen 'kolay' ya da 'zor' olarak giriniz...")
            
tahmin_hakki = zorluk_belirle()
print(f"Tahmin Hakkınız: {tahmin_hakki}")

while tahmin_hakki > 0:
    print(f"Kalan tahmin hakkınız: {tahmin_hakki}")
    oyun()
    tahmin_hakki -= 1
    
print("Tahmin hakkınız bitti ve oyun sonra erdi")

# from random import randint
# 
# def oyun():
#     rand = randint(1, 100)
#     sayac = 0
# 
#     while True:
#         sayac += 1
#         sayi = int(input("1 ile 100 arasında değer girin (0 çıkış): "))
# 
#         if sayi == 0:
#             print("Oyunu İptal Ettiniz")
#             break
#         elif sayi < rand:
#             print("Daha Yüksek Bir Sayı Girin.")
#         elif sayi > rand:
#             print("Daha Düşük Bir Sayı Girin.")
#         else:
#             print("Rastele seçilen sayı {0}!".format(rand))
#             print("Tahmin sayınız {0}".format(sayac))
#             break
# # buraya kadar ki kodu hoca vermiş olup buradan sonrasına oyuna zorluk veya kolaylık tanımladım.
# # zoru seçerse 5  kolayı seçerse 10 tahmin hakkı verdirttim.
# 
# def zorluk_belirle():
#     while True:
#         zorluk = input("Oyun zorluk seviyesini seçin (kolay/zor): ").lower()
#         if zorluk == "kolay":
#             return 10
#         elif zorluk == "zor":
#             return 5
#         else:
#             print("Geçersiz giriş, lütfen 'kolay' veya 'zor' olarak girin.")
# 
# tahmin_hakki = zorluk_belirle()
# print(f"Tahmin hakkınız: {tahmin_hakki}")
# 
# while tahmin_hakki > 0:
#     print(f"Kalan tahmin hakkınız: {tahmin_hakki}")
#     oyun()
#     tahmin_hakki -= 1
# 
# print("Tahmin hakkınız bitti. Oyun sona erdi.")






            
 
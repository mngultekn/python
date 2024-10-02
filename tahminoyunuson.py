from random import randint

def oyun(rand, tahmin_hakki):
    sayac = 0

    while sayac < tahmin_hakki:
        sayac += 1
        sayi = int(input("1 ile 100 arasında değer girin (0 çıkış): "))

        if sayi == 0:
            print("Oyunu İptal Ettiniz")
            break
        elif sayi < rand:
            print("Daha Yüksek Bir Sayı Girin.")
        elif sayi > rand:
            print("Daha Düşük Bir Sayı Girin.")
        else:
            print("Tebrikler! Doğru tahmin ettiniz.")
            print("Tahmin sayınız {0}".format(sayac))
            return True

    print("Bütün tahmin haklarınızı kullandınız. Doğru tahmin yapamadınız.")
    return False

def zorluk_belirle():
    while True:
        zorluk = input("Oyun zorluk seviyesini seçin (çok kolay/kolay/zor/çok zor): ").lower()
        if zorluk == "çok kolay":
            return 20
        if zorluk == "kolay":
            return 10
        if zorluk == "zor":
            return 6
        elif zorluk == "çok zor":
            return 3
        else:
            print("Geçersiz giriş, lütfen 'çok kolay','kolay' veya 'zor' olarak giriniz.")

while True:
    tahmin_hakki = zorluk_belirle()
    print(f"Tahmin hakkınız: {tahmin_hakki}")

    rand_num = randint(1, 100)  

    kazandi = oyun(rand_num, tahmin_hakki)

    if not kazandi:
        print(f"Kaybettiniz! Tutulan sayı: {rand_num}")

    devam = input("Yeni oyun oynamak ister misiniz? (evet/hayır): ").lower()
    if devam != "evet":
        print("Oyun bitti... İyi günler!")
        break

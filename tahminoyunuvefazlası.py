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
#             return False
#         elif sayi < rand:
#             print("Daha Yüksek Bir Sayı Girin.")
#         elif sayi > rand:
#             print("Daha Düşük Bir Sayı Girin.")
#         else:
#             print(f"Rastele seçilen sayı {rand}!")
#             print(f"Tahmin sayınız {sayac}")
#             return True
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
# kalan_tahmin = tahmin_hakki
# oyun_devam = True
# 
# while kalan_tahmin > 0 and oyun_devam:
#     print(f"Kalan tahmin hakkınız: {kalan_tahmin}")
#     oyun_devam = oyun()
#     kalan_tahmin -= 1
# 
# if kalan_tahmin == 0:
#     print("Tahmin hakkınız bitti. Oyun sona erdi.")



# -----------------------------------



#  İSİMDE Kİ HARF SAYISINI HESAPLAYAN UYGULAMA!
# from tkinter import *
# from tkinter import messagebox
# 
# def onayla():
#     ad = E1.get()
#     if ad:
#         harf_sayisi = len(ad)
#         messagebox.showinfo("Onay", f"Merhaba, {ad}!\nAdınızda {harf_sayisi} harf bulunmaktadır.")
#     else:
#         messagebox.showwarning("Uyarı", "Lütfen bir ad girin.")
# 
# pencere = Tk()
# pencere.title("BY Tarık Garavar")
# pencere.geometry("400x300")
# 
# uygulama = Frame(pencere)
# uygulama.grid()
# 
# L1 = Label(uygulama, text="Adınızı Girin")
# L1.grid(padx=110, pady=10)
# 
# E1 = Entry(uygulama, bd=2)
# E1.grid(padx=110, pady=3)
# 
# onay_button = Button(uygulama, text="Onayla", command=onayla)
# onay_button.grid(pady=10)
# 
# pencere.mainloop()


# -----------------------------------


# from tkinter import *
# from tkinter import messagebox
# 
# def check_name():
#     entered_name = E1.get().lower()
#     if entered_name == "Tarık":
#         messagebox.showinfo("Hoş Geldiniz", "Hoş geldiniz efendim, şu an her şey yolunda.")
#     elif entered_name == "Muhammed":
#         messagebox.showinfo("Özel Mesaj", "Sayın Muhammed, özel erişim algılandı!")
#     else:
#         messagebox.showinfo("Hoş Geldiniz", f"Hoş geldiniz, {entered_name}!")
# 
# # Create the main window
# pencere = Tk()
# pencere.title("Muhammed Gültekin")
# pencere.geometry("350x250")
# 
# # Create a frame to organize widgets
# uygulama = Frame(pencere)
# uygulama.grid()
# 
# # Create a label and place it in the frame
# L1 = Label(uygulama, text="Adınızı Girin: ")
# L1.grid(padx=110, pady=10)
# 
# # Create an entry widget (for user input) and place it in the frame
# E1 = Entry(uygulama, bd=2)
# E1.grid(padx=110, pady=3)
# 
# # Create a button and associate the check_name function with it
# btn = Button(uygulama, text="Hoş Geldiniz ", command=check_name)
# btn.grid(pady=10)
# 
# # Start the Tkinter event loop
# pencere.mainloop()
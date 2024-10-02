import tkinter as tk
from tkinter import ttk

def film_sec():
    film_secim = var_film.get()

    if film_secim == "1":
        return 150
    elif film_secim == "2":
        return 180
    elif film_secim == "3":
        return 160
    elif film_secim == "4":
        return 100
    else:
        print("Geçersiz film seçimi. Varsayılan olarak 'Kolpaçino 4 4'lük' seçildi.")
        return 150

def tiyatro_sec():
    tiyatro_secim = var_tiyatro.get()

    if tiyatro_secim == "1":
        return 150
    elif tiyatro_secim == "2":
        return 140
    elif tiyatro_secim == "3":
        return 120
    else:
        print("Geçersiz tiyatro seçimi. Varsayılan olarak 'Bir Yaz Gecesi Rüyası' seçildi.")
        return 120

def hesapla():
    secim = var_secim.get()

    if secim == "1":
        ucret = film_sec()
    elif secim == "2":
        ucret = tiyatro_sec()
    else:
        result_label.config(text="Geçersiz seçim. Program sonlandırılıyor.")
        return

    ogrenci = var_ogrenci.get()
    kisi_sayisi = int(var_kisi_sayisi.get())
    cinsiyet = var_cinsiyet.get()

    if ogrenci.lower() == "e":
        ucret = ucret / 2

    if cinsiyet.lower() == "erkek":
        ucret = ucret * 0.85

    toplam_tutar = ucret * kisi_sayisi

    result_label.config(text="Ödemeniz gereken toplam tutar: {}".format(toplam_tutar))

# Tkinter penceresini oluşturur
root = tk.Tk()
root.title("Bilet Satış Uygulaması")

# Değişkenler
var_secim = tk.StringVar()
var_film = tk.StringVar()
var_tiyatro = tk.StringVar()
var_ogrenci = tk.StringVar()
var_kisi_sayisi = tk.StringVar()
var_cinsiyet = tk.StringVar()

# Arayüz öğeleri
film_label = tk.Label(root, text="Film Seçenekleri:")
film_label.grid(row=0, column=0, sticky="w")

film_options = ["Ölümlü Dünya 2 - 150 TL", "Kolpaçino 4 4'lük - 180 TL", "Nefes: Yer Eksi İki - 160 TL", "Hayrimatör - 100 TL"]
film_menu = tk.OptionMenu(root, var_film, *film_options)
film_menu.grid(row=1, column=0)

tiyatro_label = tk.Label(root, text="Tiyatro Seçenekleri:")
tiyatro_label.grid(row=2, column=0, sticky="w")

tiyatro_options = ["Macbeth- 150 TL", "Romeo ve Juliet - 140 TL", "Bir Yaz Gecesi Rüyası - 120 TL"]
tiyatro_menu = tk.OptionMenu(root, var_tiyatro, *tiyatro_options)
tiyatro_menu.grid(row=3, column=0)

secim_label = tk.Label(root, text="Lütfen Sinema için (1) Tiyatro için (2) tuşlayınız:")
secim_label.grid(row=4, column=0, sticky="w")

secim_entry = tk.Entry(root, textvariable=var_secim)
secim_entry.grid(row=5, column=0)

ogrenci_label = tk.Label(root, text="Öğrenci misiniz? (E/H):")
ogrenci_label.grid(row=6, column=0, sticky="w")

ogrenci_entry = tk.Entry(root, textvariable=var_ogrenci)
ogrenci_entry.grid(row=7, column=0)

kisi_sayisi_label = tk.Label(root, text="Kaç kişi için bilet alacaksınız?")
kisi_sayisi_label.grid(row=8, column=0, sticky="w")

kisi_sayisi_entry = tk.Entry(root, textvariable=var_kisi_sayisi)
kisi_sayisi_entry.grid(row=9, column=0)

cinsiyet_label = tk.Label(root, text="Cinsiyetiniz (Erkek/Kadın):")
cinsiyet_label.grid(row=10, column=0, sticky="w")

cinsiyet_entry = tk.Entry(root, textvariable=var_cinsiyet)
cinsiyet_entry.grid(row=11, column=0)

calculate_button = tk.Button(root, text="Hesapla", command=hesapla)
calculate_button.grid(row=12, column=0, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=13, column=0)

# Tkinter penceresini başlat
root.mainloop()

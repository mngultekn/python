# #  Vize final notu
# vize = input("lütfen vize notunuzu giriniz:")
# final = input("lütfen final notunuzu giriniz:")
# 
# ortalama = (float(vize)*0.3) +(float(final)*0.7)
# 
# print("ort. notunuz: {0}" .format(ortalama))

# vize = input('Vize Notunuz : ')
# final = input('Final Notunuz : ')
# ortalama = (float(vize)*0.3)+(float(final)*0.7)
# print("Ortalama :{0} " .format(ortalama))

# Boy kilo endeksi
# 
boy = float(input("Boy(m): "))
kilo = float(input("Kilo(kg):"))

endeks = kilo/(boy*boy)
if endeks <=18:
    print("\n Zayıf VKİ:{}" .format(endeks))
elif endeks > 18 and endeks <=25 :
    print("\n Normal VKİ:{}" .format(endeks))
elif endeks > 25 and endeks <=30 :
    print("\n Obez VKİ:{}" .format(endeks))
elif endeks > 30 :
    print("\n Ciddi Obez VKİ:{}" .format(endeks))


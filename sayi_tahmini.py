import random
import time

"""

SAYI TAHMİNİ

1 ve 40 ARASINDAKİ SAYILARI TAHMİN EDİNİZ

"""


rastgele_sayi = random.randint(1,40)

tahmin_hakki = 7

while True:
    tahmin = int(input("Tahmininiz: "))

    if(tahmin<rastgele_sayi):
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin...")

        tahmin_hakki = tahmin_hakki - 1

    elif(tahmin > rastgele_sayi):
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin...")

        tahmin_hakki = tahmin_hakki - 1

    else:
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)

        print("Tebrikler, sayıyı doğru bildiniz.. :)", rastgele_sayi)
        break

    if(tahmin_hakki == 0):
        print("Tahmin Hakkınız Bitmiştir...")
        print("Sayımız: ",rastgele_sayi)
        break




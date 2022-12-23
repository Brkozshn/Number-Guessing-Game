'''
Make a number guessing game from 1 to 100
Scoring out of 100 each question 20 points
use random module
The rating will be out of 100.
get the right information from the user, each question will be calculated over the specified number of lives, and 10 rights will be set as -10.
reduce from 100
Guide the user up and down.
Take the right from user
'''

import random

rastgeleSayi = random.randint(1,100)
print(rastgeleSayi)


hak = int(input("Lutfen istediginiz hak sayisini girin :"))

kullaniciSayi = int(input("Lutfen tahmin icin bir sayi girin :"))

puan = 100 
ceza = puan / hak

while 0 < hak <= 20:
    print(f'Tahmin icin {hak} hakkiniz bulunmaktadir.')
    if rastgeleSayi > kullaniciSayi:
        print("Sayi yukaridadir.")
        hak -= 1
        puan -= ceza
        kullaniciSayi = int(input("Lutfen tahmin icin bir sayi girin :"))


    elif rastgeleSayi < kullaniciSayi:
        print("Sayi asagidadir.")
        hak -= 1
        puan -= ceza
        kullaniciSayi = int(input("Lutfen tahmin icin bir sayi girin :"))

    elif rastgeleSayi == kullaniciSayi:
        print(f'Tebrikler {puan} aldiniz.')
        break

    elif hak == 0:
        print(f'Kaybettiniz {hak} hakkiniz kaldi')
        break

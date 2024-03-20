#soru3
sayi1 = int(input("Bir sayi giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))
sayi3 = int(input("Üçüncü sayiyi giriniz: "))

if (sayi1>sayi2) and (sayi1>= sayi3):
    buyukSayi = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    buyukSayi=sayi2
else:
    buyukSayi=sayi3

totalText = f"Girdiğiniz sayilardan en büyüğü= {buyukSayi}."
print(totalText)
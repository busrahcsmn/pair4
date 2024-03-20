#soru5
sayi =input("Lütfen bir sayi giriniz: ")

tersten = sayi[::-1]

if sayi == tersten:
    print("Bu sayi bir palindromdur.")
else:
    print("Bu sayi bir palindrom değildir.")



#soru5 (2. yol)
def palindrom_mu(sayi):
    sayi_str = str(sayi)
    tersi = sayi_str[::-1]

    if sayi_str == tersi:
        return True
    else:
        return False

sayi = (input("Bir sayi girin: "))

if palindrom_mu(sayi):
    print("Girdiğiniz sayi bir palindromdur.")
else:
    print("Girdiğiniz sayi bir palindrom değildir.")
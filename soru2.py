#soru2:
maas = float(input("Lütfen maaşiniiı giriniz: "))
zamOrani = float(input("Lütfen zam oraninizin yüzde kaç olduğunu giriniz: "))
zamliMaas = (maas*(100 + zamOrani)/100)

totalText = f"Zamli maaşiniz= {zamliMaas}"
print(totalText)
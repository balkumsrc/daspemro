bulan = int(input("Bulan lahir saya: "))
for i in range (1,101):
    if i % bulan == 0:
        print("Bulan")
    else:
        print(i)

n = int(input("Ievadiet savu skaitli: "))
skaitlis = 1

if n == 1:
    print(f"Summa ir {n}")
elif n <= 0:
    print("Ievadīts nederīgs skaitlis, pamēģiniet vēlreiz")
else:
    for i in range (n-1):
        n = n + skaitlis
        skaitlis = skaitlis + 1
    summa = n
    print(f"Summa ir {summa}")
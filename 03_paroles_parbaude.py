password = "123456789"
parole = ""
meginajumi = 3

while meginajumi >= 1 and parole != password:
    parole = input("Ievadiet paroli: ")
    if parole == password:
        print("Piekļuve atļauta")
    else:
        print("Piekļuve bloķēta")
        meginajumi = meginajumi - 1
        print(f"Jums palika {meginajumi} mēģinājumi")
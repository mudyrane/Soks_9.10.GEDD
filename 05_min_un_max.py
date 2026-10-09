skaitlis = int(input("Ievadiet skaitļu skaitu: "))
if skaitlis <=0:
    print("Kļuda, nevar būt mazāk par 1")
else:
    for i in range(skaitlis):
        skaitlis = int(input(f"Ievadiet {i + 1} skaitli: "))
        if i == 0:
            mazakais = skaitlis
            lielakais = skaitlis
        else:
            if skaitlis < mazakais:
                mazakais = skaitlis
            if skaitlis > lielakais:
                lielakais = skaitlis
    print(f"Mazakais skaitlis ir {mazakais}")
    print(f"Lielakais skaitlis ir {lielakais}")
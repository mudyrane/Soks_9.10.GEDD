vecums = int(input("Ievadi savu vecumu: "))

grupa = "bērns"

if vecums <= 10:
    grupa = "bērns"
elif vecums <= 17:
    grupa = "pusaudzis"
elif vecums <= 64:
    grupa = "pieaugušais"
else:
    grupa = "seniors"

print(f"Jūsu vecuma grupa ir {grupa}.")
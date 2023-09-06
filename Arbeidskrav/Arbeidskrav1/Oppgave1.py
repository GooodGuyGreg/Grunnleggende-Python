# Oppgave 1
# 1
navn = str(input("Skriv inn ditt navn her: "))
print(f"Hei, {navn}")

# 2
tall = int(input("Skriv inn et positivt, negativt eller null: "))
if tall > 0:
    print(f"{tall} er positivt!")
elif tall < 0:
    print(f"{tall} er negativt!")
else:
    print(f"{tall} er null!")

# 3
dobbeltTall = int(input("Skriv inn et tall du vil ha det dobbelte av: "))
print(dobbeltTall*2)

# 4
baktekst = str(input("Skriv inn tekst du vil ha baklengs: ")[::-1])
print(baktekst)

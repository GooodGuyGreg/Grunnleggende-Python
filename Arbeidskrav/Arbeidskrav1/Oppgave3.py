# Oppgave 3
# 1
print("___Oppg1:___")
DyrListe = ["Zebra", "Orangutang", "Katt", "Sel", "Slange"]
print(*DyrListe, sep= "\n")
print()
# 2
print("___Oppg2:___")
DyrNavn = ["Milly", "Oliver", "Luna", "Sammy", "Slytherin"]

print(f"{DyrNavn[0]} er en {DyrListe[0]}")
print(f"{DyrNavn[1]} er en {DyrListe[1]}")
print(f"{DyrNavn[2]} er en {DyrListe[2]}")
print(f"{DyrNavn[3]} er en {DyrListe[3]}")
print(f"{DyrNavn[4]} er en {DyrListe[4]}\n")

# 3
print("___Oppg3:___")
print(f"Det første dyret er {DyrListe[0]} og det siste dyret er {DyrListe[-1]} i en uorganisert liste.\n")

# 4
print("___Oppg4:___")
DyrListe.sort()
DyrListe.reverse()
print(f"{DyrListe}\n")

# 5
print("___Oppg5:___")
DyrDict = {
    "Luna":
        "Katt",
    "Oliver":
        "Orangutang",
    "Sammy":
        "Sel",
    "Slytherin":
        "Slange",
    "Milly":
        "Zebra"
}

for i in DyrDict:
    print(i," er en ", DyrDict[i])


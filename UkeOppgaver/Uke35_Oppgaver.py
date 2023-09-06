import math
#Oppgave 1
"""
# Setter variabelen til alderen min
alder = 23
# Printer ut variabel alder
print(alder)
"""

# Oppgave 2
"""
# Lagrer input som en variabel slik at navnet blir lagret i name
name = input("Hva heter du? :")
# Printer ut name
print(f"Heisann, {name}")
"""

# Oppgave 3
"""
tall1 = int(input("Skriv et heltall :"))
tall2 = float(input("Skriv inn et desimaltall :"))

print(f"Her har du tallene addert: {tall1 + tall2}")
print(f"Her har du tallene substrahert: {tall1 - tall2}")
print(f"Her har du tallene multiplisert: {tall1 * tall2}")
print(f"Her har du tallene dividert: {tall1 / tall2}")
"""

# Oppgave 4
"""
tall1 = int(input("Skriv inn tall1 :"))
tall2 = int(input("Skriv inn et tall2 :"))

if tall1 > tall2:
    print("Tall1 er større en tall2")
elif tall1 == tall2:
    print("Tall1 er lik tall2")
else:
    print("Tall1 er mindre enn tall2")
"""

# Oppgave 5
"""
boolsk1 = input("Gi meg en boolsk verdi. (true eller false): ")
boolsk2 = input("Gi meg enda en boolsk verdi. (true eller false: ")

verdi1 = boolsk1 == "true"
verdi2 = boolsk2 == "true"

andop = verdi1 and verdi2

orop = verdi1 or verdi2

notop1 = not verdi1
notop2 = not verdi2

print(f"AND-operasjonen er: {andop}")
print(f"OR-operasjonen er: {orop}")
print(f"NOT-operasjonen1 er: {notop1}")
print(f"NOT-operasjonen2 er: {notop2}")
"""

# Oppgave 6
"""
# Spør brukeren om temperaturen i celsius
TempCelsius = int(input(f"Skriv in Temp i celsius:"))
# Bruker formelen celsius til fahrenhet:
TempFah = (TempCelsius*9/5)+32
# Printer ut til konsoll
print(f"Temperaturen i fahrenhet er {TempFah}°F")
"""

# Oppgave 7
"""
navn = input("Skriv navn:")
alder = input("Skriv alder")
print(f"Hei, {navn}! Du er {alder} år gammel.")
"""

# Oppgave 8
"""
desi_verdi = float(input("Skriv inn desimaltall:"))
print(int(desi_verdi))
"""

# Oppgave 9
"""
tall = int(input("Skriv inn et tall som blir omgjort til kvadraten og kubbikken av: "))
kvadrat_tall = math.sqrt(tall)
kubikk_tall = tall**3

print(f"Tallet ditt er {tall}. Kvadrattallet er: {kvadrat_tall} og Kubikk tallet er: {kubikk_tall}")
"""

# Oppgave 10
fav_ord = str(input("Skriv inn ditt favorittord: "))


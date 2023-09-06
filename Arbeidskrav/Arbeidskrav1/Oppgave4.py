# Oppgave 5
# 1
print("__Kalkulator__\n")
# Har en while True løkke her siden løkken kan kjøre så lenge vi har en avsluttningsknapp.
while True:
    print("Velg en av de fire regneartene: \n"
        "1. Addisjon (Pluss) \n"
        "2. Substraksjon (Minus) \n"
        "3. Multiplikasjon \n"
        "4. Divisjon \n"
        "5. Avslutt \n")
    # Jeg spør brukeren av kalkulatoren om hvilken operasjon han har lyst å utføre og lagrer det i en variabel.
    brukerValg = int(input("Velg en av de fire regneartene her: "))

# If Else statement for hver operasjon
    if brukerValg == 1:
        addTall1 = int(input("Skriv inn et tall: "))
        addTall2 = int(input(f"Skriv inn et tall du vil addere {addTall1} med: "))
        print(f"************** {addTall1} + {addTall2} = {addTall1 + addTall2} **************")

    elif brukerValg == 2:
        subTall1 = int(input("Skriv inn et tall: "))
        subTall2 = int(input(f"Skriv inn et tall du vil subtrahere {subTall1} med: "))
        print(f"************** {subTall1} - {subTall2} = {subTall1 - subTall2} **************")

    elif brukerValg == 3:
        mulTall1 = int(input("Skriv inn et tall: "))
        mulTall2 = int(input(f"Skriv inn et tall du vil multipliere {mulTall1} med: "))
        print(f"************** {mulTall1} * {mulTall2} = {mulTall1 * mulTall2} **************")

    elif brukerValg == 4:
        divTall1 = int(input("Skriv inn et tall: "))
        divTall2 = int(input(f"Skriv inn et tall du vil dividere {divTall1} med: "))
        print(f"************** {divTall1} / {divTall2} = {divTall1 / divTall2} **************")

    else:
        print("Kalkulator avsluttet")
        quit()

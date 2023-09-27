# # Oppgave 1a
# # Lagrer alderen til brukeren i en variabel.
# alder = input("Hvor gammel er du? \n")
# # Printer ut variabelen i konsollen.
# print(f"Du er {alder} år gammel!")

# # Oppgave 1b
# # Prøver å få et heltall ut av brukeren.
# try:
#     heltall = int(input("Skriv inn et heltall: "))
#     print(f"Heltallet du valgte er {heltall}")
#
# # Hvis ikke det er et heltall som blir skrevet i inputen over blir det feilmelding.
# except ValueError:
#     print("Du må skrive inn et heltall! \n Programmet avsluttes.")

# # Oppgave 1c
# # Får brukeren til å velge 2 tall:
# tall1 = float(input("Skriv inn et tall: "))
# tall2 = float(input("Skriv inn et tall til: "))
# # Summerer tallene.
# svar = tall1 + tall2
# # Printer svaret.
# print(f"Svar: {svar}

# Oppgave 1d
# Får brukeren til å skrive inn en setning.
setning = str(input("Skriv en setning: "))
# Splitter setningen der det er mellomrom.
ord = setning.split()
# Teller ordene.
ord_i_setning = len(ord)
# Printer ordene.
print(f"Setningen har {ord_i_setning} ord i seg.")

# Oppgave 1e
lengsteOrd = max(ord)
print(f"Lengste ord: {lengsteOrd}")
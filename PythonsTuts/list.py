frukt = ["eple", "banan", "appelsin"]
print(frukt)
gronnsak = ["gulrot", "brokkoli", "tomat"]
print(gronnsak)
handleliste = frukt + gronnsak

print(handleliste)

handleliste.append("salat")     # Append legger til et element
print(handleliste)

handleliste.pop()   # Fjerner siste element
print(handleliste)

print(handleliste[1]) # Printer Printer element nr 1

for handleliste
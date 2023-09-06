import random
# Oppgave 2

# 1, 2
heltallliste = [1, 63, 23, 54, 98]
heltallliste.sort()
print(f"{heltallliste}")

# 3
hundretall = random.sample(range(1, 200), 100)
print(hundretall)

# 4
hundretall = [i for i in hundretall if i <= 100]
print(hundretall)

# 5
nyliste = [i for i in hundretall if i % 3 != 0]
print(nyliste)

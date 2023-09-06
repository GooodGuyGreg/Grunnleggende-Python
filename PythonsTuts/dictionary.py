
# Mini database
kontakter = {
    "Alice": {
        "epost": "aliceexample.com",
        "tlf": "22222222",
        "adresse": "veien123"},
    "Bob": {
        "epost": "bobexample.com",
        "tlf": "123132123"
    }}

# Henter ut informasjon om gitt person
print(kontakter.get("Bob"))
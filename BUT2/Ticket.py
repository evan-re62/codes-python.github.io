class Ticket:
    compteur = 0
    def __init__(self):
        self.id = Ticket.compteur
        Ticket.compteur += 1
    def __repr__ (self):
        return f"Votre Ticket est le numéro {self.id}"

# --- Tests à valider ---
ticket1 = Ticket()
ticket2 = Ticket()
ticket3 = Ticket()

print(ticket1)
print(ticket2)
print(ticket3)

assert ticket1.id == 0
assert ticket2.id == 1
assert ticket3.id == 2
assert Ticket.compteur == 3, "Le compteur de classe devrait être à 3"

print("Tests de l'exercice 2 passés avec succès !")
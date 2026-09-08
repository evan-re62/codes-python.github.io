class Ticket:
    compteur = 0
    def __init__(self):
        self.id = Ticket.compteur
        Ticket.compteur += 1
    def __repr__ (self):
        return f"Votre Ticket est le numéro {self.id}"

t1 = Ticket()
t2 = Ticket()
t3 = Ticket()

print(t1)
print(t2)
print(t3)


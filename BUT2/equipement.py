class EquipementReseau:
    compteur_id = 0
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        self.id = EquipementReseau.compteur_id
        self.statut = "Inactif"
        EquipementReseau.compteur_id += 1
    def __repr__(self):
        return f"Equipement(id={self.id}, hostname={self.hostname}, ip={self.ip_address}, statut={self.statut})"
    def activer(self):
        self.statut = "Actif"
    def desactiver(self):
        self.statut = "Inactif"
    @property
    def est_actif(self):
        return self.statut == "Actif"






















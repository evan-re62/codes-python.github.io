from equipement import EquipementReseau
class GestionnaireParc:
    def __init__(self, mon_parc):
        self.mon_parc = mon_parc
        self.equipement = []

    def ajouter_equipements(self, equipement):
        if isinstance(equipement, EquipementReseau):
            self.equipement.append(equipement)
        else:
            raise ValueError(f"{equipement} n'est pas une instance")
    def liste_equipement(self):
        for equipement in self.equipement:
            print(equipement)
    def recherche_par_hostname(self, hostname):
        for equipement in self.equipement:
            if equipement.hostname == hostname:
                return equipement
        return False 
    def statistiques(self):
        nombre_equipement = 0
        equipement_actif = 0
        for equipement in self.equipement:
            nombre_equipement += 1
            if equipement.statut == "Actif":
                equipement_actif += 1
        print(f"Total : {nombre_equipement}, Actif : {equipement_actif}, Inactif : {nombre_equipement - equipement_actif}")
        return True
        
        

    







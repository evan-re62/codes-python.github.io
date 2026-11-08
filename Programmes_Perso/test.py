import random

class Roulette:
    def __init__(self, solde_initial=1000):
        self.solde = solde_initial
        self.rouges = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
        self.noirs = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
        self.rapports = {
            'plein': 35, 'cheval': 17, 'transversale': 11, 'carre': 8,
            'sixain': 5, 'colonne_douzaine': 2, 'chance_simple': 1
        }

    def determiner_type_mise(self, cible):
        """Vérifie le VRAI positionnement géométrique sur le tapis de roulette"""
        if isinstance(cible, str):
            return 'chance_simple'

        if isinstance(cible, list):
            cible.sort() # On trie les numéros du plus petit au plus grand
            l = len(cible)

            # PLEIN (1 numéro)
            if l == 1:
                if 0 <= cible[0] <= 36: 
                    return 'plein'

            # CHEVAL (2 numéros adjacents)
            elif l == 2:
                a, b = cible
                # Avec le zéro
                if a == 0 and b in [1, 2, 3]: return 'cheval'
                # Horizontalement (ex: 1-2, mais pas 3-4 car changement de ligne)
                if b == a + 1 and a % 3 != 0: return 'cheval'
                # Verticalement (ex: 1-4 ou 14-17)
                if b == a + 3: return 'cheval'

            # TRANSVERSALE (3 numéros sur la même ligne)
            elif l == 3:
                # Transversales avec le zéro
                if cible == [0, 1, 2] or cible == [0, 2, 3]: return 'transversale'
                # Transversales classiques (ex: 4-5-6)
                a, b, c = cible
                if a % 3 == 1 and b == a + 1 and c == a + 2: return 'transversale'

            # CARRÉ (4 numéros qui se touchent)
            elif l == 4:
                # Le carré spécial avec le zéro (Les quatre premiers)
                if cible == [0, 1, 2, 3]: return 'carre'
                # Carré classique (ex: 4-5-7-8)
                a, b, c, d = cible
                if a % 3 != 0 and b == a + 1 and c == a + 3 and d == a + 4: return 'carre'

            # SIXAIN (6 numéros, soit 2 lignes adjacentes)
            elif l == 6:
                a = cible[0]
                # Doit commencer en début de ligne (1, 4, 7...) et être une suite parfaite
                if a % 3 == 1 and cible == list(range(a, a + 6)): return 'sixain'

            # COLONNES ET DOUZAINES (12 numéros)
            elif l == 12:
                # Douzaines
                if cible == list(range(1, 13)) or cible == list(range(13, 25)) or cible == list(range(25, 37)):
                    return 'colonne_douzaine'
                # Colonnes
                col1 = list(range(1, 37, 3))
                col2 = list(range(2, 37, 3))
                col3 = list(range(3, 37, 3))
                if cible in [col1, col2, col3]:
                    return 'colonne_douzaine'

        return None # Si on arrive ici, c'est que la combinaison est physiquement impossible

    def verifier_victoire(self, cible, resultat):
        if resultat == 0:
            if isinstance(cible, list) and 0 in cible: return True
            return False
            
        if isinstance(cible, list): return resultat in cible
        elif isinstance(cible, str):
            cible = cible.lower()
            if cible == 'rouge': return resultat in self.rouges
            if cible == 'noir': return resultat in self.noirs
            if cible == 'pair': return resultat % 2 == 0
            if cible == 'impair': return resultat % 2 != 0
            if cible == 'manque': return 1 <= resultat <= 18
            if cible == 'passe': return 19 <= resultat <= 36
        return False

    def jouer(self, mises):
        cout_total = sum(montant for _, montant in mises)
        if cout_total > self.solde:
            print(f"❌ Solde insuffisant ! (Requis: {cout_total}€, Solde: {self.solde}€)")
            return

        self.solde -= cout_total
        resultat = random.randint(0, 36)
        
        couleur = "Rouge" if resultat in self.rouges else "Noir" if resultat in self.noirs else "Vert"
        print(f"\n{'='*40}")
        print(f"🎰 RIEN NE VA PLUS ! Le numéro est le {resultat} ({couleur})")
        print(f"{'='*40}")
        
        gains_tour = 0
        for cible, montant in mises:
            type_mise = self.determiner_type_mise(cible)
            nom_mise = cible if isinstance(cible, str) else f"la combinaison {cible}"
            
            if type_mise is None:
                print(f"⚠️ Combinaison IMPOSSIBLE sur le tapis. Mise remboursée : {cible}")
                self.solde += montant
                continue

            if self.verifier_victoire(cible, resultat):
                gain = montant + (montant * self.rapports[type_mise])
                gains_tour += gain
                print(f"✅ GAGNÉ sur {nom_mise} (+{montant * self.rapports[type_mise]}€ nets)")
            else:
                print(f"❌ PERDU sur {nom_mise} (-{montant}€)")
        
        self.solde += gains_tour
        print(f"\n💰 Nouveau solde : {self.solde}€\n")


# --- BOUCLE INTERACTIVE ---
if __name__ == "__main__":
    jeu = Roulette(solde_initial=500)
    print("=== BIENVENUE À LA ROULETTE ===")
    print("Ce tapis respecte les vraies règles de placement.")
    print(f"Votre solde de départ est de {jeu.solde}€\n")

    while jeu.solde > 0:
        print("Mises acceptées :")
        print("- Chance simple : rouge, noir, pair, impair, manque, passe")
        print("- Combinaisons valides du tapis séparées par un espace ou tiret (ex: '2 5', '4 5 7 8', '0 1 2 3')")
        print("- 'quitter' pour arrêter.")
        
        choix = input("\nVotre choix : ").strip().lower()
        
        if choix == 'quitter':
            print(f"Vous quittez la table avec {jeu.solde}€. À bientôt !")
            break

        montant_str = input("Montant de la mise (€) : ")
        try:
            montant = int(montant_str)
            if montant <= 0:
                print("⚠️ La mise doit être supérieure à 0.\n")
                continue
        except ValueError:
            print("⚠️ Veuillez entrer un montant valide (chiffre entier).\n")
            continue

        mots_valides = ['rouge', 'noir', 'pair', 'impair', 'manque', 'passe']
        if choix in mots_valides:
            cible = choix
        else:
            choix_propre = choix.replace('-', ' ').replace(',', ' ')
            try:
                cible = [int(x) for x in choix_propre.split()]
            except ValueError:
                print("⚠️ Saisie invalide. Vérifiez l'orthographe ou les numéros.\n")
                continue

        jeu.jouer([(cible, montant)])

    if jeu.solde <= 0:
        print("💸 Vous êtes ruiné ! Fin de la partie.")
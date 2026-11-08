import subprocess
import sys

def menu_principal():
    while True:
        print("\n" + "="*30)
        print("       CASINO MINI-JEUX       ")
        print("="*30)
        print("1. Jouer au Black Jack")
        print("2. Jouer à la Machine à sous")
        print("3. Quitter")
        print("="*30)
        
        choix = input("\nQue voulez-vous faire ? (1, 2 ou 3) : ")
        
        if choix == '1':
            print("\n>>> Démarrage du Black Jack...\n")
            # sys.executable correspond au chemin du Python actuellement utilisé
            subprocess.run([sys.executable, "BLACK_JACK.py"])
        elif choix == '2':
            print("\n>>> Démarrage de la Machine à sous...\n")
            subprocess.run([sys.executable, "MACHINE_SOUS.py"])
        elif choix == '3':
            print("\nFermeture de l'interface. À bientôt !")
            sys.exit()
        else:
            print("\nChoix invalide, veuillez taper 1, 2 ou 3.")

if __name__ == "__main__":
    menu_principal()
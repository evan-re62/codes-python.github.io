import random
from nicegui import ui

# Données du jeu
CARTES = [
    f"{valeur} de {couleur}"
    for couleur in ["Cœur", "Carreau", "Pique", "Trèfle"]
    for valeur in [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Valet",
        "Dame",
        "Roi",
        "As",
    ]
]

VALEURS_CARTES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Valet": 10,
    "Dame": 10,
    "Roi": 10,
    "As": 11,
}

# État global du jeu
argent = 500
mise_actuelle = 50
main_joueur = []
main_croupier = []
paquet = []
croupier_cache = True
partie_en_cours = False


def calculer_score(main):
  score = 0
  nombre_as = 0
  for carte in main:
    valeur_nom = carte.split(" ")[0]
    score += VALEURS_CARTES[valeur_nom]
    if valeur_nom == "As":
      nombre_as += 1
  while score > 21 and nombre_as > 0:
    score -= 10
    nombre_as -= 1
  return score


# Fonction pour générer le HTML/CSS d'une carte stylisée
def afficher_carte_html(carte_str, cachee=False):
  if cachee:
    return """
        <div style="width: 75px; height: 110px; background: #0f4c81; border: 2px solid #2980b9; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
            ♠♣
        </div>
        """

  parties = carte_str.split(" ")
  valeur = parties[0]
  couleur = parties[2]

  correspondance = {"Valet": "V", "Dame": "D", "Roi": "R", "As": "A"}
  v_courte = correspondance.get(valeur, valeur)
  symbole = {"Cœur": "♥", "Carreau": "♦", "Pique": "♠", "Trèfle": "♣"}[couleur]
  est_rouge = couleur in ["Cœur", "Carreau"]
  couleur_txt = "#c0392b" if est_rouge else "#151216"

  return f"""
    <div style="width: 75px; height: 110px; background: white; border: 2px solid #bdc3c7; border-radius: 8px; display: flex; flex-direction: column; justify-content: space-between; padding: 5px; color: {couleur_txt}; font-weight: bold; box-shadow: 0 4px 8px rgba(0,0,0,0.3); font-size: 13px;">
        <div>{v_courte}<br>{symbole}</div>
        <div style="align-self: center; font-size: 22px;">{symbole}</div>
        <div style="align-self: flex-end; transform: rotate(180deg);">{v_courte}<br>{symbole}</div>
    </div>
    """


# --- INTERFACE NICEGUI ---
ui.add_head_html("""
    <style>
        body { background-color: #160c06; }
    </style>
""")

with ui.column().classes("w-full items-center justify-center min-h-screen p-4"):
  ui.label("♠ BLACKJACK ROYAL CASINO ♣").classes(
      "text-2xl font-bold text-yellow-400 mb-4"
  )

  # Conteneur de la table de casino
  with ui.column().style(
      "background: radial-gradient(circle, #124a28 0%, #082412"
      " 100%); border: 10px solid #1a0e08; border-radius: 16px; width: 850px;"
      " padding: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.7);"
  ):

    # Zone Croupier
    with ui.column().style(
        "background: rgba(12, 52, 28, 0.9); border: 2px solid #18693c;"
        " border-radius: 10px; width: 100%; padding: 12px; min-height: 140px;"
    ):
      lbl_score_croupier = ui.label("Score Croupier : -").classes(
          "text-yellow-300 font-bold"
      )
      container_croupier = ui.row().classes("gap-2 items-center min-h-[110px]")
      ui.label("CROUPIER").classes(
          "text-xs text-gray-400 font-bold self-end -mt-4"
      )

    # Message de statut au centre
    lbl_statut = ui.label(
        "Sélectionnez votre mise et lancez la partie !"
    ).classes("text-lg font-bold text-white text-center my-3 w-full")

    # Zone Joueur
    with ui.column().style(
        "background: rgba(12, 52, 28, 0.9); border: 2px solid #18693c;"
        " border-radius: 10px; width: 100%; padding: 12px; min-height: 140px;"
    ):
      with ui.row().classes("w-full justify-between items-center"):
        lbl_score_joueur = ui.label("Votre Score : -").classes(
            "text-yellow-400 font-bold text-lg"
        )
        lbl_bank = ui.label("Bankroll : 500 € | Mise : 50 €").classes(
            "text-white font-bold"
        )
      container_joueur = ui.row().classes("gap-2 items-center min-h-[110px]")
      ui.label("JOUEUR").classes(
          "text-xs text-gray-400 font-bold self-end -mt-4"
      )

  # --- LOGIQUE DE MISE À JOUR DE L'UI ---
  def actualiser_affichage():
    container_croupier.clear()
    with container_croupier:
      for i, carte in enumerate(main_croupier):
        cache = i == 1 and croupier_cache
        ui.html(afficher_carte_html(carte, cachee=cache))

    container_joueur.clear()
    with container_joueur:
      for carte in main_joueur:
        ui.html(afficher_carte_html(carte))

    if len(main_croupier) > 0:
      if croupier_cache:
        v_vis = VALEURS_CARTES[main_croupier[0].split(" ")[0]]
        lbl_score_croupier.text = f"Score Croupier : {v_vis} + ?"
      else:
        lbl_score_croupier.text = (
            f"Score Croupier : {calculer_score(main_croupier)}"
        )

    if len(main_joueur) > 0:
      lbl_score_joueur.text = f"Votre Score : {calculer_score(main_joueur)}"

    lbl_bank.text = f"Bankroll : {argent} € | Mise : {mise_actuelle} €"

  # --- ACTIONS DE JEU ---
  def lancer_partie():
    global paquet, main_joueur, main_croupier, croupier_cache, argent, mise_actuelle, partie_en_cours
    if argent <= 0:
      lbl_statut.text = "Plus d'argent ! Rechargez la page."
      return
    if mise_actuelle > argent:
      mise_actuelle = argent

    argent -= mise_actuelle
    paquet = list(CARTES)
    random.shuffle(paquet)
    main_joueur = [paquet.pop(0), paquet.pop(0)]
    main_croupier = [paquet.pop(0), paquet.pop(0)]
    croupier_cache = True
    partie_en_cours = True

    btn_demarrer.disable()
    btn_tirer.enable()
    btn_rester.enable()
    btn_moins.disable()
    btn_plus.disable()

    lbl_statut.text = "À vous de jouer !"
    actualiser_affichage()

    # Vérification Blackjack naturel
    if calculer_score(main_joueur) == 21:
      croupier_cache = False
      actualiser_affichage()
      if calculer_score(main_croupier) == 21:
        lbl_statut.text = "🤝 Égalité Blackjack ! Mise remboursée."
        argent += mise_actuelle
      else:
        gain = int(mise_actuelle * 2.5)
        lbl_statut.text = f"🎉 BLACKJACK NATUREL ! +{gain} €"
        argent += gain
      fin_tour()

  def tirer():
    global partie_en_cours, croupier_cache
    if not partie_en_cours:
      return
    main_joueur.append(paquet.pop(0))
    actualiser_affichage()
    score_j = calculer_score(main_joueur)
    if score_j > 21:
      croupier_cache = False
      actualiser_affichage()
      lbl_statut.text = f"❌ Score de {score_j} : Vous avez dépassé 21 !"
      fin_tour()

  def rester():
    global partie_en_cours, croupier_cache, argent
    if not partie_en_cours:
      return
    partie_en_cours = False
    croupier_cache = False

    score_c = calculer_score(main_croupier)
    while score_c < 17:
      main_croupier.append(paquet.pop(0))
      score_c = calculer_score(main_croupier)

    actualiser_affichage()
    score_j = calculer_score(main_joueur)

    if score_c > 21 or score_j > score_c:
      gain = mise_actuelle * 2
      lbl_statut.text = f"🎉 Victoire ! Vous remportez {gain} €"
      argent += gain
    elif score_j == score_c:
      lbl_statut.text = "🤝 Égalité ! Mise remboursée."
      argent += mise_actuelle
    else:
      lbl_statut.text = f"😢 Défaite. Vous perdez {mise_actuelle} €"

    fin_tour()

  def fin_tour():
    global partie_en_cours
    partie_en_cours = False
    btn_tirer.disable()
    btn_rester.disable()
    btn_demarrer.enable()
    btn_moins.enable()
    btn_plus.enable()
    lbl_bank.text = f"Bankroll : {argent} € | Mise : {mise_actuelle} €"

  # --- BOUTONS DE CONTRÔLE ---
  with ui.row().classes("mt-4 gap-3 items-center"):
    btn_demarrer = ui.button(
        "Lancer une partie", on_click=lancer_partie
    ).classes("bg-green-600 font-bold")
    btn_tirer = (
        ui.button("Tirer (+1)", on_click=tirer)
        .classes("bg-blue-600 font-bold")
        .disable()
    )
    btn_rester = (
        ui.button("Rester", on_click=rester)
        .classes("bg-red-600 font-bold")
        .disable()
    )

    ui.separator().props("vertical").classes("h-8 mx-2")

    def modifier_mise(delta):
      global mise_actuelle
      mise_actuelle = max(10, min(argent, mise_actuelle + delta))
      lbl_bank.text = f"Bankroll : {argent} € | Mise : {mise_actuelle} €"

    btn_moins = ui.button("-10", on_click=lambda: modifier_mise(-10)).classes(
        "bg-gray-700"
    )
    btn_plus = ui.button("+10", on_click=lambda: modifier_mise(10)).classes(
        "bg-gray-700"
    )

ui.run(port=8080, title="Blackjack Royal Casino")
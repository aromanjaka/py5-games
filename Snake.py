import py5

# Variables du jeu
largeur_ecran = 400
hauteur_ecran = 400
taille_case = 20
serpent = [(5, 5)]  # Position initiale du serpent
nourriture = (10, 10)  # Position initiale de la nourriture
direction = (1, 0)  # Direction initiale (vers la droite)
jeu_termine = False

def setup():
    py5.size(largeur_ecran, hauteur_ecran)
    py5.frame_rate(10)  # Vitesse du jeu

def draw():
    global serpent, nourriture, direction, jeu_termine

    if jeu_termine:
        py5.background(255, 0, 0)  # Fond rouge en cas de Game Over
    else:
        py5.background(0)  # Fond noir en cours de jeu

    # Dessiner la nourriture (rouge)
    py5.fill(255, 0, 0)
    py5.rect(nourriture[0] * taille_case, nourriture[1] * taille_case, taille_case, taille_case)

    # Mettre à jour la position de la tête du serpent
    nouvelle_tete = (serpent[0][0] + direction[0], serpent[0][1] + direction[1])

    # Vérifier si le serpent mange la nourriture
    if nouvelle_tete == nourriture:
        serpent = [nouvelle_tete] + serpent
        nourriture = obtenir_nouvelle_nourriture()
    else:
        # Déplacer le serpent
        serpent = [nouvelle_tete] + serpent[:-1]

    # Dessiner le serpent (vert)
    py5.fill(0, 255, 0)
    for partie in serpent:
        py5.rect(partie[0] * taille_case, partie[1] * taille_case, taille_case, taille_case)

    # Vérifier les conditions de Game Over
    if serpent[0][0] < 0 or serpent[0][0] >= largeur_ecran / taille_case or serpent[0][1] < 0 or serpent[0][1] >= hauteur_ecran / taille_case:
        fin_jeu()

    if not jeu_termine and serpent[0] in serpent[1:]:
        fin_jeu()

    if jeu_termine:
        py5.fill(255)
        py5.text("Game Over", largeur_ecran // 2 - 50, hauteur_ecran // 2)
        py5.no_loop()

def key_pressed():
    global direction, jeu_termine

    if not jeu_termine:
        if py5.key == py5.UP and direction != (0, 1):
            direction = (0, -1)
        elif py5.key == py5.DOWN and direction != (0, -1):
            direction = (0, 1)
        elif py5.key == py5.LEFT and direction != (1, 0):
            direction = (-1, 0)
        elif py5.key == py5.RIGHT and direction != (-1, 0):
            direction = (1, 0)

def obtenir_nouvelle_nourriture():
    nouvelle_position = (py5.int(py5.random(largeur_ecran / taille_case)), py5.int(py5.random(hauteur_ecran / taille_case))

    while nouvelle_position in serpent:
        nouvelle_position = (py5.int(py5.random(largeur_ecran / taille_case)), py5.int(py5.random(hauteur_ecran / taille_case))

    return nouvelle_position

def fin_jeu():
    global jeu_termine
    jeu_termine = True

py5.run_sketch()

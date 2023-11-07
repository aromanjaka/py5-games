import py5

# Variables du jeu
largeur_ecran = 400
hauteur_ecran = 500
x_oiseau = 50
y_oiseau = hauteur_ecran // 2
taille_oiseau = 20
vitesse_chute_oiseau = 0
gravite = 0.5
force_saut = -10
largeur_tuyau = 50
espace_tuyau = 150
x_tuyau = largeur_ecran
vitesse_tuyau = 2
score = 0

def setup():
    py5.size(largeur_ecran, hauteur_ecran)
    py5.frame_rate(60)

def draw():
    global x_oiseau, y_oiseau, vitesse_chute_oiseau, x_tuyau, score

    # Dessiner l'arrière-plan (ciel)
    py5.background(135, 206, 235)  # Ciel bleu

    # Dessiner l'oiseau (un carré jaune)
    py5.fill(255, 255, 0)  # Jaune
    py5.rect(x_oiseau, y_oiseau, taille_oiseau, taille_oiseau)

    # Appliquer la gravité à l'oiseau
    vitesse_chute_oiseau += gravite
    y_oiseau += vitesse_chute_oiseau

    # Dessiner les tuyaux (verts)
    py5.fill(0, 128, 0)  # Vert foncé
    py5.rect(x_tuyau, 0, largeur_tuyau, hauteur_ecran - espace_tuyau)
    py5.rect(x_tuyau, hauteur_ecran - espace_tuyau, largeur_tuyau, hauteur_ecran)

    # Mettre à jour la position des tuyaux
    x_tuyau -= vitesse_tuyau

    # Vérifier si l'oiseau touche un tuyau
    if x_oiseau + taille_oiseau > x_tuyau and x_oiseau < x_tuyau + largeur_tuyau:
        if y_oiseau < hauteur_ecran - espace_tuyau or y_oiseau + taille_oiseau > hauteur_ecran:
            fin_jeu()

    # Vérifier si l'oiseau touche le sol
    if y_oiseau + taille_oiseau > hauteur_ecran:
        fin_jeu()

    # Vérifier si l'oiseau a passé le tuyau
    if x_oiseau > x_tuyau + largeur_tuyau:
        score += 1

    # Afficher le score
    py5.fill(255)  # Blanc
    py5.text("Score : " + str(score), 20, 20)

def fin_jeu():
    py5.text("Game Over", largeur_ecran // 2 - 50, hauteur_ecran // 2)
    py5.no_loop()

def key_pressed():
    global vitesse_chute_oiseau
    vitesse_chute_oiseau = force_saut

py5.run_sketch()

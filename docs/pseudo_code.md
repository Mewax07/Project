# Pseudo Code

```plaintext
FONCTION up()
DEBUT
    // Léve le stylo pour déplacer sans tracer
FIN

FONCTION down()
DEBUT
    // Baisse le stylo pour tracer lors des déplacements
FIN

FONCTION goto(x, y)
DEBUT
    // Déplace le curseur à la position (x, y)
FIN

FONCTION fillcolor(couleur)
DEBUT
    // Définit la couleur de remplissage
FIN

FONCTION pencolor(couleur)
DEBUT
    // Définit la couleur du trait
FIN

FONCTION begin_fill()
DEBUT
    // Commence a mémoriser les points pour remplir une forme
FIN

FONCTION end_fill()
DEBUT
    // Remplit la forme definie depuis begin_fill()
FIN

FONCTION longueur(tableau)
DEBUT
    // Retourne le nombre d'éléments dans le tableau
FIN

FONCTION aléatoire(min, max)
DEBUT
    // Retourne un nombre entier aléatoire entre min et max
FIN

FONCTION update()
DEBUT
    // Met a jour l'affichage à l'écran
FIN

// Fonction pour tracer une colline arrondie
FONCTION dessiner_colline(y_base, largeur, hauteur_max, nb_points, color)
DEBUT
    points[] est un tableau
    step ← largeur / (nb_points - 1)
    
    POUR i ALLANT DE 0 À (nb_points - 1)
        x ← -largeur / 2 + i * step
        y ← y_base + aléatoire(20, hauteur_max)
        points[i] ← (x, y)
    FINPOUR
    
    t ← draw_t
    
    t.up()
    t.goto(-largeur / 2, y_base)
    t.down()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()

    POUR i ALLANT DE 0 À (longueur(points) - 2)
        x1 ← points[i][0]
        y1 ← points[i][1]
        x2 ← points[i+1][0]
        y2 ← points[i+1][1]
        
        POUR k ALLANT DE 0 À 39
            u ← k / 40
            x ← x1 + (x2 - x1) * u
            y ← y1 + (y2 - y1) * u
            t.goto(x, y)
        FINPOUR
    FINPOUR

    t.goto(largeur / 2, y_base)
    t.goto(-largeur / 2, y_base)
    t.end_fill()
    t.up()
    
    screen.update()
FIN
```

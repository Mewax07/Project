# Pseudo Code

## Antoine

```plaintext
// Fonction pour tracer une colline arrondie
FONCTION dessiner_colline(y_base, largeur, hauteur_max, nb_points, color)
DEBUT
    // Générer des points de contrôle aléatoires
    points[] est un tableau
    step ← largeur / (nb_points - 1)
    
    POUR i ALLANT DE 0 À (nb_points - 1)
        x ← -largeur / 2 + i * step
        y ← y_base + aléatoire(20, hauteur_max)
        points[i] ← (x, y)
    FINPOUR
    
    t ← draw_t
    
    // Lever le crayon et se positionner
    t.up()
    t.goto(-largeur / 2, y_base)
    t.down()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    
    // Monter progressivement en courbe lissée
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
    
    // Descendre au sol
    t.goto(largeur / 2, y_base)
    t.goto(-largeur / 2, y_base)
    t.end_fill()
    t.up()
    
    screen.update()
FIN
```

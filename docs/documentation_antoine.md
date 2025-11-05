# Documentation du script

## Base & Constantes

### Importation des modules
```python
import turtle
import random
```

### Création d'un "screen" avec turtle
```python
screen = turtle.Screen()
screen.colormode(1.0)  # Indique que les couleurs vont de 0.0 à 1.0 (1 = 256)
```

### Passage en plein écran (hors Capytale)
```python
if screen.getcanvas():
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.attributes("-fullscreen", True)
```

### Création des tortues
```python
menu_t = turtle.Turtle()
draw_t = turtle.Turtle()
```
Ces deux tortues sont utilisées pour séparer le **menu** et le **dessin du décor**.

### Réglages de vitesse et affichage
```python
for tt in (menu_t, draw_t):
    tt.speed(0)
    tt.hideturtle()

screen.tracer(0)
```
Les tortues sont masquées et la vitesse est maximale.  
`screen.tracer(0)` désactive l'animation pour un rendu instantané.

### Taille de la fenêtre
```python
largeur = screen.window_height()
longueur = screen.window_width()
```

---

## Menu (Interface Graphique)

### Mouvement d’un point A à un point B
```python
def move_to(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()
```

### Variables du menu
```python
longueur_totale = 20
font_size = 18
line_spacing = 24
```
Ces variables définissent les espacements et la taille du texte du menu.

### Bordures et texte du menu
```python
espace_avant_apres = int((longueur_totale + 26) / 2)
espace_avant_apres_texte = int((longueur_totale - 10) / 2)

ligne_titre = "[]" + "=" * (espace_avant_apres - 3) + "[MENU]" + "=" * (espace_avant_apres - 3) + "[]"
```

### Variables globales
```python
status = ["J"]
menu_start_y = 100
user_input = ""
```

### Fonction `center_line`
```python
def center_line(text, width=36):
    text = text.strip()
    if len(text) > width:
        text = text[:width]
    return text.center(width, " ")
```

### Fonction `afficher_menu`
```python
def afficher_menu():
    global user_input
    menu_t.clear()
    menu_lines = [
        ligne_titre,
        "||" + " " * (espace_avant_apres * 2) + "||",
        "||" + " " * espace_avant_apres_texte + center_line("Pour change les paramêtres il") + " " * espace_avant_apres_texte + "||",
        "||" + " " * espace_avant_apres_texte + center_line("faut entrer la valeur dans ce") + " " * espace_avant_apres_texte + "||",
        "||" + " " * espace_avant_apres_texte + center_line("format : \"nombre:lettre\"") + " " * espace_avant_apres_texte + "||",
        "||" + " " * (espace_avant_apres * 2) + "||",
        "||" + " " * espace_avant_apres_texte + center_line(f"1. Ciel: [J]: Jour / [N]: Nuit ({status[0]})") + " " * espace_avant_apres_texte + "||",
        "||" + " " * (espace_avant_apres * 2) + "||",
        "[]" + "=" * (espace_avant_apres * 2) + "[]"
    ]

    for i, line in enumerate(menu_lines):
        y = menu_start_y - (i * line_spacing)
        move_to(menu_t, 0, y)
        menu_t.write(line, font=("Courier", font_size, "normal"), align="center")

    move_to(menu_t, 0, menu_start_y - ((len(menu_lines) + 1) * line_spacing))
    menu_t.write("> " + user_input, font=("Courier", font_size, "normal"), align="center")
    screen.update()
```

### Fonction `clear_menu`
```python
def clear_menu():
    menu_t.clear()
    screen.update()
```

### Ensemble des caractères autorisés
```python
ALLOWED = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:")
```

### Fonction `key_press`
Cette fonction gère la saisie clavier et les commandes du menu.

- `1:J` → Mode Jour  
- `1:N` → Mode Nuit  
- `CLEAR` → Réinitialise  
- `EXIT` → Ferme le programme  
- `START` → Lance le dessin

```python
def key_press(key):
    global user_input
    ...
```

### Liaison clavier
Toutes les touches sont liées à `key_press` :
```python
screen.listen()
screen.onkey(lambda: key_press("Return"), "Return")
screen.onkey(lambda: key_press("BackSpace"), "BackSpace")
screen.onkey(lambda: key_press("Colon"), "colon")
```

---

## Dessin du décor

### Fonction `interpolate_color`
Crée une transition entre deux couleurs hexadécimales.
```python
def interpolate_color(c1, c2, t):
    ...
```

### Fonction `draw_gradient`
Dessine un dégradé de ciel.
```python
def draw_gradient(c1, c2, steps=200):
    ...
```

### Fonction `dessiner_bloc`
Dessine un rectangle plein servant de sol.
```python
def dessiner_bloc(y_base, color):
    ...
```

### Fonction `dessiner_colline`
Génère et dessine une colline à base arrondie.
```python
def dessiner_colline(y_base, largeur, hauteur_max, nb_points=15, color="#158A13"):
    ...
```

---

## Étapes de génération du paysage

### Fonction `setup`
Prépare les couleurs selon le mode Jour/Nuit.
```python
def setup():
    ...
```

### Étape 1 : Ciel
```python
def etape_1():
    draw_gradient(ciel_1_color, ciel_2_color, steps=200)
    etape_2()
```

### Étape 2 : Montagne
```python
def etape_2():
    hauteur_max = random.randint(150, 250)
    dessiner_colline(-30, longueur, hauteur_max, 20, montagne_color)
    dessiner_bloc(-30, montagne_color)
    etape_3()
```

### Étape 3 : Colline
```python
def etape_3():
    y_base = -150
    hauteur_max = random.randint(50, 150)
    dessiner_colline(y_base, longueur, hauteur_max, 10, colline_color)
    dessiner_bloc(y_base, colline_color)
```

### Fin du programme
```python
turtle.done()
```
Maintient la fenêtre ouverte après le rendu.

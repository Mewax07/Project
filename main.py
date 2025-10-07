import turtle
import random

# Cette partie a été réalisée par Coletta Tymeo
screen = turtle.Screen()
screen.colormode(1.0)

if screen.getcanvas():
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.attributes("-fullscreen", True)

menu_t = turtle.Turtle()
draw_t = turtle.Turtle()

for tt in (menu_t, draw_t):
    tt.speed(0)
    tt.hideturtle()

screen.tracer(0)

largeur = screen.window_height()
longueur = screen.window_width()

# Cette partie a été réalisée par Thiebaut Antoine

def move_to(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()

longueur_totale = 20
font_size = 18
line_spacing = 24

espace_avant_apres = int((longueur_totale + 26) / 2)
espace_avant_apres_texte = int((longueur_totale - 10) / 2)

ligne_titre = "[]" + "=" * (espace_avant_apres - 3) + "[MENU]" + "=" * (espace_avant_apres - 3) + "[]"

# Liste des status par défaut du menu
status = ["J"]

menu_start_y = 100

user_input = ""

def center_line(text, width=36):
    """Centre le texte dans un espace de longueur fixe."""
    text = text.strip()
    if len(text) > width:
        text = text[:width]
    return text.center(width, " ")

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

def clear_menu():
    menu_t.clear()
    screen.update()

# ensemble des caractères autorisés
ALLOWED = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:")

def key_press(key):
    global user_input

    if len(key) == 1:
        key = key.upper() if key.isalpha() else key

    if key == "Return":
        cmd = user_input.strip().upper()
        if cmd == "1:J":
            print("Commande : Jour")
            status[0] = "J"
            user_input = ""
            afficher_menu()
        elif cmd == "1:N":
            print("Commande : Nuit")
            status[0] = "N"
            user_input = ""
            afficher_menu()
        elif cmd == "CLEAR":
            status["J"]
            afficher_menu()
        elif cmd == "EXIT":
            exit(0)
        elif cmd == "START":
            user_input = ""
            setup()
        return

    elif key == "BackSpace":
        user_input = user_input[:-1]
        afficher_menu()
        return

    elif key == "Colon":
        user_input = user_input + ":"
        afficher_menu()
        return

    elif len(key) == 1 and key in ALLOWED:
        user_input += key
        afficher_menu()
        return

    return

screen.listen()
screen.onkey(lambda: key_press("Return"), "Return")
screen.onkey(lambda: key_press("BackSpace"), "BackSpace")
screen.onkey(lambda: key_press("Colon"), "colon")

chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:"
for ch in chars:
    name1 = ch.lower()
    name2 = ch.upper()
    try:
        screen.onkey(lambda c=ch: key_press(c), name1)
    except Exception:
        pass
    try:
        screen.onkey(lambda c=ch: key_press(c), name2)
    except Exception:
        pass

afficher_menu()

def interpolate_color(c1, c2, t):
    c1 = (int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16))
    c2 = (int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16))
    r = int(c1[0] + (c2[0] - c1[0]) * t)
    g = int(c1[1] + (c2[1] - c1[1]) * t)
    b = int(c1[2] + (c2[2] - c1[2]) * t)
    return (r/255, g/255, b/255)

def draw_gradient(c1, c2, steps=200):
    screen.tracer(False)
    hauteur = largeur / steps
    t = draw_t
    t.up()
    for i in range(steps):
        color = interpolate_color(c1, c2, i/steps)
        t.fillcolor(color)
        t.pencolor(color)
        t.down()
        t.goto(-longueur / 2, -largeur / 2 + i * hauteur)
        t.begin_fill()
        for _ in range(2):
            t.forward(longueur)
            t.left(90)
            t.forward(hauteur)
            t.left(90)
        t.end_fill()
        t.up()
    screen.update()

# Fonction pour dessiner un bloc
def dessiner_bloc(y_base, color):
    t = draw_t
    t.up()
    t.goto(-longueur / 2, -largeur)
    t.down()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.goto(longueur / 2, -largeur / 2)
    t.goto(longueur / 2, y_base)
    t.goto(-longueur / 2, y_base)
    t.goto(-longueur / 2, -largeur / 2)
    t.end_fill()

    screen.update()

# Fonction pour tracer une colline arrondis
def dessiner_colline(y_base, largeur, hauteur_max, nb_points=15, color="#158A13"):
    # Générer des points de controle aléatoires
    points = []
    step = largeur / (nb_points - 1)
    for i in range(nb_points):
        x = -largeur / 2 + i * step
        y = y_base + random.randint(20, hauteur_max)
        points.append((x, y))

    t = draw_t

    t.up()
    t.goto(-largeur / 2, y_base)
    t.down()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()

    # Monter progressivement en courbe lissée
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        for k in range(40):
            u = k / 40
            x = x1 + (x2 - x1) * u
            y = y1 + (y2 - y1) * u
            t.goto(x, y)

    # Descendre au sol
    t.goto(largeur / 2, y_base)
    t.goto(-largeur / 2, y_base)
    t.end_fill()

    screen.update()

def setup():
    clear_menu()
    draw_t.clear()

    global ciel_1_color, ciel_2_color, montagne_color, colline_color, bloc_col_color

    if status[0] == "N":
        ciel_1_color, ciel_2_color = "#11151D", "#101A22"
        montagne_color = "#242527"
        colline_color = "#083407"
        bloc_col_color = "#0a1b0a"
    else:
        ciel_1_color, ciel_2_color = "#617AA9", "#6EB2E6"
        montagne_color = "#80838A"
        colline_color = "#158A13"
        bloc_col_color = "#1EAB19"

    etape_1()

def etape_1():
    draw_gradient(ciel_1_color, ciel_2_color, steps=200)
    etape_2()

# TODO: Étape: Montagne
def etape_2():
    hauteur_max = random.randint(150, 250)
    dessiner_colline(-30, longueur, hauteur_max, 20, montagne_color)
    dessiner_bloc(-30, montagne_color)
    etape_3()

# TODO: Étape: Colline
def etape_3():
    y_base = -150
    hauteur_max = random.randint(50, 150)
    dessiner_colline(y_base, longueur, hauteur_max, 10, colline_color)
    dessiner_bloc(y_base, colline_color)

turtle.done()
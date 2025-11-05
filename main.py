import turtle
import random
import math

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

# Cette partie a été réalisée par Thiebaut Antoine et Coletta Tyméo
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
status = ["J", "O"]

menu_start_y = 100

user_input = ""

# Centrer une ligne
def center_line(text, width=36):
    text = text.strip()
    if len(text) > width:
        text = text[:width]
    return text.center(width, " ")

# Afficher le menu
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
        "||" + " " * espace_avant_apres_texte + center_line(f"2. Musique: [O]: Oui / [N]: Non ({status[1]})") + " " * espace_avant_apres_texte + "||",
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

# Effacer le menu
def clear_menu():
    menu_t.clear()
    screen.update()

# ensemble des caractères autorisés
ALLOWED = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:")

# Touche du clavier presser
def key_press(key):
    global user_input

    if len(key) == 1:
        key = key.upper() if key.isalpha() else key

    if key == "Return":
        cmd = user_input.strip().upper()
        if cmd == "CLEAR":
            status[0] = "J"
            user_input = ""
            afficher_menu()

        elif cmd == "EXIT":
            exit(0)

        elif cmd == "START":
            user_input = ""
            setup()

        elif ":" in cmd:
            try:
                num, res = cmd.split(":", 1)
                num = int(num)
                res = res.strip().upper()

                if 1 <= num <= len(status) and len(res) == 1:
                    status[num - 1] = res
                    print(f"Commande : {cmd} -> status[{num - 1}] = '{res}'")
                    user_input = ""
                    afficher_menu()
                else:
                    print("Commande invalide.")
            except ValueError:
                print("Format de commande invalide. Utilisez le format number:result.")

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

# Ecouter les touches du clavier et executer les bonnes actions
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

# Code trouver en ligne pour calculer le dégarder entre 2 couleurs
def interpolate_color(c1, c2, t):
    c1 = (int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16))
    c2 = (int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16))
    r = int(c1[0] + (c2[0] - c1[0]) * t)
    g = int(c1[1] + (c2[1] - c1[1]) * t)
    b = int(c1[2] + (c2[2] - c1[2]) * t)
    return (r/255, g/255, b/255)

# Dessiner un dégrader
def dessiner_gradient(c1, c2, steps=200):
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
    t.up()

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
    t.up()

    screen.update()

# (Partie Tyméo)
# Dessin des rayons de soleil
def rayon(longueur, largeur):
    t = draw_t
    t.color("yellow")
    t.fillcolor("yellow")
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(longueur)
        t.right(90)
        t.forward(largeur)
        t.right(90)
    t.end_fill()
    t.up()

# Dessin des nuages
def nuage(longueur=10, angle=120):
    t = draw_t
    t.color("black")
    t.fillcolor("white")
    t.down()
    t.begin_fill()
    for _ in range(4):
        t.circle(longueur, angle)
        t.right(80)
    for _ in range(2):
        t.circle(longueur, angle)
        t.right(120)
    for _ in range(4):
        t.circle(longueur, angle)
        t.right(80)
    for _ in range(3):
        t.circle(longueur, angle)
        t.right(110)
    t.end_fill()
    t.up()

# Dessin des nenuphare
def nenuphar():
    t = draw_t
    t.color("black")
    t.fillcolor("green")
    t.down()
    t.begin_fill()
    t.circle(10, 300)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.end_fill()
    t.up()

# Dessin du soleil
def dessiner_soleil(positionY):
    t = draw_t
    t.up()
    t.goto(0, positionY)
    t.down()
    t.color("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    # Rayons
    for i in range(8):
        t.up()
        t.goto(0, positionY + 60)
        t.setheading(i * 45)
        t.forward(60)
        t.down()
        rayon(80, 10)
    t.up()

# Dessin de l'ensemble des nuages
def dessiner_nuages(nb):
    t = draw_t
    for _ in range(nb):
        x = random.randint(-int(longueur / 2), int(longueur / 2))
        y = random.randint(160, 220)
        t.up()
        t.goto(x, y)
        nuage()

# Dessin du lac
def dessiner_lac(cx=0, cy=-200, rx=160, ry=70, points=120):
    t = draw_t
    t.up()
    angle0 = 0
    x0 = cx + rx * math.cos(math.radians(angle0))
    y0 = cy + ry * math.sin(math.radians(angle0))
    t.goto(x0, y0)
    t.setheading(0)
    t.fillcolor("#4FB3FF")
    t.down()
    t.begin_fill()

    for i in range(1, points + 1):
        angle = (i / points) * 360.0
        vrx = rx + random.uniform(-8, 8)
        vry = ry + random.uniform(-4, 4)
        x = cx + vrx * math.cos(math.radians(angle))
        y = cy + vry * math.sin(math.radians(angle))
        t.goto(x, y)

    t.end_fill()
    t.up()
    screen.update()

# Dessin de l'ensemble des nenuphares
def dessiner_nenuphars(nb, cx=0, cy=-200, rx=140, ry=60):
    t = draw_t
    for _ in range(nb):
        theta = random.random() * 2 * math.pi
        u = random.random()
        r = math.sqrt(u)
        x = cx + r * rx * math.cos(theta)
        y = cy + r * ry * math.sin(theta)

        t.up()
        t.goto(x, y)
        t.setheading(0)
        nenuphar()

    screen.update()

# (Partie Antoine)
# Code qui configure les variables
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

# TODO: Étape: Dessiner le ciel
def etape_1():
    dessiner_gradient(ciel_1_color, ciel_2_color, steps=200)
    etape_2()

# TODO: Étape: Montagne
def etape_2():
    dessiner_soleil(200)
    dessiner_nuages(nb=random.randint(7, 9))
    etape_3()

# TODO: Étape: Colline
def etape_3():
    hauteur_max = random.randint(150, 250)
    dessiner_colline(-30, longueur, hauteur_max, 20, montagne_color)
    dessiner_bloc(-30, montagne_color)
    etape_4()

# TODO: Étape: Ciel (soleil + nuage)
def etape_4():
    y_base = -150
    hauteur_max = random.randint(50, 150)
    dessiner_colline(y_base, longueur, hauteur_max, 10, colline_color)
    dessiner_bloc(y_base, colline_color)
    etape_5()

# TODO: Étape: Nenupahre + Étant
def etape_5():
    dessiner_lac(cx=0, cy=-200, rx=160, ry=70, points=160)
    dessiner_nenuphars(nb=random.randint(5, 7), cx=0, cy=-200, rx=140, ry=60)

turtle.done()
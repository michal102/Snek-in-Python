import os
import msvcrt
import random
import time
import math


def load_maps():

    levels = []
    file = open("snake_maps.txt", "r")
    mapy = file.read().split("\n >\n")

    for i in mapy:
        levels += [i.split("\n")]

    for i in range(len(levels)):
        for j in range(len(levels[i])):
            levels[i][j] = levels[i][j].split(" ")

    file.close()

    return levels


def distance_to_apple(jablko_x, jablko_y, snek_x, snek_y):
    return abs(math.sqrt((jablko_x - snek_x)**2 + (jablko_y - snek_y)**2))


def draw(mapad):

    if current_main_lvl != 3:
        display = ("Poziom " + str(current_main_lvl) + " / 3 \nPunkty: " + str(punkty) + " / "
                   + str(wymagane_punkty[current_main_lvl-1]) + "\t \t  liczba żyć: " + str(hp) + "\n")
    else:
        display = ("Poziom " + str(current_main_lvl) + " / 3 \nPunkty: " + str(punkty) + " / "
                   + str(wymagane_punkty[current_main_lvl - 1]) + "\t  liczba żyć: " + str(hp) + "\n")
    # + str(snek) + "\n")

    for i in range(len(mapad)):
        for j in range(len(mapad[i])):
            # rysowanie węża
            skip = False
            for n in range(len(snek)):
                if j == snek[n][0] and i == snek[n][1] and n == 0:
                    display += "\033[0;32mo\033[0m "
                    skip = True
                    break
                elif j == snek[n][0] and i == snek[n][1]:
                    display += "\033[0;32m*\033[0m "
                    skip = True
                    break
            if skip:
                continue

            # rysowanie przeciwnika
            if bad_snek_active:
                skip2 = False
                for n in range(len(bad_snek)):
                    if j == bad_snek[n][0] and i == bad_snek[n][1] and n == 0:
                        display += "\033[7mo\033[0m "
                        skip2 = True
                        break
                    elif j == bad_snek[n][0] and i == bad_snek[n][1]:
                        display += "\033[7m*\033[0m "
                        skip2 = True
                        break
                if skip2:
                    continue

            if j == jablko_x and i == jablko_y:
                display += "\033[0;31mo\033[0m "
            elif j == heal_x and i == heal_y:
                display += "\033[1;33mo\033[0m "
            elif mapad[i][j] == '+':
                display += "\033[1;36m+\033[0m "
            else:
                display += (mapad[i][j] + " ")
        display += "\n"

    # os.system('cls')
    os.system("echo \033[0;0H")
    print(display, end="")
    time.sleep(czas + 0.01)


# stary sposób losowania - nie obejmował przypadku wylosowania jabłka na ciele węża + był bardzo wolny
"""

def wylosuj_jablko():

    ny = 0
    nx = 0

    if bad_snek_active:
        while (current_map[ny][nx] != '.' or abs(nx - snek[0][0]) < dead_zone or abs(ny - snek[0][1]) < dead_zone
               or abs(nx - bad_snek[0][0]) < dead_zone or abs(ny - bad_snek[0][1]) < dead_zone):
            nx = random.randint(0, len(current_map[0]) - 1)
            ny = random.randint(0, len(current_map) - 1)
    else:
        while current_map[ny][nx] != '.' or abs(nx - snek[0][0]) < dead_zone or abs(ny - snek[0][1]) < dead_zone:
            nx = random.randint(0, len(current_map[0]) - 1)
            ny = random.randint(0, len(current_map) - 1)

    return nx, ny
    
"""


def wylosuj_pozycje():
    free_space = []

    # wypełnianie wolnego miejsca
    for i in range(len(current_map[0])):
        for j in range(len(current_map)):
            free_space += [[i, j]]

    # usuwanie pól gdzie jabłko nie może się wylosować
    for i in range(len(current_map[0])):
        for j in range(len(current_map)):

            if bad_snek_active:

                if abs(i - bad_snek[0][0]) < dead_zone or abs(j - bad_snek[0][1]) < dead_zone:
                    if [i, j] in free_space:
                        free_space.remove([i, j])

                for n in range(1, len(bad_snek)):
                    if i == bad_snek[n][0] and j == bad_snek[n][1]:
                        if [i, j] in free_space:
                            free_space.remove([i, j])

            if current_map[j][i] != '.' or abs(i - snek[0][0]) < dead_zone or abs(j - snek[0][1]) < dead_zone:
                if [i, j] in free_space:
                    free_space.remove([i, j])

            if len(snek) > 5:
                for n in range(1, len(snek)):
                    if i == snek[n][0] and j == snek[n][1]:
                        if [i, j] in free_space:
                            free_space.remove([i, j])

            if i == jablko_x and j == jablko_y:
                if [i, j] in free_space:
                    free_space.remove([i, j])

            if i == heal_x and j == heal_y:
                if [i, j] in free_space:
                    free_space.remove([i, j])

    pozycja = random.choice(free_space)

    return pozycja[0], pozycja[1]


# stara obsługa map - przed implementacją wczytywania map z pliku
"""

mapa = [
    "# # # # # # . . . . . . . . . # # # # #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    ". . . . . . . . + + + + + . . . . . . .".split(),
    ". . . . . . . . + + + + + . . . . . . .".split(),
    ". . . . . . . . + + + + + . . . . . . .".split(),
    ". . . . . . . . + + + + + . . . . . . .".split(),
    ". . . . . . . . . . . . . . . . . . . .".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# # # # # # . . . . . . . . . # # # # #".split(),
]

mapa1 = [
    "# # # # # # . . . . . . . . . # # # # #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    ". . . . . . . . + + + + + . . . . . . .".split(),
    ". . . . . . . . + + + + + . . . . . . .".split(),
    ". . . . . . . . + + + + + . . . . . . .".split(),
    ". . . . . . . . + + + + + . . . . . . .".split(),
    ". . . . . . . . . . . . . . . . . . . .".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# . . . . . . . . . . . . . . . . . . #".split(),
    "# # # # # # . . . . . . . . . # # # # #".split(),
]

mapa2 = [
    "# # # # # # # . . . . . . # # # # # # #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    ". . # . . . . . . . . . . . . . . # . .".split(),
    ". . # . . . . . . . . . . . . . . # . .".split(),
    ". . # . . . . . . . . . . . . . . # . .".split(),
    ". . # . . . . . . . . . . . . . . # . .".split(),
    ". . # . . . . # # # # # # . . . . . . .".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# # # # # # # . . . . . . # # # # # # #".split(),
]

mapa3 = [
    "# # # # # # # . . . . . . # # # # # # #".split(),
    "# + + + + . . . . . . . . . . # # # # #".split(),
    "# + + + + . . . . . . . . . . # # # # #".split(),
    "# + + + + . . . . . . . . . . # # # # #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    ". . # . . . . . . . . . . . . . . # . .".split(),
    ". . # . . . . . . . . . . . . . . # . .".split(),
    ". . # . . . . . . . . . . . . . . # . .".split(),
    ". . # . . . . . . . . . . . . . . # . .".split(),
    ". . # . . . . # # # # # # . . . . . . .".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# . . . . . . # # # # # # . . . . . . #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# # # # # . . . . . . . . . . # # # # #".split(),
    "# # # # # # # . . . . . . # # # # # # #".split(),
]

"""

poziomy = load_maps()
# poziomy = []
# poziomy += [mapa] + [mapa1] + [mapa2] + [mapa3]

current_lvl = 0
current_main_lvl = 1
current_map = poziomy[current_lvl]
one_time_event = True

won = False

punkty = 0
wymagane_punkty = [20, 50, 100]
req = 0
winning_condition = 100
hp = 3
max_hp = 3
wylosowano = False
lvl_changed = True
dead_zone = 5
gracz_x, gracz_y = 1, 1
kierunek_x, kierunek_y = 0, 0
czas = 0.1

snek = [[gracz_x, gracz_y, kierunek_x, kierunek_y]]

bad_snek = [[len(current_map[0])-7, len(current_map)-2, -1, 0], [len(current_map[0])-6, len(current_map)-2, -1, 0],
            [len(current_map[0])-5, len(current_map)-2, -1, 0], [len(current_map[0])-4, len(current_map)-2, -1, 0],
            [len(current_map[0])-3, len(current_map)-2, -1, 0], [len(current_map[0])-2, len(current_map)-2, -1, 0]]
bad_snek_active = False
bad_snek_ded = False
bad_snek_delay = 3
current_delay = 1

heal_x, heal_y = len(current_map), len(current_map)
jablko_x, jablko_y = 0, 0
jablko_x, jablko_y = wylosuj_pozycje()


gra_trwa = True

while gra_trwa:

    # aktywacja przeciwnika
    if current_lvl == 4 and not bad_snek_ded:
        bad_snek_active = True
    else:
        bad_snek_active = False

    # sterowanie
    if msvcrt.kbhit():
        klawisz = msvcrt.getwch()

        if klawisz == 'w' and (snek[0][2] != 0 or snek[0][3] != 1):
            snek[0][2] = 0
            snek[0][3] = -1

        if klawisz == 's' and (snek[0][2] != 0 or snek[0][3] != -1):
            snek[0][2] = 0
            snek[0][3] = 1

        if klawisz == 'a' and (snek[0][2] != 1 or snek[0][3] != 0):
            snek[0][2] = -1
            snek[0][3] = 0

        if klawisz == 'd' and (snek[0][2] != -1 or snek[0][3] != 0):
            snek[0][2] = 1
            snek[0][3] = 0

    if bad_snek_active:
        # sterowanie przeciwnikiem
        distances = []
        # obliczanie odległości
        distance_up = distance_to_apple(jablko_x, jablko_y, bad_snek[0][0], bad_snek[0][1]-1)
        distance_left = distance_to_apple(jablko_x, jablko_y, bad_snek[0][0]-1, bad_snek[0][1])
        distance_right = distance_to_apple(jablko_x, jablko_y, bad_snek[0][0]+1, bad_snek[0][1])
        distance_down = distance_to_apple(jablko_x, jablko_y, bad_snek[0][0], bad_snek[0][1]+1)

        distances += [distance_up]
        distances += [distance_down]
        distances += [distance_left]
        distances += [distance_right]

        # sprawdzanie czy przeciwnik w siebie nie wpadnie
        for i in range(len(bad_snek)):
            if bad_snek[0][0] == bad_snek[i][0] and bad_snek[0][1]-1 == bad_snek[i][1]:
                distances[0] = 100
            if bad_snek[0][0] == bad_snek[i][0] and bad_snek[0][1]+1 == bad_snek[i][1]:
                distances[1] = 100
            if bad_snek[0][0]-1 == bad_snek[i][0] and bad_snek[0][1] == bad_snek[i][1]:
                distances[2] = 100
            if bad_snek[0][0]+1 == bad_snek[i][0] and bad_snek[0][1] == bad_snek[i][1]:
                distances[3] = 100

        # sprawdzanie czy przeciwnik nie wpadnie w ogon gracza
        for i in range(len(snek)):
            if bad_snek[0][0] == snek[i][0] and bad_snek[0][1]-1 == snek[i][1]:
                distances[0] = 100
            if bad_snek[0][0] == snek[i][0] and bad_snek[0][1]+1 == snek[i][1]:
                distances[1] = 100
            if bad_snek[0][0]-1 == snek[i][0] and bad_snek[0][1] == snek[i][1]:
                distances[2] = 100
            if bad_snek[0][0]+1 == snek[i][0] and bad_snek[0][1] == snek[i][1]:
                distances[3] = 100

        # sprawdzanie czy przeciwnik nie wpadnie w ścianę
        if bad_snek[0][1]-1 >= 0:
            if current_map[bad_snek[0][1]-1][bad_snek[0][0]] == '#':
                distances[0] = 100
        if bad_snek[0][1]+1 <= len(current_map)-1:
            if current_map[bad_snek[0][1]+1][bad_snek[0][0]] == '#':
                distances[1] = 100
        if bad_snek[0][0] - 1 >= 0:
            if current_map[bad_snek[0][1]][bad_snek[0][0]-1] == '#':
                distances[2] = 100
        if bad_snek[0][0] + 1 <= len(current_map[0])-1:
            if current_map[bad_snek[0][1]][bad_snek[0][0]+1] == '#':
                distances[3] = 100

        # znajdowanie najmniejszej odległości
        min_distance = min(distances)

        ktory_kierunek = 0
        # wybieranie kierunku na podstawie odległości (pierwszej najmniejszej)
        for i in range(len(distances)):
            if distances[i] == min_distance:
                ktory_kierunek = i

        if ktory_kierunek == 0:
            bad_snek[0][2] = 0
            bad_snek[0][3] = -1
        elif ktory_kierunek == 1:
            bad_snek[0][2] = 0
            bad_snek[0][3] = 1
        elif ktory_kierunek == 2:
            bad_snek[0][2] = -1
            bad_snek[0][3] = 0
        elif ktory_kierunek == 3:
            bad_snek[0][2] = 1
            bad_snek[0][3] = 0

        # poruszanie przeciwnikiem
        if current_delay >= bad_snek_delay:
            for i in range(len(bad_snek)):
                bad_snek[i][0] += bad_snek[i][2]
                bad_snek[i][1] += bad_snek[i][3]

        # aktualizowanie kierunku ruchu ciała przeciwnika
        if current_delay >= bad_snek_delay:
            if len(bad_snek) > 1:
                for i in reversed(range(1, len(bad_snek))):
                    bad_snek[i][2] = bad_snek[i-1][2]
                    bad_snek[i][3] = bad_snek[i-1][3]

            current_delay = 1

    # poruszanie wężem
    for i in range(len(snek)):
        snek[i][0] += snek[i][2]
        snek[i][1] += snek[i][3]

    # aktualizowanie kierunku ruchu ciała
    if len(snek) > 1:
        for i in reversed(range(1, len(snek))):
            snek[i][2] = snek[i-1][2]
            snek[i][3] = snek[i-1][3]

    # warunki na przechodzenie przez koniec mapy
    for i in range(len(snek)):
        if snek[i][0] == len(current_map[0]):
            snek[i][0] = 0
        elif snek[i][0] == -1:
            snek[i][0] = len(current_map[0])-1

        if snek[i][1] == len(current_map):
            snek[i][1] = 0
        elif snek[i][1] == -1:
            snek[i][1] = len(current_map)-1

    # zderzenie z włąsnym ogonem
    if len(snek) > 2:
        for i in range(2, len(snek)):
            if snek[0][0] == snek[i][0] and snek[0][1] == snek[i][1]:
                hp -= 1

    # zebranie jabłka/ zderzenie ze ścianą/ przejście do nowej mapy/ zebranie złotego jabłka
    if snek[0][0] == jablko_x and snek[0][1] == jablko_y:
        punkty += 10
        czas = czas / 1.05
        snek += [[snek[len(snek)-1][0], snek[len(snek)-1][1], 0, 0]]
        
        # losowanie złotego jabłka
        if hp < max_hp and not wylosowano and lvl_changed:
            heal_x, heal_y = wylosuj_pozycje()
            wylosowano = True

        # warunek wygrania/ zmiana mapy/ losowanie jabłka
        if punkty >= winning_condition:
            won = True
            gra_trwa = False
        elif (req < len(wymagane_punkty) and punkty == wymagane_punkty[req] and one_time_event
              and current_lvl < len(poziomy)-1):
            # gra_trwa = False
            current_lvl += 1
            current_map = poziomy[current_lvl]
            jablko_x, jablko_y = len(current_map[0]), len(current_map)
            req += 1
        else:
            jablko_x, jablko_y = wylosuj_pozycje()
    elif current_map[snek[0][1]][snek[0][0]] == '#':
        hp -= 1
        # gra_trwa = False
    elif current_map[snek[0][1]][snek[0][0]] == '+':
        if len(poziomy) - 1 == current_lvl:
            won = True
            gra_trwa = False
        else:
            current_lvl += 1
            current_main_lvl += 1
            current_map = poziomy[current_lvl]
            jablko_x, jablko_y = wylosuj_pozycje()
            one_time_event = True
            lvl_changed = True
    elif snek[0][0] == heal_x and snek[0][1] == heal_y:
        hp += 1
        heal_x = len(current_map)
        heal_y = len(current_map)
        wylosowano = False
        lvl_changed = False

    # zderzenie gracza z przeciwnikiem
    if bad_snek_active:
        for i in range(len(bad_snek)):
            if snek[0][0] == bad_snek[i][0] and snek[0][1] == bad_snek[i][1]:
                hp -= 1

    # zderzenie przeciwnika z graczem albo ze sobą
    if bad_snek_active:
        for i in range(len(snek)):
            if bad_snek[0][0] == snek[i][0] and bad_snek[0][1] == snek[i][1]:
                bad_snek_ded = True
        for i in range(2, len(bad_snek)):
            if bad_snek[0][0] == bad_snek[i][0] and bad_snek[0][1] == bad_snek[i][1]:
                bad_snek_ded = True

    # zebranie jablka przez przeciwnika
    if bad_snek_active:
        if bad_snek[0][0] == jablko_x and bad_snek[0][1] == jablko_y:
            if bad_snek_delay > 1:
                bad_snek_delay -= 1
            bad_snek += [[bad_snek[len(bad_snek) - 1][0], bad_snek[len(bad_snek) - 1][1], 0, 0]]
            jablko_x, jablko_y = wylosuj_pozycje()

    if hp <= 0:
        gra_trwa = False

    draw(current_map)
    if bad_snek_active:
        current_delay += 1

if won:
    print("\033[1;33m!!! WYGRANA !!!\033[0m")
else:
    print("\033[0;31mGAME OVER\033[0m")
os.system("pause")

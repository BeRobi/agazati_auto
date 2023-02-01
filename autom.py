from Auto import Auto

autok = []


def beolvas():
    file = open("auto.txt", "r", encoding="UTF-8")
    file.readline()
    kocsi = file.readlines()
    file.close()
    i = 0
    while i < len(kocsi):
        sor = kocsi[i].strip().split("$")
        autok.append(Auto(sor))
        i += 1


def flotta():
    return len(autok)


def legfiatalabb():
    i = 0
    fiatalabb = 0
    while i < len(autok):
        if autok[fiatalabb].datum < autok[i].datum:
            fiatalabb = i
        i += 1
    return f"{autok[fiatalabb].tipus}({autok[fiatalabb].datum})"


def legoregebb():
    i = 0
    oregebb = 0
    while i < len(autok):
        if autok[oregebb].datum > autok[i].datum:
            oregebb = i
        i += 1
    return f"{autok[oregebb].tipus}({autok[oregebb].datum})"

import random


def vel_szamok():
    lista = []
    i = 0
    while i < 5:
        lista.append(int(random.random()*90)+1)
        i += 1
    szamok_lista(lista)
    konzol_kiir(lista)


def szamok_lista(lista):
    i = 0
    szamok = ""
    while i < len(lista):
        if i == len(lista)-1:
            szamok += str(lista[i])
        else:
            szamok += str(lista[i])+"; "
        i += 1
    print(f"\nII/A, B, C:\n\t{szamok}")


def konzol_kiir(lista):
    print(f"\nII/D, E:\n\tAz egyjegyűek száma: {egyjegyuek_szama(lista)}.")
    file_kiir(egyjegyuek_szama(lista))


def egyjegyuek_szama(lista):
    i = 0
    db = 0
    while i < len(lista):
        if lista[i] < 10:
            db += 1
        i += 1
    return db


def file_kiir(db):
    f = open("szamok.txt", "w", encoding="UTF-8")
    f.write(f"II/F:\n\tA fejek száma: {db}.")
    f.close()

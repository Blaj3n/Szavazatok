'''
A list comprehension Pythonban egy rövid és hatékony módja a listák létrehozásának, amely lehetővé teszi,
hogy egy új listát készíts egy meglévő lista elemeiből, bizonyos feltételek alapján. A szintaxisa a
következő:
new_list = [kifejezés for elem in iterable if feltétel]

A list comprehension lényegében egy olyan módja a listák létrehozásának, ahol egy lépésben lehetőségünk
van elemeket átalakítani és szűrni.


Mikor érdemes használni?
    Ha egyszerűbbé akarod tenni a kódot, és csökkenteni szeretnéd a sorok számát.
    Ha a lista generálásához szükséges feltételeket egyszerűen meg tudod adni.

'''

# kód újraformázása: Ctrl + Alt + Shift + L
# Példák:

print("1. Kockák számítása: Itt az 1-től 5-ig terjedő számok négyzetét számoljuk ki: ")
szamok = [1, 2, 3, 4, 5]  # Eredeti lista
kockak = [x**2 for x in szamok]  # Új lista, ahol minden szám négyzetre van emelve
print(kockak)  # Eredmény: [1, 4, 9, 16, 25]

print("")

print("2. Szűrés: Itt csak a páros számokat szűrjük ki az 1-től 10-ig terjedő számokból: ")
szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

paros_szamok = [x for x in szamok if x % 2 == 0]  # Csak a páros számokat választjuk ki
print(paros_szamok)  # Eredmény: [2, 4, 6, 8, 10]

print("")

print("3. Karakterek kiválasztása: A következő példa egy szóban lévő kisbetűs karaktereket gyűjt össze: ")
szo = "Hello"
kisbetusok = [char for char in szo if char.islower()]  # Csak a kisbetűket választjuk ki
print(kisbetusok)  # Eredmény: ['e', 'l', 'l', 'o']

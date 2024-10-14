# print("1. feladat")
szavazatok = []

with open("szavazatok.txt", "r", encoding="utf-8") as file:
    for szavazat in file:
        szavazat = szavazat.strip().split()
        szavazatok.append([int(szavazat[0]), int(szavazat[1]), str(szavazat[2]), str(szavazat[3]), str(szavazat[4])])
print(szavazatok)

print("\n2. feladat:")

print(f"A helyhatósági választáson {len(szavazatok)} képviselőjelölt indult.")

print("\n3. feladat:")
v_nev = "Hold"  # input("Kérek egy vezetéknevet: ")
k_nev = "Ferenc"  # input("Kérek egy keresztnevet: ")

van = False  # nincs ilyen
for szavazat in szavazatok:
    if v_nev == szavazat[2] and k_nev == szavazat[3]:
        print(f"{v_nev} {k_nev} {szavazat[1]} szavazatot kapott.")
        van = True  # van ilyen

if not van:  # nincs ilyen, TEHÁT a van == False
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
# if van: # van == True
#     print("van ilyen")

print("")
# HF 4. FELADAT ÉS 3. FELADATOT MEGFORMÁLNI round()

print("4. feladat:")

szavazasra_jog = 12345

osszes_szavazat = 0
for szavazat in szavazatok:
    osszes_szavazat += szavazat[1]
arany = (osszes_szavazat / szavazasra_jog) * 100
print(f"A választáson {osszes_szavazat} állampolgár, a jogosultak {round(arany, 2)}%-a vett részt.")

print("")

print("5. feladat: ")
fuggetlen_szamlalo = 0
GYEP_szamlalo = 0
ZEP_szamlalo = 0
HEP_szamlalo = 0
TISZ_szamlalo = 0
for szavazat in szavazatok:
    if szavazat[4] == "GYEP":
        GYEP_szamlalo += szavazat[1]
    elif szavazat[4] == "HEP":
        HEP_szamlalo += szavazat[1]
    elif szavazat[4] == "TISZ":
        TISZ_szamlalo += szavazat[1]
    elif szavazat[4] == "ZEP":
        ZEP_szamlalo += szavazat[1]
    else:
        fuggetlen_szamlalo += szavazat[1]
print(f"Gyümölcsevők Pártja = {round(szavazasra_jog / GYEP_szamlalo, 2)}%")
print(f"Húsevők Pártja = {round(szavazasra_jog / HEP_szamlalo, 2)}%")
print(f"Tejivók Szövetsége = {round(szavazasra_jog / TISZ_szamlalo, 2)}%")
print(f"Zöldségevők Pártja= {round(szavazasra_jog / ZEP_szamlalo, 2)}%")
print(f"Független jelöltek = {round(szavazasra_jog / fuggetlen_szamlalo, 2)}%")

print("")

print("6. feladat: ")
legtobb_szavazat = max(szavazat[1] for szavazat in szavazatok)
legnagyobb_jeloltek = [szavazat for szavazat in szavazatok if szavazat[1] == legtobb_szavazat]

for jelolt in legnagyobb_jeloltek:
    if jelolt[4] != "-":
        print(f"A jelölt neve: {jelolt[2]} {jelolt[3]}, Szavazatok száma: {jelolt[1]}, Párt: {jelolt[4]}")
    else:
        print(f"A jelölt neve: {jelolt[2]} {jelolt[3]}, Szavazatok száma: {jelolt[1]}, Párt: Független")

print("")

# print("7. feladat:")
korzetek = []
for szavazat in szavazatok:
    if szavazat[0] not in korzetek:
        korzetek.append(szavazat[0])
# print(sorted(korzetek))

with open("kepviselok.txt", "w", encoding="utf-8") as fajl:

    for korzet in sorted(korzetek): # korzet == 1
        legnagyobb_szavazat = 0
        legn_szav_lista = []
        for szavazat in szavazatok:
            if korzet == szavazat[0] and legnagyobb_szavazat < szavazat[1]:
                legn_szav_lista = []
                legnagyobb_szavazat = szavazat[1]
                legn_szav_lista.append(szavazat)
        if legn_szav_lista[0][4] != "-":
            fajl.write(f"{legn_szav_lista[0][0]} {legn_szav_lista[0][2]} {legn_szav_lista[0][3]} {legn_szav_lista[0][4]}\n")
        else:
            fajl.write(f"{legn_szav_lista[0][0]} {legn_szav_lista[0][2]} {legn_szav_lista[0][3]} független\n")


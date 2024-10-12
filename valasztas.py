#print("1. feladat")
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
        van = True # van ilyen

if not van: # nincs ilyen, TEHÁT a van == False
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


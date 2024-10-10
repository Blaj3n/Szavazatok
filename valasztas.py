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
v_nev = input("Kérek egy vezetéknevet: ")
k_nev = input("Kérek egy keresztnevet: ")

van = False # nincs ilyen
for szavazat in szavazatok:
    if v_nev == szavazat[2] and k_nev == szavazat[3]:
        print(szavazat[1])
        van = True # van ilyen

if not van: # nincs ilyen, TEHÁT a van == False
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
# if van: # van == True
#     print("van ilyen")



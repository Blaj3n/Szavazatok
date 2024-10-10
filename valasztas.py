#print("1. feladat")
szavazatok = []


with open("szavazatok.txt", "r", encoding="utf-8") as file:
    for szavazat in file:
        szavazat = szavazat.strip().split()
        szavazatok.append([int(szavazat[0]), int(szavazat[1]), str(szavazat[2]), str(szavazat[3]), str(szavazat[4])])
print(szavazatok)



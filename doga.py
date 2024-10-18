"""
mennyi = int(input("Hány állatot szeretnél hozzáadni? "))
allatok = []
szam = 1
for a in range(mennyi):
    allat = input(f"Add meg az {szam}. állat nevét: ")
    szam += 1
    pont = int(input(f"Add meg {allat} pontszámát: "))
    allatok.append((allat, pont))
    
megjel = input("Szeretnéd látni az összes állatot? (igen/nem): ")
if megjel == "igen":
    print(*allatok)
 
atlag = input("Szeretnéd tudni az átlagos pontszámot? (igen/nem): ")
ossz = 0
for i in allatok:
    ossz += i[1]
if atlag == "igen":
    print(f"Az átlagos pontszám: {ossz / mennyi}")

nagykicsi = input("Szeretnéd tudni a legmagasabb és a legalacsonyabb pontszámot? ")
nagy = 0
kicsi = 999999999999999999999999999999999999999990
for allat, pont in allatok:
    if pont > nagy:
        nagy = pont
    if pont < kicsi:
        kicsi = pont
print(f"Legmagasabb pontszám: {nagy}\nLegalacsonyabb pontszám: {kicsi}")
        
elt = input("Szeretnél eltávolítani egy állatot? (igen/nem): ")
kit = input("Add meg az állat nevét, akit el szeretnél távolítani: ")
if elt == "igen":
    for allat in allatok:
        if allat[0] == kit:
            allatok.remove(allat)
            
osz = input("Szeretnéd látni az összes állatot? (igen/nem): ")
if osz == "igen":
    print(allatok)
"""
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
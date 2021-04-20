file = open("input_adventofcode3.txt", "r")

sez = []
for line in file:
    sez.append(list(line.strip()))


nakloni = [(1,1), (3,1), (5,1), (7,1), (1,2)]

r = 0
d = 0
odgovor = 1

for (a,b) in nakloni:
    r=0
    d=0
    rezultat=0

    while r < len (sez):
        d += a
        r += b

        if r < len(sez) and sez[r][d%len(sez[r])] == "#":
            rezultat += 1

    odgovor *= rezultat
    
    if a==3 and b==1:
        print(rezultat)

print(odgovor)


def bencin(x):
   y=x // 3 - 2
   return y


datoteka_in=open("vhod_01.txt", "r")
vsebina=datoteka_in.read()
vsebina1=vsebina.split()
y=0


for i in vsebina1:
    

    y=bencin(int(i))

print(s(i))



"""p=0
while vsota>0:
    p=p+ int(i) // 3 -2


"""


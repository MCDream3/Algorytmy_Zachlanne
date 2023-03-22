#PSEUDOKOD

#T -> [50,20,10,5,2,1]
#x -> wpisz

  #dla i w zakresie T
    #ilosc -> x//i
    #jeżeli ilosc > 0
      #x -> x-ilosc * T[i]
#wypisz i oraz ilosc


#ZWYKŁY KOD sposób 1

x = int(input())
T = [50,20,10,5,2,1]

for i in T:
  ilosc = x//i
  if ilosc > i:
    x = x - ilosc
    * i
    print(f"Nominał {i} ilosc {ilosc}")

#ZWYKŁY KOD sposób 2

x = int(input())
T = [50,20,10,5,2,1]
W = []

for i in T:
  ilosc = x//i
  if ilosc > i:
    x = x - ilosc * i
    W = W + ilosc*[i]
print(W)

#ZWYKŁY KOD sposób 3

x = int(input())
T = [50,20,10,5,2,1]
W = []

for i in T:
  ilosc = x//i
  if ilosc > i:
    x = x - ilosc * i
    for j in range(ilosc):
      W.append(i)

print(W)

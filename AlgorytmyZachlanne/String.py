#napis string to jakby lista, więc diała foreach i for z range
s = input()
for x in s:
  print(x)

for i in range(len(s)):
  print(s[i])

#napis to nie jest lista sensu w strict-ie
L = [7,4,5,2]
L.sort            #s.sort  <-- to był by błąd! Napis to nie jest "pełna" lista
print(s,L)

#przechodzenie z napisu w liście i z listy w napis
L = list(s)
print(L)
L.sort
print(L)
w = "-".join(L)
print(w)

#sprawdż czy wpisane słowo jest palindromem

s = input()
L = list(s)
R = L.copy
R.reverse()
print(L,R)
if L == R:
  print("Jest palindromem")
else:
  print("Nie jest palindromem")

#sprawdzenie palindroma za pomocą listy

# s = input()

# for i in range(len(s)// 2):
#   if s[i] != s[len(s)-1-i]:
#     exit("NIE")
# exit("TAK")

L = [i**2 for i in range(1,10)]
print(L)
print(L[:4])        #<-- pisze 4 pierwsze liczby w tablicy
print(L[::2])        #<-- pisze 2 ostatnie liczby w tablicy
print(L[1::2])
print(L[::-1])      #<--wypisze malejąco

print(L[1:6:2])        #<-- [4,16,36]
print(L[1:6:-2])      #<-- wypisze []
print(L[6:1:-2])        #<-- [49,25,9]
print(L[:1:-2])          #<-- [81,49,25,9]

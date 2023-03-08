#anagram przez sortowanie

a, b = input(), input()
X, Y = list(a), list(b)

X.sort()
Y.sort()

a, b = "".join(X), "".join(Y)

if a == b:
  print("TAK")
else:
  print("NIE")
  
#anagram przez tablicę

c, d = input(), input()
V, Z = [0] * 150, [0] * 150

for j in range(len(c)):
  V[ord(c[j])] +=1
  
for j in range(len(d)):
  Z[ord(d[j])] += 1
print(V)

if V == Z:
  print("TAK")
else:
  print("NIE")


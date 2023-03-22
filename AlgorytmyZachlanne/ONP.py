#ONP --> Odwrotne Notowanie Polskie

s = input()
stos = []
for elem in s:
  if elem.isdigit() : stos.append(int(elem))
  else:
    b, a = stos.pop(), stos.pop()
    if elem == "+" : stos.append(a+b)
    elif elem == "*" : stos.append(a*b)
    elif elem == "-" : stos.append(a-b)
    elif elem == "/" : stos.append(a//b)
  print(stos)


#FIFO --> First In First Out
#LIFO --> Last In First Out

# 5 7 2 1 + 2 - 3 * + +    
  
# 5 7 2 1 --> 2 3 7 5 --> 3 1 7 5 --> 3 7 5 --> 10 5 --> 15

# 12 7 5 - / 4 2 5 * + -
  
# 12 2    <-- 7-5
# 6 4 2 5    <-- 12/2 wrzucamy na stos  4 2 i 5
# 6 4 10    <-- 2*5
# 6 14    <-- 4+10
# -8    <-- 6-14

#Priorytety

#    ( = 0
#    + - = 1
#    * / = 2
#    ^ = 3

# NA STOS WCHODZI TYLKO TEN ZNAK KTÓRY MA WYŻSZY PRIORYTET A JEŚLI NIE TO JEST NA WYJŚCIU WE WSKAZANYM MIEJSCU!!!
#np.  jeśli jest + to - nie może wejść - może wejść tylko * / i ^

# 5+2*8-7*6/3+2+3  --> stos[+]    wyjście[5 2 8 * + 7 6 * 3 / - 2 + 3]

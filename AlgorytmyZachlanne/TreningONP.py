#Przykład 1a
#3 7 2 1 4 3 + - - + *      <-- ZACZYNAMY OD KOŃCOWYCH LICZB!!
#3 7 2 1 7
#3 7 2 -6
#3 7 8
#3 15
#45

#Przykład 1b
# 2 7 4 - * 8 4 2 - / 3 3 + + +   <-- ZACZYNAMY OD KOŃCOWYCH LICZB PRZED ZNAKAMI!!
#2 3 * 8 4 2 - / 3 3 + + +
#6 8 4 2 - / 3 3 + + +
#6 8 2 / 3 3 + + +
#6 4 3 3 + + +
#6 4 6
#6 10
#16

#Przykład 2a
#4*(8+5)-2*(3-(7+4-2)/3*5)    <-- NAWIAS ZAWSZE WCHODZI NA STOS!

#Stos[*(+)]  Wyjście[4 8 5]
#Stos[*]  Wyjście[4 8 5 +]
#Stos[-*(-(+]  Wyjście[4 8 5 + * 2 3 7 4]
#Stos[-*(-(-))]  Wyjście[4 8 5 + * 2 3 7 4 + 2]
#Stos[-*]  Wyjście[4 8 5 + * 2 3 7 4 + 2 - -]
#Stos[-/]  Wyjście[4 8 5 + * 2 3 7 4 + 2 - - * 3]
#Stos[-*]  Wyjście[4 8 5 + * 2 3 7 4 + 2 - - * 3 / 6 * -]

#Przykład 2b
#(8-7)*(4+2-3+5)*(8-(4*(3+5)))

#Stos[*(+]  Wyjście[8 7 - 4 2]
#Stos[*(+]  Wyjście[8 7 - 4 2 + 3 - 5]
#Stos[*(-(*(-]  Wyjście[8 7 - 4 2 + 3 - 5 + * 8 4 3 5]
#Stos[ ]  Wyjście[8 7 - 4 2 + 3 - 5 + * 8 4 3 5 + * - *]

# 3(8-4(3))*3-(5/3)-5

#Stos[(-())*] Wyjście[3 8 4 3 3]
#Stos[-(/)] Wyjście[3 8 4 3 3 - *]
#Stos[-] Wyjście[3 8 4 3 3 - * - / 5]

#3*(5-4*2)/3+2*8-5

#Stos[*(]  Wyjście[3 5 - 4 *]
#Stos[/]  Wyjście[3 5 - 4 * * 3 + 2]
#Stos[*]  Wyjście[3 5 - 4 * * 3 + 2 / 8 - 5]


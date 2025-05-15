# Tady si napíšeme kolik máme lahví a využijeme to k počtu opakování cyklu while
pocet_lahvi = 10

# While bude fungovat pokud počet lahví bude vetší nebo rovno číslu 1
while (pocet_lahvi >= 1):

    # Hláška počtu lahví pokud máme jen jednu lahev
    if(pocet_lahvi == 1):
        print(f"{pocet_lahvi} zelená láhev stojí na stole a jedna spadne")
    # Hlášky pro počet lahví 2, 3, a 4
    elif (pocet_lahvi >= 2 and pocet_lahvi <= 4):
        print(f"{pocet_lahvi} zelené láhve stojí na stole a jedna spadne")
    # Hlášky pro všechny ostatní případy
    else:
        print(f"{pocet_lahvi} zelených láhví stojí na stole a jedna spadne")

    # tady po každém cyklu odečteme -1 z počtu lahví
    pocet_lahvi -= 1
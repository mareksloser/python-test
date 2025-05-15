pocet_lahvi = 10

while (pocet_lahvi >= 1):

    if(pocet_lahvi == 1):
        print(f"{pocet_lahvi} zelená láhev stojí na stole a jedna spadne")
    elif (pocet_lahvi >= 2 and pocet_lahvi <= 4):
        print(f"{pocet_lahvi} zelené láhve stojí na stole a jedna spadne")
    else:
        print(f"{pocet_lahvi} zelených láhví stojí na stole a jedna spadne")

    pocet_lahvi -= 1
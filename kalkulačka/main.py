from kalkulacka import Kalkulacka
k = Kalkulacka()


cislo_1 = float(input('Zadej 1. číslo: '))
cislo_2 = float(input('Zadej 2. číslo: '))

print(f"Součet: {k.secist(cislo_1, cislo_2)}")
print(f"Rozdíl: {k.odecist(cislo_1, cislo_2)}")
print(f"Součin: {k.nasobit(cislo_1, cislo_2)}")
print(f"Podíl: {k.vydelit(cislo_1, cislo_2)}")
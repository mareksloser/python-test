from nakladniAuto import NakladniAuto

vozovy_park = [1000, 2000, 3000, 4000]

for nakladak in vozovy_park:
    a = NakladniAuto(nakladak)
    a.naloz(2000)

    a.zobraz_stav()
    print()
    print("___________")
    print()
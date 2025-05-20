from clovek import Clovek

def main():
    clovek = Clovek("Karel Nový", 25)
    print(clovek)

    # První běh - 10 km
    clovek.bez(10)

    # Druhý běh - 10 km
    clovek.bez(10)

    # Třetí běh - 10 km (příliš unavený, nemělo by se povést)
    clovek.bez(10)

    # Spánek - 1 hodina
    clovek.spi(1)

    # Třetí běh znovu - nyní by měl projít
    clovek.bez(10)

if __name__ == "__main__":
    main()
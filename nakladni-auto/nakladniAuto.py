class NakladniAuto:
    def __init__(self, max_nosnost):
        self.max_nosnost = max_nosnost
        self.naklad_kg = 0

    def naloz(self, hmotnost_kg):
        if self.naklad_kg + hmotnost_kg <= self.max_nosnost:
            self.naklad_kg += hmotnost_kg
            print(f"Naloženo {hmotnost_kg} kg. Aktuální náklad: {self.naklad_kg} kg.")
        else:
            print(f"Nelze naložit {hmotnost_kg} kg. Překročilo by to nosnost.")

    def vyloz(self, hmotnost_kg):
        if self.naklad_kg >= hmotnost_kg:
            self.naklad_kg -= hmotnost_kg
            print(f"Vyloženo {hmotnost_kg} kg. Aktuální náklad: {self.naklad_kg} kg.")
        else:
            print(f"Nelze vyložit {hmotnost_kg} kg. Není tolik nákladu k vyložení.")

    def zobraz_stav(self):
        print(f"Aktuální náklad v autě: {self.naklad_kg} kg. Maximální hmotnost je {self.max_nosnost}. Ještě můžeme naložit {self.max_nosnost - self.naklad_kg}")
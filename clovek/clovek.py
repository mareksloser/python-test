class Clovek:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.unava = 0  # počáteční únava

    def __str__(self):
        return f"{self.jmeno} {self.vek}"

    def bez(self, km):
        nova_unava = self.unava + km
        if nova_unava > 20:
            print("Jsem příliš unavený")
            return False
        else:
            self.unava = nova_unava
            return True

    def spi(self, hodiny):
        self.unava -= hodiny * 10
        if self.unava < 0:
            self.unava = 0

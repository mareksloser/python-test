from Svatky import Svatky
import datetime

s = Svatky()
dnes = datetime.date.today()
den = dnes.timetuple().tm_yday

print()
print(f"Dnes má svátek: {s.kdo_ma_svatek(den)}")
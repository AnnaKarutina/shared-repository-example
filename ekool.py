from õpilane import Õpilane
from kool import Kool

kati = Õpilane('Kati', 8)
mati = Õpilane('Mati', 8)

kool = Kool('Minu kool')

kool.registreeri_kooli(kati)
print(kool.õpilased)
kool.registreeri_kooli(mati)
print(kool.õpilased)
kool.registreeri_kooli(kati)
print(kool.õpilased)
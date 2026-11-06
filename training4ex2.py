hi_ha_deu = False
nota = int(input("Introdueix una nota (-1 per acabar): "))
while True:
    nota = float(input("Introdueix una nota: "))
    if nota == 1:
        break
    if nota == 10:
        hi_ha_deu = True
if hi_ha_deu:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")
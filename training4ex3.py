hi_ha_negatiu = False
for i in range(10):
    num = float(input(f"Introdueix el nombre {i + 1}: "))
    if num < 0:
        hi_ha_negatiu = True
if hi_ha_negatiu:
    print("Hi havia almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")
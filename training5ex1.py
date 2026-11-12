def calcular_preu(preu_peces, cost_ma_obra):
    total = preu_peces + cost_ma_obra
    return total

preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")
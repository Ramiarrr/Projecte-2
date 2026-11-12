def calcular_preu(preu_peces, cost_ma_obra):
    total = preu_peces + cost_ma_obra
    return total
preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")

DESCOMPTES = {
    "particular": 0,
    "empresa": 10,
    "client habitual": 15
}
def obtenir_percentatge(tipus_client):
    """Retorna el % de descompte, o None si el tipus no és vàlid."""
    return DESCOMPTES.get(tipus_client.strip().lower())
def aplicar_descompte(preu, tipus_client):
    percentatge = obtenir_percentatge(tipus_client)
    if percentatge is None:
        print("Error: tipus de client no vàlid ->", tipus_client)
        return preu
    return preu - preu * percentatge / 100
print(aplicar_descompte(100, "Particular"))
print(aplicar_descompte(100, "EMPRESA"))
print(aplicar_descompte(100, "client habitual"))
print(aplicar_descompte(100, "VIP"))
def calcular_iva(preu):
    return preu * 0.21          # només l'import de l'IVA
def calcular_factura(preu, tipus_client):
    preu_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descompte)
    return preu_descompte + iva
print(calcular_factura(100, "empresa"))
def mostrar_menu():
    print("\n     SERVEI TÈCNIC INFORMÀTIC     ")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")
def demanar_numero(missatge):
    """Demana un número positiu i repeteix fins que sigui vàlid."""
    while True:
        try:
            valor = float(input(missatge))
            if valor >= 0:
                return valor
            print("El valor no pot ser negatiu.")
        except ValueError:
            print("Introdueix un número vàlid.")
def demanar_tipus_client():
    """Demana el tipus de client fins que sigui un dels vàlids."""
    while True:
        tipus = input("Tipus de client (particular / empresa / client habitual): ")
        if obtenir_percentatge(tipus) is not None:
            return tipus
        print("Tipus no vàlid, torna-ho a provar.")
def mostrar_factura(nom, preu_inicial, descompte, iva, total):
    print("\n------------- FACTURA -------------")
    print(f"Client:            {nom}")
    print(f"Preu inicial:      {preu_inicial:.2f} €")
    print(f"Descompte aplicat: {descompte:.2f} €")
    print(f"IVA (21%):         {iva:.2f} €")
    print(f"TOTAL A PAGAR:     {total:.2f} €")
    print("-----------------------------------")
def registrar_reparacio():
    """Demana les dades, calcula i mostra la factura. Retorna el total."""
    nom = input("Nom del client: ")
    peces = demanar_numero("Cost de les peces (€): ")
    ma_obra = demanar_numero("Cost de la mà d'obra (€): ")
    tipus = demanar_tipus_client()

    preu_inicial = calcular_preu(peces, ma_obra)
    preu_descompte = aplicar_descompte(preu_inicial, tipus)
    descompte = preu_inicial - preu_descompte
    iva = calcular_iva(preu_descompte)
    total = calcular_factura(preu_inicial, tipus)

    mostrar_factura(nom, preu_inicial, descompte, iva, total)
    return total
def main():
    num_reparacions = 0
    facturacio_total = 0
    opcio = 0
    while opcio != 4:
        mostrar_menu()
        opcio = input("Selecciona una opció: ")
        if opcio == "1":
            facturacio_total += registrar_reparacio()
            num_reparacions += 1
        elif opcio == "2":
            print("Reparacions realitzades:", num_reparacions)
        elif opcio == "3":
            print(f"Facturació acumulada: {facturacio_total:.2f} €")
        elif opcio == "4":
            print("Hasta la pròxima")
            opcio = 4
        else:
            print("Opció no vàlida.")
        if opcio == "4":
            opcio = 4
main()

def main():
    num_reparacions = 0
    facturacio_total = 0

    while True:
        mostrar_menu()
        opcio = input("Selecciona una opció: ")
        if opcio == "1":
            facturacio_total += registrar_reparacio()
            num_reparacions += 1
        elif opcio == "2":
            print("Reparacions realitzades:", num_reparacions)
        elif opcio == "3":
            print(f"Facturació acumulada: {facturacio_total:.2f} €")
        elif opcio == "4":
            print("Fins aviat!")
            break
        else:
            print("Opció no vàlida.")
main()

#      EXERCICI 5: Reflexió final
# 4. print() mostra informació per pantalla; return envia un valor a qui ha
#    cridat la funció (es pot guardar i reutilitzar) i acaba la funció.
# 5. Perquè el codi queda més ordenat, llegible, fàcil de provar i de
#    modificar, i cada funció fa una única tasca.
# 6. Un paràmetre és una variable indicada a la definició de la funció
#    que rep les dades (arguments) quan es crida.
# 7. Una variable local és la que es crea dins d'una funció i només
#    existeix i es pot utilitzar dins d'aquesta funció.
# 8. Evita repetir codi, estalvia temps, redueix errors i, si cal canviar
#    alguna cosa, només es modifica en un lloc.

def mostrar_reparacions(reparacions):
    if not reparacions:
        print("Encara no hi ha reparacions.")
        return
    for r in reparacions:
        mostrar_factura(r["nom"], r["preu_inicial"], r["descompte"], r["iva"], r["total"])
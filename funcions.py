# EXERCICI 1. Calculadora de preus
def calcular_preu(preu_peces, ma_obra):
    """Calcula i retorna el cost total d'una reparació."""
    total = preu_peces + ma_obra
    return total
# Prova de l'Exercici 1
print("-PROVA EXERCICI 1")
preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")
# EXERCICI 2. Funcions amb condicions
def aplicar_descompte(preu, tipus_client):
    """
    Aplica un descompte segons el tipus de client i retorna el preu final.
    Nota: S'utilitza .strip().lower() per acceptar el text tant en minúscules,
    majúscules o amb inicial majúscula (ex: 'Empresa', 'empresa', 'EMPRESA').
    """
    tipus_normalitzat = tipus_client.strip().lower()
    if tipus_normalitzat == "particular":
        descompte = 0.0
    elif tipus_normalitzat == "empresa":
        descompte = 0.10
    elif tipus_normalitzat == "client habitual":
        descompte = 0.15
    else:
        print(f"Error: El tipus de client '{tipus_client}' no és vàlid. No s'aplica descompte.")
        return preu
    preu_final = preu - (preu * descompte)
    return preu_final
# Proves de l'Exercici 2 amb els 3 tipus vàlids i un d'incorrecte
print("\n-PROVES EXERCICI 2")
print("Particular (100 €):", aplicar_descompte(100, "Particular"), "€")
print("Empresa (100 €):", aplicar_descompte(100, "empresa"), "€")
print("Client habitual (100 €):", aplicar_descompte(100, "CLIENT HABITUAL"), "€")
print("Tipus incorrecte (100 €):", aplicar_descompte(100, "VIP"), "€")
# EXERCICI 3. Funcions que criden altres funcions
def calcular_iva(preu):
    """Calcula i retorna únicament l'import del 21% d'IVA sobre un import."""
    return preu * 0.21
def calcular_factura(preu, tipus_client):
    """
    Calcula el total d'una factura reutilitzant les funcions anteriors:
    aplica primer el descompte i després suma el 21% d'IVA.
    """
    preu_amb_descompte = aplicar_descompte(preu, tipus_client)
    import_iva = calcular_iva(preu_amb_descompte)
    total_factura = preu_amb_descompte + import_iva
    return total_factura
# Prova de l'Exercici 3
print("\n-PROVA EXERCICI 3")
print("Factura Empresa (100 € base):", round(calcular_factura(100, "Empresa"), 2), "€")
# EXERCICI 4. Programa complet: servei tècnic (i Ampliació opcional)
def mostrar_menu():
    """Mostra per pantalla les opcions del menú del servei tècnic."""
    print("\n-SERVEI TÈCNIC INFORMÀTIC")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")
def mostrar_factura(nom_client, preu_inicial, descompte_aplicat, iva, total):
    """Imprimeix el resum detallat de la factura d'una reparació."""
    print("\n-FACTURA")
    print(f"Client:             {nom_client}")
    print(f"Preu inicial:       {preu_inicial:.2f} €")
    print(f"Descompte aplicat: -{descompte_aplicat:.2f} €")
    print(f"IVA (21%):          +{iva:.2f} €")
    print(f"TOTAL A PAGAR:      {total:.2f} €")
def processar_nova_reparacio():
    """
    Demana les dades d'una reparació, calcula la factura mitjançant les
    funcions anteriors, la mostra i retorna el total cobrat.
    """
    nom_client = input("Nom del client: ")
    cost_peces = float(input("Cost de les peces (€): "))
    cost_ma_obra = float(input("Cost de la mà d'obra (€): "))
    tipus_client = input("Tipus de client (Particular / Empresa / Client habitual): ")
    # Càlculs reutilitzant les funcions dels exercicis 1, 2 i 3
    preu_inicial = calcular_preu(cost_peces, cost_ma_obra)
    preu_descomptat = aplicar_descompte(preu_inicial, tipus_client)
    descompte_aplicat = preu_inicial - preu_descomptat
    iva = calcular_iva(preu_descomptat)
    total_pagar = calcular_factura(preu_inicial, tipus_client)
    mostrar_factura(nom_client, preu_inicial, descompte_aplicat, iva, total_pagar)
    return total_pagar
def executar_programa():
    """Funció principal que controla el bucle del menú del servei tècnic."""
    num_reparacions = 0
    facturacio_acumulada = 0.0
    while True:
        mostrar_menu()
        opcio = input("Selecciona una opció: ").strip()
        if opcio == "1":
            try:
                total_reparacio = processar_nova_reparacio()
                num_reparacions += 1
                facturacio_acumulada += total_reparacio
            except ValueError:
                print("\nError: El cost de les peces i de la mà d'obra han de ser valors numèrics.")
        elif opcio == "2":
            print(f"\nNombre de reparacions realitzades: {num_reparacions}")
        elif opcio == "3":
            print(f"\nFacturació total acumulada: {facturacio_acumulada:.2f} €")
        elif opcio == "4":
            print("\nSortint del programa.")
            break
        else:
            print("\nOpció no vàlida. Si us plau, tria una opció entre 1 i 4.")
# Inici del programa principal
if __name__ == "__main__":
    executar_programa()
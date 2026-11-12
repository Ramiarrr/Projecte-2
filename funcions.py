# ==============================================================================
# ACTIVITAT PRÀCTICA: FUNCIONS EN PYTHON - GESTIÓ D'UN SERVEI TÈCNIC INFORMÀTIC
# Cicle Formatiu: 2n de Sistemes Microinformàtics i Xarxes (SMX)
# ==============================================================================
# ------------------------------------------------------------------------------
# EXERCICI 1. Calculadora de preus
# ------------------------------------------------------------------------------
def calcular_preu(preu_peces, ma_obra):
    """Calcula i retorna el cost total d'una reparació."""
    total = preu_peces + ma_obra
    return total


# Prova de l'Exercici 1
print("--- PROVA EXERCICI 1 ---")
preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")

# Respostes a les preguntes de l'Exercici 1:
# 1. Quants paràmetres té la funció?
#    Té 2 paràmetres: 'preu_peces' i 'ma_obra'.
#
# 2. Quin valor retorna?
#    Retorna el resultat de sumar el preu de les peces i el cost de la mà d'obra
#    (en l'exemple de prova retorna el valor numèric 75).
#
# 3. Què passaria si eliminéssim el return?
#    La funció retornaria 'None' per defecte. La variable 'preu' emmagatzemaria
#    'None' i per pantalla es mostraria "Cost total: None €", sense poder fer
#    servir el resultat en càlculs posteriors.


# ------------------------------------------------------------------------------
# EXERCICI 2. Funcions amb condicions
# ------------------------------------------------------------------------------
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
print("\n--- PROVES EXERCICI 2 ---")
print("Particular (100 €):", aplicar_descompte(100, "Particular"), "€")
print("Empresa (100 €):", aplicar_descompte(100, "empresa"), "€")
print("Client habitual (100 €):", aplicar_descompte(100, "CLIENT HABITUAL"), "€")
print("Tipus incorrecte (100 €):", aplicar_descompte(100, "VIP"), "€")


# ------------------------------------------------------------------------------
# EXERCICI 3. Funcions que criden altres funcions
# ------------------------------------------------------------------------------
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
print("\n--- PROVA EXERCICI 3 ---")
print("Factura Empresa (100 € base):", round(calcular_factura(100, "Empresa"), 2), "€")


# ------------------------------------------------------------------------------
# EXERCICI 4. Programa complet: servei tècnic (i Ampliació opcional)
# ------------------------------------------------------------------------------
def mostrar_menu():
    """Mostra per pantalla les opcions del menú del servei tècnic."""
    print("\n===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")


def mostrar_factura(nom_client, preu_inicial, descompte_aplicat, iva, total):
    """Imprimeix el resum detallat de la factura d'una reparació."""
    print("\n---------- FACTURA ----------")
    print(f"Client:            {nom_client}")
    print(f"Preu inicial:      {preu_inicial:.2f} €")
    print(f"Descompte aplicat: -{descompte_aplicat:.2f} €")
    print(f"IVA (21%):         +{iva:.2f} €")
    print(f"TOTAL A PAGAR:     {total:.2f} €")
    print("-----------------------------\n")


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
            print("\nSortint del programa. Fins aviat!")
            break
        else:
            print("\nOpció no vàlida. Si us plau, tria una opció entre 1 i 4.")


# Inici del programa principal
if __name__ == "__main__":
    executar_programa()


# ------------------------------------------------------------------------------
# EXERCICI 5. Reflexió final
# ------------------------------------------------------------------------------
# 4. Quina diferència hi ha entre print() i return?
#    print() únicament mostra un text o valor per la consola perquè el vegi
#    l'usuari, però aquest valor es perd. En canvi, return envia el resultat
#    calculat cap enfora de la funció per poder-lo desar en una variable o fer-lo
#    servir en altres operacions del programa.
#
# 5. Per què és millor dividir un programa en funcions?
#    Perquè el codi queda molt més ordenat, llegible i fàcil de mantenir. A més,
#    permet detectar errors més ràpidament i treballar per parts independents
#    (modularitat).
#
# 6. Què és un paràmetre?
#    És una variable definida dins dels parèntesis d'una funció (a la instrucció
#    def) que serveix per rebre les dades d'entrada (arguments) quan la funció
#    és cridada.
#
# 7. Què és una variable local?
#    És una variable que es crea dins d'una funció i que només existeix i es pot
#    utilitzar dins d'aquesta mateixa funció; un cop acaba la seva execució,
#    desapareix de la memòria.
#
# 8. Quins avantatges té reutilitzar una funció?
#    Evita repetir el mateix codi en diferents llocs del programa, estalvia temps
#    de desenvolupament i facilita les modificacions: si canvia una fórmula (per
#    exemple, el percentatge d'IVA), només cal modificar-la en un únic lloc.
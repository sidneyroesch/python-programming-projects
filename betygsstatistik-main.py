# Betygsstatistik
# Programmet läser in poäng i fem ämnen och omvandlar poängen till
# bokstavsbetyg. Därefter visas statistik på elevens resultat.

def läs_in_poäng(ämnen):
    """
    Läser in poäng för varje ämne och sparar poängen i en lista.
    """

    poäng = []

    # En lista används eftersom man behöver kunna spara
    # flera poäng och därmed koppla dem till ämnena.
    for ämne in ämnen:
        poäng_för_ämne = int(input(f"Ange poäng i {ämne} (0-100): "))
        poäng.append(poäng_för_ämne)

    return poäng


def omvandla_till_betyg(poäng):
    """
    Omvandlar poäng till bokstavsbetyg och returnerar en lista
    med alla betyg.
    """

    betyg = []

    # Gränserna kontrolleras och kontrollen utförs uppifrån och ned.
    # Loopen gör att man inte behöver skriva samma kod flertal gånger.
    for poäng_i_ämne in poäng:
        if poäng_i_ämne >= 90:
            betyg.append("A")
        elif poäng_i_ämne >= 80:
            betyg.append("B")
        elif poäng_i_ämne >= 70:
            betyg.append("C")
        elif poäng_i_ämne >= 60:
            betyg.append("D")
        elif poäng_i_ämne >= 50:
            betyg.append("E")
        else:
            betyg.append("F")

    return betyg


def skriv_ut_resultat(ämnen, poäng, betyg):
    """
    Skriver ut elevens poäng och betyg för varje ämne.
    """

    print("\n--- Resultat ---")

    # range används eftersom man behöver hämta samma position
    # från tre olika listor: ämne, poäng och betyg.
    for i in range(len(ämnen)):
        print(f"{ämnen[i]}: {poäng[i]} poäng - betyg {betyg[i]}")


def Statistik(betyg, poäng):
    """
    Räknar ut hur många av varje betyg eleven fått
    samt totalpoäng och medelpoäng.
    """

    # Börjar med 0 eftersom man ännu inte har räknat
    # något betyg.
    antal_A = 0
    antal_B = 0
    antal_C = 0
    antal_D = 0
    antal_E = 0
    antal_F = 0

    # Varje betyg i listan kontrolleras och rätt räknare ökas.
    for betyg_i_ämne in betyg:
        if betyg_i_ämne == "A":
            antal_A += 1
        elif betyg_i_ämne == "B":
            antal_B += 1
        elif betyg_i_ämne == "C":
            antal_C += 1
        elif betyg_i_ämne == "D":
            antal_D += 1
        elif betyg_i_ämne == "E":
            antal_E += 1
        elif betyg_i_ämne == "F":
            antal_F += 1

    # sum() gör att man slipper lägga ihop varje poäng manuellt.
    total_poäng = sum(poäng)

    # Medelpoängen räknas genom att dela totalpoängen
    # med antalet ämnen.
    medelpoäng = total_poäng / len(poäng)

    print("\n--- Betygsstatistik ---")
    print(f"A: {antal_A}")
    print(f"B: {antal_B}")
    print(f"C: {antal_C}")
    print(f"D: {antal_D}")
    print(f"E: {antal_E}")
    print(f"F: {antal_F}")

    print(f"\nTotalpoäng: {total_poäng}")
    print(f"Medelpoäng: {medelpoäng:.1f}")


# ---------------- Huvudprogrammet ----------------

print("================================")
print("       BETYGSSTATISTIK")
print("================================\n")
print("Välkommen! Ange dina poäng i de fem ämnena.")
print("Poängen ska vara mellan 0 och 100.\n")

# Ämnena ligger i en lista så att programmet enkelt
# kan arbeta med alla ämnen genom en loop.
ämnen = ["Svenska", "Matematik", "Engelska", "Programmering", "Webbutveckling"]

# Läs in poängen och spara dem i en enskild lista.
poäng = läs_in_poäng(ämnen)

# Omvandla poängen till bokstavsbetyg och spara dem
# i en enskild lista.
betyg = omvandla_till_betyg(poäng)

# Visa resultatet för varje ämne.
skriv_ut_resultat(ämnen, poäng, betyg)

# Beräkna och visa den sammanlagda statistiken.
Statistik(betyg, poäng)

print("\nProgrammet avslutas.")


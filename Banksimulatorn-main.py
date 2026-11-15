# Banksimulatorn

# Planering av programmet
# Visa ett välkomstmeddelande för banksystemet.
# Skapa en variabel för saldo som börjar på 0 kr.
# Visa en meny med följande alternativ i en loop:
# [I]nsättning, [U]ttag, [S]aldo, [T]ransaktioner, [R]äntesimulering, [A]vsluta.
# Läs in användarens val och kör rätt funktion:
# - Om insättning - be om belopp och lägg till på saldot.
# - Om uttag - be om belopp, kontrollera att det räcker, och dra av från saldot.
# - Om saldot - visa aktuellt saldo.
# - Om transaktioner - spara en logg över transaktioner.
# - Om ränteberäkning - be om årlig insättning, räntesats och antal år. Beräkna nytt saldo i en loop.
# - Om avsluta - avsluta loopen och visa ett hej då - meddelande.
# Programmet avslutas.

# Funktioner
# Insättning
def insättning(saldo, transaktioner):
    # Felhantering för felaktig inmatning
    while True:
        try:
            belopp = float(input("Ange belopp: "))
            # Felhantering för inmatning av ett negativt belopp
            if belopp <= 0:
                print("Felaktig inmatning. Ange ett belopp som är större än 0")
            else:
                break
        except ValueError:
            print("Felaktig inmatning. Ange belopp i siffror.")
    saldo += belopp
    transaktioner.append(f"Insättning: +{belopp:.2f} kr")
    print("Insättning genomförd.")
    print(f"Du har {saldo:.2f} kr på kontot.")
    return saldo

# Uttag
def uttag(saldo, transaktioner):
    # Felhantering för felaktig inmatning
    while True:
        try:
            belopp = float(input("Ange belopp för uttag: "))
            # Felhantering för inmatning av ett negativt belopp
            if belopp <= 0:
                print("Felaktig inmatning. Ange ett belopp som är större än 0")
            else:
                break
        except ValueError:
            print("Felaktig inmatning. Ange belopp i siffror.")
    # Felhantering vid uttag av ett belopp större än saldot
    if saldo < belopp:
        print("För lågt saldo.")
        print("Uttaget kunde inte genomföras.")
    else:
        saldo -= belopp
        transaktioner.append(f"Uttag: -{belopp:.2f} kr")
        print("Uttag genomfört.")
        print(f"Du har nu {saldo:.2f} kr på kontot.")
    return saldo

# Transaktioner
def transaktions_lista(transaktioner):
    # Felhantering om transaktionslistan är tom vid första körning av programmet
    if not transaktioner:
        print("Inga utförda transaktioner vid tillfället.")
        print("Gör ett nytt val.")
    else:
        for transaktion in transaktioner:
            print(transaktion)

# Räntesimulering
def räntesimulering(saldo):
    # Felhantering för felaktig inmatning
    while True:
        try:
            årlig_insättning = float(input("Ange årlig insättning: "))
            räntesats = float(input("Ange räntesats: "))
            antal_år = int(input("Ange antal år: "))

            # Felhantering för inmatning av ett negativt belopp
            if årlig_insättning <= 0:
                print("Felaktig inmatning. Årlig insättning måste vara större än 0.")
            elif räntesats < 0:
                print("Felaktig inmatning. Räntesatsen måste vara större än 0.")
            elif antal_år <= 0:
                print("Felaktig inmatning. Antal år måste vara större än 0.")
            else:
                break
        except ValueError:
            print("Felaktig inmatning. Ange endast siffror.")

    # Ny variable så att saldo inte ska påverkas då detta är en simulering
    framtida_saldo = saldo

    # Programmet räknar ut framtida saldo med hjälp av en loop
    print("\nResultat av räntesimuleringen:") # En rubrik
    for år in range(antal_år):
        framtida_saldo += årlig_insättning
        framtida_saldo += framtida_saldo * (räntesats / 100)
        print(f"År {år + 1}: Saldo = {framtida_saldo:.2f} kr")


# Huvudprogram
# Visar ett välkomstmeddelande för banksystemet
name = input("Logga in med ditt namn:")
print(f"Välkommen {name}!")

# Skapar en variabel för saldo som börjar på 0 kr
saldo = 0

# Skapar en variabel för transaktioner som uppdateras vid varje transaktion
transaktioner = []

# Visar en meny och be användaren att göra ett val och efter varje val uppdateras saldon
# loop som håller igång menyn tills användaren avslutar
while True:
    # Meny
    print("\n=================")
    print("Banksimulator")
    print("=================")
    print("[I] Insättning")
    print("[U] Uttag")
    print("[S] Saldo")
    print("[T] Transaktioner")
    print("[R] Räntesimulering")
    print("[A] Avsluta")

    # Ber användaren att göra ett val och inmatningen ändras till stor bokstav
    val = input("Vänligen välj: ").upper()

    # Insättning
    if val == "I":
        saldo = insättning(saldo, transaktioner)

    # Uttag
    elif val == "U":
        saldo = uttag(saldo, transaktioner)

    # Saldo
    elif val == "S":
        print(f"Du har {saldo:.2f} kr på kontot.")

    # Transaktioner
    elif val == "T":
        transaktions_lista(transaktioner)

    # Räntesats
    elif val == "R":
        räntesimulering(saldo)

    # Avsluta programmet
    elif val == "A":
        print(f"Hej då {name}!")
        break

    # Felhantering text för ogiltiga val
    else:
        print("Ogiltigt val.")
        print("Välj I, U, S, T, R eller A")
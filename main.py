# Växelprogrammet

# Visa ett välkomstmeddelande
print("Välkommen till växelprogrammet!")


# Användarens inmatning av varans pris, betalt belopp
# samt felhantering om användaren matar in bokstäver istället för siffror
try:
    varans_pris = float(input("Ange varans pris: "))
    betalt_belopp = float(input("Ange betalt belopp: "))
except ValueError:
    print("Felaktig inmatning. Programmet avslutas.")
    raise SystemExit

# Kontrollera om användaren har betalt för lite och ge svar vid betalning
if betalt_belopp < varans_pris:
    print("Erhållet belopp är för litet.")

# Avrundning av växeln samt utskrivning av växeln
else:
    växel = betalt_belopp - varans_pris
    hela_kronor = int(växel)    # Tar bort decimalerna för att kunna räkna ut hur många ören som finns kvar
    öre = växel - hela_kronor
    if öre < 0.25:
        växel = hela_kronor
    elif öre < 0.75:
        växel = hela_kronor + 0.50
    else:
        växel = hela_kronor + 1

grund_växel = växel
print(f"Du får tillbaka {grund_växel} kr.")
print()     # Tom rad för att underlätta läsningen då det blir två text rader efter varandra.
print("Din växel består av:")

# Räknar ut hur många sedlar och mynt kunden ska få som växel
tusenlappar = växel // 1000
växel = växel % 1000
femhundralappar = växel // 500
växel = växel % 500
tvåhundralappar = växel // 200
växel = växel % 200
hundralappar = växel // 100
växel = växel % 100
femtiolappar = växel // 50
växel = växel % 50
tjugolappar = växel // 20
växel = växel % 20
tiokronor = växel // 10
växel = växel % 10
femkronor = växel // 5
växel = växel % 5
tvåkronor = växel // 2
växel = växel % 2
enkronor = växel // 1
växel = växel % 1

if tusenlappar > 0:
    print(f"1000 kr: {tusenlappar}")
if femhundralappar > 0:
    print(f"500 kr: {femhundralappar}")
if tvåhundralappar > 0:
    print(f"200 kr: {tvåhundralappar}")
if hundralappar > 0:
    print(f"100 kr: {hundralappar}")
if femtiolappar > 0:
    print(f"50 kr: {femtiolappar}")
if tjugolappar > 0:
    print(f"20 kr: {tjugolappar}")
if tiokronor > 0:
    print(f"10 kr: {tiokronor}")
if femkronor > 0:
    print(f"5 kr: {femkronor}")
if tvåkronor > 0:
    print(f"2 kr: {tvåkronor}")
if enkronor > 0:
    print(f"1 kr: {enkronor}")
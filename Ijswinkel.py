print('Welkom bij Papi Gelato')
def soort_bolletje(aantal):
    x = 1
    for i in range(1,aantal+1):
        soort = input('Welke smaak wilt u voor bolletje nummer' + str(x) + '? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?')
        if soort == "V" or "M" or "C" or "A":
            x += 1
        else:
            print('Sorry dat snap ik niet...')
            soort_bolletje()

def aantal_bolletjes():
    aantal = int(input('Hoeveel bolletjes wilt u?'))
    if aantal >= 1 and aantal <= 3:
        soort_bolletje(aantal)
        bakje_hoorntje(aantal)
        
    elif aantal >= 4 and aantal <= 8:
        print('Dan krijgt u van mij een bakje met ' + str(aantal) + ' bolletjes')
        soort_bolletje(aantal)
    elif aantal > 8:
        print('Sorry, zulke grote bakken hebben we niet')
    else:
        print('Sorry dat snap ik niet...')
def bakje_hoorntje(aantal):
    bakje_hoorntje = input('Wilt u deze ' + str(aantal) + ' bolletje(s) in A) een hoorntje of B) een bakje?')
    if bakje_hoorntje == "A":
        totaal = prijs(aantal, True, False)
        hoorntje = input('Hier is uw hoorntje met ' + str(aantal) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if hoorntje == 'Y':
            aantal_bolletjes()
            
        elif hoorntje == 'N':
            print('Bedankt en tot ziens')

    elif bakje_hoorntje == "B":
        totaal = prijs(aantal, False, True)
        bakje = input('Hier is uw bakje met ' + str(aantal) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if bakje == 'Y':
            aantal_bolletjes()
        elif bakje == 'N':
            print(str(totaal))
            print('Bedankt en tot ziens')
    else:
        print('sorry dat snap ik niet...')

def prijs(aantal,hoorntje, bol):
    totaal_prijs = 0
    bolletje = 1.10
    hoorn = 1.25
    bakje = 0.75
    if hoorntje == True:
        totaal_prijs += hoorn
    elif bol == True:
        totaal_prijs =+ bakje
    bolletje_prijs = bolletje * aantal
    totaal_prijs = totaal_prijs + bolletje_prijs
    return totaal_prijs
def totaal(aantal,hoorn,bol):
    print("--------[Papi Gelato]--------")
    print("Bolletjes        " + str(aantal) + " x €1.10 = €" + str(aantal + 1.10))
    print("Hoorntje        " + str(hoorn) + " x €1.25 = €" + str(aantal + 1.25))
    print("Bakje      " + str(bol) + " x €1.25 = €" + str(aantal + 0.75))
aantal_bolletjes()
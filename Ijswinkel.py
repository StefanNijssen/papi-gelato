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
        
        totaal = prijs(aantal, 1, 0, 0)
        hoorntje = input('Hier is uw hoorntje met ' + str(aantal) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if hoorntje == 'Y':
            aantal_bolletjes()
            
        elif hoorntje == 'N':
            
            print('Bedankt en tot ziens')

    elif bakje_hoorntje == "B":
        totaal = prijs(aantal, 0, 1, 1)
        bakje = input('Hier is uw bakje met ' + str(aantal) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if bakje == 'Y':
            aantal_bolletjes()
        elif bakje == 'N':
            totaal()
            print('Bedankt en tot ziens')
    else:
        print('sorry dat snap ik niet...')

def prijs(aantal,hoorntje, bol, top):
    top = toppings(top)
    totaal_prijs = 0
    bolletje = round(1.10, 2)
    hoorn = 1.25
    bakje = 0.75
    if hoorntje == 1:
        totaal_prijs += hoorn
    elif bol == 1:
        totaal_prijs =+ bakje
    bolletje_prijs = bolletje * aantal
    totaal_prijs = totaal_prijs + bolletje_prijs
    totaal_prijs = totaal_prijs + top
    
    print("--------[Papi Gelato]--------")
    print("Bolletjes        " + str(aantal) + " x €1.10 = €" + str(aantal * 1.10))
    print("Hoorntje         " + str(hoorntje) + " x €1.25 = €" + str(hoorntje * 1.25))
    print("Bakje            " + str(bol) + " x €0.75 = €" + str(bol * 0.75))
    print("Toppings                   = €" + str(round(top,2)) )
    print("Totaal                     = €" + str(round(totaal_prijs,2)))

    return totaal_prijs
def toppings(bakje):
    top = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
    if top == "A":
        totaal_topping = 0
        return totaal_topping
    elif top == "B":
        totaal_topping = 0.50
        return totaal_topping

    elif top == "C":
        totaal_topping = 0.30
        return totaal_topping
        
    elif top == "D":
        if bakje == 0:
            totaal_topping = 0.60
            return totaal_topping
           
        elif bakje == 1:
            totaal_topping = 0.90
            return totaal_topping
        
            
    else:
        print("Sorry dat begrijp ik niet.")
        
aantal_bolletjes()

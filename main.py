print('𝓒𝓪𝓯é 𝓐𝓾 𝓛𝓪𝓲𝓽')
a = 1
EspShotPrc = 0.60
CapMilkPrc = 0.15
LatMilPrc = 0.50
IcCofMilkPrc = 0.75
IcCofIcCrmPrc = 0.40

CapPrc = 3.00
EspPrc = 2.25
LatPrc = 2.50
IcCofPrc = 2.50
while a == 1:
    Mode = input('Would you like to order or view the daily report (employee only)? ').lower()
    if Mode == 'order':
        print('''Menu
Cappuccino                  $3.00
    A shot of espresso steamed 
    milk and a thick layer of milk
    foam

Espresso                    $2.25
    A singular shot of espresso

Latte                       $2.50
    A shot of espresso with 
    steamed milk and a thin layer 
    of milk foam

Iced Coffee                 $2.50
    A shot of espresso with cold
    milk, a few ice cubes and a 
    scoop of vanilla ice-cream''')
        CapNum = int(input('How Many Cappuccinos Would You Like? '))
        EspNum = int(input('How Many Espressos Would You Like? '))
        LatNum = int(input('How Many Lattes Would You Like? '))
        IcCofNum = int(input('How Many Iced Coffees Would You Like? '))
        OrderPrc = (CapNum * CapPrc) * (EspNum * EspPrc) * (LatNum * LatPrc) * (IcCofNum * IcCofPrc)
        OrderType = input('Would you like this order to be dine-in or take-away (keep in mind that a take-away order will incur an additional 5% surcharge)? ').lower()
        if OrderType == 'dine-in' or 'dine in' or 'dinein':
            print('this is a place keeper to alleviate errors for testing')
        elif OrderType == 'take-away' or 'take away' or 'takeaway':
            print('this is a place keeper to alleviate errors for testing')
    elif Mode == 'Daily Report' or 'Daily report' or 'daily Report' or 'daily report':
        print('this is a place keeper to alleviate errors for testing')
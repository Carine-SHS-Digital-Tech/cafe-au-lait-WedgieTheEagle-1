print('𝓒𝓪𝓯é 𝓐𝓾 𝓛𝓪𝓲𝓽')
a = 1
cfeshotprc = 0.60
capmilkpr = 0.15
latmmilkprc = 0.50
iccofmilkprc = 0.75
iccoficcrmprc = 0.40

capprc = 3.00
espprc = 2.25
latprc = 2.50
iccofprc = 2.50
while a == 1:
    mode = input('Would you like to order or view the daily report (employee only)? ')
    if mode == 'order' or 'Order':
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
        capnum = int(input('How Many Cappuccinos Would You Like? '))
        espnum = int(input('How Many Espressos Would You Like? '))
        latnum = int(input('How Many Lattes Would You Like? '))
        iccofnum = int(input('How Many Iced Coffees Would You Like? '))
    elif mode == 'Daily Report' or 'Daily report' or 'daily Report' or 'daily report':
        print('this is a place keeper to alleviate errors')
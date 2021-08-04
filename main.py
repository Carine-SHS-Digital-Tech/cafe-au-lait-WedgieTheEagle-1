print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
╭━━━╮   ╭━╮   ╭━━━╮   ╭╮      ╭╮
┃╭━╮┃   ┃╭╯   ┃╭━╮┃   ┃┃     ╭╯╰╮
┃┃ ╰╋━━┳╯╰┳━━╮┃┃ ┃┣╮╭╮┃┃  ╭━━╋╮╭╯
┃┃ ╭┫╭╮┣╮╭┫┃━┫┃╰━╯┃┃┃┃┃┃ ╭┫╭╮┣┫┃
┃╰━╯┃╭╮┃┃┃┃┃━┫┃╭━╮┃╰╯┃┃╰━╯┃╭╮┃┃╰╮
╰━━━┻╯╰╯╰╯╰━━╯╰╯ ╰┻━━╯╰━━━┻╯╰┻┻━╯
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                          ''')
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
        OrderPrc = (CapNum * CapPrc) + (EspNum * EspPrc) + (LatNum * LatPrc) + (IcCofNum * IcCofPrc)
        OrderType = input('Would you like this order to be dine-in or take-away (keep in mind that a take-away order will incur an additional 5% surcharge)? ').lower()
        if OrderType == 'dine-in' or 'dine in' or 'dinein':
            TotalIncGST = "{:.2f}".format(OrderPrc * 1.1)
            print(f'''{CapNum} Cappuccinos at ${"{:.2f}".format(CapNum * CapPrc)}
{EspNum} Espressos at ${"{:.2f}".format(EspNum * EspPrc)}
{LatNum} Lattes at ${"{:.2f}".format(LatNum * LatPrc)}
{IcCofNum} Iced Coffees at ${"{:.2f}".format(IcCofNum * IcCofPrc)}
    Total Price +GST: ${TotalIncGST}
''')
            TotalIncGST = float(TotalIncGST)
            AmtPaid = float(input('How much have you paid? $'))
            if AmtPaid > TotalIncGST:
                Change = "{:.2f}".format(AmtPaid - TotalIncGST)
                print(f'Your Change Is ${Change}')
                print('Thank You For Coming To Cafe Au Lait. Enjoy Your Drinks.')
                print('')
            elif AmtPaid < TotalIncGST:
                SumExtra = float("{:.2f}".format(TotalIncGST - AmtPaid))
                print(f'You Need To Pay An Extra ${SumExtra}')
                while float(SumExtra) > float(0.00):
                    AmtPaid = float(input('How much have you paid? $'))
                    SumExtra = float("{:.2f}".format(SumExtra - AmtPaid))
                    if SumExtra > float(0.00):
                        print(f'You Need To Pay An Extra ${SumExtra}')
                    elif float(SumExtra) < float(0.00):
                        Change = (-1 * SumExtra)
                        print(f'Your Change Is ${Change}')
                print('Thank You For Coming To Cafe Au Lait. Enjoy Your Drinks.')
                print('')
            elif AmtPaid == TotalIncGST:
                print('Thank You For Coming To Cafe Au Lait. Enjoy Your Drinks.')
            else:
                print('Invalid Response Try Again')
        elif OrderType == 'take-away' or 'take away' or 'takeaway':
            print('this is a place keeper to alleviate errors for testing')
    elif Mode == 'daily report':
        print('this is a place keeper to alleviate errors for testing')
    else:
        print('Invalid Response Try Again')
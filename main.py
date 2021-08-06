print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
╭━━━╮   ╭━╮   ╭━━━╮   ╭╮      ╭╮
┃╭━╮┃   ┃╭╯   ┃╭━╮┃   ┃┃     ╭╯╰╮
┃┃ ╰╋━━┳╯╰┳━━╮┃┃ ┃┣╮╭╮┃┃  ╭━━╋╮╭╯
┃┃ ╭┫╭╮┣╮╭┫┃━┫┃╰━╯┃┃┃┃┃┃ ╭┫╭╮┣┫┃
┃╰━╯┃╭╮┃┃┃┃┃━┫┃╭━╮┃╰╯┃┃╰━╯┃╭╮┃┃╰╮
╰━━━┻╯╰╯╰╯╰━━╯╰╯ ╰┻━━╯╰━━━┻╯╰┻┻━╯
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                          ''')
a = 1

TotalEarnings = float(0.00)
TotalOrders = 0
TotalCap = 0
TotalEsp = 0
TotalLat = 0
TotalIcCof = 0
TotalDineIn = 0
TotalTakeAway = 0

EspShotPrc = float(0.60)
CapMilkPrc = float(0.15)
LatMilPrc = float(0.50)
IcCofMilkPrc = float(0.75)
IcCofIcCrmPrc = float(0.40)

CapPrc = float(3.00)
EspPrc = float(2.25)
LatPrc = float(2.50)
IcCofPrc = float(2.50)
while a == 1:
    Mode = input('Would you like to order or view the daily report (employee only)? ').lower()
    if Mode == 'order':
        print('')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('')
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
        print('')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('')
        CapNum = int(input('How Many Cappuccinos Would You Like? '))
        EspNum = int(input('How Many Espressos Would You Like? '))
        LatNum = int(input('How Many Lattes Would You Like? '))
        IcCofNum = int(input('How Many Iced Coffees Would You Like? '))
        OrderPrc = (CapNum * CapPrc) + (EspNum * EspPrc) + (LatNum * LatPrc) + (IcCofNum * IcCofPrc)
        OrderType = input('Would you like this order to be dine-in or take-away (keep in mind that a take-away order will incur an additional 5% surcharge)? ').lower()
        if OrderType == 'dine-in' or 'dine in' or 'dinein':
            TotalIncGST = "{:.2f}".format(OrderPrc * 1.1)
            print(f'''
{CapNum} Cappuccinos at ${"{:.2f}".format(CapNum * CapPrc)}
{EspNum} Espressos at ${"{:.2f}".format(EspNum * EspPrc)}
{LatNum} Lattes at ${"{:.2f}".format(LatNum * LatPrc)}
{IcCofNum} Iced Coffees at ${"{:.2f}".format(IcCofNum * IcCofPrc)}
    Total Price +GST: ${TotalIncGST}''')
            print('')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('')
            TotalIncGST = float(TotalIncGST)
            AmtPaid = float(input('How much have you paid? $'))
            if AmtPaid > TotalIncGST:
                Change = "{:.2f}".format(AmtPaid - TotalIncGST)
                print(f'Your Change Is ${Change}')
                print('Thank You For Coming To Cafe Au Lait. Enjoy Your Drinks.')
                print('')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
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
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('')
            elif AmtPaid == TotalIncGST:
                print('Thank You For Coming To Cafe Au Lait. Enjoy Your Drinks.')
                print('')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('')
            else:
                print('Invalid Response Try Again')
                print('')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('')
            TotalEarnings = TotalEarnings + TotalIncGST
            TotalOrders = TotalOrders + 1
            TotalCap = TotalCap + CapNum
            TotalEsp = TotalEsp + EspNum
            TotalLat = TotalLat + LatNum
            TotalIcCof = TotalIcCof + IcCofNum
            TotalDineIn = TotalDineIn + 1
        elif OrderType == 'take-away' or 'take away' or 'takeaway':
            TotalIncGST = "{:.2f}".format((OrderPrc * 1.1) * 1.05)
            print(f'''
{CapNum} Cappuccinos at ${"{:.2f}".format(CapNum * CapPrc)}
{EspNum} Espressos at ${"{:.2f}".format(EspNum * EspPrc)}
{LatNum} Lattes at ${"{:.2f}".format(LatNum * LatPrc)}
{IcCofNum} Iced Coffees at ${"{:.2f}".format(IcCofNum * IcCofPrc)}
    Total Price +GST: ${"{:.2f}".format(float(TotalIncGST))}''')
            print('')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('')
            TotalIncGST = float(TotalIncGST)
            AmtPaid = float(input('How much have you paid? $'))
            if AmtPaid > TotalIncGST:
                Change = "{:.2f}".format(AmtPaid - TotalIncGST)
                print(f'Your Change Is ${"{:.2f}".format(float(Change))}')
                print('Thank You For Coming To Cafe Au Lait. Enjoy Your Drinks.')
                print('')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('')
            elif AmtPaid < TotalIncGST:
                SumExtra = float("{:.2f}".format(TotalIncGST - AmtPaid))
                print(f'You Need To Pay An Extra ${"{:.2f}".format(SumExtra)}')
                while float(SumExtra) > float(0.00):
                    AmtPaid = float(input('How much have you paid? $'))
                    SumExtra = float("{:.2f}".format(SumExtra - AmtPaid))
                    if SumExtra > float(0.00):
                        print(f'You Need To Pay An Extra ${"{:.2f}".format(float(SumExtra))}')
                    elif float(SumExtra) < float(0.00):
                        Change = (-1 * SumExtra)
                        print(f'Your Change Is ${"{:.2f}".format(Change)}')
                print('Thank You For Coming To Cafe Au Lait. Enjoy Your Drinks.')
                print('')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('')
            elif AmtPaid == TotalIncGST:
                print('Thank You For Coming To Cafe Au Lait. Enjoy Your Drinks.')
                print('')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('')
            else:
                print('Invalid Response Try Again')
                print('')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('')
            TotalEarnings = TotalEarnings + TotalIncGST
            TotalOrders = TotalOrders + 1
            TotalCap = TotalCap + CapNum
            TotalEsp = TotalEsp + EspNum
            TotalLat = TotalLat + LatNum
            TotalIcCof = TotalIcCof + IcCofNum
            TotalTakeAway = TotalTakeAway + 1
    elif Mode == 'daily report':
        Code = input('What Is The Employee Code? ')
        if Code == 'Coffee6969':
            CoffeeSpend = EspShotPrc * (TotalCap + TotalEsp + TotalIcCof + TotalIcCof)
            MilkSpend = (TotalCap * CapMilkPrc) + (TotalLat * LatMilPrc) + (TotalIcCof * IcCofMilkPrc)
            IceCreamSpend = TotalLat * IcCofIcCrmPrc
            TotalSpend = CoffeeSpend + MilkSpend + IceCreamSpend
            print(f'''Daily Summary

Order Statistics:
    Number Of Orders            {TotalOrders}
    Number Of Coffees           {TotalCap + TotalEsp + TotalLat + TotalIcCof}

    Number Of Cappuccinos       {TotalCap}
    Number Of Espressos         {TotalEsp}
    Number Of Lattes            {TotalLat}
    Number Of Iced Coffees      {TotalIcCof}

Money
    Daily Earnings              ${"{:.2f}".format(TotalEarnings)}
    Coffee Spending             ${"{:.2f}".format(CoffeeSpend)}
    Milk Spending               ${"{:.2f}".format(MilkSpend)}
    Ice Cream Spending          ${"{:.2f}".format(IceCreamSpend)}
    Total profit                ${"{:.2f}".format(TotalEarnings - TotalSpend)}''')
            print('')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('')
        else:
            print('Wrong Code. Try Again')
            print('')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('')
    else:
        print('Invalid Response Try Again')
        print('')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('')
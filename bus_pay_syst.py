
passenger = int(input("how much you hold: \u20A6 "))
min_amt = 400
if passenger < min_amt:
    print('your money no reach, abeg trek')
else:
    seat = int(input("how many seats you dey pay for: "))
    bus_to_AF = 400 * seat


    if passenger < bus_to_AF:
        print('your money no reach, abeg trek')

    if passenger == bus_to_AF :
        print('welcom enjoy your ride')

    change= passenger - bus_to_AF
    
    if passenger > bus_to_AF :
        print (f'welcome, enjoy your ride \n your change is: \u20A6{change}')




 
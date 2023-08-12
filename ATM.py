while True:
    balance=10000
    print("  ATM  ")
    opt= int(input ('''
Enter Option:
1. Balance
2. Withdraw          
3. Deposit
4. Quit

        '''))
    
    if opt==1:
        print("Balance: Rs.",balance)

    elif opt==2:
        print("Balance: Rs.",balance)
        amt= float( input(" Enter Amount to be withdrawn: "))

        if amt>0:
            forewardbalance = balance-amt
            print("Remaining Balance: Rs.",forewardbalance)

        elif amt>balance:
            print(" Not sufficient balance ")
        
        else:
            print(" No withdrawl done ")
            print(" Your Balance: Rs.")
    
    if opt==3:
        print("Balance: Rs.",balance)
        depositamount= float(input(" Amount to be depoisted: Rs."))

        if depositamount>0:
            newbalance= balance+depositamount
            print(" New Balance: Rs.",newbalance)

        else:
            print(" No deposit made")
            print(" Your Balance: Rs.",balance)

    if opt==4:
        break
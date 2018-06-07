print('Welcome to ABC Bank ATM\n')
print('Please insert your card')
restart=('Y')
chances = 3
balance = 1000
while chances >= 0:
    while restart not in ('n','NO','no','N'):
        pin = int(input('\nPlease Enter You 4 Digit Pin: '))
        if pin == (1234):
            print('You entered your pin Correctly\n')

            print('-->Please Press 1 For Your Balance\n')
            print('-->Please Press 2 To Make a Withdrawl\n')
            print('-->Please Press 3 To Deposit\n')
            print('-->Please Press 4 to print monthly Statement\n')
            option = int(input('\nWhat Would you like to choose? '))
            if option == 1:
                print('Your Balance is Rs.',balance,'\n')
                restart = input('\nWould You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You for using ABC bank ATM')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? \nRs.10/Rs.20/Rs.40/Rs.60/Rs.80/Rs.100/Rs.500, for other enter 1: '))
                if withdrawl in [10, 20, 40, 60, 80, 100, 500]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now Rs.',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank you for using ABC Bank ATM')

                elif withdrawl != [10, 20, 40, 60, 80, 100, 500]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))

            elif option == 3:
                deposit = float(input('How Much Would You Like To Deposit? '))
                balance = balance + deposit
                print ('\nYour Balance is now Rs.',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank you for using ABC Bank ATM')
                    break
            elif option == 4:
                month = input('\nEnter the month name for which you want statement: ')
                if month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
                    print('\nPlease wait while your statement for', month, 'is being printed...\n')
                    print('Please collect your statement')
                    restart = input('\nWould You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('\n\nThank You for using ABC bank ATM')
                        break
                else:
                    print('\nEnter a valid Month name')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
        elif pin != ('1234'):
            print('Incorrect Password')
            chances = chances - 1
            if chances == 0:
                print('\nYou have reached maximum tries limit, please insert your card again.')
                break

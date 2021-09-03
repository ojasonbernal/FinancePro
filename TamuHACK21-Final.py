import test
import random
import csv


loop = True
while loop:
    print('Welcome To Finance Pro')
    print('Go pro or go Broke')
    print()
    print('Menu')
    print('*Enter "q" at any point for an input to quit.')

    def yes_or_no(answer):
        loop = True
        while loop:
            if answer.lower() != 'no' and answer.lower() != 'yes':
                print('Wrong input.')
                continue
            elif answer.lower() == 'no':
                loop = False
                print('Thank you and Goodbye.')
                exit()
            elif answer.lower() == 'yes':
                return 'main'
            else:
                continue

    def error_prompt_():
        loop = True
        while loop:
            error_prompt = input('Would you like to try again? (Enter yes/no): ')
            if error_prompt.lower() != 'no' and error_prompt.lower() != 'yes':
                print('Wrong input.')
                continue
            elif error_prompt.lower() == 'no':
                loop = False
                print('Thank you and Goodbye.')
                exit()
            elif error_prompt.lower() == 'yes':
                break
            else:
                continue

    def login():
        user_name = input('Please enter user name: ')
        count = 0
        for letter in user_name:  # removes unnecessary spaces users input with their name
            if count == 0:
                user_name = ''
            if letter != ' ':
                user_name += letter
                count += 1
        user_password = input('Please enter user password: ')
        user_info = []
        with open('user_database.csv', 'r+') as name_and_password:
            check_user = csv.reader(name_and_password, delimiter=',')
            for value in check_user:
                user_info.append(value)
        present = 0
        for list_info in user_info:
            if user_name.lower() == list_info[1].lower():
                if user_password == list_info[2]:
                    present = 1
                    print('Welcome', list_info[0], list_info[1])
                    while True:
                        print('1. Display account info \n2. Edit account info')
                        second_menu = input('Please input an option from above (input 1 or 2): ')
                        if second_menu != '1' and second_menu != '2':
                            print("Wrong input from menu. Please input 1 or 2")
                            error_prompt_()
                        elif second_menu == '1':
                            while True:
                                print()
                                user_id = input('Please input your Finance Pro ID number: ')
                                if len(user_id) == 6:
                                    try:
                                        fp_id = int(user_id)
                                        break
                                    except:
                                        print(
                                            'Wrong input for ID number. Acceptable input is a 6-digit number.')
                                        error_prompt_()
                            if user_id == list_info[6]:
                                print('Name:', list_info[0] + ' ' + list_info[1], '\nD.O.B:', list_info[3],
                                      '\nFinance Pro ID No:', list_info[6], '\nEmail Address:', list_info[7],
                                      '\nYour loan amount from', list_info[9], 'is:', list_info[8],
                                      '\nHourly wage:', list_info[10], '\nPay after 4 weeks:', list_info[11])
                                print('It will take you', float(list_info[8])/float(list_info[12]),
                                      'months to pay of the loan.')
                                break
                        elif second_menu == '2':
                            print()
                            while True:
                                print('1. Change Email \n2. Change Password \n3. Change First or Last Name or Both')
                                menu_3 = input('Please input an option from above (1, 2 or 3): ')
                                if menu_3 != '1' and menu_3 != '2' and menu_3 != '3':
                                    print("Wrong input from menu. Please input 1, 2 or 3")
                                    error_prompt_()
                                else:
                                    break
                            if menu_3 == '1':
                                old_email = input('Please enter old email: ')
                                if old_email == list_info[7]:
                                    loop = True
                                    new_email = None
                                    while loop:
                                        new_email = input("Enter your new email: ")
                                        for character in new_email:
                                            if character == '@':
                                                loop = False
                                                break
                                            else:
                                                continue
                                        if loop:
                                            print('Wrong input for email. Valid input must include @ sign.')
                                            error_prompt_()
                                    list_info[7] = new_email
                                    choice = False
                                    print()
                                    while True:
                                        print('1. Previous Menu \n2. Main Menu')
                                        menu_option = input('Please input your choice from above (1 or 2): ')
                                        if menu_option != '1' and menu_option != '2':
                                            print("Wrong input from menu. Please input 1 or 2")
                                            error_prompt_()
                                        elif menu_option == '1':
                                            choice = False
                                            break
                                        else:
                                            choice = True
                                            break
                                    if choice:
                                        break

                        else:
                            break
                    break
                else:
                    continue
            else:
                continue
        if present == 0:
            print('Your information does not match our records')
        else:
            return 'valid'


    def signup():
        with open("user_database.csv", "a") as file:
            user_name = input("Enter first name: ")
            if user_name.lower() == 'q':
                exit()
            user_last = input("Enter last name: ")
            if user_last.lower() == 'q':
                exit()
            user_password = input("Enter your Password: ")

            dob = True
            while dob:
                user_dob = input("Enter your DOB(EX:01/19/1997): ")
                month = 0
                day = 0
                year = 0
                try:
                    month = int(user_dob[0: 2])
                    day = int(user_dob[3: 5])
                    year = int(user_dob[6:])
                except:
                    print('Wrong input for date of birth. Please input in the correct format.')
                    error_prompt_()
                if month <= 12 and day <= 31 and 2010 >= year >= 1900 \
                        and user_dob[2] == '/' and user_dob[5] == '/':
                    break
                else:
                    continue
            while True:
                user_ssn = input("Enter your SSN (9-digit number): ")
                if len(user_ssn) == 9:
                    try:
                        ssn = int(user_ssn)
                        break
                    except:
                        print('Wrong input for Social Security Number. Acceptable input is a 9-digit number.')
                        error_prompt_()
                else:
                    print('Wrong input for Social Security Number. Acceptable input is a 9-digit number.')
                    error_prompt_()
            while_loop = True
            while while_loop:
                dl = input('Please enter your state drivers number (8-digit number): ')
                if len(dl) == 8:
                    try:
                        drivers_l = int(dl)
                        break
                    except:
                        print('Wrong input for Drivers License. Acceptable input is an 8-digit number.')
                        error_prompt_()
            loop = True
            while loop:
                user_email = input("Enter your email: ")
                for character in user_email:
                    if character == '@':
                        loop = False
                        break
                    else:
                        continue
                if loop:
                    print('Wrong input for email. Valid input must include @ sign.')
                    error_prompt_()

            user_acct_number = random.randint(100000, 900000)
            while True:
                try:
                    present_loans = float(input('Please input the amount of loans you have: '))
                    pay_hour = float(input('Please enter hourly wage: '))
                    hours_works = float(input('Please enter weekly work hours: '))
                    monthly_payment = float(input('Please enter your monthly payment: '))
                    break
                except:
                    print('Wrong input for loan, company, hourly wage or weekly hours. Please enter double check.')
                    error_prompt_()
            loan_company = input('Please enter the company that issued you the loan: ')

            storage = [user_name, user_last, user_password, user_dob, str(ssn), str(drivers_l), str(user_acct_number),
                       user_email, str(present_loans), loan_company, str(pay_hour), str(hours_works),
                       str(monthly_payment)]
            num = 0
            for item in storage:
                file.write(item)
                if num < len(storage)-1:
                    file.write(',')
                    num += 1
            file.write('\n')
            print('Your user generated ID is:', user_acct_number)


    sign_up_log_in = None
    try_again = True
    while try_again:
        try_again = True
        sign_up_log_in = input("If signing up enter S if logging in enter L: ")
        if sign_up_log_in.lower() == 'q':
            exit()
        if sign_up_log_in.lower() != 's' and sign_up_log_in.lower() != 'l':
            print('Wrong input')
            error_prompt_()
        else:
            break

    if sign_up_log_in.lower() == 'l':
        login()
    elif sign_up_log_in.lower() == 's':
        signup()
    menu = input('Return to Main Menu? (Enter yes or no): ')
    question = yes_or_no(menu)
    if question == 'main':
        print()
        print()
        continue
    else:
        print('Thank you and goodbye.')
        break












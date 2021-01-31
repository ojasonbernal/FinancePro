# from user import User
import  random
import csv
print('Welcome To Finance Pro')
print('Go pro or go Broke')
print()
print('Menu')
sign_up_log_in = None
try_again = True
while try_again:
    try_again = True
    sign_up_log_in = input("If signing up enter S if logging in enter L: ")
    if sign_up_log_in.lower() != 's' and sign_up_log_in.lower() != 'l':
        print('Wrong input')
        while try_again:
            try_again_prompt = input('Would you like to try again? (Enter yes/no): ')
            if try_again_prompt.lower() != 'no' and try_again_prompt.lower() != 'yes':
                print('Wrong input.')
                continue
            elif try_again_prompt.lower() == 'no':
                try_again = False
                break
            elif try_again_prompt.lower() == 'yes':
                break
            else:
                continue
    else:
        break


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
        user_last = input("Enter last name: ")
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
        while_loop = True
        while while_loop:
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
        storage = [user_name, user_last, user_password, user_dob, str(ssn), str(drivers_l), str(user_acct_number),
                   user_email]
        num = 0
        for item in storage:
            file.write(item)
            if num < len(storage)-1:
                file.write(',')
                num += 1


if sign_up_log_in.lower() == 'l':
    login()
elif sign_up_log_in.lower() == 's':
    signup()
else:
    print('Thank you, goodbye.')









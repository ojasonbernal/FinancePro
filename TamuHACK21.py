from user import User
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
        user_name = input("Enter name: ")
        user_last = input("Enter Last name: ")
        user_password = input("Enter your Password: ")
        user_dob = (input("Enter your DOB(EX:01/19/1997): "))
        user_ssn = int(input("Enter your SSN: "))
        user_i_d = int(input("Enter your id: "))
        user_email = input("Enter your email: ")
        user_acct_number = random.randint(100, 300)
        storage = [user_name,user_last,user_password,user_dob,str(user_ssn),str(user_i_d),str(user_acct_number), user_email, user_password]
        num = 0
        for item in storage:
            file.write(item)
            if num < len(storage)-1:
                file.write(',')
                num += 1
        file.write("\n")


if sign_up_log_in.lower() == 'l':
    login()
elif sign_up_log_in.lower() == 's':
    signup()
else:
    print('Thank you, goodbye.')









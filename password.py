# password strength checker

# length>8,digit,upper case,lower case,special characters

import re


def psc(password):
    if len(password) < 8:
        return "Weak:password must contain atleast 8 characters."
    elif not any(char.isdigit() for char in password):
        return "Weak: password must contain atleast one number"
    elif not any(char.isupper() for char in password):
        return "Weak : password must contain atleast one upper case alphabet"
    elif not any(char.islower() for char in password):
        return "Weak: password must contain atleast one lower case alphabate"
    elif not re.search(r'[!@#$%^&*(){}]', password):
        return "Weak: password must contain atleast one special characture"
    return 'strong : your password is secured..'


def check():
    print("create your password..")

    while True:
        password = input("enter password or type 'exit' to quit : ")
        if password.lower() == 'exit':
            print('Thank You')
            break
        result = psc(password)
        print(result)


check()

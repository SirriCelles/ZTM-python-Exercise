# password should be atleast 8 characters long
# it should contain any sort of letters and numbers and $%#@

import re

# regex = r"(^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$%#])[A-Za-z\d@$#%]{8,}$)"

regex2 = r"([A-Za-z0-9$%#@]{7,}[0-9])"
pattern = re.compile(regex2)


def pwd_validation(pwd):
    if pattern.fullmatch(pwd):
        print("Password Valid")
        return True
    else:
        print("Password Invalid \n")
        print('''
               Password must atleast 8 characters long
               must contain uppercase letter
               must contain special characters
               must end with a number
               ''')
        return  False



if __name__ == '__main__':
    while True:
        pwd = input("Please Enter Your password: ")
        if pwd_validation(pwd):
            break

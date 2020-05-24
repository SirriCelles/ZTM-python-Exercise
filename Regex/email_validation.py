# Python program to validate email
import re

pattern = re.compile(r"(^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$)")


def validate_email(email):
    if pattern.search(email):
        print("Email Valid")
        return True
    else:
        print("Invalid Email")
        return False

if __name__ == '__main__':
    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break



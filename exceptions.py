# Error Handling
while True:
    try:
        age = int(input('What is your age'))
        # print(age)
        print(age / 12)
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print('Enter age higher than zero')
    else:
        print('Thank you')
        break
    finally:
        print('ok, I am finally done')


# example two

def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum(1, '3'))
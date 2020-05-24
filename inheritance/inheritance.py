# this is a class to demonstrate the concept of inheritance


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Your are logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with the power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: Arrows left - {self.num_arrows} arrows")


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Arrow', 500, 'arrow@gmail.com')
print(wizard1.email)
print((archer1.email))
wizard1.attack()
wizard1.sign_in()
archer1.attack()
archer1.sign_in()


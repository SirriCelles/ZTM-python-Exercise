# OOP
class PlayerCharacter:
    # class object attribute, unlike class attributes this is static and not dynamic
    # used when theres no change. going to be true for instances of this class
    membership = True

    # __init__ a dunder or magic method. used at the top when building a class.
    # it also refers to the constructor method. it is called automatically when the class is instantiated
    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self._name = name  # attributes
            self._age = age

    def shout(self):
        print(f'my name is {self._name} and I am {self._age}')
        return 0

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


# creating an object from the above class
# player1 = PlayerCharacter('sirrie', 4)
player2 = PlayerCharacter('Nasah', 21)
player2.name = 'new name'
player2.shout = 'BOOOO'

# print(player2.name, player2.membership)
print(PlayerCharacter.adding_things(2, 3))
# player1.shout()
# player2.shout()
print(player2.shout)




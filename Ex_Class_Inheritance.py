class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('no weapon, do nothing')


class Wizard(User):  # Wizard inherit the User class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):  # this attack function overrides that of the parent class
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):  # Archer inherit the User class
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):  # this attack function overrides that of the parent class
        print(f'attacking with {self.arrows} arrows')


wiz1 = Wizard('Merlin', 50)
arch1 = Archer('Robin', 100)
wiz1.sign_in()
arch1.sign_in()
wiz1.attack()
arch1.attack()

print(isinstance(wiz1, Wizard))
print(isinstance(wiz1, User))
print(isinstance(wiz1, object))

for obj in [wiz1, arch1]:
    obj.attack()

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    # def attack(self):
    #     print('no weapon, do nothing')


class Wizard(User):  # Wizard inherit the User class
    def __init__(self, name, power, email):
        self._name = name
        self._power = power
        User.__init__(self, email)

    def attack(self):  # this attack function overrides that of the parent class
        # User.attack(self)
        print(f'attacking with power of {self._power}')


class Archer(User):  # Archer inherit the User class
    def __init__(self, name, arrows, email):
        self.name = name
        self.arrows = arrows
        # super() is the same as calling the parent User, but allows to omit the self paramter in the parent function
        super().__init__(email)

    def attack(self):  # this attack function overrides that of the parent class
        print(f'attacking with {self.arrows} arrows')


wiz1 = Wizard('Merlin', 50, 'merlin@email.com')
arch1 = Archer('Robin', 100, 'Robin@email.com')
wiz1.sign_in()
arch1.sign_in()
wiz1.attack()
arch1.attack()

# check the class of an obj
print(isinstance(wiz1, Wizard))
print(isinstance(wiz1, User))
print(isinstance(wiz1, object))

for obj in [wiz1, arch1]:
    obj.attack()

print(arch1.email)

# introspection of an object
print(dir(wiz1))

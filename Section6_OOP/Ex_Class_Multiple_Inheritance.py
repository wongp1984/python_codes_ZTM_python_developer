class User():

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):  # Wizard inherit the User class
    def __init__(self, name, power, email):
        self._name = name
        self._power = power

    def attack(self):  # this attack function overrides that of the parent class
        print(f'attacking with power of {self._power}')


class Archer(User):  # Archer inherit the User class
    def __init__(self, name, arrows, email):
        self.name = name
        self.arrows = arrows
        # super() is the same as calling the parent User, but allows to omit the self paramter in the parent function
        super().__init__(email)

    def attack(self):  # this attack function overrides that of the parent class
        print(f'attacking with {self.arrows} arrows')

    def run(self):
        print('Run as fast as you can!')


class HybridBrog(Wizard, Archer):
    def __init__(self, name, power, arrows, email):
        Archer.__init__(self, name, arrows, email)
        Wizard.__init__(self, name, power, email)


# instantiate the hybrid
hb1 = HybridBrog('Borgie', 50, 88, 'Borgie@email.com')
hb1.run()
hb1.attack()

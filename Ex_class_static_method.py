class PlayChar:
    membership = False

    def __init__(self, name='anaynoums', age=0):
        # the underscore character denotes that the variable is a private and should not be accessible from outside.
        self._name = name
        self._age = age

    def run(self):
        print('run!! ' + self.name)
        print('Your age is ' + str(self.age))

    def checkmember(self, greeting):
        if self.membership:
            print(f'{greeting} I am member')
        else:
            print(f'{greeting} I am NOT member')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')

    def ReturnSelf(self):
        return self

    @classmethod
    def CreatePlayer(cls, name, age):
        return cls(name, age)  # instantiate the self class and return

    @staticmethod
    def SimpleStaticFunc(name, age):
        print("Hi I am a static method")


player1 = PlayChar('AKss', 42)

PlayChar.SimpleStaticFunc('Dummy', 88)

player3 = PlayChar.CreatePlayer('Kate', 38)

print(player3._name)

print(player1.ReturnSelf().ReturnSelf().ReturnSelf())


# player1.run()
# player1.name = 'Mama'
# print(player1.membership)

# player1.abc = True
player1.checkmember('Good morning')
player1.membership = False
print(player1.membership)
print(PlayChar.membership)

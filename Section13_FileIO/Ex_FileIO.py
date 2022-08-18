

myfile = open('test.txt')

print(myfile.read())
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(myfile.readline())

myfile.seek(0)
print(myfile.readlines())

myfile.close()

print('using the with open method does not need to close the file')
with open('test.txt', mode='a+') as myfile:
    myfile.write('\n')
    text = myfile.write('Hey it is me')
    myfile.seek(0)
    print(myfile.readlines())

try:
    with open('sad.txt', mode='r') as myfile:
        print(myfile.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err

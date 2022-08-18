from translate import Translator

translator= Translator(to_lang="zh")

srcfile = input('Please input the file name for translation: ')
 

try:
    with open(srcfile, mode='r') as myfile:
        srctext=myfile.readlines()
        for statement in srctext:
            translation = translator.translate(statement)
            print(f'{statement.strip()} => {translation}')
except FileNotFoundError as err:
    print(f'{srcfile} does not exist!')
else:
    pass
finally:
    pass


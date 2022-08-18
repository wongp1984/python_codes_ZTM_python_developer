import random
import sys

def PromptUserInput(st, en):
    re =  None
    re = input(f'>>>>Please guess a number between {st} and {en}: ')
    try:
        re = int(re)

        if (re not in range(st,en)):
             print('Incorrect type.  Please input integers only.')
             re = 'Input is not in range.'
    except (ValueError) as err:
        print('Incorrect type.  Please input integers only.')
        re = err
    
    return re

if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    ans = random.choice(range(start, end))
   
    reply = None
    while reply != ans:
        reply = PromptUserInput(start, end)
        if reply == ans:
            print('Bingo!! You win.')
            break
        else:
            print('Please try again.')
            print('')

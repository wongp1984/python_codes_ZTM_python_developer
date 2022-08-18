'''Hello 123'''

import random
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
ans = random.choice(range(start, end))


reply = -1
while reply != ans:
    reply = input(f'Please guess a number between {start} and {end}: ')
    try:
        reply = int(reply)
    except (ValueError) as err:
        print('Incorrect type.  Please input integers only.')

    if reply == ans:
        print('Bingo!! You win.')
        break
    else:
        print('Please try again.')

import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install('pyjokes')

import pyjokes
joke = pyjokes.get_jokes('en', 'neutral')
print(joke)

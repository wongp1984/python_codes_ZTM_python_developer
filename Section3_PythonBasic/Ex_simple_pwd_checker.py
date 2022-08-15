import getpass
 
strusername = input('Please input your user name: ')

strpwd = getpass.getpass(prompt='Please input your password: ')  # not echo the password for security

strmaskedpwd = 'X'*len(strpwd)

print(f'{strusername}, you password {strmaskedpwd} has {len(strpwd)} characters.')
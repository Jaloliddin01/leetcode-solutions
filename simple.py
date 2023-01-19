import os

if os.path.exists('test.py'):
    os.remove('test.py')
else:
    print('such file does not exist')


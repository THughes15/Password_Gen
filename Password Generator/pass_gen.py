#Random Password Generator

import random, sys, pyperclip

print()
print('Password Generator')
print('------------------')

lower = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '1234567890'
special = '!"£$%^&*()'
chars = ''

ans = 'Y'
while ans in ['Y', 'y']:

    chars = lower

    print()
    length = input('How many characters do you want your password to be?: ')
    length = int(length)
    print()

    caps_q = ''
    while caps_q not in ['Y', 'y', 'N', 'n']:
        caps_q = input('Do you want the password to contain capitals? (Y/N): ')
        if caps_q in ['Y', 'y']:
            chars = chars + caps
        elif caps_q in ['N', 'n']:
            pass
        else:
            print()
            print('Error: That is not a valid input, please enter Y/N')

    nums_q = ''
    while nums_q not in ['Y', 'y', 'N', 'n']:
        nums_q = input('Do you want the password to contain numbers? (Y/N): ')
        if nums_q in ['Y', 'y']:
            chars = chars + nums
        elif nums_q in ['N', 'n']:
            pass
        else:
            print()
            print('Error: That is not a valid input, please enter Y/N')

    special_q = ''
    while special_q not in ['Y', 'y', 'N', 'n']:
        special_q = input('Do you want the password to contain special characters? (Y/N): ')
        if special_q in ['Y', 'y']:
            chars = chars + special
        elif special_q in ['N', 'n']:
            pass
        else:
            print()
            print('Error: That is not a valid input, please enter Y/N')

    while ans in ['Y', 'y']:
        print()
        print('Password:')

        password = ''
        for char in range(length):
            password += random.choice(chars)
        print(password)

        print()
        ans = ''
        while ans not in ['Y', 'y', 'N', 'n']:
            print()
            ans = input('Do you want to change the password? (Y/N): ')
            if ans in ['Y', 'y']:
                pass
            elif ans in ['N', 'n']:
                pass
            else:
                print()
                print('Error: That is not a valid input, please enter Y/N')

    copy = ''
    while copy not in ['Y', 'y', 'N', 'n']:
        print()
        copy = input('Do you want to copy password to clipboard? (Y/N): ')
        if copy in ['Y', 'y']:
            pyperclip.copy(password)
            print('Password copied to clipboard.')
        elif copy in ['N', 'n']:
            pass
        else:
            print()
            print('Error: That is not a valid input, please enter Y/N')

    ans = ''
    while ans not in ['Y', 'y']:
        print()
        ans = input('Do you want to generate another password? (Y/N): ')
        if ans in ['Y', 'y']:
            pass
        elif ans in ['N', 'n']:
            print('Okay, Goodbye!')
            sys.exit()
        else:
            print()
            print('Error: That is not a valid input, please enter Y/N')
        

    


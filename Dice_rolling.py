import random

def rolling():

    flag = input('Would you like to roll the dice [y/n]?\n')

    while flag != 'n':
        if flag == 'y':
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(die1, die2)
            flag = input('Would you like to roll the dice [y/n]?\n')
        elif flag == 'n':
            print('Good-bye!')
            break

        else:
            print('Invalid response. Please type "y" or "n".')
            flag = input('Would you like to roll the dice [y/n]?\n')   

rolling()


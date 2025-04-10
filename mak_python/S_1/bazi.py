import random

win_number = random.randint(1 , 99)

my_number = int(input('please guess my win number: '))


while my_number != win_number:
    if my_number > win_number:
        print('guess a smaller than this!')
    else:
        print('guess a bigger than this!')
    my_number = int(input('please guess my win number: '))
    
print('******** YES ! you win ********')
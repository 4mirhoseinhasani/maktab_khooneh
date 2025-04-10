import random

min_choice = 1
max_choice = 100
name = input('what is your name? ')

if name == '':
        print('ok! i call you Unknown! ')
        name = 'Unknown'

computer_choice = random.randint(1,99)
print(name, 'my first choice is :', computer_choice)
choice = input("Is it bigger or smaller? Please answer with 'b' and 'k' \n" "and if i win please type 'd' : ")


while choice != 'd':
    if choice == 'b':
        min_choice = computer_choice
        computer_choice = random.randrange(min_choice,max_choice)
        print('my choice is :', computer_choice)
        #print('min choice is: ',min_choice)
        #print('max choice is: ',max_choice)
        choice = input("press 'b' or 'k' or 'd' : ")
    elif choice == 'k':
        max_choice = computer_choice
        computer_choice = random.randrange(min_choice,max_choice)
        print('my choice is :', computer_choice)
        #print('min choice is: ',min_choice)
        #print('max choice is: ',max_choice)
        choice = input("press 'b' or 'k' or 'd' : ")
    else:
        print("please give me a valid answer! (beatween 'b' or 'k' or 'd'): ")
        choice = input("press 'b' or 'k' or 'd' : ")

print('**********************************************************************\n'
      '\n'
      '****** Hey! I finally found it! I can read you mind',name,'! ************\n'
      '\n'
      '**********************************************************************\n')
        

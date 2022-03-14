import random

# enter a letter, r p or s
# rps = input('Enter R, P or S: ')

# assigning a number to the input and also telling user what they have chosen
def choose():
    rps = input('Enter R, P or S: ').upper()
    if rps == 'R':
        assign_number = 0
        print('You have chosen Rock')
    elif rps == 'P':
        assign_number = 1
        print('You have chosen Paper')
    elif rps == 'S':
        assign_number = 2
        print('You have chosen Scissors')
    else:
        print('Error')
    return assign_number

# generating a random number for computer decision
def selection():
    computer = random.randint(0, 2)
    if computer == 0:
        print('Computer chose Rock')
    elif computer == 1:
        print('Computer chose Paper')
    else:
        print('Computer chose Scissors')
    return computer

def game (user_selection, computer_selection):
    if user_selection == computer_selection:
        print('You have drawn')
    elif user_selection == 0 and computer_selection == 2:
        print('You have Won!')
    elif user_selection == 1 and computer_selection == 0:
        print('You have Won!')
    elif user_selection == 2 and computer_selection == 1:
        print('You have Won!')
    else:
        print('You lost!')

print(game(choose(), selection() ))

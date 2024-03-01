import random 
player = input('Player Name: ')

print(f"Hey {player}! Let's play ROCK PAPER SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    while True:
        user_choice = input('Enter your move: \n\tROCK: r\n\tPAPER: p\n\tSCISSORS: s\n\tQUIT: q\n')
        
        if user_choice == 'r':
            print('ROCK versus ', end='')
            break # ends the loop statement
        elif user_choice == 'p':
            print('PAPER versus ', end='')
            break
        elif user_choice == 's':
            print('SCISSORS versus ', end='')
            break
        elif user_choice == 'q':
            exit() # end of program
        else:
            print('Wrong choice. Try again')
            

    n = random.randint(1,3)

    if n == 1:
        comp_choice = 'r'
        print('ROCK')
    elif n == 2:
        comp_choice = 'p'
        print('PAPER')
    else:
        comp_choice = 's'
        print('SCISSORS')

    if user_choice == comp_choice:
        print("It's a tie")
        ties += 1
    elif user_choice == 'r' and comp_choice =='p':
        print('You loose')
        losses += 1
    elif user_choice == 'r' and comp_choice =='s':
        print('You win')
        wins += 1
    elif comp_choice == 'r' and user_choice =='p':
        print('You win')
        wins += 1
    elif comp_choice == 'r' and user_choice =='s':
        print('You loose')
        losses += 1
    elif comp_choice == 's' and user_choice =='p':
        print('You loose')
        losses += 1
    elif comp_choice == 'p' and user_choice =='s':
        print('You win')
        wins += 1
    print('\n ---- END ---- \n\n')

import random, sys



def main():

    wins = 0
    losses = 0
    ties = 0


    print("""Rock/Paper/Scissors is a hand game originating from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). "Scissors" is identical to the two-fingered V sign (also indicating "victory" or "peace") except that it is pointed horizontally instead of being held upright in the air.
        
        
    Rules: Enter in R for (R)ock, P for (P)apper, and S for (S)cissors
    Paper beats Rock,
    Scissors beats Paper
    Rock beats Scissors""")

    while True:
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')
        while True:
            print('Enter your move Enter in R for (R)ock, P for (P)apper, S for (S)cissors or Q for (Q)uit')
            
            playerMove = input().upper()
            
            if playerMove == 'Q':
                sys.exit()
            if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
                break
            print('Input is invalid. Please type r, p, s, or q. Then press enter to continue.')

        if playerMove == 'R':
            print('Rock versus...')
        if playerMove == 'P':
            print('Paper versus...')
        if playerMove == 'S':
            print('Scissors versus...')

        randomNumber = random.randint(1,3)

        if randomNumber == 1:
            computerMove = 'R'
            print('Rock')
        if randomNumber == 2:
            computerMove = 'P'
            print('Papper')
        if randomNumber == 3:
            computerMove = 'S'
            print('Scissor')

        
        if playerMove == 'R' and computerMove == 'S':
            print('Player crushed this wins!')
            wins += 1
        elif playerMove == 'S' and computerMove == 'P':
            print('Player is cutting out the competition!')
            wins += 1
        elif playerMove == 'P' and computerMove == 'R':
            print('Player has wrapped up the win!')
            wins += 1
        elif computerMove == 'R' and playerMove == 'S':
            print('Computer crushed this wins!')
            losses += 1
        elif computerMove == 'S' and playerMove == 'P':
            print('Computer is cutting out the competition!')
            losses += 1
        elif computerMove == 'P' and playerMove == 'R':
            print('Computer has wrapped up the win!')
            losses += 1
        else:
            print('It\'s a Tie! Play again!')
            ties += 1

if __name__ == '__main__': 
    main()
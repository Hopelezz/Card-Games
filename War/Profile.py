import sys

def getStats(money, gamesWon, gamesLost):
    money = 5000
    gamesWon = 0
    gamesLost = 0
    return money, gamesWon, gamesLost

def getFirstBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True: #Keep asking until they enter a valid amount.
        print(f'How much do you bet? (1-{maxBet}, or (Q)UIT)')
        
        bet = input('> ').upper().strip()
        
        if bet == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue #If the player didn't enter a number, ask again.

        bet = int(bet)
        
        if 1 <= bet <= maxBet:
            return bet #Player entered a valid bet.

def getSecondBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True: #Keep asking until they enter a valid amount.
        print(f'How much do you bet? (1-{maxBet}, (M)ax Bet, or QUIT)')
        
        bet = input('> ').upper().strip()
        
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif bet == 'M':
            bet = int(maxBet)
            return bet

        if not bet.isdecimal():
            continue #If the player didn't enter a number, ask again.

        bet = int(bet)
        
        if 1 <= bet <= maxBet:
            return bet #Player entered a valid bet.

def getMove(playerHand, money):
    while True:
        moves = ['(S)tand']
        
        if money > 0:
            moves.append('(D)ouble down')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('S'):
            return move #player has entered a valid move.
        if move == 'D' or 'M' and '(D)ouble down' in moves:
            return move
"""Blackjack, also known as 21.
 This version doesn't have splitting or insurance"""
import random, sys

#setup the constants:
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    print(''' Blackjack

    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards
        On your first play you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.
    ''')

    money = 5000
    while True: #Game loop
        if money <= 0:
            print("You are broke!")
            print('Good thing you weren\'t playing with real money!')
            print('Thanks for playing!')
            sys.exit()

        print(f'Money: {money}')
        bet = getBet(money)

        deck = getDeck() #Sets dealers and players hands
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print(f'Bet: {bet}')
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move =='D':
                #player is doubling down, they can increase their bet
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}')
                print(f'Bet: {bet}')

            if move in ('H', 'D'):
                #if H / D take another card
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}')
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue #The player buested

            if move in ('S', 'D'): #Stand/Doubling down stops on players turn
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('The dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break #The dealer busted
                input('Press Enter to continue...')
                print('\n\n')

        #Show the final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        #Determine if player or dealer won:
        if dealerValue > 21:
            print(f'Dealer Busts! You win ${bet}')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue> dealerValue:
            print(f'You won ${bet}')
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you')

        input('Press Enter to continue...')
        print('\n\n')

def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True: #Keep asking until they enter a valid amount.
        print(f'How much do you bet? (1-{maxBet}, or QUIT)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue #If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet #Player entered a valid bet.


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) #Add the numbered Cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) #Add the face and ace cards.
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first
    card if showDealerHand is False.
    """
    print()
    if showDealerHand:
        print(f'DEALER: {getHandValue(dealerHand)}')
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        #Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    print(f'PLAYER: {getHandValue(playerHand)}')
    displayCards(playerHand)

def getHandValue(cards):
    """Return the value of the cards. Face cards are worth 10,
    aces are worth 11 or 1 (This function picks the most suitable ace value).
    """
    value = 0
    numberOfAces = 0

    #Add the value fo the non-ace cards:
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): #Face cards are worth 10 points.
            value += 10
        else: 
            value += int(rank) # Numbered cards are worth their numbered
    #Add the value for the aces:
    value += numberOfAces #Add 1 per ace.
    
    for i in range(numberOfAces):
        #If another 10 can be added with busting do so:
        if value + 10 <= 21:
            value += 10

    return value

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', ''] #The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___  ' #Print the top line of the card.
        if card == BACKSIDE:
            #Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            #print the card's front:
            rank, suit = card # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows: #Print each row on the screen:
        print(row)

def getMove(playerHand, money):
    # Asks the playerr for their move, and returns
    # 'H' for hit
    # 'S' for stnad
    # 'D' for double down.
    while True: #keep looping until the player enters a correct move.
        moves = ['(H)it', '(S)tand']

    #the player can double down on their first move, which we can
    #tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        #get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move #player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move #Player has entered a valid move.

#If the program is run (instead of imported), run the game:
if __name__ == '__main__': main()
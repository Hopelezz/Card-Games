import random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) #Add the numbered Cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) #Add the face and ace cards.
    random.shuffle(deck)
    return deck

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', ''] #The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___ ' #Print the top line of the card.
        if card == BACKSIDE:
            #Print a card's back:
            rows[1] += '|#  | '
            rows[2] += '|###| '
            rows[3] += '|__#| '
        else:
            #print the card's front:
            rank, suit = card # The card is a tuple data structure.
            rows[1] += f'|{rank}  | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|__{rank}| '

    for row in rows: #Print each row on the screen:
        print(row)

def displayHands(playerHand, dealerHand, showDealerHand):
    """Shows players hand. Hides dealers card if dealerHand is False otherwise shows.
    """
    print()
    if showDealerHand:
        print(f'DEALER: {getHandValue(dealerHand)}')
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        #Hide the dealer's first card:
        displayCards([BACKSIDE])
    print(f'PLAYER: {getHandValue(playerHand)}')
    displayCards(playerHand)

def getHandValue(cards):
    """Return the value of the cards. Number cards are worth their Value.
    Face cards are worth J = 11, Q = 12, K = 13.
    Aces cards are worth 1.
    """
    value = 0
    
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            value += 1
        elif rank == 'K': #Face cards are worth 10 points.
            value += 13
        elif rank == 'Q':
            value += 12
        elif rank == 'J':
            value += 11
        else: 
            value += int(rank) # Numbered cards are worth their numbered
    return value

import sys
import Deck
import Profile

def main():
    print('''War by BlackSkies Inc.
    Goal: Bet on the odds of having the higher card. 
    
    Rules:
        Bet before you see your card and then choose to (D)ouble Down or (S)tand
        Play for 26 rounds. If you win more rounds then recieve a bonus payout.
    ''')
    money = 5000

    while True:
        if money <= 0:
            print('Looks like you\'re broke')
            sys.exit()

        games = 1
        win = 0
        lose = 0
        deck = Deck.getDeck()
        
        while games <= 26: #When you reach 26 games the loop ends
            print(f'Money: {money}')
            print(f'Games: {win}(wins)/{lose}(lose).') 
            print(f'{games}/26 rounds.')
            print(f'Cards in deck: {len(deck)}')
            
            bet = Profile.getFirstBet(money)
            print(f'Bet: {bet}')

            dealerHand = [deck.pop()]
            playerHand = [deck.pop()]
            
            while True:
                Deck.displayHands(playerHand, dealerHand, False)
                print()
                
                move = Profile.getMove(playerHand, money - bet)

                if move == 'S':
                    break
                if move == 'D' or 'M':
                    additionalBet = Profile.getSecondBet(min(bet, (money - bet)))
                    bet += additionalBet
                    print(f'Bet increased to {bet}')
                    print(f'Bet: {bet}')
                    break
            
            Deck.displayHands(playerHand,dealerHand, True)

            playerValue = Deck.getHandValue(playerHand)
            dealerValue = Deck.getHandValue(dealerHand)

            if playerValue > dealerValue:
                print(f'You won ${bet}!')
                money += bet
                win += 1
            elif playerValue < dealerValue:
                print(f'You lost ${bet}!')
                money -= bet
                lose += 1
            elif playerValue == dealerValue:
                print(f'It\'s a tie, the {bet} is returned to you')

            input('Press Enter to continue...')
            print('\n\n')
            games += 1

        if games >= 26 and win >= lose:
            money += 2500
            print('You won the War!')
            print('Payout bonus: $2500!')
            
        else:
            print(f'Sorry you lost the war {win}(wins) & {lose}(lose).')

        
if __name__ == '__main__': 
    main()
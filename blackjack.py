import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        return f'{self.value} of {self.suit}'

    def get_value(self):
        return self.value


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for card in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
            for val in range(1, 14):
                if val == 1:
                    self.cards.append(Card(card, 'Ace'))
                elif val == 11:
                    self.cards.append(Card(card, 'Jack'))
                elif val == 12:
                    self.cards.append(Card(card, 'Queen'))
                elif val == 13:
                    self.cards.append(Card(card, 'King'))
                else:
                    self.cards.append(Card(card, val))

    def show(self):
        for card in self.cards:
            print(card.show())

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw(self):
        return self.cards.pop()


class Player:

    def __init__(self, n, bal=500):
        self.name = n
        self.balance = bal
        self.card = []
        self.bet = 0

    def place_bet(self):
        amount = int(input(f'Place your bet {self.name}: $'))
        while amount > self.balance and not isinstance(amount, int):
            print(f'You are not Bernie Sanders {self.name}, no financial support will be granted!')
            amount = int(input(f'Place your bet {self.name}: $'))
        else:
            self.bet = amount
            self.balance -= amount
            print(f"{self.name}'s Balance: {self.balance}")

    def deal(self, deck):
        self.card.append(deck.draw())
        return self

    def show(self):
        tab = '          '
        print(f'{self.name} has:')
        for i in self.card:
            print(f'{tab}' + i.show())

    def calculate_hand(self):
        royals = ['Jack', 'Queen', 'King']
        total = 0
        for i in self.card:
            if i.get_value() == 'Ace':
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
            elif i.get_value() in royals:
                total += 10
            else:
                total += int(i.get_value())

        return total


class Game:
    def __init__(self):
        self.players = []

# Create Ea. Player receives a list of names ( the people playing and accordingly creates each Player)

    def create_each_player(self, name):
        self.players.append(Player(name))

    def who_is_playing(self):
        val = input('Hello there, would you like to play a little game? (Y/N): ')
        options = ['Y', 'N']
        while val not in options:
            val = input("Don't be afraid....:  ")
        else:
            while True:
                if val == 'Y':
                    name = input("Enter your name: ")
                    self.create_each_player(name)
                    val = input("Can I have more good sir? (Y/N): ")
                elif val == 'N':
                    print('I invested a lot of time into this... Are you sure? *cough* CUNT *cough*')
                    name = input("Sorry your name was?: ")
                    if name == 'N':
                        self.players.append(Player('Dealer'))
                        break
                    else:
                        self.create_each_player(name)
                        val = input("Can I have more good sir? (Y/N): ")

    def lets_play(self, deck):
        x = 0
        tab = '          '
        while x <= 2:
            for p in self.players:
                if x == 0:
                    if p.name == 'Dealer':
                        pass
                    else:
                        p.place_bet()
                elif x == 1:
                    p.deal(deck)
                    p.show()
                else:
                    p.deal(deck)
                    p.show()
                    print(f'{tab}{p.calculate_hand()}')
            x += 1

    def hit_pass(self, deck):
        tab = '          '
        for p in self.players:
            if p.name == 'Dealer':
                while True and p.calculate_hand() <= 16:
                    if p.calculate_hand() <= 16:
                        p.deal(deck)
                        p.show()
                        print(f'{tab}{p.calculate_hand()}')
                        print(f'To beat {p.name} you need more than {p.calculate_hand()}')
                    elif 17 >= p.calculate_hand() <= 21:
                        break

            else:
                val = input(f"{p.name} on {p.calculate_hand()} HIT or PASS? (Y/N): ")
                while True:
                    if val == 'Y':
                        p.deal(deck)
                        p.show()
                        print(f'{tab}{p.calculate_hand()}')
                        val = input(f"{p.name} HIT or PASS? (Y/N): ")
                    else:
                        break

    def win_lose(self):
        dealer_hand = self.players[-1].calculate_hand()
        if dealer_hand > 21:
            dealer_hand = 0
        else:
            pass

        for p in self.players:
            if p.name == 'Dealer' and p.calculate_hand() < 21:
                print(f'Dealers total is {p.calculate_hand()}')
            elif p.calculate_hand() > 21:
                print(f'{p.name} has BUST')
            elif p.calculate_hand() < dealer_hand != 0:
                print(f'{p.name} has LOST')
            elif p.calculate_hand() == dealer_hand:
                p.balance += p.bet
                print(f'{p.name} has DRAW')
            elif len(p.card) == 2 and p.calculate_hand() == 21:
                p.balance += (p.bet + (p.bet*1.5))
                print(f'{p.name} hit BLACKJACK')
            elif dealer_hand == 0 or dealer_hand < p.calculate_hand() <= 21:
                p.balance += (p.bet*2)
                print(f'{p.name} has WON')
        for s in self.players:
            print(f'{s.name} has ${s.balance} available')

    def add_player(self):
        name = input("Do you want to add another player? (Y/N): ")
        if name == 'Y':
            name = input('Who will be joining us: ')
            self.create_each_player(name)
        elif name == 'N':
            pass

    def clear_hand(self):
        for p in self.players:
            p.card.clear()


def play_game():
    first = Game()
    first.who_is_playing()

    some = input("Let's platy (Y/N): ")
    while some == 'Y':
        my_deck = Deck()
        my_deck.shuffle()
        first.lets_play(my_deck)
        first.hit_pass(my_deck)
        first.win_lose()
        some = input("Continue (Y/N): ")
        first.add_player()
        first.clear_hand()
    else:
        print("THANK YOU FOR PLAYING")
        exit()


if __name__ == "__main__":
    play_game()

    # take input from user for name

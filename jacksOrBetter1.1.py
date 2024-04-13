import random

# Define Unicode for colorful text.
class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Define Unicode characters for card suits
class Suits:
    SPADES = '\u2660'  # ♠
    HEARTS = '\u2665'  # ♥
    DIAMONDS = '\u2666'  # ♦
    CLUBS = '\u2663'  # ♣
    
class Payouts:
    def __init__(self, *args):
        # Define payout values for different hand combinations
        self.flush = 800
        self.four_of_a_kind = 200
        self.full_house = 45
        self.straight = 25
        self.three_of_a_kind = 15
        self.two_pair = 10
        self.jacks_or_better = 5

class Card:
    # A class to create card objects for constructing a Deck from a linked list.
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        self.next = None

class Deck:
    # References the Card class to create new card objects which point to each other.
    def __init__(self):
        self.head = None
        self.initialize_deck()

    def initialize_deck(self):
        suits = [Suits.HEARTS, Suits.DIAMONDS, Suits.CLUBS, Suits.SPADES]
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                self.add_card(value, suit)

    def add_card(self, value, suit):
        new_card = Card(value, suit)
        if not self.head:
            self.head = new_card
        else:
            current = self.head
            while current.next:     # Iterates along the linked list until the last card is reached.
                current = current.next
            current.next = new_card     # Pointing the most recent card object at the next.

    def shuffle(self):
        if not self.head:     # If true...
            return None
        current = self.head     # Start from the first node and count through the rest.
        count = 0
        while current:
            count += 1
            current = current.next

        shuffle_nodes = []
        prev = None
        current = self.head

        # Shuffle deck using Fisher Yates Algorithm
        for i in range(count):
            # Generate a random index
            random_index = random.randint(0, count - i - 1)
            prev = None
            current = self.head
            for j in range(random_index):
                prev = current
                current = current.next

            # Remove the current node from the list
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

            # Append the current node to the shuffled list
            shuffle_nodes.append(current)

        # Reassign the head of the original list with the shuffled list
        self.head = shuffle_nodes[0]
        current = self.head
        for node in shuffle_nodes[1:]:
            current.next = node
            current = current.next
        current.next = None

    def deal_cards(self, player):
        count = 0
        current = self.head
        dealt_cards = None  # Initialize a variable to keep track of the dealt cards

        # Deal five cards or until the end of the deck is reached
        while count < 5 and current:
            card_to_deal = current  # Get the current card to deal
            current = current.next  # Move to the next card in the deck
            card_to_deal.next = None  # Remove the card from the deck
            player.receive_card(card_to_deal)  # Deal the card to the player
            if not dealt_cards:
                dealt_cards = card_to_deal  # Update the dealt cards variable if it's the first dealt card
            count += 1

        # Update the head of the deck to the next card after the dealt cards
        self.head = current

        return dealt_cards
                        
class Player:
    def __init__(self):
        self.hand = None
        
    def receive_card(self, card):
        if not self.hand:
            self.hand = card
        else:
            current = self.hand
            while current.next:
                current = current.next
            current.next = card

class Game:
    def __init__(self):
        self.payouts = Payouts()

    def evaluate_hand(self, hand):
        
        # Placeholder method for evaluating the player's hand and determining the payout
        # You would implement the logic here to evaluate the hand and determine the payout
        pass

    def play_round(self):
        # Placeholder method for playing a round of the game
        # This method could deal cards, evaluate the player's hand, and determine the payout
        pass
        
def colorfulBannerRows(rowCount):
    # This function displays a colorful banner of asteristics with row-width as the parameter.
    for i in range(rowCount):
        if i != 0:
            print('\n')
        for j in range(100):
            if i == 1:
                print(colors.RED + '*' + colors.END, end='')
            elif i == 2:
                print(colors.GREEN + '*' + colors.END, end='')
            elif i == 3:
                print(colors.PURPLE + '*' + colors.END, end='')
            elif i == 4:
                print(colors.CYAN + '*' + colors.END, end='')
            elif i == 5:
                print(colors.YELLOW + '*' + colors.END, end='')
            elif i == 6:
                print(colors.BLUE + '*' + colors.END, end='')
            elif i == 7:
                print(colors.DARKCYAN + '*' + colors.END, end='')
            else:
                print(colors.YELLOW + '*' + colors.END, end='')
                
colorfulBannerRows(8)
print('\n')  
print(colors.RED + '                **********      *******          ******    **** *****    ********                 ' + colors.END)
print(colors.RED + '                   ****          *****          ***  ***    **   **     **    ****                ' + colors.END)
print(colors.RED + '                   ****         **   **        ***          **  **     **                         ' + colors.END)
print(colors.RED + '                   ****        **     **       ***          ** **      ***                        ' + colors.END)
print(colors.YELLOW + '                   ****       ***********      ***          ****        *******                   ' + colors.END)
print(colors.YELLOW + '                   ****      *************     ***          ****            *******               ' + colors.END)
print(colors.YELLOW + '                   ****     **           **    ***          ** **                ***              ' + colors.END)
print(colors.YELLOW + '              **** ****    **             **   ***          **  **                **              ' + colors.END)
print(colors.YELLOW + '               **  ****   **               **   ***  ***    **   **     ****     **               ' + colors.END)
print(colors.GREEN + '                ******  *****             *****  ******    **** *****    *********                ' + colors.END)

print(colors.GREEN + '                                               *****   **** ***                                   ' + colors.END)
print(colors.GREEN + '                                              *** ***   ****  **                                  ' + colors.END)
print(colors.GREEN + '                                              *** ***   ***                                       ' + colors.END)
print(colors.GREEN + '                                              *** ***   ***                                       ' + colors.END)
print(colors.GREEN + '                                               *****   *****                                      ' + colors.END)

print(colors.BLUE + '             **********    **********   ************** **************  ********** ********       ' + colors.END)
print(colors.BLUE + '              ***    ***   ***     **   **    **    ** **    **    **  ***     **  **    **      ' + colors.END)
print(colors.BLUE + '              ***     **   ***                **             **        ***         **    **      ' + colors.END)
print(colors.BLUE + '              ***    ***   ***  ***           **             **        ***  ***    **    *       ' + colors.END)
print(colors.CYAN + '              *********    ********           **             **        ********    ******        ' + colors.END)
print(colors.CYAN + '              ***    ***   ***  ***           **             **        ***  ***    **   ***      ' + colors.END)
print(colors.CYAN + '              ***     **   ***                **             **        ***         **    **      ' + colors.END)
print(colors.PURPLE + '              ***    ***   ***     **         **             **        ***     **  **    **      ' + colors.END)
print(colors.PURPLE + '             **********    **********       ******         ******      ********** ****  ****     ' + colors.END)
colorfulBannerRows(4)

deck = Deck()
deck.shuffle()
user = Player()
user_hand = deck.deal_cards(user)
computer = Player()
computer_hand = deck.deal_cards(computer)

# Print the player's hand

print('')

# Define a function to print a single card
def print_card(card):
    virtual_card = (
        colors.PURPLE + ' ----------------- ' + colors.END + '\n' +
        colors.PURPLE + (f'| {card.value}{card.suit}             |' if len(f'{card.value}{card.suit}') == 3 else f'| {card.value}{card.suit}              |') + colors.END + '\n' +
        colors.PURPLE + '|                 |' + colors.END + '\n' +
        colors.PURPLE + '|                 |' + colors.END + '\n' +
        colors.PURPLE + '|                 |' + colors.END + '\n' +
        colors.PURPLE + '|                 |' + colors.END + '\n' +
        colors.PURPLE + '|                 |' + colors.END + '\n' +
        colors.PURPLE + '|                 |' + colors.END + '\n' +
        colors.PURPLE + '|                 |' + colors.END + '\n' +
        colors.PURPLE + (f'|             {card.value}{card.suit} |' if len(f'{card.value}{card.suit}') == 3 else f'|              {card.value}{card.suit} |') + colors.END + '\n' + 
        colors.PURPLE + ' ----------------- ' + colors.END + '\n'
    )
    return virtual_card

user_current_card = user_hand
computer_current_card = computer_hand

user_list = []
computer_list = []

while user_current_card or computer_current_card:
    user_list.append(print_card(user_current_card))
    computer_list.append(print_card(computer_current_card))
    user_current_card = user_current_card.next
    computer_current_card = computer_current_card.next

print(colors.BOLD + colors.UNDERLINE + colors.GREEN + '                                  YOUR HAND:                                         ' + colors.END)

# Print user's cards above computer's cards
for i in range(11):  # 9 lines in each card
    for card in user_list:
        print(card.split('\n')[i], end='  ')  # Print the ith line of each card with two spaces between
    print()  # Move to the next line after printing all user's cards

print()  # Add a line break between user's and computer's cards

print(colors.BOLD + colors.UNDERLINE + colors.GREEN + '                                  COMPUTER HAND:                                         ' + colors.END)

for i in range(11):  # 9 lines in each card
    for card in computer_list:
        print(card.split('\n')[i], end='  ')  # Print the ith line of each card with two spaces between
    print()  # Move to the next line after printing all computer's cards


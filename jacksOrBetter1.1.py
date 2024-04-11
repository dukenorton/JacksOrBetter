import random

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
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.next = None

class Deck:
    # References the Card class to create new card objects which point to each other.
    def __init__(self):
        self.head = None
        self.initialize_deck()

    def initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for value in values:
                self.add_card(suit, value)

    def add_card(self, suit, value):
        new_card = Card(suit, value)
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

        shuffled_nodes = []
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
            shuffled_nodes.append(current)

        # Reassign the head of the original list with the shuffled list
        self.head = shuffled_nodes[0]
        current = self.head
        for node in shuffled_nodes[1:]:
            current.next = node
            current = current.next
        current.next = None

        def deal_cards(self):
            if not self.head:
                return None
            else:
                dealt_card = self.head
                self.head = self.head.next
                return dealt_card
            
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
shuffled_deck = deck.shuffle()
player = Player()
player_hand = player.receive_card(shuffled_deck.deal_cards())

# Print the player's hand
current_card = player_hand
while current_card:
    print(current_card.suit, current_card.value)
    current_card = current_card.next

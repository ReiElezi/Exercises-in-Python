import random

# Create a list representing a deck of playing cards (54 tuples)
# Assume each tuple contains a card represented as a string
deck_of_cards = [("Ace", "Hearts"), ("2", "Hearts"), ("3", "Hearts"), ("4", "Hearts"), ("5", "Hearts"),
                 ("6", "Hearts"), ("7", "Hearts"), ("8", "Hearts"), ("9", "Hearts"), ("10", "Hearts"),
                 ("Jack", "Hearts"), ("Queen", "Hearts"), ("King", "Hearts"),
                 ("Ace", "Diamonds"), ("2", "Diamonds"), ("3", "Diamonds"), ("4", "Diamonds"), ("5", "Diamonds"),
                 ("6", "Diamonds"), ("7", "Diamonds"), ("8", "Diamonds"), ("9", "Diamonds"), ("10", "Diamonds"),
                 ("Jack", "Diamonds"), ("Queen", "Diamonds"), ("King", "Diamonds"),
                 ("Ace", "Clubs"), ("2", "Clubs"), ("3", "Clubs"), ("4", "Clubs"), ("5", "Clubs"),
                 ("6", "Clubs"), ("7", "Clubs"), ("8", "Clubs"), ("9", "Clubs"), ("10", "Clubs"),
                 ("Jack", "Clubs"), ("Queen", "Clubs"), ("King", "Clubs"),
                 ("Ace", "Spades"), ("2", "Spades"), ("3", "Spades"), ("4", "Spades"), ("5", "Spades"),
                 ("6", "Spades"), ("7", "Spades"), ("8", "Spades"), ("9", "Spades"), ("10", "Spades"),
                 ("Jack", "Spades"), ("Queen", "Spades"), ("King", "Spades"),
                 ("Joker", "Black"), ("Joker", "Red")]

# Shuffle the deck of cards
random.shuffle(deck_of_cards)

# Divide the shuffled deck into 4 different lists
hand1, hand2, hand3, hand4 = [], [], [], []

for i in range(len(deck_of_cards)):
    if i % 4 == 0:
        hand1.append(deck_of_cards[i])
    elif i % 4 == 1:
        hand2.append(deck_of_cards[i])
    elif i % 4 == 2:
        hand3.append(deck_of_cards[i])
    else:
        hand4.append(deck_of_cards[i])

# Print the hands
print("Hand 1:", hand1)
print("Hand 2:", hand2)
print("Hand 3:", hand3)
print("Hand 4:", hand4)

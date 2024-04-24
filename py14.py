import random

# English-Albanian dictionary
english_albanian_dict = {
    "apple": "mollë",
    "banana": "banane",
    "cherry": "manaferr",
    "orange": "portokall",
    "grape": "rrush",
    "pear": "dardhë",
    "peach": "kajsi",
    "strawberry": "boronica",
    "pineapple": "ananas",
    "watermelon": "karpuz",
}

# Function to randomly choose 4 English words
def choose_english_words(english_words_dict, num_words=4):
    english_words = list(english_words_dict.keys())
    chosen_words = random.sample(english_words, num_words)
    return chosen_words

# Function to translate English words to Albanian
def translate_to_albanian(english_words, english_albanian_dict):
    translated_words = [english_albanian_dict[word] for word in english_words]
    return translated_words

# Test the functions
english_words = choose_english_words(english_albanian_dict)
translated_words = translate_to_albanian(english_words, english_albanian_dict)

print("English words:", english_words)
print("Translated Albanian words:", translated_words)

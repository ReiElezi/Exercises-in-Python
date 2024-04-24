import random

def generate_sentence(weather, place, feeling):
    selected_weather = random.choice(weather)
    selected_place = random.choice(place)
    selected_feeling = random.choice(feeling)
    return f"It is {selected_weather} in {selected_place} and I am {selected_feeling}"

# Lists
weather = ['Sunny', 'Windy', 'Snowy', 'Rainy', 'Warm']
place = ['Epoka', 'Tirana', 'Korca', 'Qyteza']
feeling = ['Bored', 'Happy', 'Sad', 'Excited']

# Generate and print a sentence
sentence = generate_sentence(weather, place, feeling)
print(sentence)

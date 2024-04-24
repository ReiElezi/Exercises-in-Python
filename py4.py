def longer_than_n(words, n):
    return [word for word in words if len(word) > n]

# Test the function
word_list = ["apple", "banana", "orange", "kiwi", "pineapple", "grape"]
n = 5
print("Original list of words:", word_list)
print("Words longer than", n, "characters:", longer_than_n(word_list, n))   
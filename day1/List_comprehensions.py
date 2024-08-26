sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

list = [len(word) for word in words]
print(list)
not_the = [len(word) for word in words if word != "the"]
print(not_the)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_int = [num for num in numbers if num > 0]
print(positive_int)

negative_int = [num for num in numbers if not num > 0]
print(negative_int)


number_s = [12, 54, 33, 67, 24, 89, 11, 24, 47]
even_numbers =  [num for num in number_s if num % 2 == 0]
print(even_numbers)


word_s = ["hello", "my", "name", "is", "Sam"]
upper_case = [(word_s.upper(), len(word_s)) for word_s in word_s ]
print(upper_case)

lower_case = [(word_s.lower(), len(word_s)) for word_s in word_s ]
print(lower_case)
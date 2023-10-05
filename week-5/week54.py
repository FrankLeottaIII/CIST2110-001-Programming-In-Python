# For Each loops in Python

# For each loop
# for <variable> in <sequence>:
#     <body>

# Example 1

word = "Hello"

# for each letter in word

for letter in word:
    print(letter)

print(len(word))
# H E L L O
# 0 1 2 3 4 - index (what the computer sees)
# 1 2 3 4 5 - length (what the human sees)
for i in range(len(word)): 
#equivalt to for i in range(5):
    print(i)

for i in word:
    print(i)

# for i in range(len(word)) gets the index
# for i in word gets the letter's value

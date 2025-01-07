# import random


# random_words = []

# word = random.choice(random_words)
# empty_list = [" "] * len(word)          #?Generates an empyty list with length of word
# count = 5
# letter_found = True
# for i in range(word):
#     if count == -1:
#         print("You have lost the game")
#     elif " " not in empty_list:
#         print("You have won the game")
#         break
#     letter = input("Enter your letter: ")
#     if letter_found == False:
#         count -= 1
#         print(f"Wrong letter, you have {count} chances remaining")
#     letter_found = False
#     for c in range(word):
#         if word[c] == letter:
#             empty_list[c] = letter
#             word = word[:c:] + word[c+1::]
#             letter_found = True
#             break




import random
random_words = ["Batman"]

new_word = random.choice(random_words)
new_word = new_word.lower()
empty_list = ["_"] * len(new_word)
# print("".join(empty_list))
count = 5
found = True
while True:
    if found == False:
        count -= 1
        print(f"The guess was wrong. You have {count} left")
        print("".join(empty_list))
        if count == 0:
            print("The game is lost")
            break
    found = False
    letter = input("Enter your letter: ")
    for i in range(len(new_word)):
        if new_word[i] == letter:
            new_word = new_word[:i] + "*" + new_word[i+1::]
            empty_list[i] = letter
            found = True
            print(("\nCorrect, Welldone! \n" + "".join(empty_list)))
            # r += 1
            break
    if "_" not in empty_list:
        print("The game is won, Bloody well done kid. ")
        print(f"The word was {("".join(empty_list))}")
        break



# import random

# random_words = ["Batman"]
# new_word = random.choice(random_words)
# new_word = new_word.lower()
# empty_list = ["_"] * len(new_word)
# count = 5
# found = True
# while True:
#     if found == False:
#         count -= 1
#         print(f"The guess was wrong. You have {count} chances left")
#         print("".join(empty_list))
#         if count == 0:
#             print("The game is lost")
#             break
#     found = False
#     letter = input("Enter your letter: ").lower()
#     for i in range(len(new_word)):
#         if new_word[i] == letter:
#             empty_list[i] = letter
#             found = True
#             new_word = new_word[:i] + "*" + new_word[i+1:]  # Mark the found letter with a '*'
#             print("\nCorrect!\n" + "".join(empty_list))
#     if "_" not in empty_list:
#         print("The game is won, well done!")
#         print(f"The word was {''.join(empty_list)}")
#         break

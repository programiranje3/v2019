# Task 1:
# Write a function that receives an integer value (n) and
# generates and prints a dictionary with entries in the
# form x:x*x, where x is a number between 1 and n.

def create_dictionary(n):
    d = dict()
    for x in range(1, n+1):
        d[x] = x*x
    for key, val in d.items():
        print("{}:{}".format(key, val))


# Task 2:
# Write a function that receives a string as its input parameter and
# calculates the number of digits and the number of letters in this string.
# The function returns the dictionary with the computed values.

def string_stats(s):
    # d = {"letters":0, "digits":0}
    # for ch in s:
    #     if ch.isalpha():
    #         d['letters'] += 1
    #     elif ch.isdigit():
    #         d['digits'] += 1
    # return d

    digits = [ch for ch in s if ch.isdigit()]
    letters = [ch for ch in s if ch.isalpha()]
    d = {"digits":len(digits), "letters":len(letters)}
    return d




# Task 3:
# Write a function to play a guessing game: to guess a number between 1 to 9.
# (scenario: user is prompted to enter a guess. If the user guesses wrongly,
# the prompt reappears; the user can try to guess max 3 times;
# on successful guess, user should get a "Well guessed!" message,
# and the function terminates
#
# Hint: use function randint from random package to generate a number to
# be guessed in the game

from random import randint

def guessing_game():
    number = randint(1,9)
    for trial in range(3):
        guess = input(f"Please enter your guess for the number (this is your {trial+1} attempt)\n")
        if not guess.isdigit():
            print("Wrong input! Only numbers in the [1-9] range are allowed")
            continue
        if int(guess) == number:
            print("Right guess! Congrats!")
            return
        msg = "Wrong! Try again" if trial < 2 else "Wrong! More luck next time"
        print(msg)


# Task 4:
# Write a function that receives two strings and checks if the second string
# when reversed is equal to the first one.
# The comparison should be based on letters and digits only (alphanumerics)
# and should be case insensitive.
# The function returns the result of the comparison as a boolean value.



def compare_reversed(s1, s2):
    l1 = [ch.lower() for ch in s1 if ch.isalnum()]
    l2 = [ch.lower() for ch in s2 if ch.isalnum()]
    new_s1 = "".join(l1)
    l2.reverse()
    new_s2 = "".join(l2)
    print(new_s1, new_s2)
    return new_s1 == new_s2




# Task 5:
# Write a function that asks the user for a word or a sentence
# and prints out whether the entered text is a palindrome or not.
# Consider only letters of the input text, regardless of the case
# (i.e. comparison should be case insensitive)





# Task 6:
# Write a function that checks and returns whether a given string is a pangram or not.
# Pangrams are sentences containing every letter of the alphabet at least once.
# (e.g.: "The quick brown fox jumps over the lazy dog")
#
# Hint: use ascii_lowercase from the string module to get all letters





# Task 7:
# Write a function that finds numbers between 100 and 400 (both included)
# where each digit of a number is even. The numbers that match this criterion
# should be printed in a comma-separated sequence.






# Task 8:
# Write a function that accepts a string input and returns slices of that
# string according to the following rules:
# - if the input string is less than 3 characters long, returns a list
#   with the input string as the only element
# - otherwise, returns a list with all string slices more than 1 character long
# Examples:
# input: 'are'
# result: ['ar', 'are', 're']
# input: 'table'
# result: ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']






if __name__ == '__main__':


    # create_dictionary(6)

    # print(string_stats("Today is October 15, 2019"))

    # print(digiti_letter_counter("Today is October 14, 2018"))

    # guessing_game()

    print(compare_reversed("Cat?", "tac!!!"))
    print(compare_reversed("Hello there!", "hello world!!!"))

    # palindrom()

    # print(pangram("The quick brown fox jumps over the lazy dog"))
    # print(pangram("The quick brown fox jumps over the lazy cat"))

    # all_even_digits()

    # print(string_slices('are'))
    # print(string_slices('table'))
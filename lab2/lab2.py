# Task 1:
# Write a function that receives an integer value (n) and
# generates and prints a dictionary with entries in the
# form x:x*x, where x is a number between 1 and n.





# Task 2:
# Write a function that receives a string as its input parameter and
# calculates the number of digits and the number of letters in this string.
# The function returns the dictionary with the computed values.





# Task 3:
# Write a function to play a guessing game: to guess a number between 1 to 9.
# (scenario: user is prompted to enter a guess. If the user guesses wrongly,
# the prompt reappears; the user can try to guess max 3 times;
# on successful guess, user should get a "Well guessed!" message,
# and the function terminates
#
# Hint: use function randint from random package to generate a number to
# be guessed in the game





# Task 4:
# Write a function that receives two strings and checks if the second string
# when reversed is equal to the first one.
# The comparison should be based on letters and digits only (alphanumerics)
# and should be case insensitive.
# The function returns the result of the comparison as a boolean value.





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

    pass

    # create_dict(6)

    # print(digiti_letter_counter("Today is October 14, 2018"))

    # guess_number()

    # print(compare_reversed("Cat?", "tac!!!"))
    # print(compare_reversed("Hello there!", "hello world!!!"))

    # palindrom()

    # print(pangram("The quick brown fox jumps over the lazy dog"))
    # print(pangram("The quick brown fox jumps over the lazy cat"))

    # all_even_digits()

    # print(string_slices('are'))
    # print(string_slices('table'))
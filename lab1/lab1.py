# Write a function that asks the user for a number, and depending on whether
# the number is even or odd, prints out an appropriate message.

def print_odd_or_even():
    num_str = input("Please enter a integer value\n")

    # Option 1:
    num = int(num_str)
    if num % 2 == 0:
        print("Number", num_str, "is EVEN")
    else:
        print("Number", num_str, "is ODD")

    # Option 2:
    # result = 'even' if int(num) % 2 == 0 else 'odd'
    # print('This is an', result.upper(), 'number')


# Write a function that calculates and returns the factorial of a number.
# The function accepts the number (a non-negative integer) as its argument.

def factorial(n):
    result = 1
    for x in range(n, 1, -1):
        result *= x
    return result


# Write a function that returns nth lowest value of a list
# (or an iterable in general). Return the lowest if n (2nd argument)
# is greater than the number of elements in the iterable.

def nth_lowest(a_list, n):
    # Option 1:
    if len(a_list) < n:
        return min(a_list)
    a_list = sorted(a_list)
    return a_list[n-1]

    # Option 2:
    # sorted_list = sorted(a_list)
    # if n > len(sorted_list):
    #     n = 1
    # return sorted_list[n - 1]


# Write a function that receives a list of numbers and returns
# a tuple with the following elements:
# - the list element with the smallest absolute value
# - the list element with the largest absolute value
# - the sum of all positive elements in the list
# - the product of all negative elements in the list

def list_stats(numbers):
    min_abs = numbers[0]
    max_abs = numbers[0]
    sum = 0
    prod = 1
    for number in numbers:
        if abs(number) < abs(min_abs):
            min_abs = number
        if abs(number) > abs(max_abs):
            max_abs = number
        if number > 0:
            sum += number
        if number < 0:
            prod *= number
    return min_abs, max_abs, sum, prod




# Write a function that receives a list of numbers and a
# threshold value (number). The function:
# - makes a new list that has unique elements from the input list
#   that are less than the given number
# - prints the number of elements in the new list
# - sorts the elements in the list from the largest to the smallest,
#   and prints them, an element per line

def print_new_list(numbers, threshold):
    new_list = list()
    for item in list(set(numbers)):
        if item > threshold:
            new_list.append(item)

    print("The new list has ", str(len(new_list)), " elements")

    for index, item in enumerate(sorted(new_list, reverse=True)):
        print(str(index +1) + ". element: " + str(item))



# Write a function that receives two strings and checks if they
# are anagrams (assume input consists of alphabets only).
# The function returns appropriate boolean value.

def anagrams(s1, s2):
    s1_sorted = sorted(s1.lower())
    s2_sorted = sorted(s2.lower())
    return s1_sorted == s2_sorted

def anagrams_v2(s1, s2):
    s1_reversed = list(reversed(s1.lower()))
    return s1_reversed == list(s2.lower())




# Write a function to play a guessing game: to guess a number between 1 to 9.
# (scenario: user is prompted to enter a guess. If the user guesses wrongly,
# the prompt reappears; the user can try to guess max 3 times;
# on successful guess, user should get a "Well guessed!" message,
# and the function terminates
#
# Hint: use function randint from random package to generate a number to
# be guessed in the game





if __name__ == '__main__':

    # print_odd_or_even()

    # print(factorial(5))

    # a = [31, 72, 13, 41, 5, 16, 87, 98, 9]
    # print(nth_lowest(a, 10))
    # print(nth_lowest(['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c'], 6))
    # print(nth_lowest('today', 3))

    # print(list_stats([1.2, 3.4, 5.6, -4.2, -5.6, 9, 11.3, -23.45, -81]))

     # print_new_list([1, 1, 2, 3, 5, 8, 8, 13, 13, 21, 34, 55, 89, 8], 9)

    print(anagrams_v2('Cat', 'Tac'))
    print(anagrams_v2('Bob', 'Bill'))

    # create_dictionary(5)

    # print(digits_letters_counter('Tuesday, Oct 9, 2018'))

    # guess_number()

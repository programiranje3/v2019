# import functools
# from statistics import median, mean, stdev

# Task 1
# Write a function that receives an arbitrary number of numeric values
# and computes their product. The function also receives a named argument
# "absolute" with the default value False, which determines if the computed
# product or the absolute value of the product is to be returned.
# Implement the function in two different ways:
#
# 1) using a for loop
# 2) using the reduce() f. from the functools module together with an appropriate lambda f.
#   for an example and explanation of reduce() f. check, e.g., the following link:
#   https://www.python-course.eu/lambda.php






# Task 2
# Write a function that receives an arbitrary number of strings and returns a list
# of those strings where the first and the last character are the same and the
# total number of unique characters is above the given threshold. The threshold
# is given as a named argument with the default value of 3.
#
# Implement the function in three different ways:
# 1) using the for loop
# 2) using list comprehension
# 3) using the filter() f. together with an appropriate lambda f.

# def filter_strings(*strings, threshold=3):
#     selected_strings = []
#     for s in strings:
#         if s[0].lower()==s[-1].lower() and len(set(s.lower())) > threshold:
#             selected_strings.append(s)
#     return selected_strings


# def filter_strings(*strings, threshold=3):
#     return [s for s in strings if s[0].lower()==s[-1].lower() and len(set(s.lower())) > threshold]

def check_string(s, threshold):
    return s[0].lower()==s[-1].lower() and len(set(s.lower())) > threshold

def filter_strings(*strings, threshold=3):
    # return list(filter(lambda s: s[0].lower()==s[-1].lower() and len(set(s.lower())) > threshold, strings))
    return list(filter(lambda s: check_string(s, threshold), strings))


# Task 3
# Write a function that receives a list of product orders, where each order is a 4-tuple
# of the form (order_id, product_name, quantity, price_per_item). The function returns
# a list of 2-tuples of the form (order_id, total_price) where total price (in USD) for
# an order is the product of the quantity and the price per item (in USD) plus the shipping
# cost for orders with total value less than 100 USD. The shipping cost is given as the
# value of the input argument 'shipping' with default value of 10 (USD).
#
# Implement the function in three different ways:
# 1) using the for loop
# 2) using list comprehension
# 3) using the map() f. together with an appropriate lambda f.

def process_order(orders, shipping=10):
    processed_orders = []
    for order_id, pname, quantity, price in orders:
        tot_price = quantity * price
        # if tot_price < 100:
        #     tot_price += 10
        # tot_price = tot_price if tot_price > 100 else tot_price+shipping
        tot_price += 0 if tot_price > 100 else shipping
        processed_orders.append((order_id, tot_price))
    return processed_orders

# def process_order(orders, shipping=10):
#     processed_orders = [(order_id, quantity*price) for order_id, pname, quantity, price in orders ]
#     return [(order_id, tot_price if tot_price > 100 else tot_price+shipping) for order_id, tot_price in processed_orders]

# def process_order(orders, shipping=10):
#     processed_orders = map(lambda order: (order[0], order[2] * order[3]), orders)
#     return list(map(lambda order: (order[0], order[1] if order[1] > 100 else order[1] + shipping), processed_orders))


# Task 4
# Create a decorator that measures the time a function takes to execute
# and prints the duration to the console.
#
# Hint 1: use the decorator-writing pattern:
# import functools
# def decorator(func):
#     @functools.wraps(func)			                # preserves func's identity after it's decorated
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
#
# Hint 2: to measure the time a function takes, use the perf_counter() f.
# from the time module (it returns the float value of time in seconds).

import functools
from time import perf_counter

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):

        # Do something before
        start_time = perf_counter()

        value = func(*args, **kwargs)

        # Do something after
        end_time = perf_counter()
        print(f"Function {func.__name__} ran for {end_time - start_time: .4f} seconds")

        return value

    return wrapper_timer


# Write a function that for each number x in the range 1..n (n is the input parameter)
# computes the sum: S(x) = 1 + 2 + ... + x-1 + x, and returns the sum of all S(x).
# Decorate the function with the timer decorator.

@timer
def sum_of_sums(n):
    result = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            result += j
    return result


@timer
def sum_of_sums_v2(n):
    result = 0
    for i in range(1, n+1):
       result += sum(range(1, i+1))
    return result


# Write a function that creates a list by generating n random numbers between
# 1 and k (n and k are input parameters). After generating and adding each
# number to the list, the function determines and prints the difference
# between mean and median of the list elements. Decorate the function with
# the timer decorator.

from random import randint, seed
from statistics import mean, median

@timer
def mean_median_diff(n, k):
    rnumbers = []
    seed(4)
    for _ in range(n):
        rnum = randint(1, k)
        rnumbers.append(rnum)
        print(f"With {len(rnumbers)} elements in list, mean median difference is: {mean(rnumbers) - median(rnumbers)}")




# Task 5
# Create a decorator that standardizes a list of numbers
# before passing the list to a function for further computations.
# The decorator also rounds the computation result to 4
# digits before returning it (as its return value).
#
# Bonus: before calling the wrapped function, print, to the console,
# its name with the list of input parameters (after standardisation)






# Write a function that receives an arbitrary number of int values
# and for each value (x) computes the following sum:
# S(x) = x + x**2 + x**3 + ... + x**n
# where n is the keyword argument with default value 10.
# The function returns the sum of S(x) of all received int values.
# Decorate the function with the standardise decorator.






if __name__ == '__main__':

    # pass

    # print(compute_product(1,-4,13,2))
    # print(compute_product(1, -4, 13, 2, absolute=True))

    # # calling the compute_product function with a list
    # num_list = [2, 7, -11, 9, 24, -3]
    # # this is NOT a way to make the call:
    # print(compute_product(num_list))
    # # instead, this is how it should be done:
    # print(compute_product(*num_list)) # the * operator is 'unpacking' the list

    # str_list = ['yellowy', 'Boyb', 'lovely', 'yesterday', 'too']
    # print(filter_strings(*str_list, threshold=2))

    # orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
    #           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
    #           ("77226", "Head First Python, Paul Barry", 3, 32.95),
    #           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
    #
    # print(process_order(orders))

    # print(sum_of_sums(10000))
    # print()
    # print(sum_of_sums_v2(10000))
    mean_median_diff(100, 250)

    # print(sum_of_sums(1,3,5,7,9, n=5))



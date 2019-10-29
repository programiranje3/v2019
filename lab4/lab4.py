import functools
from statistics import median, mean, stdev

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

# Option 1
# def compute_product(*numbers, absolute=False):
#     product = 1
#     for number in numbers:
#         product *= number
#
#     # Option 1.1:
#     # if absolute:
#     #     product = abs(product)
#     # Option 1.2
#     product = abs(product) if absolute else product
#
#     return product


# Option 2
def compute_product(*numbers, absolute=False):
    product = functools.reduce(lambda a,b: a*b, numbers)
    return abs(product) if absolute else product




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

# Option 1
# def select_strings(*strings, threshold=3):
#     result = []
#     for s in strings:
#         if len(set(s.lower())) > threshold and s[0].lower()==s[-1].lower():
#             result.append(s)
#     return result

# Option 2
# def select_strings(*strings, threshold=3):
#     return [s for s in strings if len(set(s.lower())) > threshold and s[0].lower()==s[-1].lower()]

# Option 3
def select_strings(*strings, threshold=3):
    return list(filter(lambda s: len(set(s.lower()))>threshold and s[0].lower()==s[-1].lower(), strings))





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

# Option 1
# def process_product_orders(orders, shipping=10):
#     processed_orders = []
#     for order_id, product_name, quantity, price_per_item in orders:
#         total_price = quantity * price_per_item
#         if total_price < 100:
#             total_price += shipping
#         processed_orders.append((order_id, total_price))
#     return processed_orders

# Option 2
# def process_product_orders(orders, shipping=10):
#     processed_orders = [(id, quantity*price) for id, product, quantity, price in orders]
#     return [(id, tot_price if tot_price > 100 else tot_price+shipping) for id, tot_price in processed_orders]


# Option 3
# def process_product_orders(orders, shipping=10):
#     processed_orders = map(lambda order: (order[0], order[2]*order[3]), orders)
#     processed_orders = map(lambda porder: (porder[0], porder[1] if porder[1] > 100 else porder[1]+shipping),
#                            processed_orders)
#     return list(processed_orders)


# Option 4
def process_product_orders(orders, shipping=10):

    # this is an inner function of the process_product_orders() f.
    def process_order(order):
        order_id, product_name, quantity, price = order
        tot_price = quantity * price
        return order_id, tot_price if tot_price > 100 else tot_price + shipping

    return  list(map(lambda order: process_order(order), orders))




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


import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):

        # Do something before
        start_time = time.perf_counter()

        value = func(*args, **kwargs)

        # Do something after
        end_time = time.perf_counter()
        tot_time = end_time - start_time
        print(f"Function {func.__name__} took {tot_time: .2f} seconds to execute")

        return value
    return wrapper_timer



# Write a function that for each number x in the range 1..n (n is the input parameter)
# computes the sum: S(x) = 1 + 2 + ... + x-1 + x, and returns the sum of all S(x).
# Decorate the function with the timer decorator.

@timer
def compute_sum_v1(n):
    s = 0
    for x in range(n+1):
        for j in range(x+1):
            s += j
    return s


@timer
def compute_sum_v2(n):
    s = 0
    for x in range(n+1):
        s += sum(range(x+1))
    return s


@timer
def compute_sum_v3(n):
    s = 0
    for x in range(n+1):
        s += functools.reduce(lambda a,b: a+b, range(x+1))
    return s



# Write a function that creates a list by generating n random numbers between
# 1 and k (n and k are input parameters). After generating and adding each
# number to the list, the function determines and prints the difference
# between mean and median of the list elements. Decorate the function with
# the timer decorator.

@timer
def mean_median_diff(n, k):
    from random import randint, seed

    random_ints = []
    seed(1)
    for _ in range(n):
        random_ints.append(randint(1,k))
        mm_diff = abs(mean(random_ints) - median(random_ints))
        print(f"Difference between mean and median of {len(random_ints)} "
              f"random numbers in the [1-{k}] range is {mm_diff:.4f}")



# Task 5
# Create a decorator that standardizes a list of numbers
# before passing the list to a function for further computations.
# The decorator also rounds the computation result to 4
# digits before returning it (as its return value).
#
# Bonus: before calling the wrapped function, print, to the console,
# its name with the list of input parameters (after standardisation)


def standardise(func):

    @functools.wraps(func)
    def wrapper_standardise(*args, **kwargs):

        # standardizes the list of numbers that func receives as its args
        mean_args = mean(args)
        sd_args = stdev(args)
        standardised_args = [(a-mean_args)/sd_args for a in args]

        args_str = ", ".join([str(round(arg, 4)) for arg in standardised_args])
        kwargs_str = ", ".join([f"{key}={val}" for key, val in kwargs.items()])
        print(f"Calling function {func.__name__} ({args_str}, {kwargs_str})")

        value = func(*standardised_args, **kwargs)

        # rounds the computation result to 4 digits
        value = round(value, 4)

        return value

    return wrapper_standardise



# Write a function that receives an arbitrary number of int values
# and for each value (x) computes the following sum:
# S(x) = x + x**2 + x**3 + ... + x**n
# where n is the keyword argument with default value 10.
# The function returns the sum of S(x) of all received int values.
# Decorate the function with the standardise decorator.

@standardise
def sum_of_sums(*numbers, n=10):
    s = 0
    for number in numbers:
        s += sum([number**i for i in range(1,n+1)])
    return s





if __name__ == '__main__':

    # print(compute_product(1,-4,13,2))
    # print(compute_product(1, -4, 13, 2, absolute=True))

    # # calling the compute_product function with a list
    # num_list = [2, 7, -11, 9, 24, -3]
    # # this is NOT a way to make the call:
    # print(compute_product(num_list))
    # # instead, this is how it should be done:
    # print(compute_product(*num_list)) # the * operator is 'unpacking' the list

    # str_list = ['yellowy', 'Bob', 'lovely', 'yesterday', 'too']
    # print(select_strings(*str_list))

    # orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
    #           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
    #           ("77226", "Head First Python, Paul Barry", 3, 32.95),
    #           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
    #
    # print(process_product_orders(orders))

    # print(compute_sum_v1(10000))
    # print()
    # print(compute_sum_v2(10000))
    # print()
    # print(compute_sum_v3(10000))

    # mean_median_diff(100, 250)

    print(sum_of_sums(1,3,5,7,9, n=5))



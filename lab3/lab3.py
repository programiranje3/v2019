# Task 1
# Write a function that receives a piece of text and computes the frequency of
# the tokens appearing in the text (consider that a token is a string of contiguous
# characters between two spaces).
# Tokens and their frequencies are to be stored in a dictionary. The function
# prints tokens and their frequencies after sorting the tokens alphanumerically.
#
# After testing the function, alter it so that the dictionary entries are printed
# in the decreasing order of the tokens' frequencies.
# (hint: use itemgetter() f. from the operator module)

<<<<<<< HEAD
from collections import defaultdict
from operator import itemgetter

def clean_token(token):
    token = [ch for ch in token if ch.isalnum()]
    return "".join(token)

def token_frequencies(txt):
    d = dict()
    tokens = [clean_token(token) for token in txt.split()]
    for token in set(tokens):
        d[token] = 0
    for token in tokens:
        d[token] += 1

    print("Tokens in aplhanumeric order:")
    for token, freq in sorted(d.items(), key=lambda item: item[0].lower()):
        print(f"{token}:{freq}")

    print("\nTokens in decreasing frequency order:")
    for token, freq in sorted(d.items(), key=itemgetter(1), reverse=True):
        print(f"{token}:{freq}")


def token_frequencies_v2(txt):
    d = defaultdict(int)
    for token in txt.split():
        token = clean_token(token)
        d[token] += 1

    print("Tokens in decreasing frequency order:")
    for key, val in sorted(d.items(), key=lambda item: item[1], reverse=True):
        print(f"{key}: {val}")

=======
>>>>>>> origin/master


# Task 2
# Write a function that accepts a sequence of comma separated passwords
# and checks their validity using the following criteria:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length: 6
# 6. Maximum length: 12
# Passwords that match the criteria should be printed in one row
# separated by a comma.

<<<<<<< HEAD
import string

def check_passwords(passwords):
    verified = list()
    for p in passwords.split(","):
        p = p.strip()
        if len(p) < 6 or len(p) > 12:
            continue
        if not any([ch in string.ascii_lowercase for ch in p]):
            continue
        if not any([ch in string.digits for ch in p]):
            continue
        if not any([ch in string.ascii_uppercase for ch in p]):
            continue
        if not any([ch in '$#@' for ch in p]):
            continue
        verified.append(p)
    print(", ".join(verified))


def check_passwords_v2(passwords):
    verified = list()
    for p in passwords.split(","):
        p = p.strip()
        conditions = [False]*5
        conditions[0] = 6 <= len(p) <= 12
        conditions[1] = any([ch in string.ascii_lowercase for ch in p])
        conditions[2] = any([ch in string.digits for ch in p])
        conditions[3] = any([ch in string.ascii_uppercase for ch in p])
        conditions[4] = any([ch in "#@$" for ch in p])
        if all(conditions):
            verified.append(p)
    print(", ".join(verified))

=======
>>>>>>> origin/master



# Task 3
# Write a function that prompts the user for name, age, and competition score (0-100) of members
# of a sports team. All data items for one member should be entered in a single line, separated
<<<<<<< HEAD
# by a comma (e.g. Bob, 19, 55). The entry stops when the user enters 'done'.
=======
# by a comma (e.g. Bob, 19, 1.78, 75, 55). The entry stops when the user enters 'done'.
>>>>>>> origin/master
# The function stores the data for each team member as a dictionary, such as
# {name:Bob, age:19, score:55}
# where name is string, age is integer, and score is a real value.
# The data for all team members should form a list of dicitonaries.
# The function prints this list sorted by the members' scores and also return the list as its
# return value.

<<<<<<< HEAD
def collecte_team_data():
    print('''
            Please enter the following data for each team member: name, age, score
            Enter 'done' to terminate data entry. 
            ''')

    members_data = list()
    while True:
        data = input("Data for the next team member:\n")
        if data == 'done': break
        name, age, score = data.split(",")
        members_data.append({'name': name, 'age': int(age), 'score': float(score)})

    for member in sorted(members_data, key=itemgetter('score'), reverse=True):
        name, age, score = member.values()
        print(f"{name}, {age}, {score}")
=======

>>>>>>> origin/master



# Task 4
# Write a function that takes as its input the list of dictionaries created by the previous
# function and computes and prints the following statistics:
# - the average (mean) age and score of the team members
# - interquartile range for the team's score
# - name of the player with the highest score among those under 21 years of age
#
# Hint: the 'statistics' module provides functions for the required computations





# Task 5
# Write a function that creates a dictionary from the two given lists.
# Assure the lists are of equal length. Print the dictionary sorted based on
# the key values.
# Example: a list of countries and a list of the countries' national dishes
# should be turned into a dictionary where keys are country names and values
# are the corresponding dishes.


<<<<<<< HEAD
def lists_to_dict(l1, l2):
    if len(l1) != len(l2):
        print("Lists of unequal size - cannot proceed!")
        return
    d = dict(zip(l1, l2))
    for key, val in sorted(d.items(), key=lambda item: item[0].lower()):
        print(f"{key}: {val}")
=======

>>>>>>> origin/master


# Task 6
# Write a function to count the total number of students per class. The function receives
# a list of tuples of the form (<class>,<stud_count>). For example:
# [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
# The function creates a dictionary of classes and their student numbers; it then
# prints the classes and their sizes in the decreasing order of the class size.
#
# Hint: consider using defaultdict from the collections module
#
# After testing the function, try writing it using the Counter class from
# the collections module.





if __name__ == '__main__':

    pass

    # token_frequencies("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")

<<<<<<< HEAD
    # check_passwords_v2("ABd1234@1, a F1#, 2w3E*T@, 2We3345")
=======
    # check_passwords("ABd1234@1, a F1#, 2w3E*, 2We3345")
>>>>>>> origin/master
    
    # collecte_team_data()

    # team = [{'name': 'Bob', 'age': 18, 'score': 50.0},
    #         {'name': 'Tim', 'age': 17, 'score': 84.0},
    #         {'name': 'Jim', 'age': 19, 'score': 94.0}]
    # team_stats(team)

<<<<<<< HEAD
    dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    countries = ["Italy", "Germany", "Spain", "USA"]
    lists_to_dict(countries, dishes)
=======
    # dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    # countries = ["Italy", "Germany", "Spain", "USA"]
    # lists_to_dict(countries, dishes)
>>>>>>> origin/master

    # l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
    # classroom_stats(l)
    
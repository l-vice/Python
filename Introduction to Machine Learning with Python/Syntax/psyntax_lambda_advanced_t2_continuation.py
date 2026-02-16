##################################
# Redo: 34, 40, 46, 47, 49, 51
#
# 
#
#
#
#
#
#
#
#
#
################ SOLUTIONS
from functools import reduce
from string import punctuation
from itertools import accumulate

# 26.0
# Task: Write a Python program to find a list with maximum and minimum length using lambda. 
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

q26 = {"max": (len(max(list1, key = lambda x: len(x))),max(list1, key = lambda x: len(x))), "min": (len(min(list1, key = lambda x: len(x))),min(list1, key = lambda x: len(x)))}
q26

# 26.1
# Task: Write a Python program to find the sublist with the maximum sum and the sublist with the minimum sum using lambda.
my_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

q27 = {"max_sum": max(my_list, key = lambda x: sum(x)), "min_sum": min(my_list, key = lambda x: sum(x))}

# 26.2
# Task: Write a Python program to identify the sublist with the highest average value and the one with the lowest average using lambda.
my_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

average = lambda x: sum(x) / float(len(x))

q26_2 = {"hi_avg": max(my_list, key = lambda x: average(x)), "low_avg": min(my_list, key = lambda x: average(x))}

# 26.3
# Task: Write a Python program to determine the list with the maximum number of unique elements and the one with the minimum using lambda.
my_list = [[0], [7, 7, 7],[1, 3], [5, 7], [9, 11], [13, 15, 17]]

q26_3 = {"max_unique": max(my_list, key = lambda x: len(set(x))), "min_unique": min(my_list, key = lambda x: len(set(x)))}

# 26.4
# Task: Write a Python program to find the sublist with the longest and shortest total string length when elements are concatenated, using lambda.
my_list = [["cooper", "cod"], ["english", "warrior", "stealth"], ["wild", "monster", "incognito", "reckless"], ["partition", "blacklisted"]]

q26_4  = {"max_length": max(my_list, key = lambda x: len(''.join(x))), "min_length": min(my_list, key = lambda x: len(''.join(x)))}
q26_4

# 27.0
# Task: Write a Python program to sort each sublist of strings in a given list of lists using lambda.  
my_list = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
 
q27 = list(map(lambda x: sorted(x), my_list))
q27

# 27.1
# Task: Write a Python program to sort each sublist of integers in descending order using lambda.
my_list = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]

q27_1 = list(map(lambda x: sorted(x, reverse=True), my_list))

# 27.2
# Task: Write a Python program to sort each sublist of integers in descending order using lambda.
my_list = [[2, 3, 6], [24, 41, 53], [44, 42, 1], [4, 6, 11]]

q27_2 = list(map(lambda x: sorted(x, reverse=True), my_list))

# 27.3
# Task: Write a Python program to sort each sublist of mixed data types by converting each element to a string using lambda.
my_list = [[1, "nickelodion", "riveting"], ["englishman", 12, 5], ["new_york", "peloponesian", 12, 55]]

q27_3 = sorted([list(map(lambda x: str(x), sublist)) for sublist in my_list])

# 27.4
# Task: Write a Python program to sort each sublist based on the length of its elements using lambda.
my_list = [[1, "nickelodion", "riveting"], ["englishman", 12, 5], ["new_york", "peloponesian", 12, 55]]

q27_4 = sorted([list(map(lambda x: str(x), sublist)) for sublist in my_list], key = lambda x: len(''.join(x)))

# 27.5
# Task: Write a Python program to sort each sublist in reverse alphabetical order using lambda.
my_list = [[1, "nickelodion", "riveting"], ["englishman", 12, 5], ["new_york", "peloponesian", 12, 55]]
q27_5 = sorted([list(map(lambda x: str(x), sublist)) for sublist in my_list], reverse=True)

# 28.0
# Task: Write a Python program to sort a given list of lists by length and value using lambda.
my_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

q28 = sorted(my_list, key = lambda x: (len(x), x))

# 28.1 
# Task: Write a Python program to sort a list of lists first by the sum of their elements and then by the maximum element in each sublist using lambda. 
my_list = [[2], [0], [1, 3], [0, 7], [9, 11], [28, 1, 1, 1], [13, 15, 17]]

q28_1 = sorted(my_list, key = lambda x: (sum(x), max(x)))

# 28.2
# Task: Write a Python program to sort a list of lists based on the average value of their elements using lambda.
my_list = [[2], [0], [1, 3], [0, 7], [9, 11], [28, 1, 1, 1], [13, 15, 17]]

q28_2 = sorted(my_list, key = lambda x: sum(x) / float(len(x)))
q28_2

# 28.3
# Task: Write a Python program to sort a list of lists by the product of the elements in each sublist using lambda.
my_list = [[2], [0], [1, 3], [0, 7], [9, 11], [28, 1, 1, 1], [13, 15, 17]]
q28_3 = sorted(my_list, key = lambda x: reduce(lambda a, b: a*b, x))
q28_3

# 28.4
# Task: Write a Python program to sort a list of lists by the count of even numbers in each sublist using lambda.
my_list = [[2], [0], [1, 3], [0, 2, 7], [9, 11], [28, 1, 1, 1], [13, 15, 17]]

q28_4 = sorted(my_list, key = lambda sublist: sum(map(lambda x: x % 2 == 0, sublist)))   
q28_4

# 29.0
# Task: Write a Python program to find the maximum value in a given heterogeneous list using lambda.
my_list = ['Python', 3, 2, 4, 5, 'version']

q29 = max(my_list, key = lambda x: (isinstance(x, int), x))
q29

# 29.1
# Task: Write a Python program to find the minimum value in a heterogeneous list using lambda, ignoring non-comparable types.
my_list = ['Python', 3, 2, 4, 5, 'version']
q29_1 = min(filter(lambda x: isinstance(x, int), my_list))
q29_1

# 29.2
# Task: Write a Python program to determine the maximum string (lexicographically) in a heterogeneous list using lambda.
my_list = ['Python', 3, 2, 4, 5, 'version']
q29_2 = max(my_list, key = lambda x: (isinstance(x, str), x))
q29_2

# 29.3
# Task: Write a Python program to find the longest element in a heterogeneous list based on length (for strings) or value (for numbers) using lambda. 
my_list = ['Python', 3, 2, 4, 15, 'version']
q29_3 = max(my_list, key = lambda x: len(x) if isinstance(x, str) else x)
q29_3  

# 29.4
# Task: Write a Python program to extract numeric values from a heterogeneous list and calculate their average using lambda.
my_list = ['Python', 3, 2, 4, 15, 'version']

nums = list(filter(lambda x: isinstance(x, int), my_list))
average = lambda lst: sum(lst) / float(len(lst))

q29_4 = average(nums) 

# 30.0
# Task: Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. 
my_matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

q30 = sorted(my_matrix, key = lambda vector: sum(vector))

# 30.1
# Task: Write a Python program to sort a matrix in descending order according to the product of its rows using lambda.
my_matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

q30_1 = sorted(my_matrix, key = lambda vector: reduce(lambda a,b: a*b, vector), reverse=True)

# 30.2
# Task: Write a Python program to sort a matrix based on the maximum element in each row using lambda.
my_matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

q30_2 = sorted(my_matrix, key = lambda vector: max(vector))
q30_2

# 30.3
# Task: Write a Python program to sort a matrix based on the difference between the first and last elements of each row using lambda.
my_matrix = [[1, 2, 3], [2, 2, 5], [1, 1, 1]]
q30_3 = sorted(my_matrix, key = lambda vector: abs(vector[0] - vector[len(vector)-1]))


# 30.4
# Task: Write a Python program to sort a matrix by the average of its rows in descending order using lambda. 
my_matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

q30_4 = sorted(my_matrix, key = lambda vector: sum(vector) / float(len(vector)), reverse=True)
q30_4

# 31.0
# Task: Write a Python program to extract a specified size of strings from a given list of string values using lambda. 
my_list = ['Python', 'list', 'exercises', 'practice', 'solution']
length = 4

q31 = list(filter(lambda s: len(s) == length, my_list))
q31

# 31.1
# Task: Write a Python program to extract strings from a list that contain exactly a specified number of vowels using lambda. 
my_list = ['Python', 'list', 'exercises', 'practice', 'solution']
vowels = 2

q31_1 = list(filter(lambda s: sum(1 if c in 'aeiouAEIOU' else 0 for c in s) > vowels, my_list))

# 31.2
# Task: Write a Python program to extract strings that are exactly half the length of the longest string in the list using lambda.
my_list = ['Python', 'list', 'exercises', 'practice', 'solution']

q31_2 = list(filter(lambda s: len(s) == len(max(my_list, key = lambda x: len(x)))/2, my_list))
q31_2

# 31.3
# Task: Write a Python program to extract strings that start and end with a given character using lambda.
my_list = ['Python', 'list', 'exercises', 'practice', 'solution']

q31_3 = list(filter(lambda s: s.lower().startswith('p') and s.lower().endswith('n'), my_list))
q31_3

# 31.4
# Task: Write a Python program to extract strings whose length is a prime number using lambda.
my_list = ['Python', 'list', 'exercises', 'practice', 'solution']
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**.5) + 1))

q31_4 = list(filter(lambda s: is_prime(len(s)), my_list))
q31_4

# 32.0
# Task: Write a Python program to count float values in a mixed list using lambda.
my_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

q32 = len(list(filter(lambda x: isinstance(x, float), my_list))) 
#q32 = sum((1 if isinstance(item, float) else 0 for item in my_list))

# 32.1
# Task: Write a Python program to count the integer values in a mixed list using lambda.
my_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
q32_1 = len(list(filter(lambda x: isinstance(x, int), my_list)))


# 32.2
# Task: Write a Python program to count the string values in a mixed list using lambda.
my_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

q32_2 = len(list(filter(lambda x: isinstance(x, str), my_list)))
q32_2

# 32.3
# Task: Write a Python program to count all numeric values (both integers and floats) in a mixed list using lambda.
my_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
q32_3 = sum((1 if isinstance(item, (int, float)) else 0 for item in my_list))
q32_3

# 32.4
# Task: Write a Python program to count the occurrences of boolean values in a mixed list using lambda.
my_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22, False, True]
q32_4 = len(list(filter(lambda x: isinstance(x, bool), my_list)))
q32_4


## 33.0
# Task: Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.

def check_string():
    string = input("Enter password: ")
    messg = [
        lambda string: any(c.isupper() for c in string) or "String must have one uppercase character.",
        lambda string: any(c.islower() for c in string) or "String must have one lowercase character.",
        lambda string: any(c.isdigit() for c in string) or "String must have one digit.",
        lambda string: len(string) >= 6 or "String must have at least 6 characters."
    ]
    
    result = [x for x in [i(string) for i in messg] if x != True]
    
    if not result:
        result.append("Valid string.")
    
    return result
 
# 33.1
# Task: Write a Python program to validate if a string contains at least one special character, one number, and both uppercase and lowercase letters using lambda.

def check_string():
    password = input("Enter password: ")
    messg = [
        lambda password: any(c in punctuation for c in password) or "String must have at least one special character.",
        lambda password: any(c.isdigit() for c in password) or "String must have at least one digit.",
        lambda password: any(c.isupper() for c in password) or "String must have at least one uppercase character.",
        lambda password: any(c.islower() for c in password) or "String must have at least one lowercase character."
    ]
    
    result = [x for x in [i(password) for i in messg] if x != True]
    
    if not result: 
        result.append("Valid string.")
        
    return result
    

# 33.2 
# Task: Write a Python program to check if a string contains no whitespace, includes at least one digit, and at least one uppercase letter using lambda.

def check_string():
    password = input("Enter password: ")
    messg = [ 
        lambda password: all(c != " " for c in password) or "String must not contain whitespace.",
        lambda password: any(c.isdigit() for c in password) or "String must have at least one digit.",
        lambda password: any(c.isupper() for c in password) or "String must contain at least one uppercase letter."
    ]    
    result = [x for x in [i(password) for i in messg] if x != True]
        
    if not result:
        result.append("Valid string.")
        
    return result   
    
# 33.3
# Task: Write a Python program to verify if a string qualifies as a strong password (uppercase, lowercase, digit, special character, minimum length 8) using lambda.

def check_string():
    password = input("Enter password: ")
    messg = [
        lambda password: any(c.isupper() for c in password) or "Password must contain one uppercase character.",
        lambda password: any(c.islower() for c in password) or "Password must contain one lowercase character.",
        lambda password: any(c.isdigit() for c in password) or "Password must contain one digit.",
        lambda password: len(password) >= 8 or "Password must have a minimum length of 8."
    ]
    
    result = [x for x in [i(password) for i in messg] if x != True]
    
    if not result:
        result.append("Valid string.")
        
    return result
  
# 33.4
# Task: Write a Python program to check if a string contains exactly two uppercase letters, three lowercase letters, and one digit using lambda.

def check_string():
    pw = input("Enter password: ")
    messg = [
    lambda pw: True if sum((1 if c.isupper() else 0 for c in pw)) >= 2 else "The password must contain at least two uppercase characters.",
    lambda pw: True if sum((1 if c.islower() else 0 for c in pw)) >= 3 else "The password must contain at least three lowercase letters.",
    lambda pw: any(c.isdigit() for c in pw) or "The password must contain at least one digit."    
    ]
    
    result = [x for x in [i(pw) for i in messg] if x != True]
    
    if not result:
        result.append("Valid password.")
    
    return result
 
# 34.0
# Task: Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda. 
my_dict = {
    'Cierra Vega': (6.2, 70),
    'Alden Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (5.8, 66)
}

q34 = dict(filter(lambda x: x[1][0] > 6.0 and x[1][1] > 65, my_dict.items()))
q34

# 34.1
# Task: Write a Python program to filter students from a dictionary based on weight and age using lambda.
my_dict = {
    "Alice": {"age": 19, "weight": 55},
    "Bob": {"age": 22, "weight": 78},
    "Charlie": {"age": 20, "weight": 68},
    "Diana": {"age": 18, "weight": 50},
    "Ethan": {"age": 25, "weight": 90}
}

q34_1 = dict(filter(lambda x: (x[1]['age'] > 18 and x[1]['weight'] > 55), my_dict.items()))

# 34.2
# Task: Write a Python program to filter a dictionary of students to include only those whose height is above a threshold and whose names start with a vowel using lambda.
my_dict = {
    "Alice": {"height": 168},
    "Ethan": {"height": 182},
    "Olivia": {"height": 170},
    "Uma": {"height": 160},
    "Brian": {"height": 175},
    "Chris": {"height": 180}
}

q34_2 = dict(filter(lambda x: (x[1]['height'] > 180 and x[0].lower().startswith(('a', 'e', 'i', 'o', 'u'))), my_dict.items()))
q34_2

# 34.3
# Task: Write a Python program to filter a dictionary of students by height range and a minimum score using lambda.
my_dict = {
    "Liam": {"height": 165, "score": 82},
    "Noah": {"height": 172, "score": 91},
    "Emma": {"height": 158, "score": 88},
    "Sophia": {"height": 180, "score": 95},
    "Mason": {"height": 169, "score": 76}
}

q34_3 = lambda input_dict, min_height, max_height, min_score: dict(filter(lambda x: (min_height <= x[1]['height'] <= max_height and x[1]['score'] > min_score), input_dict.items()))
q34_3
# 34.4
# Task: Write a Python program to filter students based on multiple criteria such as height, weight, and gender using lambda.
my_dict = {
    "Anna": {"height": 162, "weight": 54, "gender": "F"},
    "Mark": {"height": 178, "weight": 80, "gender": "M"},
    "Julia": {"height": 170, "weight": 65, "gender": "F"},
    "Tom": {"height": 185, "weight": 92, "gender": "M"},
    "Eva": {"height": 160, "weight": 58, "gender": "F"}
}

q34_4 = dict(filter(lambda x: (x[1]['height'] > 180 and x[1]['weight'] < 60 and x[1]['gender'] == 'F' and x[0] == "Miriam"), my_dict.items()))
q34_4

# 35.0
# Task: Write a Python program to check whether a specified list is sorted or not using lambda.
my_list = [1, 2, 4, 6, 8, 10, 12, 14, 166, 17]

q35 = True if sorted(my_list) == my_list else False

# 35.1
# Task: Write a Python program to check if a list is sorted in descending order using lambda.
my_list = [10, 9, 8, 7, 6, 5, 2, 1]

q35_1 = True if my_list[::1] == my_list else False

# 35.2
# Task: Write a Python program to verify if a list of strings is sorted lexicographically, ignoring case, using lambda.
my_list = ["vestron", "vulture", "seaghull", "einstein", "bartolomeus", "rudiger"]

q35_2 = True if sorted(my_list, key = lambda s: s.lower()) == my_list else False

# 35.3
# Task: Write a Python program to check if a list of tuples is sorted based on the second element using lambda.
my_list = [(11, 14, 11), (66, 24, 62, 12), (77, 432, 12, 75), (88, 22, 11), (33, 18, 43)]

q35_3 = True if sorted(my_list, key = lambda x: x[1]) == my_list else False

# 35.4
# Task: Write a Python program to determine if a list is sorted based on a custom comparator (e.g., even numbers followed by odd numbers) using lambda.
my_list = [2, 4, 6, 8, 10, 12, 13, 15, 17, 19, 21, 23, 25]

q35_4 = True if sorted(my_list, key = lambda x: (x % 2 != 0)) == my_list else False

# 36
# Task: Write a Python program to extract the nth element from a given list of tuples using lambda.
my_tuple = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 91, 94),
    ('Beau Turnbull', 94, 98)
]

q36 = lambda input_tuple, ele: tuple(map(lambda t: t[ele], input_tuple))
q36

# 36.1
# Task: Write a Python program to extract the last element from each tuple in a given list using lambda.
my_tuple = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 91, 94),
    ('Beau Turnbull', 94, 98)
]

q36_1 = tuple(map(lambda t: t[len(t)-1], my_tuple))
q36_1

# 36.2
# Task: Write a Python program to extract the element at a specified index from each tuple only if the tuple's length exceeds that index using lambda.
my_tuple = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 2, 94),
    ('Beau Turnbull', 94, 98)
]

q36_2 = lambda input_tuple, ele: list(map(lambda t: t[ele], list(filter(lambda t: len(t) > t[ele], input_tuple))))
q36_2

# 36.3
# Task: Write a Python program to extract the middle element from each tuple in a list using lambda

my_tuple = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 91, 94),
    ('Beau Turnbull', 94, 98, 1111)
]

q36_3 = list(map(lambda t: t[int(len(t)/2)], my_tuple)) 
q36_3 

# 36.4
# Task: Write a Python program to extract elements using negative indexing from each tuple in a list using lambda.

my_tuple = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 91, 94),
    ('Beau Turnbull', 94, 98)
]

q36_4 = list(map(lambda t: t[-3], my_tuple))
q36_4

# 37
# Task: Write a Python program to sort a list of lists by a given index of the inner list using lambda.
my_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 

q37 = lambda lst, ele: sorted(lst, key = lambda t: t[ele])
q37

# 37.1
# Task: Write a Python program to sort a list of lists by the element at a specified index in each inner list using lambda.
my_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

q37_1 = lambda lst, ele: sorted(lst, key = lambda t: t[ele])

# 37.2
# Task: Write a Python program to sort a list of lists by the sum of the elements in the inner list using lambda.
my_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

q37_2 = sorted(my_list, key = lambda t: sum(filter(lambda x: isinstance(x, int), t)))
q37_2

# 37.3
# Task: Write a Python program to sort a list of lists by the difference between two specified indices using lambda.
my_list = [['Greyson Fulton', 98, 99], ['Brady Kent', 97, 96], ['Wyatt Knott', 91, 94], ['Beau Turnbull', 94, 98]]

q37_3 = lambda lst, ele1, ele2: sorted(lst, key = lambda l: abs((l[ele1] if isinstance(l[ele1], (int, float)) else 0) - (l[ele2] if isinstance(l[ele2], (int, float)) else 0)))
q37_3

# 37.4
# Task: Write a Python program to sort a list of lists by the maximum element in each inner list using lambda.
my_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

q37_4 = sorted(my_list, key = lambda l: max(filter(lambda x: isinstance(x, int), l)))
q37_4

# q38
# Task: Write a Python program to remove all elements from a given list present in another list using lambda.
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = [2, 4, 6, 8]

q38 = list(filter(lambda x: x in my_list2, my_list1))

# q38.1
# Task: Write a Python program to retain only those elements in a list that are not present in another reference list using lambda.
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = [3, 7, 5, 9]

q38_1 = list(filter(lambda x: x not in my_list2, my_list1))

# q38.2
# Task: Write a Python program to remove duplicates from one list based on the elements in another list using lambda.
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = [3, 7, 5, 9, 10, 13]

q38_2 = list(filter(lambda x: x not in my_list2, my_list1))

# q38.3
# Task: Write a Python program to filter out elements from a list that are multiples of any element in a given reference list using lambda. 
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = [3, 7, 5, 9, 10, 13]

q38_3 = list(filter(lambda x: not any(x % r == 0 for r in my_list2), my_list1))
q38_3
# q38.4
# Task: Write a Python program to remove elements from a list if they appear more than once in another list using lambda. 
my_list1 = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]
my_list2 = [3, 7, 5, 9, 10, 13]

q38_4 = list(filter(lambda x: my_list1.count(x) <= 1, my_list2))
q38_4

# 39.0 
# Task: Write a Python program to find the elements of a given list of strings that contain a specific substring using lambda.
my_list = ['red', 'black', 'white', 'green', 'orange']
substring = 'ed'
q39 = list(filter(lambda x: substring in x, my_list))
q39

# 39.1 
# Task: Write a Python program to find strings in a list that end with a specified substring using lambda.
my_list = ["red", "black", "white", "green", "orange", "teal", "purple"]
substring = 'ite'

q39_1 = list(filter(lambda x: x.endswith(substring), my_list))

# 39.2
# Task: Write a Python program to find strings that start with a given substring using lambda.
my_list = ["red", "black", "white", "green", "orange", "teal", "purple"]
substring = 'bla'

q39_2 = list(filter(lambda x: x.startswith(substring), my_list))

# 39.3
# Task: Write a Python program to find strings that contain a specified substring in a case-insensitive manner using lambda.
my_list = ["red", "black", "white", "green", "orange", "teal", "purple"]
substring = "Ack"

q39_3 = list(filter(lambda x: substring.lower() in x, my_list))

# 39.4
# Task: Write a Python program to count how many strings in a list contain a specific substring using lambda.
my_list = ["red", "black", "white", "green", "orange", "teal", "purple"]
substring = "Ack"

q39_4 = sum((1 if substring.lower() in string else 0 for string in my_list))

# 40.0
# Task: Write a Python program to find the nested list elements, which are present in another list using lambda.
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
my_list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

q40 = [list(filter(lambda x: x in my_list1, sublist)) for sublist in my_list2]

# 40.1
# Task: Write a Python program to find nested list elements that are absent in another given list using lambda.
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
my_list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

q40_1 = [list(filter(lambda x: x not in my_list1, sublist)) for sublist in my_list2]

# 40.2
# Task: Write a Python program to find common elements across multiple nested lists using lambda.
my_list1 = [[12, 18, 1237, 751, 8231], [4111, 11, 624, 24, 131], [2, 90, 17, 1, 2, 16]]
my_list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

q40_2 = list(filter(lambda x: x in set(sum(my_list1, [])), set(sum(my_list2, []))))
q40_2

# 40.3
# Task: Write a Python program to flatten a list of nested lists and then remove elements that appear in a reference list using lambda.
my_list1 = [[12, 18, 1237, 751, 8231], [4111, 11, 624, 24, 131], [2, 90, 17, 1, 2, 16]]
my_list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

flattened_list = [x for sublist in my_list2 for x in sublist]

q40_3 = [list(filter(lambda x: x not in flattened_list, sublist)) for sublist in my_list1]

# 40.4
# Task: Write a Python program to compare two nested lists and return the elements that differ using lambda.
my_list1 = [[12, 18, 1237, 751, 8231], [4111, 11, 624, 24, 131], [2, 90, 17, 1, 2, 16]]
my_list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

q40_4 = list((lambda a, b: a ^ b)(set(sum(my_list1, [])), set(sum(my_list2, []))))

# 41.0
# Task: Write a Python program to reverse strings in a given list of string values using lambda. 
my_list = ['Red', 'Green', 'Blue', 'White', 'Black']

q41 = list(map(lambda x: x[::-1], my_list))

# 41.1
# Task: Write a Python program to reverse only the vowels in each string of a list using lambda.
my_list = ['Red', 'Green', 'Blue', 'White', 'Black']
vowels = "aeiouAEIOU"

q41_1 = list(map(lambda s:
    (lambda v: ''.join(map(lambda c: v.pop(0) if c in vowels else c, s)))(list(filter(lambda c: c in vowels, s))[::-1]), my_list
    ))
    
# 41.2
# Task: Write a Python program to reverse each word in a sentence while keeping the word order intact using lambda.
sentence = "I walk the line."

q41_2 = ' '.join(list(map(lambda x: x[::-1], sentence.split(' '))))

# 41.3
# Task: Write a Python program to reverse the order of characters in each string, excluding punctuation, using lambda.
sentence = "I walk the line."

q41_3 = lambda s: (lambda v: ''.join(map(lambda c: v.pop(0) if c not in punctuation else c, s)))(list(filter(lambda c: c not in punctuation, s))[::-1])

# 41.4
# Task: Write a Python program to reverse each string in a list and then sort the list lexicographically using lambda.
my_list = ['Red', 'Green', 'Blue', 'White', 'Black']

q41_4 = sorted(list(map(lambda x: x[::-1], my_list)))

# 42.0 
# Task: Write a Python program to calculate the product of a given list of numbers using lambda.
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = [2.2, 4.12, 6.6, 8.1, 8.3]

q42 = reduce(lambda a,b: a*b, my_list2)

# 42.1
# Task: Write a Python program to calculate the cumulative product of elements in a list using lambda.
my_list = [2.2, 4.12, 6.6, 8.1, 8.3]

q42_1 = list(accumulate(my_list, lambda x, y: x*y))

# 42.2
# Task: Write a Python program to compute the product of only the even numbers in a list using lambda.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

q42_2 = reduce(lambda a, b: a*b, filter(lambda x: x % 2 == 0, my_list))

# 42.3
# Task: Write a Python program to compute the product of numbers in a list after filtering out zeros using lambda.
my_list = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 8, 9, 10]

q42_3 = reduce(lambda a, b: a*b, filter(lambda x: x != 0, my_list))

# 42.4
# Task: Write a Python program to calculate the product of a list of numbers and then compute the sum of its digits using lambda.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

q42_4 = sum(map(int, str(reduce(lambda a, b: a*b, my_list))))

# 43.0
# Task: Write a Python program to multiply all the numbers in a given list using lambda.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

q43 = reduce(lambda a, b: a*b, my_list)

# 43.1
# Task: Write a Python program to multiply all positive numbers in a given list using lambda.
my_list = [1, 2, 3, -3, 4, -6, 5, 6, 7, 8, 9, 10]

q43_1 = reduce(lambda a, b: a*b, filter(lambda x: x > 0, my_list))

# 43.2
# Task: Write a Python program to multiply numbers at even indices in a list using lambda.
my_list = [1, 2, 3, -3, 4, -6, 5, 6, 7, 8, 9, 10]

q43_2 = reduce(lambda a, b: a*b, map(lambda i: my_list[i], filter(lambda i: i % 2 == 0, range(1, len(my_list)))))

# 43.3
# Task: Write a Python program to multiply all numbers in a list and then add a specified constant to the result using lambda.
my_list = [1, 2, 3, -3, 4, -6, 5, 6, 7, 8, 9, 10]

q43_3 = lambda const: reduce(lambda a, b: a*b, my_list) + const

# 43.4
# Task: Write a Python program to multiply all numbers in a list and then compute the modulus of the result with a given divisor using lambda.
my_list = [1, 2, 3, -3, 4, -6, 5, 6, 7, 8, 9, 10]

q43_4 = lambda divisor: reduce(lambda a, b: a*b, my_list) % divisor

# 44.0
# Task: Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
my_tuples = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))

q44 = tuple(map(lambda t: sum(t) / float(len(t)), my_tuples))

# 44.1
# Task: Write a Python program to calculate the median of numbers in a tuple of tuples using lambda.
my_tuples = ((10, 10, 10), (30, 45, 56), (81, 80, 39, 16), (1, 2, 3, 11))

q44_1 = tuple(map(lambda t: ((t[int(len(t)/2)] + t[int(len(t)/2) - 1]) / 2) if len(t) == 4 else t[int(len(t)/2)], my_tuples))

# 44.2
# Task: Write a Python program to compute the average value for each inner tuple separately using lambda.
my_tuples = ((10, 10, 10), (30, 45, 56), (81, 80, 39, 16), (1, 2, 3, 11))

q44_2 = tuple(map(lambda t: sum(t) / float(len(t)), my_tuples))

# 44.3
# Task: Write a Python program to calculate the weighted average of numbers in a tuple of tuples using lambda.
my_tuples = ((10, 10, 10), (30, 45, 56), (81, 80, 39, 16), (1, 2, 3, 11))
weights = ((30, 40, 30), (20, 20, 60), (20, 30, 30, 20), (30, 30, 30, 10))

q44_3 = lambda nums, wts: tuple(map(lambda xw: sum(map(lambda a: a[0] * a[1], zip(xw[0], xw[1]))) / sum(xw[1]), zip(nums, wts)))

# 44.4
# Task: Write a Python program to calculate the average value of numbers in a tuple of tuples, excluding the highest and lowest values in each inner tuple, using lambda.
my_tuples = ((10, 10, 10), (30, 45, 56), (81, 80, 39, 16), (1, 2, 3, 11))

q44_4 = tuple(map(lambda x: sum(sorted(x)[1:-1]) / float(len(sorted(x)[1:-1])), my_tuples))

# 45.0
# Task: Write a Python program to convert string elements to integers inside a given tuple using lambda.
my_tuples = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

q45 = [tuple(map(int, filter(lambda x: x.isdigit(), my_tuple))) for my_tuple in my_tuples]

# 45.1
# Task: Write a Python program to convert numeric string elements to floats inside a tuple of tuples using lambda.
my_tuples = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

q45_1 = [tuple(map(float, filter(lambda x: x.isdigit(), my_tuple))) for my_tuple in my_tuples]

# 45.2
# Task: Write a Python program to convert string elements to integers and replace non-numeric strings with zero using lambda.
my_tuples = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

q45_2 = [tuple(map(lambda x: int(x) if x.isdigit() else 0, my_tuple)) for my_tuple in my_tuples]

# 45.3
# Task: Write a Python program to convert all convertible string elements in a tuple of mixed types to integers using lambda.
my_tuples = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55', '15.2'), ('2345', 'WERT', '34', '16.23'))

is_int = lambda s: s.replace('-', '', 1).isdigit()

q45_3 = [tuple(map(lambda x: int(x) if is_int(x) else str(x), my_tuple)) for my_tuple in my_tuples]

# 45.4
# Task: Write a Python program to convert hexadecimal string elements to integers in a given tuple using lambda.
my_tuples = (
    ('1A', 'FF', 'hello', 25),
    ('0x10', '3B', 'XYZ', 42),
    ('ABC', '12F', 'world', -7),
    ('7E', '19', 'data', 3.14)
)

hexadecimals = "x0123456789ABCDEFabcdef"

is_hex = lambda s: all(c in hexadecimals for c in str(s)) and isinstance(s, str)

q45_4 = [tuple(map(lambda x: int(x, base = 16) if is_hex(x) else x, my_tuple)) for my_tuple in my_tuples]

# 46.0
# Task: Write a Python program to find the index position and value of the maximum and minimum values in a given list of numbers using lambda. 
my_list = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]

q46 = {"max_val": max(enumerate(my_list)), "min_val": min(enumerate(my_list))}

# 46.1
# Task: Write a Python program to find the indices of all occurrences of the maximum value in a list using lambda.
my_list = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54, 89]

q46_1 = tuple(map(lambda x: x[0], filter(lambda x: x[1] == max(my_list), enumerate(my_list))))

# 46.2
# Task: Write a Python program to determine the index positions of the top two maximum values in a list using lambda.
my_list = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54, 89]

q46_2 = list(map(lambda x: x[0], sorted(enumerate(my_list), key = lambda x: x[1])))[-2::]

# 46.3
# Task: Write a Python program to return the index and value of the first occurrence of the minimum value in a list using lambda.
my_list = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54, 89]

q46_3 = min(enumerate(my_list), key = lambda x: x[1])

# 46.4
# Task: Write a Python program to find the indices of both the maximum and minimum values in a list and swap them using lambda.
my_list = [12, 33, 23, 10.11, 67, 16, 45, 66.7, 23, 12, 11, 10.25, 54, 89]

def swap_minmax(lst):
    min_ind = min(enumerate(my_list), key = lambda x: x[1])[0]
    max_ind = max(enumerate(my_list), key = lambda x: x[1])[0]
    
    lst[max_ind], lst[min_ind] = lst[min_ind], lst[max_ind]

    return lst
 
q46_4 = swap_minmax(my_list)

# 47
# Task: Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
my_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

q47 = sorted(my_list, key = lambda x: (isinstance(x, str), x))

# 47_1
# Task: Write a Python program to sort a mixed list by placing numbers (sorted in ascending order) before strings sorted by length using lambda.
my_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

q47_1 = sorted(my_list, key = lambda x: (isinstance(x, str), (len(str(x)), x)))

# 47_2
# Task: Write a Python program to sort a mixed list with numbers in descending order followed by strings in alphabetical order using lambda.
my_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

q47_2 = sorted(my_list, key = lambda x: (isinstance(x, str), -x if isinstance(x, int) else x))

# 47_3
# Task: Write a Python program to sort a mixed list by ordering negative numbers first, then positive numbers, and finally strings using lambda.
my_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1, -1, 2, -5, 11, -6, 'orange', 'silver', 'gold']

q47_3 = sorted(my_list, key = lambda x: (0 if isinstance(x, (int, float)) and x < 0 else 1 if isinstance(x, (int, float)) else 2, x))

# 47.4
# Task: Write a Python program to sort a mixed list by converting numbers to strings and sorting them lexicographically using lambda.
my_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1, -1, 2, -5, 0, 'aquamarine']

q47_4 = sorted(my_list, key = lambda x: str(x)) 

# 48.0
# Task: Write a Python program to sort a given list of strings (numbers) numerically using lambda.
my_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

q48 = sorted(my_list, key = lambda x: int(x))

# 48.1
# Task: Write a Python program to sort a list of strings representing floating-point numbers numerically using lambda.
my_list = ['4.11', '12.75', '45.15', '7.6', '0.12', '100.12', '200.11', '-12.78', '-500.98']

q48_1 = sorted(my_list, key = lambda x: float(x))
q48_1

# 48.2
# Task: Write a Python program to sort a list of numeric strings in descending order using lambda.
my_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

q48_2 = sorted(my_list, key = lambda x: int(x), reverse = True)

# 48.3
# Task: Write a Python program to sort a list of numeric strings that include negative values correctly using lambda.
my_list = ['4', '12', '-45', '-7', '0', '-100', '200', '-12', '-500']

q48_3 = sorted(my_list, key = lambda x: int(x))

# 48.4
# Task: Write a Python program to sort a list of alphanumeric strings by extracting and sorting the numeric parts using lambda.
my_list = ['aaaa4', 'dafv12', 'hwe145', 'dsaf7dfa', 'dda0gasd', 'dfasagds100', 'dsag20gda0', '-1gads2dsaga', '-dsafa5fsdafa0fdas0']
nums = [list(filter(lambda c: c.isdigit() or c == '-', item)) for item in my_list]
nums = [''.join(sublist) for sublist in nums]

q48_4 = sorted(nums, key = lambda x: int(x),reverse = True)

# 49.0
# Task: Write a Python program to count the occurrences of items in a given list using lambda.
my_list = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]

q49 = dict(map(lambda x: (x, list(my_list).count(x)), my_list))

# 49.1
# Task: Write a Python program to count the occurrences of each character in a string using lambda.
my_string = "Super Marius"

q49_1 = dict(map(lambda c: (c, list(my_string).count(c)), my_string))

# 49.2
# Task: Write a Python program to count the occurrences of each word in a list using lambda.
my_list = ['orange', 'teal', 'aquamarine', 'darkred', 'stellar', 'gloss', 'stellar', 'goldline']

q49_2 = dict(map(lambda word: (word, my_list.count(word)), my_list))

# 49.3
# Task: Write a Python program to count the frequency of even and odd numbers separately in a list using lambda.
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

q49_3 = {"Even": len(list(filter(lambda x: x % 2 == 0, my_list))), "Odd": len(list(filter(lambda x: x % 2 != 0, my_list)))}


# 49.4
# Task: Write a Python program to count the occurrences of items in a list and return a dictionary sorted by frequency using lambda.
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 7, 4, 4, 3, 3, 2, 2, 1, 5, 5, 5, 5, 5, 5, 4, 4]

q49_4 = dict(sorted(dict(map(lambda x: (x, my_list.count(x)), my_list)).items(), key = lambda x: x[1]))  


# 50.0
# Task: Write a Python program to remove specific words from a given list using lambda.
my_list = ['watchet', 'smaragdine', 'aquamarine', 'falu', 'eburnean', 'atrovirens', 'phlox', 'amaranth', 'fulvous', 'skobeloff', 'sinoper', 'vantablack']

q50 = list(filter(lambda x: any(c in 'aeiouAEIOU' for c in x) == False, my_list))

# 50.1
# Task: Write a Python program to remove words containing a specific substring from a list using lambda.
my_list = ['watchet', 'smaragdine', 'aquamarine', 'falu', 'eburnean', 'atrovirens', 'phlox', 'amaranth', 'fulvous', 'skobeloff', 'sinoper', 'vantablack']
substring = ['ack', 'chet', 'marine', 'lu']
q50_1 = list(filter(lambda x: any(ele in x for ele in substring) == False, my_list))

# 50.2
# Task: Write a Python program to remove words that start with a specified letter from a list using lambda.
my_list = ['watchet', 'smaragdine', 'aquamarine', 'falu', 'eburnean', 'atrovirens', 'phlox', 'amaranth', 'fulvous', 'skobeloff', 'sinoper', 'vantablack']
letter = 's'

q50_2 = list(filter(lambda s: s[0] != letter, my_list))


# 50.3
# Task: Write a Python program to remove words that have a length shorter than a given threshold from a list using lambda.
my_list = ['watchet', 'smaragdine', 'aquamarine', 'falu', 'eburnean', 'atrovirens', 'phlox', 'amaranth', 'fulvous', 'skobeloff', 'sinoper', 'vantablack']
min_length = 6

q50_3 = list(filter(lambda s: len(s) >= 6, my_list))

# 50.4
# Task: Write a Python program to remove duplicate words from a list using lambda.
my_list = ['watchet', 'smaragdine', 'aquamarine', 'falu', 'eburnean', 'atrovirens', 'phlox', 'amaranth', 'fulvous', 'skobeloff', 'sinoper', 'vantablack', 'falu', 'aquamarine']

q50_4 = list(filter(lambda s: my_list.count(s) == 1, my_list))

# 51
# Task: Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.
my_list = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

q51 = {'max': max(my_list, key = lambda item: item[1])[1], 'min': min(my_list, key = lambda item: item[1])[1]}

# 51.1
# Task: Write a Python program to find the tuple with the maximum sum of its elements using lambda.
my_list = [('V', 62, 45), ('VI', 68, 64), ('VII', 72, 65), ('VIII', 70, 99), ('IX', 74, 16), ('X', 65, 11)]

q51_1 = max(my_list, key = lambda tpl: sum(filter(lambda x: isinstance(x, int), tpl)))

# 51.2
# Task: Write a Python program to find the tuple with the minimum product of its elements using lambda.
my_list = [('V', 62, 45), ('VI', 68, 64), ('VII', 72, 65), ('VIII', 70, 99), ('IX', 74, 16), ('X', 65, 11)]

q51_2 = min(my_list, key = lambda tpl: reduce(lambda a, b: a*b, filter(lambda x: isinstance(x, int), tpl)))

# 51.3
# Task: Write a Python program to identify the tuple with the maximum difference between its elements using lambda.
my_list = [('V', 62, 45), ('VI', 68, 64), ('VII', 72, 65), ('VIII', 70, 99), ('IX', 74, 16), ('X', 65, 11)]

q51_3 = max(my_list, key = lambda tpl: reduce(lambda a,b : abs(a-b), filter(lambda x: isinstance(x, int), tpl)))

# 51.4
# Task: Write a Python program to find both the tuple with the longest first element and the tuple with the shortest last element using lambda.
my_list = [('V', 62, 45), ('VI', 68, 64), ('VII', 72, 65), ('VIII', 70, 99), ('IX', 74, 1), ('X', 65, 11)]

q51_4 = [max(my_list, key = lambda tpl: len(str(tpl[0]))), min(my_list, key = lambda tpl: len(str(tpl[-1])))]

# 52.0
# Task: Write a Python program to remove None values from a given list using the lambda function.
my_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

q52 = list(filter(lambda item: item != None, my_list))

# 52.1
# Task: Write a Python program to remove all falsy values (None, 0, '', False) from a given list using lambda.
my_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12, '']

q52_1 = list(filter(lambda item: item not in [None, 0, '', False], my_list))

# 52.2
# Task: Write a Python program to filter out None and empty string values from a list using lambda.
my_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12, '']

q52_2 = list(filter(lambda item: item not in [None, ''], my_list))

# 52.3
# Task: Write a Python program to remove None values from a list and then sort the remaining elements using lambda.
my_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

q52_3 = sorted(filter(lambda x: x != None, my_list))

# 52.4
# Task: Write a Python program to remove None values from a list and replace them with a specified default value using lambda.
my_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

q52_4 = lambda val: list(map(lambda item: val if item == None else item, my_list))

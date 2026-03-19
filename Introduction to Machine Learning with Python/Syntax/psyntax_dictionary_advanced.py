from pprint import pprint
from operator import itemgetter, getitem
from collections import OrderedDict, Counter, defaultdict
from functools import reduce
from math import prod, floor
from itertools import product, combinations, groupby
from heapq import nlargest
from string import punctuation
from tabulate import tabulate
import pandas as pd

### TO REPEAT 17

# 1.0
# Task: Write a Python script to sort (ascending and descending) a dictionary by value. 
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

result = sorted(d.items(), key = lambda x: x[1])

# OR

result = sorted(d.items(), key = itemgetter(1))

# 1.1
# Task: Write a Python script to sort a dictionary by its values in ascending order using lambda functions.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def sort_dict(input_dict, reverse = False):
    return sorted(input_dict.items(), key = lambda x: x[1], reverse = reverse)
    

result = sort_dict(d)

# 1.2
# Task: Write a Python script to sort a dictionary by its values in descending order and output the sorted key-value pairs as tuples.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def sort_dict(input_dict, reverse = False):
    return sorted(input_dict.items(), key = itemgetter(1), reverse = reverse)


result = sort_dict(d, True) 

# 1.3
# Task: Write a Python script to implement dictionary sorting by value without using the built‐in sorted() function.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def my_sorted(input_dict, reverse = False):
    items = list(input_dict.items())
    
    if reverse == False:
        for i in range(len(items)):
            min_index = i
            for j in range(i+1, len(items)):
                if items[j][1] < items[min_index][1]:
                    min_index = j
            
            items[i], items[min_index] = items[min_index], items[i]
               
    else:
        for i in range(len(items)):
            max_index = i
            for j in range(i+1, len(items)):
                if items[j][1] > items[max_index][1]:
                    max_index = j
            
            items[i], items[max_index] = items[max_index], items[i]
            
    
    return dict(items)

result = my_sorted(d, reverse = True)

# OR

def my_sorted(input_dict, reverse = False):
    items = list(input_dict.items())
    
    items.sort(key = lambda x: x[1], reverse = reverse)
    
    return dict(items)
    
result = my_sorted(d)

# 1.4
# Task: Write a Python script to compare two different methods of sorting a dictionary by value and print their results.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Method 1: Standard for loop.

def my_sorted(input_dict, reverse = False):
    items = list(input_dict)
    
    if reverse == True:
        for i in range(len(items)):
            max_index = i
            for j in range(i+1, len(items)):
                if items[j][1] > items[max_index][1]:
                    max_index = j
            
            items[i], items[max_index] = items[max_index], items[i]
    
    else:
        for i in range(len(items)):
            min_index = i
            for j in range(i+1, len(items)):
                if items[j][1] < items[min_index][1]:
                    min_index = j
                        
            items[i], items[min_index] = items[min_index], items[i]
        
    return dict(items)

# Method 2: Using list().sort

def my_sorted(input_dict, reverse = False):
    items = list(input_dict.items())
    items.sort(key = itemgetter(1), reverse = reverse)
    
    return dict(items)
    
result = my_sorted(d, reverse=True)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 2.0
# Task: Write a Python program to add a key to a dictionary.
d = {0: 10, 1: 20}

d.update({2: 40})

# 2.1
# Task: Write a Python script to add a new key=value pair to a dictionary only if the key does not exist already.
d = {0: 10, 1: 20, 2: 40}

def update_if_not(input_dict, to_update):
    if to_update not in input_dict.items():
        input_dict.update(to_update)
    else:
        return input_dict
    
    return input_dict
 
result = update_if_not(d, {2: 40}) 

# 2.2
# Task: Write a Python script to update a dictionary with multiple new keys from a list, setting each to default value.
d = {0: 10, 1: 20, 2: 40}
key_list = [{5: 100}, {7: 140}, {9: 180}, {12: 240}, {16: 320}]

def update_from_list(input_dict, keys):
    for item in keys:
            input_dict.update(item)
    return input_dict

result = update_from_list(d, key_list)

# 2.3
# Task: Write a Python script to merge a list of key-value pairs into an existing dictionary without overwriting existing keys.
d = {0: 10, 1: 20, 2: 40}
key_list = [{5: 100}, {7: 140}, {9: 180}, {12: 240}, {16: 320}]

def update_from_list(input_dict, keys):
    for item in keys:
        input_dict.update(item)
    return input_dict

result = update_from_list(d, key_list)


# 2.4
# Task: Write a Python script to insert a key into a dictionary at a specific position while preserving insertion order.
d = {0: 10, 1: 20, 2: 40}

def insert_key_value(input_dict, pos_ind, key, value):
    out_dict = {}
    if pos_ind == len(input_dict):
        out_dict = input_dict 
        out_dict.update({key: value})
    elif 0 <= pos_ind < len(input_dict):
        for k, v in input_dict.items():
            if k == pos_ind:
                out_dict[key] = value
            out_dict[k] = v
    else:
        raise IndexError("outta range")
    
    return out_dict

result = insert_key_value(d, 3, 16, 320)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ # #

# 3.0
# Task: Write a Python script to concatenate the following dictionaries to create a new one.
my_dict1 = {1: 10, 2: 20}
my_dict2 = {3: 30, 4: 40}
my_dict3 = {5: 50, 6: 60}

def concatenate_dicts(*args):
    out_dict = {}
    for item in args:
        out_dict.update(item)
    return out_dict

result = concatenate_dicts(my_dict1, my_dict2, my_dict3)

# 3.1
# Task: Write a Python script to merge three dictionaries into one using dictionary unpacking.
my_dict1 = {1: 10, 2: 20}
my_dict2 = {3: 30, 4: 40}
my_dict3 = {5: 50, 6: 60}

def merge_dicts(*args):
    out_dict = {}
    for item in args:
        out_dict.update({**item})
    
    return out_dict

result = merge_dicts(my_dict1, my_dict2, my_dict3)

# 3.2
# Task: Write a Python script to combine multiple dictionaries and resolve key conflicts by summing their values.
my_dict1 = {1: 10, 2: 20}
my_dict2 = {3: 30, 2: 40}
my_dict3 = {5: 50, 6: 60}

def merge_sum(*args):
    out_dict = {}
    for item in args:
        for k, v in item.items():
            out_dict[k] = out_dict.get(k, 0) + v  
    
    return out_dict
    
result = merge_sum(my_dict1, my_dict2, my_dict3)
    
# 3.3
# Task: Write a Python script to merge two dictionaries recursively when values are also dictionaries.
my_dict1 = {1: {'x': 10}, 2: {'y': 20}, 2: {'z': 20}, 3: {'a': 30}}
my_dict2 = {4: {'b': 40}, 5: {'c': 50}, 6: {'d': 60}, 7: {'e': 70}}

def recursive_merge(*args):
    def merge_two(a, b):
        result = a.copy()
        
        for k, v in b.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = merge_two(result[k], v)
            else:
                result[k] = v
        
        return result
    
    out_dict = {}
    for item in args:
        out_dict = merge_two(out_dict, item)
    
    return out_dict

result = recursive_merge(my_dict1, my_dict2)

# 3.4
# Task: Write a Python script to implement dictionary concatenation without using the built-in update() method.
my_dict = {1: 10, 2: 20} 

def my_update(input_dict, to_update):
    items = list(input_dict.items())
    for k, v in to_update.items():
        items.append((k, v))
    
    return dict(items)

result = my_update(my_dict, {3: 30})

# OR
def my_update(input_dict, to_update):
    return {k: v for d in (input_dict, to_update) for k, v in d.items()}
    
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 4.0
# Task: Write a Python program to check whether a given key already exists in a dictionary.
my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def contains_key(input_dict, key):
    if key in input_dict:
        return True
    
    return False
         
result = contains_key(my_dict, 4)

# 4.1
# Task: Write a Python script to check if a given key exists in a dictionary using the in operator.
my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def contains_value(input_dict, key):
    if key in input_dict:
        return True
    return False
    
result = contains_value(my_dict, 60)

# 4.2
# Task: Write a Python script to determine key existence by iterating through the dictionary keys.
my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def contains_key_iter(input_dict, key):
    for k in input_dict:
        if key == k:
            return True
    return False

result = contains_key_iter(my_dict, 3)

# 4.3
# Task: Write a Python script to use the get() method to check for a key and return a default value if it is missing.
my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def get_key_value(input_dict, key):
    return input_dict.get(key, 0)
    
result = get_key_value(my_dict, 3)

# 4.4
# Task: Write a Python script to implement a function that returns True if a key exists in a dictionary and False otherwise.
my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def contains_key(input_dict, key):
    return key in input_dict
    
result = contains_key(my_dict, 6)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 5.0
# Task: Write a Python program to iterate over dictionaries using for loops.
d = {'w': 5, 'x': 10, 'y': 20, 'z': 30} 

#for k, v in my_dict.items():
#    print(k, " --> ",v)


# 5.1
# Task: Write a Python program to iterate over a dictionary and print each key and its corresponding value.
d = {'w': 5, 'x': 10, 'y': 20, 'z': 30}

#for i in d.items():
#    print(i)
    
# 5.2
# Task: Write a Python program to iterate over a dictionary's items using the items() method and display them in a formatted table.
d = {'w': 5, 'x': 10, 'y': 20, 'z': 30}

result = pd.DataFrame(d.items(), columns=["Key", "Values"]) 

# 5.3
# Task: Write a Python program to use a for-loop to iterate over dictionary keys and access values using bracket notation.
d = {'w': 5, 'x': 10, 'y': 20, 'z': 30}

def access_with_bracket(input_dict):
    out = []
    for k in input_dict:
        out.append((k, input_dict[k]))
    return out

result = access_with_bracket(d)

# 5.4
# Task: Write a Python program to iterate over a dictionary and calculate the sum of all its numeric values.
d = {'r': 0, 's': 1,'t': 2,'u': 3,'v': '4','w': 5, 'x': 10, 'y': 20, 'z': 30}

def sum_values(input_dict): 
    res = 0
    for v in input_dict.values():
        if isinstance(v, (int, float)):
            res+=v
    
    return res
        
result = sum_values(d)

# OR
def sum_values(input_dict):
    return sum(v for v in d.values() if isinstance(v, (int, float)))

result = sum_values(d)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #    
    
# 6.0
# Task: Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 20

#for i in range(1,n+1):
#    print({i: i*i})

# 6.1
# Task: Write a Python script to create a dictionary with keys from 1 to n and values as the square of the keys using dictionary comprehension.

def create_dict(n):
    return {k: k*k for k in range(1, n+1)}

result = create_dict(20)

# 6.2
# Task: Write a Python script to generate a dictionary of numbers and their squares and then print the items sorted by key.
n = 20

def create_dict(n):
    return {k: k*k for k in range(1, n+1)}

result = dict(sorted(create_dict(n).items(), key = itemgetter(0)))

# 6.3
# Task: Write a Python script to build the same dictionary iteratively with a for-loop and then compare it to the comprehension result.
n = 20

def create_dict_loop(n):
    d = {}
    for k in range(1, n+1):
        d.update({k: k*k})
    
    return d

def create_dict_comp(n):
    return {k: k*k for k in range(1, n+1)}

result = create_dict_loop(n) == create_dict_comp(n)

# 6.4
# Task: Write a Python script to allow user input for n and output a dictionary mapping each number from 1 to n to its square.
n = 20

def user_dict():
    try:
        n = int(input("Enter an integer: "))
        return {k: k*k for k in range(1, n+1)}
    except ValueError:
        print("Please enter a valid integer.")
        return {}


# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #


# 7.0
# Task: Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

#print({k: k*k for k in range(1, 15+1)})
 
# 7.1
# Task: Write a Python script to create a dictionary with keys from 1 to 15 and their squares as values using a loop. 

def create_dict():
    d = {}
    for n in range(1, 15+1):
        d.update({n:n*n})
    return d

result = create_dict()

# 7.2
# Task: Write a Python script to generate this dictionary using dictionary comprehension and then print it sorted by key.

def create_dict():
    return {k: k*k for k in range(1, 15+1)} 
    
result = dict(sorted(create_dict().items(), key = itemgetter(0)))

# 7.3
# Task: Write a Python script to modify the dictionary so that the values are the cubes of the keys instead of squares.

my_dict = {k: k*k for k in range(1, 15+1)}

def modify_dict(d):
    for k, v in d.items():
        d[k] = v * k
    
    return d

# OR
def modify_dict(d):
    return {k: v * k for k, v in d.items()}

# OR
def modify_dict(d):
    return {k: k**3 for k in d}

result = modify_dict(my_dict)

# 7.4
# Task: Write a Python script to use a function to build a dictionary for numbers 1 to n and then test it with n=15.

def create_dict(n):
    return {k: k*k for k in range(1, n+1)}

result = create_dict(15)


# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 8.0
# Task: Write a Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
   
def merge_dicts(*dicts):
    out = {}
    for d in dicts:
        out.update(d)
    return out

result = merge_dicts(d1, d2)

# 8.1
# Task: Write a Python script to merge two dictionaries and handle overlapping keys by taking the value from the second dictionary.   
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

def merge_dicts(*args):
    return {k: v for d in dicts for k, v in d.items()}
    
# OR
def merge_dict(dct1, dct2):
    out = dct1.copy()
    for k in dct2: 
        out[k] = dct2[k]
    
    return out

# OR
def merge_dicts(dct1, dct2):
    return dct1 | dct2

# OR
def merge_dicts(d1, d2):
    return {**d1, **d2}

# 8.2
# Task: Write a Python script to merge two dictionaries using the unpacking operator (**) and print the result.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

def merge_two(dct1, dct2):
    return {**dct1, **dct2}
    
# 8.3
# Task: Write a Python script to merge two dictionaries recursively when keys map to sub-dictionaries.
d1 = {'a': 100, 'b': {'x': 10, 'y': 20}, 'c': 300}
d2 = {'b': {'y': 999, 'z': 50}, 'd': 400}

def merge_two(dct1, dct2):
    result = dct1.copy()
    
    for k, v in dct2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = merge_two(result[k], v)
        else:
            result[k] = v
    
    return result

result = merge_two(d1, d2)

# 8.4
# Task: Write a Python script to combine dictionaries and, in case of key collisions, concatenate their values if they are strings.
d1 = {'a': 100, 'b': '200', 'c': 200, 'd': 400, 'e': 600, 'f': 800}    
d2 = {'a': 200, 'b': '200', 'y': 400, 'z': 600, 'x': 700, 'd': 700}

def merge_two_concat(a, b):
    result = a.copy()
    
    for k,v in b.items():
        if k in result and isinstance(result[k], str) and isinstance(v, str):
            result[k] += v
        else:
            result[k] = v
    
    return result

result = merge_two_concat(d1, d2)
    
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #    
    
# 9.0
# Task: Write a Python program to iterate over dictionaries using for loops.
d = {'Red': 1, 'Green': 2, 'Blue': 3}

#for color_key in d:
#    print(color_key, "corresponds to", d[color_key])

# 9.1
# Task: Write a Python program to iterate over a dictionary using a for-loop and print each key, value, and index.
d = {'Red': 1, 'Green': 2, 'Blue': 3}

#for i, (k, v) in enumerate(d.items()):
#    print(i, k, v)

# 9.2
# Task: Write a Python program to loop through a dictionary and display its keys sorted in alphabetical order.
d = {'Red': 1, 'Green': 2, 'Blue': 3}

def loop_dict(dct):
    for k in sorted(dct):
        print(k)

#result = loop_dict(d)

# 9.3
# Task: Write a Python program to use dictionary comprehension to iterate and create a new dictionary with modified values.
d = {'Red': 1, 'Green': 2, 'Blue': 3}

def modify_dict(dct):
    return {k: v**17 for k, v in dct.items()}
    
result = modify_dict(d)

# 9.4
# Task: Write a Python program to iterate over a dictionary's keys and values using nested loops to print a formatted output.
d = {'Red': (1, 6), 'Green': (2, 7), 'Blue': (3, 11)}


#for key, values in d.items():
#    print(f"Key: {key}")
#    for v in values:
#        print(f" Value: {v}")


# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 10.0
# Task: Write a Python program to sum all the items in a dictionary.
d = {'Red': (7, 7), 'Green': (16, 166), 'Blue': (74, 234)}

# Method 1:

def sum_dict(dct):
    return sum(v for values in dct.values() for v in values)

# Method 2: 
def sum_dict(dct):
    res = 0
    for k, values in dct.items():
        for v in values:
            res+=v
    
    return res

# Method 3:

def sum_dict(dct):
    return sum(map(sum, dct.values()))

result = sum_dict(d)

# 10.1
# Task: Write a Python program to calculate the sum of all values in a dictionary where values are numbers.
d = {'Red': (7, 7), 'Green': (16, 1, 166), 'Blue': (74, 234, 'grrr')}

def sum_dict(dct):
    return sum(v for values in d.values() for v in values if isinstance(v, (int, float)))

result = sum_dict(d)

# 10.2 
# Task: Write a Python program to use a for-loop to iterate over dictionary values and compute their total sum.
d = {'Red': (6432432, 11), 'Green': (16, 166), 'Blue': (74, 234)}

def sum_dict(dct):
    res = 0
    for k, values in dct.items():
        for v in values:
            res+=v
    return res

result = sum_dict(d)

# 10.3
# Task: Write a Python program to implement a function that returns the sum of the items of a dictionary using the sum() function.
d = {'Red': (6432432, 11), 'Green': (16, 166), 'Blue': (74, 234)}

# Method 1:
def sum_dict(d):
    return sum(v for values in d.values() for v in values)
    
# Method 2:
def sum_dict(dct):
    return sum(map(sum, dct.values()))

result = sum_dict(d)

# 10.4
# Task: Write a Python program to combine values of a dictionary with a reduce() function to compute their sum.
d = {'Red': (6432432, 11), 'Green': (16, 166), 'Blue': (74, 234)}
 
def sum_dict(dct):
    return reduce(lambda a, b: a+b, (x for sublist in dct.values() for x in sublist), 0)
    
result = sum_dict(d)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 11.0
# Task: Write a Python program to multiply all the items in a dictionary.
d = {'data1': 100, 'data2': -54, 'data3': 247}

# Method 1: 
def dict_product(dct):
    return reduce(lambda a, b: a*b, d.values(), 1)

result = dict_product(d)

# Method 2: 
def dict_product(dct):
    result = 1 
    for v in dct.values():
        result*=v
    return result

result = dict_product(d)

# Method 2: 
def dict_product(dct):
    return prod(dct.values())

result = dict_product(d)

# 11.1
# Task: Write a Python program to compute the product of all numeric values in a dictionary using a for-loop.
d = {'a': ('botanics', 12, 66), 'b': (63, 132, 11), 'c': (125123512, 643745235132, 1), 'd': (1231231, 12313, 124214, 1)}

def dict_product(dct):
    res = 1
    for v in (v for values in dct.values() for v in values if isinstance(v, (int, float))):
       if isinstance(v, (int, float)):
            res*=v
    
    return res
    
result = dict_product(d)

# 11.2
# Task: Write a Python program to use functools.reduce() to multiply all values in a dictionary.
d = {'a': ('botanics', 12, 66), 'b': (63, 132, 11), 'c': (125123512, 643745235132, 0), 'd': (1231231, 12313, 124214, 1)}

def dict_product(dct):
    return reduce(lambda a, b: a*b, (v for values in dct.values() for v in values if isinstance(v, (int, float))), 1)

result = dict_product(d)

# 11.3
# Task: Write a Python program to implement a function that iterates through a dictionary and multiplies its values, returning the result.
d = {'a': ('botanics', 12, 66), 'b': (63, 132, 11), 'c': (125123512, 643745235132, 0), 'd': (1231231, 12313, 124214, 1)}

def dict_product(dct):
    res = 1 
    for values in dct.values():
        for v in values:
            if isinstance(v, (int, float)):
                res*=v
    return res

result = dict_product(d)

# 11.4
# Task: Write a Python program to multiply the items in a dictionary and handle the case where the dictionary is empty.
d = {'a': ('botanics', 12, 66, ''), 'b': (63, 132, 11, ''), 'c': (125123512, 643745235132, 0), 'd': (1231231, 12313, 124214, 1)}

def dict_product(dct):
    return prod(v for values in dct.values() for v in values if isinstance(v, (int, float))) 

result = dict_product(d)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 12.0
# Task: Write a Python program to remove a key from a dictionary. 
d = {'a': ('botanics', 12, 66, ''), 'b': (63, 132, 11, ''), 'c': (125123512, 643745235132, 0), 'd': (1231231, 12313, 124214, 1)}

# Method 1: Use a loop.

def remove_key(dct, key):
    items = list(dct.items())
    for k, v in items:
        if k == key:
            items.remove((k, v))
    
    return dict(items)
    
result = remove_key(d, 'a')

# Method 2: Del

def remove_key(dct, key):
    del dct[key]
    return dct
   
result = remove_key(d, 'b')

# 12.1
# Task: Write a Python program to remove a specified key from a dictionary using the del statement.
d = {'a': 16, 'b': 81, 'c': 211, 'd': 52342, 'e': 6341, 'f': 5321}

def remove_key(dct, key):
    del dct[key]
    return dct 
    
result = remove_key(d, 'c')

# 12.2
# Task: Write a Python program to remove a key from a dictionary using the pop() method and return its value.
d = {k: k*k for k in range(1, 11)}

result = d.pop(2)

# 12.3
# Task: Write a Python program to implement a function that deletes a key from a dictionary and handles the case when the key does not exist.
d = {k: k**3 for k in range(1, 11)}

def remove_key(dct, key):
    if key in dct:
        del dct[key]
    return dct
    
result = remove_key(d, 2)

# OR

def remove_key(dct, key):
    dct.pop(key, None)
    
    return dct
    
result = remove_key(d, 2)

# 12.4
# Task: Write a Python program to remove multiple keys from a dictionary by iterating over a list of keys to delete.
k = {k: k**6 for k in range(1, 11)}

def remove_keys(dct, keys):
    items = list(dct.items())
    for k, v in items:
        if k in keys:
            items.remove((k, v))
    return dict(items)
        
# OR
def remove_keys(dct, keys):
    return {k: v for k, v in dct.items() if k not in keys}

result = remove_keys(d, (2, 3, 4, 5))

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 13.0
# Task: Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

def map_lst(key_list, value_list):
    out = {}
    n = len(key_list)
    
    for i in range(n):
        out[key_list[i]] = value_list[i]
    
    return out
    
result = map_lst(keys, values)

# OR
def map_lst(key_list, value_list):
    return dict(zip(key_list, value_list))    

# 13.1
# Task: Write a Python program to convert two lists of equal length into a dictionary using the zip() function.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

def lst_to_dict(key_list, value_list):
    return dict(zip(key_list, value_list))

result = lst_to_dict(keys, values)

# 13.2
# Task: Write a Python program to map two lists into a dictionary, handling duplicate keys by storing values in a list.
keys = ['red', 'green', 'blue', 'ivory', 'lightcyan', 'lightpink', 'blue']
values = ['#FF0000', '#008000', '#0000FF', '#FFFFF0', '#E0FFFF', '#FFB6C1', '#0000FF']

def lst_to_dict(key_list, value_list):
    out = {}
    for k, v in zip(key_list, value_list):
        if k in out:
            if isinstance(out[k], list):
                out[k].append(v)
            else:
                out[k] = [out[k], v]
        else:
            out[k] = v
    return out
    
result = lst_to_dict(keys, values) 

# 13.3
# Task: Write a Python program to implement a function that takes two lists and returns a dictionary where keys come from the first list and values from the second.
list1 = [('red', '#FF0000'), ('green', '#008000'), ('blue', '#0000FF'), ('ivory', '#FFFFF0'), ('lightcyan', '#E0FFFF'), ('lightpink', '#FFB6C1'), ('blue', '#0000FF')]
list2 = [('lightsalmon', '#FFA07A'), ('lightskyblue', '#87CEFA'), ('lightsteelblue', '#B0C4DE'), ('lightpink', '#FFB6C1'), ('magneta', '#FF00FF'), ('maroon', '#B03060'), ('mediumorchid', '#BA55D3')]

def lst_to_dict(lst1, lst2):
    return dict(zip(lst1, lst2))

result = lst_to_dict(list1, list2)

# 13.4
# Task: Write a Python program to use dictionary comprehension to create a dictionary from two lists.
list1 = [('red', '#FF0000'), ('green', '#008000'), ('blue', '#0000FF'), ('ivory', '#FFFFF0'), ('lightcyan', '#E0FFFF'), ('lightpink', '#FFB6C1'), ('blue', '#0000FF')]
list2 = [('lightsalmon', '#FFA07A'), ('lightskyblue', '#87CEFA'), ('lightsteelblue', '#B0C4DE'), ('lightpink', '#FFB6C1'), ('magneta', '#FF00FF'), ('maroon', '#B03060'), ('mediumorchid', '#BA55D3')]

def lst_to_dict(lst1, lst2):
    return {k1[0]: k2[1] for k1, k2 in zip(lst1, lst2)}

result = lst_to_dict(list1, list2)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 14.0
# Task: Write a Python program to sort a given dictionary by key.
d = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}

result = sorted(d.items())

# 14.1
# Task: Write a Python program to sort a dictionary by its keys in ascending order using sorted() and dictionary comprehension.
d = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}

def sort_dict(dct, reverse=False):
    return {k: dct[k] for k in sorted(dct, reverse=reverse)}

result = sort_dict(d)

# 14.2
# Task: Write a Python program to output the items of a dictionary sorted by key using a for-loop.
d = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}

def sort_dict(dct):
    for item in sorted(dct.items()):
        print(f"Items: {item}")
        
#result = sort_dict(d)

# 14.3
# Task: Write a Python program to implement a function that returns a sorted list of keys from a dictionary.
d = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}

def sort_dict(dct):
    return sorted(dct.items())
    
result = sort_dict(d)

# 14.4
# Task: Write a Python program to sort dictionary keys case-insensitively and print the sorted key-value pairs.
d = {'rED': '#FF0000', 'GREEn': '#008000', 'BLack': '#000000', 'WHIte': '#FFFFFF'}

result = sorted(d.items(), key = lambda x: x[0].lower())

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 15.0
# Task: Write a Python program to get the maximum and minimum values of a dictionary.
d = {k: k*k for k in range(1, 11)}

def get_minmax_val(dct):
    min_val = min(dct.items(), key = itemgetter(1))[1]
    max_val = max(dct.items(), key = itemgetter(1))[1]
    
    return (max_val, min_val)

result = get_minmax_val(d)

# OR
def get_minmax_val(dct):
    return (min(dct.values()), max(dct.values()))

result = get_minmax_val(d)

# 15.1
# Task: Write a Python program to determine the maximum and minimum values in a dictionary using the max() and min() functions.
d = {k: k**3 for k in range(1, 11)}

result = (min(d.values()), max(d.values()))

# 15.2
# Task: Write a Python program to iterate over dictionary values and print the maximum and minimum values.
d = {k: k**5 for k in range(1, 11)}

def get_minmax_val(dct):
    values = list(dct.values())
    
    min_val = values[0]
    max_val = values[0]
    
    for v in values:
        if v < min_val:
            min_val = v
        elif v > max_val:
            max_val = v
    
    return (min_val, max_val)
    
result = get_minmax_val(d)

# 15.3
# Task: Write a Python program to implement a function that returns a tuple containing the min and max values from a dictionary. 
d = {k:k*k for k in range(1, 11)}

def get_minmax_val(dct):
    return (min(dct.values()), max(dct.values()))
    
result = get_minmax_val(d)

# 15.4
# Task: Write a Python program to use list comprehension to extract dictionary values and then find their maximum and minimum.     
d = {k: k**6 for k in range(1, 11)}

def get_minmax_val(dct):
    values = [v for v in dct.values()]
    return (min(values), max(values))
    
result = get_minmax_val(d)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 16.0
# Task: Write a Python program to get a dictionary from an object's fields.
class dictObj(object):
    # Define the constructor method '__init__' for initializing object attributes.
    def __init__(self):
        # Initialize attributes 'x', 'y', 'z' with string values.
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'
    # Define method 'do_nothing' that doesn't perform any actions (placeholder).
    def do_nothing(self):
        pass

# Create an instance 'test' of the 'dictObj' class. 
test = dictObj()

# Print the '__dict__' attribute of the 'test' object, which contains its attribute-value pairs. 
#print(test.__dict__)

# 16.1
# Task: Write a Python program to create a dictionary from the attributes of an object using the __dict__ attribute.

class dictObj(object):
    # Define the constructor method '__init__' for initializing object attributes.
    def __init__(self):
        self.x = 'fandango'
        self.y = 'falu'
        self.z = 'fantasy'
    # Define method 'do_nothing' that doesn't perform any actions (placeholder).
    def do_nothing(self):
        pass

# Create an instance 'test' of the 'dictObj' class.
test = dictObj()

# Print the '__dict__' attribute of the 'test' object, which contains its attribute-value pairs.
#print(test.__dict__)

# 16.2
# Task: Write a Python program to iterate over an object's fields and convert them into a dictionary.

class dictObj(object):
    def __init__(self):
        self.x = 'fawn'
        self.y = 'sarcoline'
        self.z = 'limerick'
    
    def do_nothing(self):
        pass

test = dictObj()
result = {}

for k, v in test.__dict__.items():
    result[k] = v
    
#print(result)

# 16.3
# Task: Write a Python program to implement a function that extracts public fields from a class instance and returns them as a dictionary.

class dictObj(object):
    def __init__(self):
        self.x = 'bistre'
        self.y = 'jonquil'
        self.z = 'bole'
    def do_nothing(self):
        pass
    
test = dictObj()

def extract_public_fields(init):
    return vars(init)
    
# OR
def extract_public_fields(obj):
    return {k: v for k, v in vars(obj).items() if not k.startswith('_')}

result = extract_public_fields(test)

# 16.4
# Task: Write a Python program to serialize an object's attributes into a dictionary using introspection.
class dictObj(object):
    def __init__(self):
        self.x = 'zole'
        self.y = 'catawba'
        self.z = 'cinereous'
    
    def do_nothing(self):
        pass

test = dictObj()

#print(vars(test))

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 17.0
# Task: Write a Python program to remove duplicates from the dictionary. 
d = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Luka'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}

def remove_duplicates(dct):
    out = {}
    for k, value in dct.items():
        if value not in out.values():
            out[k] = value
    return out

result = remove_duplicates(d)

# 17.1
# Task: Write a Python program to remove duplicate key-value pairs from a dictionary where values are lists by merging duplicates.
dicts = [('id1', ('Physics', 'Theology')), ('id2', ('Mathematics', 'Statistics')), ('id3', ('Computer Science', 'Biology')), ('id4', ('Chemistry', 'History')), ('id2', ('Finance', 'Combinatorics'))]

def remove_duplicates(dct):
    out = {}
    
    for k, v in dct.items():
        if k in out:
            out[k] += v
        else:
            out[k] = v
    return out

result = remove_duplicates(d)

# 17.2
# Task: Write a Python program to filter a dictionary so that each value appears only once, keeping the first occurrence.
d = {'id1': 'Physics', 'id3': 'Mathematics', 'id4': 'Chemistry', 'id2': 'Combinatorics', 'id5': 'Chemistry', 'id6': 'Chemistry', 'id12': 'Mathematics'}

def filter_dict(dct):
    out = {}
    for k, v in dct.items():
        if v not in out.values():
            out[k] = v
    return out
    
result = filter_dict(d)

# 17.3
# Task: Write a Python program to implement a function that removes duplicate items from a dictionary and returns a new dictionary with unique values.
d = {'id1': ('Physics', 'Theology'), 'id2': ('Mathematics', 'Statistics'), 'id3': ('Computer Science', 'Biology'), 'id3': ('Computer Science', 'Biology'), 'id4': ('Chemistry', 'History')}

def remove_duplicates(dct):
    out = {}
    for item in dct.items():
        if item not in out.items():
            out.update({item})
    
    return out

result = remove_duplicates(d)

# 17.4
# Task: Write a Python program to consolidate duplicate keys in a dictionary by summing their values.
d = [('a', 2), ('a', 7), ('b', 11), ('c', 17), ('d', 18), ('e', 25), ('f', 177), ('g', 12)]

def consolidate_keys(data):
    out = {}
    for k, v in data:
        if k in out:
           out[k] += v
        else:
            out[k] = v
    return out
    
result = consolidate_keys(d)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 18.0
# Task: Write a Python program to check if a dictionary is empty or not.
d = {}

def empty_dict(dct):
    return len(dct) == 0

result = empty_dict(d)

# 18.1
# Task: Write a Python program to check whether a dictionary is empty by evaluating its boolean value. 
d = {}
def empty_dict(dct):
    return bool(not dct)

result = empty_dict(d)

# 18.2
# Task: Write a Python program to implement a function that returns True if a dictionary has no keys and False otherwise.
d = {'a': 2, 'b': 2}

def empty_dict(dct):
    return len(d.keys()) == 0

result = empty_dict(d)

# 18.3
# Task: Write a Python program to test the emptiness of a dictionary by comparing its length to zero.
d = {}

def empty_dict(dct):
    return len(dct) == 0

result = empty_dict(d)

# 18.4
# Task: Write a Python program to use conditional expressions to output whether a dictionary is empty.
d = {}

def empty_dict(dct):
    if len(dct) > 0:
        return False
    return True

result = empty_dict(d)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 19.0
# Task: Write a Python program to combine two dicts by adding values for common keys.
d1 = {'a': 16, 'b': 11, 'c': 17, 'd': 74, 'e': 76}
d2 = {'a': 17, 'c': 31, 'x': 74, 'y': 76, 'w': 11}

def combine_dicts(*dicts):
    out = {}
    for d in dicts:
        for k, v in d.items():
            if k in out:
                out[k] +=v
            else:
                out[k] = v
    return out
    
result = combine_dicts(d1,d2)

# 19.1
# Task: Write a Python program to combine two dictionaries and add values for keys that appear in both using Counter (collections)
d1 = {'a': 16, 'b': 11, 'c': 17, 'd': 74, 'e': 76}
d2 = {'a': 17, 'c': 31, 'x': 74, 'y': 76, 'w': 11}

def combine_dicts(*dicts):
    out = {}
    for d in dicts:
        out =+ Counter(d)
    return result

result = combine_dicts(d1, d2)

# 19.2
# Task: Write a Python program to merge two dictionaries by summing the values of common keys with a loop.
d1 = {'a': 16, 'b': 11, 'c': 17, 'd': 74, 'e': 76}
d2 = {'a': 17, 'c': 31, 'x': 74, 'y': 76, 'w': 11}

def combine_dicts(*dicts):
    out = {}
    for d in dicts: 
        for k, v in d.items():
            if k in out:
                out[k] += v
            else:
                out[k] = v
    return out

result = combine_dicts(d1, d2)

# 19.3
# Task: Write a Python program to use dictionary comprehension to create a new dictionary that adds values for matching keys from two dictionaries.
d1 = {'a': 16, 'b': 11, 'c': 17, 'd': 74, 'e': 76}
d2 = {'a': 17, 'c': 31, 'x': 74, 'y': 76, 'w': 11}

def combine_dicts(dct1, dct2):
    return {k: dct1.get(k, 0) + dct2.get(k, 0) for k in set(dct1) | set(dct2)}
    
result = combine_dicts(d1, d2)

# 19.4 
# Write a Python program to implement a function that takes two dictionaries and returns a merged dictionary with summed values for shared keys.
d1 = {'a': 16, 'b': 11, 'c': 17, 'd': 74, 'e': 76}
d2 = {'a': 17, 'c': 31, 'x': 74, 'y': 76, 'w': 11}

# Method 1: Standard for loop

def combine_dicts(*dicts):
    out = {}
    for d in dicts: 
        for k, v in d.items():
            if k in out:
                out[k]+=v
            else: 
                out[k] = v
    return out
    
result = combine_dicts(d1, d2)

# Method 2: Counter

def combine_dicts(*dicts):
    out = {}
    for d in dicts:
        out =+ Counter(d)
    return dict(sorted(out.items()))

result = combine_dicts(d1, d2)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 20.0
# Task: Write a Python program to print all distinct values in a dictionary.
lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]    

unique_values = []
 
for d in lst:
    for v in d.values():
        unique_values.append(v)

#print(set(unique_values))           

# 20.1
# Task: Write a Python program to extract all unique values from a dictionary where values might be duplicated.
lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

unique_values = []

for d in lst:
    for v in d.values():
        unique_values.append(v)

unique_values = set(unique_values)

# 20.2
# Task: Write a Python program to iterate over a dictionary and add all distinct values to a set, then print the set.
lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

unique_values = set()

for d in lst:
    for v in d.values():
        unique_values.add(v)

#print(unique_values)

# 20.3 
# Task: Write a Python program to use set comprehension to output the distinct values of a dictionary.
d = {'a': 11, 'b': 16, 'c': 16, 'd': 17}

def distinct_values(l):
    return set(v for v in d.values())

result = distinct_values(d)

# 20.4
# Task: Write a Python program to merge multiple dictionaries and then display a sorted list of unique values.
d1 = {'a': 11, 'b': 16, 'c': 16, 'd': 17}
d2 = {'e': 12, 'f': 16, 'g': 63, 'h': 76}
d3 = {'i': 77, 'j': 17, 'k': 90, 'l': 199}

def distinct_values(*dicts):
    merged_dict = {}
    for dct in dicts:
        merged_dict.update(dct)
    
    unique_values = set()
    for v in merged_dict.values():
        unique_values.add(v)
    
    return list(sorted(unique_values))
    
result = distinct_values(d1, d2, d3)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 21.0
# Task: Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
d = {'1': ['a', 'b'], '2': ['c', 'd'], '3': ['e', 'f'], '4': ['g', 'h'], '5': ['i', 'j']}

result = []

for combo in product(*[d[k] for k in sorted(d.keys())]):
    result.append(''.join(combo))
        
# 21.1
# Task: Write a Python program to generate all combinations of letters by selecting one letter from each list in a dictionary.
d = {'1': ['a', 'b'], '2': ['c', 'd'], '3': ['e', 'f'], '4': ['g', 'h'], '5': ['i', 'j']}

result = [''.join(p) for p in product(*d.values())]

# 21.2
# Task: Write a Python program to use itertools.product to create all letter combinations from a dictionary of lists.
d = {'1': ['a', 'b'], '2': ['c', 'd'], '3': ['e', 'f'], '4': ['g', 'h'], '5': ['i', 'j']}

result = [''.join(p) for p in product(*d.values())]

# 21.3
# Task: Write a Python program to recursevly combine letters from different keys in a dictionary and print each combination.
d = {'1': ['a', 'b'], '2': ['c', 'd'], '3': ['e', 'f'], '4': ['g', 'h'], '5': ['i', 'j']}

def recursive_combine(lists, prefix = ''):
    if not lists:
        print(prefix)
        return
    
    first, *rest = lists
    
    for letter in first:
        recursive_combine(rest, prefix + letter)
    
# recursive_combine(list(d.values()))

# 21.4
# Task: Write a Python program to implement a function that outputs a list of strings formed by all possible combinations of values from a dictionary's keys.
d = {'1': ['a', 'b'], '2': ['c', 'd'], '3': ['e', 'f'], '4': ['g', 'h'], '5': ['i', 'j']}

def recursive_combine(d):
    values = list(d.values())
    
    def combine(lists):
        if not lists:
            return ['']
        rest = combine(lists[1:])
        return [x + y for x in lists[0] for y in rest]
    
    return combine(values)

result = recursive_combine(d)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 22.0
# Task: Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

result = nlargest(3, d, key = d.get)

# 22.1
# Task: Write a Python program to extract the three highest values from a dictionary and return them as a sorted list.
d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

def return_highest(dct, n_values = 1):
    return sorted(nlargest(n_values, dct, key = dct.get))

result = return_highest(d, n_values = 3)

# 22.2
# Task: Write a Python program to use heapq.nlargest to find the top three values in a dictionary.
d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

result = nlargest(3, d.values())

# 22.3
# Task: Write a Python program to implement a function that returns the keys corresponding to the highest three values in a dictionary.
d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

def highest_keys(dct, n_values = 1):
    keys = []
    largest_items = nlargest(n_values, d.items())[1]
    
    for k, v in largest_items:
        keys.append(k)
    
    return keys

result = highest_keys

# 22.4
# Task: Write a Python program to sort a dictionary by value and then output the three largest key-value pairs.
d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
def sorted_dict(dct, n_values):
    srt_dct = dict(sorted(dct.items(), key = itemgetter(1)))

    return nlargest(n_values, srt_dct.items())    

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 23.0
# Task: Write a Python program to combine values in a list of dictionaries.
l = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

out = Counter()

for d in l:
    out[d['item']] += d['amount']

# 23.1
# Task: Write a Python program to merge a list of dictionaries by summing values for common keys using collections.Counter.
l = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

out = Counter()

for d in l:
    out[d['item']] += d['amount']
    
# 23.2
# Task: Write a Python program to iterate through a list of dictionaries and accumulate the values of identical keys into a new dictionary.
l = [{'item': 'item1', 'amount': 400}, {'item': 'item3', 'amount': 360}, {'item': 'item3', 'amount': 160}, 
     {'item': 'item2', 'amount': 300}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750},
     {'item': 'item4', 'amount': 300}, {'item': 'item4', 'amount': 300}, {'item': 'item2', 'amount': 300}]

out = Counter()

for d in l:
    out[d['item']] += d['amount']
    
# 23.3
# Task: Write a Python program to use a dictionary comprehension to combine values from multiple dictionaries in a list.
l = [{'item': 'item1', 'amount': 400}, {'item': 'item3', 'amount': 360}, {'item': 'item3', 'amount': 160}, 
     {'item': 'item2', 'amount': 300}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750},
     {'item': 'item4', 'amount': 300}, {'item': 'item4', 'amount': 300}, {'item': 'item2', 'amount': 300}]

# Method 1: All in one line

def combine_values(dicts):
    return {k: sum(v['amount'] for v in dicts if v['item'] == k)
            for k in {v['item'] for v in dicts}}


def combine_values(dicts):
    return {k: sum(v['amount'] for v in dicts if v['item'] == k)
            for k in {v['item'] for v in dicts}}

result = combine_values(l)
            
# Method 3: Default dict, best way
out = defaultdict(int)

for d in l:
    out[d['item']] += d['amount']

out

# 23.4
# Task: Write a Python program to implement a function that consolidates a list of dictionaries into one by adding values for matching keys.
l = [{'item': 'item1', 'amount': 400}, {'item': 'item3', 'amount': 360}, {'item': 'item3', 'amount': 160}, 
     {'item': 'item2', 'amount': 300}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750},
     {'item': 'item4', 'amount': 300}, {'item': 'item4', 'amount': 300}, {'item': 'item2', 'amount': 300}]

# Method 1: Counter()
def consolidate_dicts(dicts):
    out = Counter()
    
    for d in dicts:
        out[d['item']] += d['amount']
    return out

# Method 2: defaultdict()
def consolidate_dicts(dicts):
    out = defaultdict()
    
    for d in dicts:
        out[d['item']] += d['amount']
    return out

# Method 3: Dictionary comprehension
def consolidate_dicts(dicts):
    return {k: sum(v['amount'] for v in dicts if v['item'] == k) for k in {v['item'] for v in dicts}}
    
result = consolidate_dicts(l)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 24.0
# Task: Write a Python program to create a dictionary from a string.
my_str = 'ULTRAGOYY'

# Method 1: loop

def str_to_dict(s):
    out = {}
    for c in s:
        if c in out:
            out[c] += 1
        else:
            out[c] = 1
    return out

result = str_to_dict(my_str)    

# Method 2: Counter()
out = Counter(my_str)

# 24.1
# Task: Write a Python program to convert a string into a dictionary where each key is a character and its value is the frequency of that character.
my_str = 'davidstar'

out = {}

for c in my_str:
    out[c] = out.get(c, 0) + 1
 
# 24.2
# Task: Write a Python program to use collections.Counter to count the frequency of each character in a string.
my_str = "idf"

out = {}

my_str = "IDF"

# 24.3
# Task: Write a Python program to iterate over a string and manually tally character counts in a dictionary.
my_str = 'letssgooo'

out = {}

for c in my_str:
    if c in out:
        out[c] += 1
    else:
        out[c] = 1

# 24.4
# Task: Write a Python program to implement a function that returns a frequency dictionary for a given string, ignoring cases.
my_str = "I went for a walk today, and I liked it."

def str_freq(s):
    new_string = ''.join(list(filter(lambda c: c not in punctuation and c != ' ', s)))
    out = {}
    for c in new_string:
        if c in out:
            out[c] += 1
        else:
            out[c] = 1
    
    return out

result = str_freq(my_str)

# 25.0
# Task: Write a Python program to print a dictionary in table format.
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

# Method 1: Pandas
result = pd.DataFrame(data=my_dict.items(), columns = ['Key', 'Value'])

# Method 2: for loop

#for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#    print(*row)
    
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #    
    
# 25.1
# Task: Write a Python program to print a dictionary contents in a tabular format with aligned columns.
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

result = pd.DataFrame(data = my_dict.items(), columns = ['Key', 'Value'])

# 25.2
# Task: Write a Python program to use the tabulate module to display a dictionary as a formatted table.
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

result = tabulate(my_dict.items(), headers = ['Key', 'Value'], tablefmt = 'pipe')

# 25.3
# Task: Write a Python program to iterate over dictionary items and print each on a new line with fixed column widths.
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

col_width_k = 10
col_width_v = 5
        
#for k, values in my_dict.items():
#    print(f"{k:<{10}}") 
#    for v in values:
#       print(f"{v:>{20}}")

# 25.4
# Task: Write a Python program to format and print a dictionary where keys and values are left-justified in a table.
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

#for k, values in my_dict.items():
#    print(f"{k:<{col_width_k}}")
#    for v in values:
#        print(f"{v:<{col_width_v}}")
        
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 26.0 
# Task: Write a Python program to count the values associated with a key in a dictionary.
my_dicts = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]

# Print the sum of 'id' values for all students in the 'student' list.
#print(sum(d['id'] for d in my_dicts))
    
# Print the sum of 'success' for all student in the 'student' list.
#print(sum(d['success'] for d in my_dicts))

# 26.1
# Task: Write a Python program to count the number of elements in a dictionary value when the value is a list. 
my_dict = {'a': [1, 2, 3], 'b': 1, 'c': [5, 7, 8], 'd': [77, 2, 1], 'e': 11}

# Method 1: Dictionary comprehension.

def count_elements_if_list(dct):
    return {k: 1 if isinstance(v, (int, float, str)) else len(v) for k, v in dct.items()}
    
result = count_elements_if_list(my_dict)

# Method 2: For loop

def count_elements_if_list(dct):
    out = {}
    
    for k, values in dct.items():
        if k in dct and isinstance(values, list):
                out[k] = len(values)
        else:
            out[k] = 1
    
    return out

result = count_elements_if_list(my_dict)

# 26.2
# Task: Write a Python program to iterate over a dictionary and sum the lengths of list values for a given key.
my_dict = {'a': [1, 2, 3], 'b': 1, 'c': [5, 7, 8], 'd': [77, 2, 1], 'e': 11}


def count_key_elements(dct, key):
    for k, v in dct.items():
        if k == key:
            if isinstance(v, list):
                return len(v)
            else:
                return 1

result = count_key_elements(my_dict, 'e')

# 26.3
# Task: Write a Python program to use a loop to calculate how many items are associated with each key in a dictionary where values are lists.
my_dict = {'a': [1, 2, 3], 'b': 1, 'c': [5, 7, 8], 'd': [77, 2, 1], 'e': 11}

def count_elements(dct):
    out = {}
    for k, v in dct.items():
        if isinstance(v, list):
            out[k] = len(v)
    return out

result = count_elements(my_dict)

# 26.4
# Task: Write a Python program to implement a function that returns the count of items for a specificed key in a dictionary.
my_dict = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Clara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Luka'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}

def count_items(dct, key):
    for k, v in dct.items():
        if k == key:
            return len(v)

result = count_items(my_dict, 'id1')

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 27.0
# Task: Write a Python program to convert a list into a nested dictionary of keys.
my_list = [1, 2, 3, 4]

new_dict = current = {}

for name in my_list:
    current[name] = {}
    current = current[name]

#print(new_dict)

# 27.1
# Task: Write a Python program to recursively convert a list of elements into a nested dictionary, where each element is a key.
my_list = [1, 2, 3, 4]

def recursive_list_conversion(lst):
    if not lst:
        return {}
    
    return {lst[0]: recursive_list_conversion(lst[1:])}

result = recursive_list_conversion(my_list)        

# 27.2
# Task: Write a Python program to create a nested dictionary from a list using a for-loop and dictionary assignment.
my_list = [1, 2, 3, 4]

def create_dict(lst):
    out = current = {}
    
    for ele in lst:
        current[ele] = {}
        current = current[ele]
    
    return new_dict

result = create_dict(my_list)
     
# 27.3
# Task: Write a Python program to use recursion to transform a list into a nested dictionary structure with each element as a key.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

def recursive_list_conversion(lst):
    if not lst:
        return {}
    
    return {lst[0]: recursive_list_conversion(lst[1:])}

result = recursive_list_conversion(my_list)

# 27.4
# Task: Write a Python program to implement a function that returns a nested dictionary representation of a list of items.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Method 1: Recursion, best.
def recursive_list_conversion(lst):
    if not lst:
        return {}
    
    return {lst[0]: recursive_list_conversion(lst[1:])}

result = recursive_list_conversion(my_list)    

# Method 2: For loop.

def loop_list_conversion(lst):
    out = current = {}
    
    for ele in lst:
        current[ele] = {}
        current = current[ele]
    
    return out
    
result = loop_list_conversion(my_list)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 28.0
# Task: Write a Python program to sort a list alphabetically in a dictionary.
my_dict = {'n1': [1, 2, 3], 'n2': [5, 11, 16], 'n3': [19, 11, 75], 'n4': [2, 6, 8]}

sorted_dict = {k: sorted(v) for k, v in my_dict.items()}

# 28.1
# Task: Write a Python program to sort the list values within a dictionary in alphabetical order.
my_dict = {'n1': [1, 2, 3], 'n2': [5, 11, 16], 'n3': [19, 11, 75], 'n4': [2, 6, 8]}

def sort_values(dct):
    out = {}
    
    for k, v in dct.items():
        if isinstance(v, list):
            out[k] = sorted(v)
        else:
            out[k] = v
    
    return out
    
# 28.2
# Task: Write a Python program to iterate over a dictionary and sort each list value alphabetically.
my_dict = {'n1': [1, 2, 3], 'n2': [5, 11, 16], 'n3': [19, 11, 75], 'n4': [2, 6, 8]}

def sort_values(dct):
    for k, v in dct.items():
        if isinstance(v, list):
            dct[k] = sorted(v)
        else:
            dct[k] = v
    
    return dct

result = sort_values(my_dict)

# 28.3
# Task: Write a Python program to use dictionary comprehension to return a new dictionary with sorted list values.
my_dict = {'n1': [1, 2, 3], 'n2': [5, 11, 16], 'n3': [19, 11, 75], 'n4': [2, 6, 8]}

sorted_dict = {k: sorted(v) for k, v in my_dict.items()}

# 28.4
# Task: Write a Python program to implement a function that takes a dictionary of lists and sorts each list alphabetically.
my_dict = {'n1': [1, 2, 3], 'n2': [5, 11, 16], 'n3': [19, 11, 75], 'n4': [2, 6, 8]}

def sorted_dict(dct):
    return {k: sorted(v) for k, v in dct.items()}

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 29.0
# Task: Write a Python program to remove spaces from dictionary keys.
my_dict = {"S 001": ['Math', 'Science'], 'S 002': ['Math', 'English']}

result = {k.translate({32: None}): v for k, v in my_dict.items()}

# 29.1
# Task: Write a Python program to remove all spaces from the keys of a dictionary and return a new dictionary.
my_dict = {"S 001": ['Math', 'Science'], 'S 002': ['Math', 'English']}

def remove_whitespace(dct):
    return {k.translate({32: None}): v for k, v in dct.items()}

# 29.2
# Task: Write a Python program to iterate over a dictionary and strip whitespace from each key.
my_dict = {"S 001": ['Math', 'Science'], 'S 002': ['Math', 'English']}

def remove_whitespace(dct):
    out = {}
    for k, v in dct.items():
        clean_key = k.translate({32: None})
        out[clean_key] = v
    
    return out
    
result = remove_whitespace(my_dict)

# 29.3
# Task: Write a Python program to use dictionary comprehension to create a dictionary with keys that have no spaces.   
my_dict = {"S 00--1": ['Math', 'Science'], 'S 0-0=2': ['Math', 'English']}

result = {k.translate({32: None}): v for k, v in my_dict.items()}

# 29.4
# Task: Write a Python program to implement a function that cleans dictionary keys by removing spaces and special characters.
my_dict = {"S 001": ['Math', 'Science'], 'S 002': ['Math', 'English']}

def filter_string(key):
    return ''.join(filter(lambda c: c != ' ' and c not in punctuation, key))

# OR
def filter_string(key):
    return ''.join(c for c in key if c.isalnum())

def remove_specials(dct):
    out = {}
    for k, v in dct.items():
        clean_key = filter_string(k)
        out[clean_key] = v
    
    return out

def remove_specials(dct):
    return {filter_string(k): v for k, v in dct.items()}

result = remove_specials(my_dict)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 30.0
# Task: Write a Python program to get the top three items in a shop. 
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

def find_largest(dct, n):
    return nlargest(n, dct.values())

result = find_largest(my_dict, 3)

# OR
#for name, value in nlargest(3, my_dict.items(), key = itemgetter(1)):
#    print(k, v)

# 30.1
# Task: Write a Python program to sort a dictionary of shop items by price in descending order and print the top three.
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

result = sorted(my_dict.items(), key = itemgetter(1), reverse = True)[:3]
    
# 30.2
# Task: Write a Python program to use heapq.nlargest to extract the top three most expensive items from a dictionary.
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

result = nlargest(3, my_dict.items(), key = itemgetter(1))

# 30.3
# Task: Write a Python program to implement a function that returns the three highest-priced items from a shop inventory dictionary.
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

def most_pricy(dct, n = 1):
    pricey_items = []
    for k, v in list(nlargest(n, dct.items(), key = lambda x: x[1])):
        pricey_items.append(k)
    
    return pricey_items
    
result = most_pricy(my_dict, n = 3)

# 30.4
# Task: Write a Python program to iterate over a shop dictionary and output the top three key-value pairs based on value.
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

result = {k: v for k, v in nlargest(3, my_dict.items(), key = lambda x: x[1])}

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 31.0
# Task: Write a Python program to get the key, value and item in a dictionary. 
my_dict =  {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

#for count, (key, value) in enumerate(my_dict.items(), 1):
#    print(count, key, value)

# 31.1
# Task: Write a Python program to iterate over a dictionary and print each key along with its value using items().
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

#for k, v in my_dict.items():
#    print(k, v)

# 31.2
# Task: Write a Python program to generate a list of tuples containing key and value pairs from a dictionary.
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

def generate_tuples(dct):
    result = []
    for k, v in dct.items():
        result.append((k, v))
    
    return result

# OR
def generate_tuples(dct):
    return {(k, v) for k, v in dct.items()}

# OR
def generate_tuples(dct):
    return list(dct.items())

result = generate_tuples(my_dict)

# 31.3
# Task: Write a Python program to use a for-loop to display each dictionary item on a separate line in the format "key: value".
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

#for k, v in my_dict.items():
#    print(f"{k}: {v}")

# 31.4
# Task: Write a Python program to create a function that returns all key, value pairs as a list of strings formatted as "key = value".
my_dict = {'item1': 166, 'item2': 421, 'item3': 3.1, 'item4': 531, 'item5': 531, 'item6': 6883, 'item7': 3218, 'item8': 412.33}

def generate_list(dct):
    string_list = []
    for k, v in dct.items():
        string_list.append(f"{k} = {v}")
    
    return string_list

result = generate_list(my_dict)

# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

# 32.0
# Task: Write a Python program to print a dictionary line by line.
my_dict = {'Nick': {'class': 'V', 'roll_id': 2}, 'Steven': {'class': 'V', 'roll_id': 3}}

#for k in my_dict:
#    print(k)
#    for v in my_dict[k]:
#        print(v, ':', my_dict[k][v])

# 32.1
# Task: Write a Python program to print each key-value pair in a dictionary on a separate line.
my_dict = {'Nick': {'class': 'V', 'roll_id': 2}, 'Steven': {'class': 'V', 'roll_id': 3}}

#for name in my_dict:
#    print(name)
#    for clss, rid in my_dict[k].items():
#       print((clss, rid))

# 32.2
# Task: Write a Python program to format and print a dictionary so that each line shows a key and its corresponding value.
my_dict = {'Nick': {'class': 'V', 'roll_id': 2}, 'Steven': {'class': 'V', 'roll_id': 3}}

#for name in my_dict.items():
#    for clss, rid in my_dict[k].items():
#        print([clss, rid])
        
        
# 32.3
# Task: Write a Python program to iterate over a dictionary and output its items line by line using f-strings.
my_dict = {'Nick': {'class': 'V', 'roll_id': 2}, 'Steven': {'class': 'V', 'roll_id': 3}}

#for name in my_dict:
#    print(name)
#    for k, v in my_dict[name].items():
#        print((k, v))

# 32.4
# Task: Write a Python program to display a dictionary in a multi-line format with each item on its own line.
my_dict = {'Nick': {'class': 'V', 'roll_id': 2}, 'Steven': {'class': 'V', 'roll_id': 3}}

#for item in my_dict.items():
#    print(item)
 
# 33.0 
# Task: Write a Python program to check if multiple keys exist in a dictionary.
my_dict = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}

#print(my_dict.keys() >= {'name', 'class'})

# 33.1
# Task: Write a Python program to verify if a list of keys are all present in a dictionary.
my_dict = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}
keys = ['name', 'class']

result = all(k in keys for k in my_dict.keys())

# 33.2
# Task: Write a Python program to use all() with a list comprehension to check for multiple keys in a dictionary.
my_dict = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}

result = all(k in keys for k in ['name', 'class', 'roll_id'])

# 33.3
# Task: Write a Python program to implement a function that returns True if every key in a given list exists in the dictionary.
my_dict = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}
keys = ['name', 'blaard', 'sect']

result = lambda dct, kys: all(k in kys for k in dct.keys())

# 33.4
# Task: Write a Python program to compare the keys of a dictionary with a given set and output whether all specified keys are found.
my_dict = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}
my_set = {'name', 'class', 'roll_id'}

result = all(k in my_set for k in my_dict.keys())

# 34.0
# Task: Write a Python program to sort Counter by value.
my_dict = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

result = Counter(my_dict)

# 34.1
# Task: Write a Python program to sort a dictionary (or Counter) by its values in descending order and output a list of tuples.
my_dict = {'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 84, 'Computer Science': 112}

result_counter = tuple(Counter(my_dict.values()).most_common())

result = tuple(sorted(my_dict.values(), reverse=True))

# 34.2
# Task: Write a Python program to use sorted() with a lambda function to arrange the items of a Counter based on frequency.
my_dict = {'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'Computer Science': 112}

freq_tbl = Counter(my_dict.items())

result = sorted(freq_tbl.items(), key = lambda x: x[1])

# 34.3
# Task:

# 34.4
# Task: 

# 35.0
# Task:
my_dict = {'Math': 11, 'Physics': 26,
           'Engineering':66, 'Biology': 76}

my_counter = Counter(my_dict)

# Solution
my_counter.most_common()

# 35.1
# Task: Write a Python program to sort a dictionary (or Counter) by its values in descending order and output a list of tuples.
my_dict = {'Math': 11, 'Physics': 26,
           'Engineering':66, 'Biology': 76}
           
result = list(sorted(my_dict.items(), key = itemgetter(1), reverse = True))

# 35.2
# Task: Write a Python program to use sorted() with a lambda function to arrange the items of a Counter based on frequency.
my_list = ['Biology', 'Math', 'Physics', 'Engineering', 'Chemistry',
           'Sociology', 'Biology', 'Physics', 'Physics']
 
result = list(sorted(Counter(my_list).items(), key = lambda x: x[1]))
result
# 35.3
# Task: Write a Python program to implement a function that takes a Counter object and returns its items sorted by value.
my_counter = Counter(my_list)

result = lambda cntr: cntr.most_common()
result(my_counter)

# 35.4
# Task: Write a Python program to compare sorting a Counter by keys versus sorting by values and display the differences.
my_list = ['Biology', 'Math', 'Physics', 'Engineering', 'Chemistry',
           'Sociology', 'Biology', 'Physics', 'Physics']
my_counter = Counter(my_list)

sorted_by_keys = sorted(my_counter.items(), key = itemgetter(0))
sorted_by_values = sorted(my_counter.items(), key = itemgetter(1))

result = sorted_by_keys == sorted_by_values
#print(f"Sorted by keys: {sorted_by_keys}\n\nSorted by values: {sorted_by_values}\n\nResult: {result}")

# 36.0
# Task: Write a Python program to create a dictionary from two lists without losing duplicate values.
my_list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
my_list2 = [1, 2, 2, 3]
# Method 1: Classic dictionary
out = {}
for k, v in zip(my_list1, my_list2):
    out[k] = v
   
# Method 2: Defaultdict
out = defaultdict(set)

for k, v in zip(my_list1, my_list2):
    out[k].add(v)

out

# 36.1
# Task: Write a Python program to convert two lists into a dictionary where keys map to a set of values to preserve duplicates.
my_list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
my_list2 = [1, 2, 2, 3]

out = {}

for k, v in zip(my_list1, my_list2):
    out[k] = {v}

out

# 36.2
# Task: Write a Python program to use collections.defaultdict(set) to merge two lists into a dictionary without losing duplicate values.
my_list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
my_list2 = [1, 2, 2, 3]

out = defaultdict(set)

for k, v in zip(my_list1, my_list2):
    out[k].add(v)
   
# 36.3
# Task: Write a Python program to iterate over two lists and store duplicate values in a set within the dictionary for each key.
my_list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII', 'Class-VIII', 'Class-VII', 'Class-VI']
my_list2 = [1, 2, 2, 3, 6, 2, 1]

# Method 1:
out = defaultdict(set)

for k, v in zip(my_list1, my_list2):
    out[k].add(v)

# Method 2:
out = {}
for k, v in zip(my_list1, my_list2):
    if k not in out:
        out[k] = set()
    out[k].add(v)

# 36.4
# Task: Write a Python program to implement a function that creates a dictionary from two lists, ensuring duplicate values are stored in a list or set.
my_list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII', 'Class-VIII', 'Class-VII', 'Class-VI']
my_list2 = [1, 2, 2, 3, 6, 2, 1]

def merge_lists(l1, l2):
    out = defaultdict(set)
    lists = zip(l1, l2)
   
    for k, v in lists:
        out[k].add(v)
   
    return out

result = merge_lists(my_list1, my_list2)
result

# 37.0
# Task: Write a Python program to replace dictionary values with their sums.
my_dict = [
  {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
  {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
  {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
]

def add_cells(lst):
    for d in lst:
        # Extract and remove 'V' and  'VI' values in a dictionary.
        n1 = d.pop('V')
        n2 = d.pop('VI')
       
        d['V + VI'] = n1+n2
   
    return lst

result = add_cells(my_dict)

# 37.1
# Task: Write a Python program to update a dictionary so that each key's value
# becomes the sum of its original value and another corresponding value from a second dictionary.
my_dict1 = {'a': 12, 'b': 16, 'c': 24}
my_dict2 = {'d': 16, 'e': 24, 'f': 40}

def sum_vals(d1, d2):
    for k, v in zip(d1.keys(), d2.values()):
        d1[k] += v
    return d1

result = sum_vals(my_dict1, my_dict2)

# 37.2
# Task: Write a Python program to iterate over a dictionary and
# replace each value with the sum of the digits of that value.
my_dict = {'a': 12, 'b': 16, 'c': 24}

def sum_digits(d):
    for k, v in d.items():
        d[k] = sum(map(int, reduce(lambda a, b: a+b, str(v))))
   
    return d
       
result = sum_digits(my_dict)
pprint(result)

# 37.3
# Task: Write a Python program to merge a dictionary with itself by
# summing values that share the same key after a transformation.
my_dict = {'a': 12, 'b': 16, 'c': 24, 'A': 40, 'B': 73, 'C': 136}

def merge_vals(d, trans):
    out = {}
   
    for k, v in d.items():
        new_key = trans(k)
       
        if new_key in out:
            out[new_key] += v
        else:
            out[new_key] = v
   
    return out

# OR
def merge_vals(d, trans):
    out = defaultdict(int)
   
    for k, v in d.items():
        out[trans(k)] += v
   
    return dict(out)

result = merge_vals(my_dict, str.lower)

# OR
def merge_vals(d, key_fn, val_fn):
    out = {}
   
    for k, v in d.items():
        nk = key_fn(k)
        nv = val_fn(v)
       
        if isinstance(nv, Real) and not isinstance(nv, bool):
            out[nk] = out.get(nk, 0) + nv
   
    return out

key_fn = lambda s: s.strip().lower()
val_fn = lambda x: float(x) if isinstance(x, str) and x.replace('.', '', 1).isdigit() else x

result = merge_vals(my_dict, key_fn, val_fn)

# 37.4
# Task: Write a Python program to implement a function that takes a
# dictionary and returns a new dictionary with each value replaced by its cumulative sum with other values.
my_dict = {'a': 12, 'b': 16, 'c': 24}

# Method 1: Loop
def accumulate_vals(d):
    out = {}
    running_sum = 0
    for k, v in d.items():
        running_sum +=v
        out[k] = running_sum
   
    return out

# Method 2: Itertools accumulate
def accumulate_vals(d):
    return dict(zip(d.keys(), accumulate(d.values())))

accumulate_vals(my_dict)

# 38.0
# Task: Write a Python program to match key values in two dictionaries.
my_dict1 = {'a': 2, 'b': 3, 'c': 11, 'd': 15, 'e': 17, 'f': 12}
my_dict2 = {'a': 8, 'b': 3, 'c': 11, 'd': 18, 'e': 12, 'f': 22}

#for (key, value) in set(my_dict1.items() & my_dict2.items()):
#    print(list((key, value)))

# 38.1
# Task: Write a Python program to compare two dictionaries
# and print the keys whose values match in both.
my_dict1 = {'a': 2, 'b': 3, 'c': 11, 'd': 15, 'e': 17, 'f': 12}
my_dict2 = {'a': 8, 'b': 3, 'c': 11, 'd': 18, 'e': 12, 'f': 22}

#for (k, v) in set(my_dict1.items() & my_dict2.items()):
#    print(list(k))

# 38.2
# Task: Write a Python program to iterate over keys in one dictionary
# and check if the corresponding value in another dictionary is the same.
my_dict1 = {'a': 2, 'b': 3, 'c': 11, 'd': 15, 'e': 17, 'f': 12}
my_dict2 = {'a': 8, 'b': 3, 'c': 21, 'd': 18, 'e': 12, 'f': 22}

result = any((k, v) in my_dict2.items() for (k, v) in my_dict1.items())

# 38.3
# Task: Write a Python program to use set intersection on the keys
# of two dictionaries and then verify matching values for each intersected key.
my_dict1 = {'a': 2, 'b': 3, 'c': 11, 'd': 15, 'e': 17, 'f': 12, 'g': 14}
my_dict2 = {'a': 8, 'b': 3, 'c': 11, 'd': 18, 'e': 12, 'f': 22}

common_keys = set(my_dict1.keys()).intersection(my_dict2.keys())

out = {}

for k in common_keys:
    if my_dict1[k] == my_dict2[k]:
        out[k] = my_dict1[k]

out

# 38.4
# Task: Write a Python program to implement a function that finds
# all keys present in both dictionaries where the
# values are equal, and print them with their common value.        
my_dict1 = {'a': 2, 'b': 3, 'c': 11, 'd': 15, 'e': 17, 'f': 12, 'g': 14}
my_dict2 = {'a': 8, 'b': 3, 'c': 11, 'd': 18, 'e': 12, 'f': 22}

def kv_intersection(d1, d2):
    out = {}
    common_keys = d1.keys() & d2.keys()
   
    for k in common_keys:
        if d1[k] == d2[k]:
            out[k] = d1[k]
   
    return out

result = kv_intersection(my_dict1, my_dict2)

# 39.0
# Task: Write a Python program to store dictionary data in a JSON file.
d = {
    "students": [
        {"firstName": "Nikki", "lastName": "Roysden"},
        {"firstName": "Mervin", "lastName": "Friedland"},
        {"firstName": "Aron", "lastName": "Wilkins"}
    ],
    "teachers": [
        {"firstName": "Amberly", "lastName": "Dober"},
        {"firstName": "Regine", "lastName": "Crowder"}
    ]
}

#with open("dictionary", "w") as f:
#    json.dump(d, f, indent = 4, sort_keys = True)
#    
#print("\nJson file to dictionary:")
#
#with open('dictionary') as f:
#    data = json.load(f)

# 39.1
# Task:
d = {
    "students": [
        {"firstName": "Nikki", "lastName": "Roysden"},
        {"firstName": "Mervin", "lastName": "Friedland"},
        {"firstName": "Aron", "lastName": "Wilkins"}
    ],
    "teachers": [
        {"firstName": "Amberly", "lastName": "Dober"},
        {"firstName": "Regine", "lastName": "Crowder"}
    ]
}

#with open("dictionary", "w") as f:
#    json.dump(d, f, indent = 4, sort_keys = True)

#print("\nJson file to dictionary: ")

#with open("dictionary") as f:
#    data = json.load(f)
   
# 39.2
# Task:
my_dict = {'name': 'Miklo', 'age': 25,
           'skills': ['Python', 'R', 'C++'],
           'active': True}

# Convert to JSON string
#json_string = json.dumps(data)

# OR
with open("data.json", "w") as f:
    json.dump(my_dict, f, indent=4)
# Load back and print
with open("data.json") as f:
    data = json.load(f)

# 39.3
# Task:
my_dict = {'name': 'Miklo', 'age': 25,
           'skills': ['Python', 'R', 'C++'],
           'active': True}
           
#try:
#    with open("data.json", "w") as f:
#        json.dump(my_dict, f, indent = 4, sort_keys = False)
#    print("File saved successfully.")
#except TypeError as e:
#    print("Serialization error:", e)
#except OSError as e:
#    print("File error: ", e)

# 39.4
# Task:

with open("data.json", "r") as f:
    data = json.load(f)

#for k, v in data.items():
#    print(f"{k:<10}: {v}")

# 40.0
# Task: Write a Python program to create a dictionary of keys x, y, and z where
# each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.

my_dict = dict(x = list(range(11, 20)), y = list(range(21, 30)), z = list(range(31, 40)))

# 40.1
# Task: Write a Python program to create a dictionary with keys 'x', 'y', and 'z'
# and assign each key a list of consecutive integers within specified ranges.
my_dict = {'x': list(range(1, 21)), 'y': list(range(21, 31)), 'z': list(range(31, 41))}

# 40.2
# Task: Write a Python program to generate a dictionary where key 'x' contains
# numbers 11–20, 'y' contains 21–30, and 'z' contains 31–40, then print the fifth element of each list.
my_dict = {'x': list(range(1, 21)), 'y': list(range(21, 31)), 'z': list(range(31, 41))}

# Fifth element
#print(f"{my_dict}\n")
#for k in my_dict:
#    print(my_dict[k][5])

# 40.3
# Task: Write a Python program to dynamically generate a dictionary with keys
# based on user input and list values as ranges, then access a specific index from each list.
user_input_keys = list(input("Please enter up to three keys: "))
user_input_keys = list(filter(lambda x: x.isalpha() or x.isdigit(), user_input_keys))

out = {}
for k in range(0, len(user_input_keys)):
    out.update({user_input_keys[k]: list(range(1, 22, k+1))})

# 40.4
# Task: Write a Python program to implement a function that builds a nested
# dictionary with keys 'x', 'y', 'z' mapping to lists of numbers and returns selected elements from each.
keys = ['x', 'y', 'z']

def build_nested_dict(kys, ele):
    out = dict()
    for k in range(len(kys)):
        out.update({kys[k]: {f'item{k+1}': list(range(1, 15, k+1))}})
   
    elements = []
   
    for k in out:
        for values in out[k].values():
            elements.append(values[ele])
   
    return elements

result = build_nested_dict(keys, 2)


# 41.0
# Task: Write a Python program to drop empty items from a given dictionary.
my_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}

#result = {k: v for k, v in my_dict.items() if v is not None}

# 41.1
# Task: Write a Python program to remove keys with values that are None, empty
# strings, or empty lists from a dictionary using dictionary comprehension.
my_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': "", 'c5': []}
eliminate = [None, "", []]

result = {k: v for k, v in my_dict.items() if v not in eliminate}
result

# 41.2
# Task: Write a Python program to filter out false values
# (e.g., None, "", [], {}) from a dictionary and return a new dictionary.
my_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': "", 'c5': [], 'c6': {}}

out = {}
for k, v in my_dict.items():
    if v not in [None, "", [], {}]:
        out[k] = v

# 41.3
# Task: Write a Python function to recursively drop empty items from a nested
# dictionary.
my_dict = {'item1': {'c1': 'Red'}, 'item2': {'c2': 'Green'}, 'item3': {'c3': None}, 'item4': {'c4': ""}, 'item5': {'c5': []}, 'item6': {'c6': {}}}
invalid = [None, "", [], {}]

def del_empty(d, inv):
    if not isinstance(d, dict):
        return d
   
    out = {}
   
    for k, v in d.items():
        if isinstance(v, dict):
            nested = del_empty(v, inv)
            if nested:
                out[k] = nested
        else:
            if v not in inv:
                out[k] = v
   
    return out

result = del_empty(my_dict, invalid)

# 41.4
# Task: Write a Python program to iterate over a dictionary and remove keys
# whose values evaluate to False.
my_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': False, 'c5': [], 'c6': {}}

def remove_false(d):
    if not isinstance(d, dict):
        return d
   
    out = {}
   
    for k, v in d.items():
        if isinstance(v, dict):
            nested = remove_false(v)
            if nested:
                out[k] = nested
        else:
            if v:
                out[k] = v
           
    return out

result = remove_false(my_dict)

# 42.0
# Task: Write a Python program to filter a dictionary based on values.
my_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

result = {k: v for k, v in my_dict.items() if v >= 178}

# 42.1
# Task: Write a Python program to filter a dictionary and return only those
# entries where the value exceeds a given threshold.
my_dict = {'Cierra Vega': 175, 'Alden Cantrell': 160}

result = dict(filter(lambda x: x[1] >= 170, my_dict.items()))
print(result)

# 42.2
# Task: Write a Python program to use a lambda function in dictionary
# comprehension to keep only key-value pairs satisfying a condition.
my_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

result = dict(filter(lambda x: x[0] == 'Alden Cantrell' and x[1] == 180, my_dict.items()))
# OR
result = {k: v for k, v in my_dict.items() if k == 'Alden Cantrell' and v == 180}

# 42.3
# Task: Write a Python program to create a new dictionary by removing entries
# whose values do not meet a specified predicate.
my_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

out = {}
for k, v in my_dict.items():
    if v >= 176:
        out[k] = v

print(out)

# 42.4
# Task: Write a Python function to filter a dictionary based on a dynamic
# condition provided as a parameter.
my_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

def rm_dynamic(d, condition):
    return {k: v for k, v in d.items() if condition(k, v)}

result = rm_dynamic(my_dict, ('Cierra Vega', 175))

# 43.0
# Task: Write a Python program to convert more than
# list to a nested dictionary.
student_id = ["S001", "S002", "S003", "S004"]
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
student_grade = [85, 98, 89, 92]

out = {}
for k, v1, v2 in zip(student_id, student_name, student_grade):
        out[k] = {v1: v2}

# OR
result = {k: {v1: v2} for k, v1, v2 in zip(student_id, student_name, student_grade)}

# 43.1
# Task: Write a Python program to merge three
# lists into a list of nested dictionaries using zip() and list comprehension.
student_id = ["S001", "S002", "S003", "S004"]
student_name = ["Peter Park", "Leyton Marsh", "Duncan Boyle", "Donald Richards"]
student_grade = [85, 98, 89, 92]

result = [{k: {v1: v2}} for k, v1, v2 in zip(student_id, student_name, student_grade)]

# 43.2
# Task: Write a Python function that takes three
# parallel lists (IDs, names, scores) and returns a nested dictionary for each item.
student_id = ["S001", "S002", "S003", "S004"]
student_name = ["Peter Park", "Leyton Marsh", "Duncan Boyle", "Donald Richards"]
student_grade = [85, 98, 89, 99]

def compress_lst(id_lst1, id_lst2, id_lst3):
    return {k: {v1: v2} for k, v1, v2 in zip(id_lst1, id_lst2, id_lst3)}
   
result = compress_lst(student_id, student_name, student_grade)

# 43.3
# Task: Write a Python program to convert multiple lists into a nested
# dictionary where each outer key maps to a dictionary of inner key-value pairs.
student_id = ["S001", "S002", "S003", "S004"]
student_name = ["Peter Park", "Leyton Marsh", "Duncan Boyle", "Donald Richards"]
student_grade = [85, 98, 89, 99]

result = {k: {v1: v2} for (k, v1, v2) in zip(student_id, student_name, student_grade)}

# 43.4
# Task: Write a Python program to build a nested.
# dictionary from several lists while ensuring proper pairing of elements.
student_id = ["S001", "S002", "S003", "S004"]
student_name = ["Peter Park", "Leyton Marsh", "Duncan Boyle", "Donald Richards"]
student_grade = [85, 98, 89, 99]

def compress_lst(l1, l2, l3):
    if not len(l1) == len(l2) == len(l3):
        raise ValueError("All lists must have the same length.")
   
    out = {}
    for k, v1, v2 in zip(l1, l2, l3):
        out[k] = {v1: v2}
           
    return out

result = compress_lst(student_id, student_name, student_grade)

# 44.0
# Task: Write a Python program to filter the height and width of students,
# which are stored in a dictionary.
my_dict = {
    'Cierra Vega': (6.2, 70),
    'Michael Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (6.3, 66)
}

def find_hw(d, height, width):
    return dict(filter(lambda x: x[1][0] > height and x[1][1] > width, d.items()))

result = find_hw(my_dict, 6, 65)
result

# 44.1
# Task: Write a Python program to filter a dictionary of student names
# and (height, weight) tuples and return only those meeting specified thresholds.
my_dict = {
    'Cierra Vega': (6.2, 70),
    'Michael Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (6.3, 66)
}

height = 6
weight = 65

out = {}

for k, v in my_dict.items():
    if v[0] > height and v[1] > weight:
        out[k] = v        

# 44.2
# Task: Write a Python program to use dictionary comprehension to extract
# student entries with height greater than 6.0 ft and weight over 70 kg.
my_dict = {
    'Cierra Vega': (6.2, 70),
    'Michael Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (6.3, 66),
    'Luke Vice': (6.6, 110)
}

def find_hw(d, height, weight):
    return dict(filter(lambda x: x[1][0] > height and x[1][1] > weight, d.items()))

result = find_hw(my_dict, 6, 70)

# 44.3
# Task: Write a Python program to iterate over a dictionary and select
# keys where both the height and weight satisfy given conditions.
my_dict = {
    'Cierra Vega': (6.2, 70),
    'Michael Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (6.3, 66)
}

def find_hw(d, height, weight):
    return dict(filter(lambda x: x[1][0] > height or x[1][1] > weight, d.items()))
   
result = find_hw(my_dict, 6.1, 70)

# 44.4
# Task: Write a Python function that takes a dictionary of
# (height, weight) pairs and returns a new dictionary with only the valid entries.
my_dict = {
    'Cierra Vega': (6.2, 70),
    'Michael Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (6.3, 66),
    'Luke Vice': (6.6, 110)
}

result = lambda h, w: dict(filter(lambda x: x[1][0] > h and x[1][1] > w, my_dict.items()))

result(6, 70)

# 45.0
# Task: Write a Python program to verify that all values in a dictionary are the same.
my_dict = {'Mike': 12, 'Steve': 12, 'Rick': 12, 'John': 12, 'Irving': 12}

# Method 1: Loop

def check_if_all_same(d):
    values = list(d.values())
   
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[j] != values[i]:
                return False
   
    return True

# Method 2:

def check_if_all_same(d):
    t = list(d.values())[0]
   
    return all(v == t for v in d.values())

result = check_if_all_same(my_dict)

# 45.1
# Task: Write a Python program to check if all values in a
# dictionary are identical using set conversion.
my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

result = len(set(my_dict.values())) == 1  

# 45.2
# Task: Write a Python program to implement an all() based check
# that verifies if every dictionary value equals the first value.
my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 13, 'Kierra Gentry': 13, 'Pierre Cox': 13}

initial_value = int(my_dict['Cierra Vega'])

result = all(v == initial_value for v in my_dict.values())

# 45.3
# Task: Write a Python program to compare each value to the first one
# in a loop and return True if they are all the same.
my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

initial_value = my_dict['Cierra Vega']

def all_loop(d, initial_value):
    for v in my_dict.values():
        if v != initial_value:
            return False
   
    return True

result = all_loop(my_dict, initial_value)

# 45.4
# Task: Write a Python function to recursively check the uniformity
# of dictionary values.
my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
initial_value = my_dict['Cierra Vega']

def recursive_all(d, first):
    for v in d.values():
        if isinstance(v, dict):
            first = check_uniform(v, first)
            if first is False:
                return False
        else:
            if first is None:
                first = v
            elif v != first:
                return False
   
    return first

def is_uniform(d, initial_value):
    return recursive_all(d, initial_value) is not False

result = is_uniform(my_dict, initial_value)

# 46.0
# Task: Write a Python program to create a dictionary grouping a sequence of
# key-value pairs into a dictionary of lists.
my_list = [('fantasy', 15), ('mediumorchid', 17), ('fantasy', 16), ('mediumorchid', 12)]

# Method 1: Standard

def group_vals(lst):
    out = {}
    for k, v in lst:
        out.setdefault(k, []).append(v)
   
    return out

result = group_vals(my_list)

# Method 2: defaultdict

def group_vals(lst):
    out = defaultdict(list)
   
    for k, v in lst:
        out[k].append(v)
   
    return out

result = group_vals(my_list)

# 46.1
# Task: Write a Python program to group a list of key-value tuples into a dictionary
# where each key maps to a list of its associated values using collections.defaultdict.
my_list = [('fantasy', 15), ('mediumorchid', 17), ('fantasy', 16), ('mediumorchid', 12)]

def group_vals(lst):
    out = defaultdict(list)
   
    for k, v in lst:
        out[k].append(v)
   
    return out

result = group_vals(my_list)

# 46.2
# Task: Write a Python program to use dictionary comprehension to form a dictionary
# of lists from a sequence of tuples.
my_tuples = [('item1', 12), ('item2', 13), ('item3', 14), ('item1', 15), ('item5', 16), ('item5', 17), ('item7', 18), ('item2', 19)]

result = {k: [v for key, v in my_tuples if key == k] for k, _ in my_tuples}

# 46.3
# Task: Write a Python program to iterate over a list of pairs and build a grouped
# dictionary, appending values for duplicate keys.
my_tuples = [('item1', 12), ('item2', 13), ('item3', 14), ('item1', 15), ('item5', 16), ('item5', 17), ('item7', 18), ('item2', 19)]

# Method 1: Loop
def groupwith_loop(lst):
    out = {}
    for k, v in lst:
        if k not in out:
            out[k] = []
        out[k].append(v)
   
    return out

result = groupwith_loop(my_tuples)

# Method 2: setdefault
def groupwith_setdefault(lst):
    out = {}
    for k, v in lst:
        out.setdefault(k, []).append(v)
   
    return out

result = groupwith_setdefault(my_tuples)

# Method 3: defaultdict

def groupwith_defaultdict(lst):
    out = defaultdict(list)
    for k, v in lst:
        out[k].append(v)
   
    return out

result = groupwith_defaultdict(my_tuples)

# 46.4
# Task: Write a Python function to convert a list of key-value pairs into a
# dictionary of lists, ensuring order is preserved.
my_tuples = [('item1', 12), ('item2', 13), ('item3', 14), ('item1', 15), ('item5', 16), ('item5', 17), ('item7', 18), ('item2', 19)]

def groupwith_defaultdict(lst):
    out = defaultdict(list)
    for k, v in lst:
        out[k].append(v)
   
    return out

result = groupwith_defaultdict(my_tuples)
 
# 47.0
# Task: Write a Python program to split a given dictionary
# of lists into lists of dictionaries.
my_dict = {'Science': [84, 70, 66, 55, 90], 'Language': [90, 88, 98, 100, 76]}
   
def list_of_dicts(marks):
    # Get the keys (subjects) from the 'marks' dictionary.
    keys = marks.keys()
   
    # Use the 'zip' function to transpose the lists of marks into tuples.
    vals = zip(*[marks[k] for k in keys])
   
    # Create a list of dictionaries by zipping the keys and the transposed tuples.
    result = [dict(zip(keys, v)) for v in vals]
    return result

result = list_of_dicts(my_dict)

# 47.1
# Task: Write a Python program to convert a dictionary of
# lists into a list of dictionaries by zipping the list values.
my_dict = {'Science': [84, 70, 66, 55, 90], 'Language': [90, 88, 98, 100, 76]}

keys = my_dict.keys()
values = zip(*[my_dict[k] for k in keys])

result = [dict(zip(keys, v)) for v in values]

# 47.2
# Task: Write a Python function that takes a dictionary
# with list values and returns a list of dictionaries for each index.
my_dict = {'Science': [84, 70, 66, 55, 90], 'Language': [90, 88, 98, 100, 76]}

def list_of_dicts(d):
    # Keys
    keys = d.keys()
    # Values
    vals = zip(*[d[k] for k in keys])
    # out
    out = [dict(zip(keys, v)) for v in vals]
   
    return out

result = list_of_dicts(my_dict)

# 47.3
# Task: Write a Python program to use list comprehension
# and zip() to transform a dictionary of lists into multiple dictionaries.
my_dict = {'Science': [84, 70, 66, 55, 90], 'Language': [90, 88, 98, 100, 76]}

def list_of_dicts(d):
    return [dict(zip(d.keys(), v)) for v in zip(*d.values())]

result = list_of_dicts(my_dict)

# 47.4
# Task: Write a Python program to implement a function that
# decomposes a dictionary of lists into a list of single-key dictionaries.
my_dict = {'Science': [84, 70, 66, 55, 90], 'Language': [90, 88, 98, 100, 76]}
   
def decompose_dict(d):
    return [{k: v} for k, values in d.items() for v in values]

result = decompose_dict(my_dict)

# 48.0 
# Task: Write a Python program to remove a specified dictionary from a given list.
my_dicts = [
    {"id": "#FF0000", "color": "Red"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#FFFF00", "color": "Yellow"},
    {"id": "#808000", "color": "Olive"}
]

target_key = '#FF0000'

def remove_dict(lst, t):
    lst[:] = [d for d in lst if d.get('id') != t]
   
    return lst

result = remove_dict(my_dicts, target_key)

# 48.1
# Task: Write a Python program to filter out a dictionary
# from a list based on a matching key-value pair using list comprehension.
my_dicts = [
    {"id": "#FF0000", "color": "Red"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#FFFF00", "color": "Yellow"},
    {"id": "#808000", "color": "Olive"}
]

target_pair = ("id", "#FF0000")

def remove_dict(lst, t):
    for d in lst:
        for k, v in d.items():
            if (k, v) == t:
                lst.remove(d)
   
    return lst

result = remove_dict(my_dicts, target_pair)

# 48.2
# Task: Write a Python program to remove a dictionary with a
# specified key from a list of dictionaries by iterating over the list.
my_dicts = [
    {"id": "#FF0000", "color": "Red"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#FFFF00", "color": "Yellow"},
    {"id": "#808000", "color": "Olive"}
]

ref_key = "id"
target_value = "#FFFF00"

def remove_dict(lst, ref_key, target_key):
    for d in lst:
        if d.get(ref_key) == target_value:
            lst.remove(d)
   
    return lst

result = remove_dict(my_dicts, ref_key, target_key)

# 48.3
# Task: Write a Python program to implement a function that
# deletes dictionaries from a list that match given criteria.
my_dicts = [
    {"id": "#FF0000", "color": "Red", "Jeans": "Yes"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#FFFF00", "color": "Yellow"},
    {"id": "#808000", "color": "Olive"}
]

criteria = lambda val: val == 2

def remove_dict(lst, criteria):
    return [d for d in lst if criteria(len(d))]

result = remove_dict(my_dicts, criteria)

# 48.4
# Task: Write a Python program to use filter()
# to exclude dictionaries that contain a specific key-value combination.
my_dicts = [
    {"id": "#FF0000", "color": "Red"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#0000FF", "color": "Blue"},
    {"id": "#FFFFFF", "color": "White"}
]

target_pair = ("color", "Maroon")

def remove_dict(lst, target_pair):
    return list(filter(lambda d: target_pair not in d.items(), lst))

result = remove_dict(my_dicts, target_pair)

# 49.0
# Task: Write a Python program to convert string
# values of a given dictionary into integer/float datatypes.
my_dicts = [{'x': '10'}, {'y': '12'}, {'z': '15'},
           {'w': '22.13'}, {'v': '24'}, {'n': '65'}]


result = [{k: int(v) if v.isdigit() else float(v) for k, v in d.items()} for d in my_dicts]

# 49.1
# Task: Write a Python program to iterate over
# a dictionary and convert numeric string values to integers using int().
my_dicts = [{'x': '10'}, {'y': '12'}, {'z': 'honey'},
           {'w': '22.13'}, {'v': '24'}, {'n': '65'}]

def convert_int(lst):
    for d in lst:
        for k, v in d.items():
            if isinstance(v, (int, float)):
                d[k] = int(v)
   
    return lst

result = convert_int(my_dicts)

# 49.2
# Task: Write a Python program to update dictionary
# values to float if they contain a decimal point, otherwise to int.
my_dicts = [{'x': '10'}, {'y': '12'}, {'z': '33.65'},
           {'w': '22.13'}, {'v': '24'}, {'n': '65'}]

result = [{k: int(v) if '.' not in v else float(v) for k, v in d.items()} for d in my_dicts]

# 49.3
# Task: Write a Python program to use try/except
# to safely cast dictionary string values to numeric types.
my_dict = {'x': '12.11', 'y': '6', 'z': '8',
            'w': '16.78', 'v': '15.42', 'u': '4'}

def convert_vals(d):
    out = {}
    for k, v in d.items():
        try:
            if '.' in v:
                out[k] = float(v)
            else:
                out[k] = int(v)
       
        except ValueError:
            out[k] = v
   
    return out

result = convert_vals(my_dict)
           
# 49.4
# Task: Write a Python function that checks each
# value of a dictionary and converts it to a numeric type if possible.
my_dict = {'x': '12.11', 'y': '6', 'z': '8',
            'w': '16.78', 'v': '15.42', 'u': 'hex'}


def convert_vals(d):
    for k, v in d.items():
        try:
            if '.' in v:
                d[k] = float(v)
            else:
                d[k] = int(v)
       
        except ValueError:
            d[k] = v
   
    return d

result = convert_vals(my_dict)

# 50.0
# Task: A Python dictionary contains List as a value. Write a
# Python program to clear the list values in the said dictionary.
my_dict = {'c1': [12, 14, 16], 'c2': [17, 12, 11], 'c3': [66, 87], 'c4': 2}

for k, v in my_dict.items():
    if isinstance(v, list):
        my_dict[k].clear()
   
    else:
        my_dict[k] = v

# 50.1
# Task: Write a Python program to iterate over a dictionary
# and set each list value to an empty list using dictionary comprehension.
my_dict = {'c1': [12, 14, 16], 'c2': [17, 12, 11], 'c3': [66, 87], 'c4': 2}

for k, v in my_dict.items():
    if isinstance(v, list):
        my_dict[k] = []
    else:
        my_dict[k] = v

# 50.2
# Task: Write a Python program to update a dictionary
# in-place by replacing each list with an empty list.
my_dict = {'c1': [12, 14, 16], 'c2': [17, 12, 11], 'c3': [66, 87], 'c4': 2}

for k in my_dict:
    my_dict[k] = []

# 50.3
# Task: Write a Python program to implement a function
# that returns a new dictionary with the same keys but empty lists as values.
my_dict = {'c1': [12, 14, 16], 'c2': [17, 12, 11], 'c3': [66, 87], 'c4': 2}

def empty_dict(d):
    out = {}
    for k, v in d.items():
        out[k] = []
   
    return out

result = empty_dict(my_dict)

# 50.4
# Task: Write a Python program to use a loop to clear
# list values for each key in a given dictionary.
my_dict = {'c1': [12, 14, 16], 'c2': [17, 12, 11], 'c3': [66, 87], 'c4': 2}

for k, v in my_dict.items():
    if isinstance(v, list):
        my_dict[k].clear()


# 51.0
# Task: A Python Dictionary contains List as a value.
# Write a Python program to update the list values in the said dictionary.
my_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

def update_dict_vals(d):
    d['Math'] = [x + 1 for x in d['Math']]
    d['Physics'] = [x - 2 for x in d['Physics']]                
   
    return d    

result = update_dict_vals(my_dict)

# 51.1
# Task: Write a Python program to update each list in
# a dictionary by applying a function (e.g., increment each element by 1) to every item.
my_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
fn = lambda x: int((x**2 - x**.5)/2)

def update_dict_vals(d, f):
    for k in d:
        d[k] = [f(v) for v in d[k]]
   
    return d

result = update_dict_vals(my_dict, fn)

# 51.2
# Task: Write a Python program to use dictionary comprehension
# to modify list values, such as squaring each number.
my_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

result = {k: [x**2 for x in v] for k, v in my_dict.items()}

# 51.3
# Task: Write a Python program to iterate over a dictionary
# and update its list values in-place with a transformation.
my_dict = {'B': ['Bali', 'Baku', 'Bengal'], 'P': ['Poland', 'Prussia', 'Pitcairn'], 'C': ['China', 'Colombia', 'Cost Rica']}

transformation = lambda x:  x.lower()

for k in my_dict:
    my_dict[k] = [transformation(v) for v in my_dict[k]]

# 51.4
# Task: Write a Python program to implement a function that takes a dictionary with list values and returns an updated dictionary after processing each list.
my_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

def process_dict(d):
    for k in d:
        d[k] = [v+ 11 for v in d[k]]
   
    return d

result = process_dict(my_dict)

# 52.0
# Task: Write a Python program to extract a list of values from a given list of dictionaries.
my_dict = [{'Math': 16}, {'Math': 12}, {'Math': 11},
           {'Physics': 12}, {'Physics': 17}, {'Physics': 22}]



def extract_values(lst, key_name):
    return [d[key_name] for d in lst if key_name in d]

result = extract_values(my_dict, 'Physics')

# 52.1
# Task: Write a Python program to extract the values for a specified key from a list of dictionaries using list comprehension.
my_dict = [{'Math': 16}, {'Math': 12}, {'Math': 11},
           {'Physics': 12}, {'Physics': 17}, {'Physics': 22}]
           
result = lambda lst, subject: [d[subject] for d in lst if subject in d]

# 52.2
# Task: Write a Python program to iterate through a list of dictionaries and collect values corresponding to a given key, handling missing keys.
my_dict = [{'Math': 16}, {'Math': 12}, {'Math': 11},
           {'Physics': 12}, {'Physics': 17}, {'Physics': 22}]

#key_name = 'Math'

out = []

#for d in my_dict:
#    for k, v in d.items():
#        if k == key_name:
#            out.append(v)
 
           {'Physics': 12}, {'Physics': 17}, {'Physics': 22}]

key_name = 'Math'

#result = list(map(lambda x: x['Math'], my_dict))

# 52.4
# Task: Write a Python function that returns a list of values for a given key from a list of dictionaries, excluding dictionaries where the key is absent.
my_dict = [{'Math': 16}, {'Math': 12}, {'Math': 11, 'Overall': 16},
           {'Physics': 12}, {'Physics': 17}, {'Physics': 22}]
           
def get_values(lst, key_name):
    return [d[key_name] for d in lst if key_name in d]

# 53.0
# Task: Write a Python program to find the length of a dictionary of values.
my_dict = {1: 'red', 2: 'green', 3: 'blue', 4: 'white', 5: 'orange'}

def sum_dict_vals(d):
    out = {}
    for k, v in d.items():
        out[k] = len(v)
   
    return out

result = sum_dict_vals(my_dict)

def sum_dict_vals(d):
    return {k: len(v) for k, v in d.items()}

# 53.1
# Task: Write a Python program to determine the number of key-value pairs in a dictionary using the len() function.
my_dict = {1: 'red', 2: 'green', 3: 'blue', 4: 'white', 5: 'orange'}

def kv_pairs(d):
    return len(d.items())

result = kv_pairs(my_dict)

# 53.2
# Task: Write a Python program to iterate through a dictionary and manually count it's items.
my_dict = {1: 'red', 2: 'green', 3: 'blue', 4: 'white', 5: 'orange'}

def kv_pairs(d):
    out = 0
   
    for item in d.items():
        out+=1
   
    return out
   
#print(f"Number of items in a dictionary: {kv_pairs(my_dict)}")

# 53.3
# Task: Write a Python program to implement a recursive function that calculates the length of a dictionary.
my_dict = {1: 'red', 2: 'green', 3: 'blue', 4: 'white', 5: 'orange'}

def dict_len(d):
    keys = list(d.keys())
   
    def count_recursive(lst):
        if not lst:
            return 0
        return 1 + count_recursive(lst[1:])
   
    return count_recursive(keys)

result = dict_len(my_dict)

# 53.4
# Task: Write a Python program to use list comprehension on dictionary keys to compute the total count of entries.
my_dict = {1: 'red', 2: 'green', 3: 'blue', 4: 'silver', 5: 'teal'}

def count_entries(keys):
    return len([k for k in keys])

keys = my_dict.keys()
result = count_entries(keys)
# print(f"The total number of entries: {result}")

# 54.0
# Write a Python program to get the depth of a dictionary.
my_dict = {'a': 1, 'b': {'c': {'d': {}}}}

def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    return 1 + max(dict_depth(v) for v in d.values())

result = dict_depth(my_dict)
       
# 54.1
# Write a Python program to recursively determine the maximum nesting depth of a dictionary.
my_dict = {'a': 1, 'b': {'c': {'d': {}}}}

def max_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
   
    return 1 + max(max_depth(v) for v in d.values())

# 54.2
# Write a Python program to implement a function that returns 1 for a flat dictionary and adds depth for nested dictionaries.
my_dict_nested = {'a': 1, 'b': {'c': {'d': {}}}}
my_dict_flat = {'a': 16, 'b': 22, 'c': 55}

def max_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
   
    return 1 + max(max_depth(v) for v in d.values())

result = max_depth(my_dict_flat)

# 54.3
# Write a Python program to iterate over dictionary values and compute the depth when values are dictionaries themselves.
my_dict = {'a': 1, 'b': {'c': {'d': {}}}, 'e': {'f': {'g': {'h': {}}}}}

def compute_dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    return 1 + max(compute_dict_depth(v) for v in d.values())

def dict_depth(d):
    out = {}
   
    for k, v in d.items():
        out[k] = compute_dict_depth(v)
   
    return out

# 54.4
# Write a Python program to use recursion to track the nesting level of a dictionary and output its maximum depth.
my_dict = {'a': 1, 'b': {'c': {'d': {}}}, 'e': {'f': {'g': {'h': {}}}}}

def max_depth(d, level = 1):
    if not isinstance(d, dict) or not d:
        return level - 1
    return max(max_depth(v, level + 1) for v in d.values())

# Loop version:
def max_depth(d, level = 1):
    if not isinstance(d, dict) or not d:
        return level - 1
   
    deepest = level
   
    for v in d.values():
        depth = max_depth(v, level+1)
        if depth > deepest:
            deepest = depth
   
    return deepest

def max_depth(d, level = 1):
    if not isinstance(d, dict) or not d:
        return level - 1
   
    deepest = level

# Print tracing:

def max_depth(d, level = 1):
    print(f"\nEntering: {d} at level {level}")
   
    if not isinstance(d, dict) or not d:
        print(f"\nReturning {level - 1} because {d} is not a dictionary")
        return level - 1
   
    result = max(max_depth(v, level + 1) for v in d.values())
   
    print(f"\nReturning {result} from level {level}")
   
    return result

# 55.0
# Task: Write a Python program to access dictionary key's element by index.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

find_ele = lambda ele: list(my_dict)[ele]

# 55.1
# Task: Write a Python program to retrieve a dictionary key by converting the keys to a list and accessing the nth element.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

find_key = lambda ele: list(my_dict.keys())[ele]

# 55.2
# Task: Write a Python program to implement a function that returns the key at a specified index from a dictionary.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

def find_key(d, index):
    return list(d.keys())[index]

# 55.3
# Task: Write a Python program to sort the dictionary keys and then return the key at a given index.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

sorted_dict = dict(sorted(my_dict.items(), key = lambda x: x[0]))

find_key = lambda d, ele: list(d)[ele]

# 55.4
# Task: Write a Python program to iterate over a dictionary with enumerate() and output the key when the index matches the input value.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

def dict_iter(d, input_value):
    for i, (k, v) in enumerate(d.items()):
        if i == input_value:
            return k
   
    return "Value not found"
    
# 56.0
# Task: Write a Python program to convert a dictionary into a list of lists.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

convert_to_list = lambda d: list(map(list, d.items()))

# 56.1
# Task: Write a Python program to convert a dictionary into a list of two-element lists using the items() method.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

convert_to_list = lambda d: list(map(list, d.items()))

# 56.2
# Task: Write a Python program to iterate over a dictionary and build a nested list where each sublist contains a key and its corresponding value.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

def dict_iterator(d):
    out = []
   
    for k, v in d.items():
        out.append([k, v])
   
    return out

# 56.3
# Task: Write a Python program to use list comprehension to convert a dictionary into a sorted list of lists based on keys.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}
 
def sorted_lst(d):
    return list(map(list, sorted(d.items(), key = lambda x: x[1])))
   
# 56.4
# Task: Write a Python program to implement a function that transforms a dictionary into a list of [key, value] pairs and returns it.
my_dict = {'Math': 90, 'Physics': 92, 'Engineering': 100}

def convert_to_list(d):
    return list(map(list, d.items()))

# 57.0
# Task: Write a Python program to filter even numbers from a dictionary of values.
my_dict = {'VI': [1, 2, 3, 4, 5], 'VII': [6, 7, 8, 9, 10],
           'VIII': [11, 12, 13, 14, 15]}

is_odd = lambda x: x % 2 != 0

def filter_dict(d, function):
    for k, values in d.items():
        d[k] = []
        for v in values:
            if function(v):
                d[k].append(v)
       
    return d

# 57.1
# Task: Write a Python program to update a dictionary by filtering each list value to include only even numbers using dictionary comprehension.
my_dict = {'VI': [1, 2, 3, 4, 5], 'VII': [6, 7, 8, 9, 10],
           'VIII': [11, 12, 13, 14, 15]}

is_even = lambda x: x % 2 == 0

def fiter_dict(d, function):
    return {k: [v for v in values if function(v)] for k, values in d.items() if function(v)}

# 57.2
# Task: Write a Python program to iterate over a dictionary and create a new dictionary with list values containing only even integers.
my_dict = {'VI': [1, 2, 3, 4, 5], 'VII': [6, 7, 8, 9, 10],
           'VIII': [11, 12, 13, 14, 15]}
           
def filter_dict(d, function):
    out = {}
   
    for k, values in d.items():
        out[k] = []
        for v in values:
            if function(v):
                out[k].append(v)
    return out

# 57.3
# Task: Write a Python program to implement a function that processes a dictionary with lists and returns a dictionary of even numbers only.
my_dict = {'VI': [1, 2, 3, 4, 5], 'VII': [6, 7, 8, 9, 10],
           'VIII': [11, 12, 13, 14, 15]}

def filter_dict(d, function):
    return {k: [v for v in values if function(v)] for k, values in d.items()}

# 57.4
# Task: Write a Python program to use a for-loop to filter out odd numbers from each list value in a dictionary.
my_dict = {'VI': [1, 2, 3, 4, 5], 'VII': [6, 7, 8, 9, 10],
           'VIII': [11, 12, 13, 14, 15]}

def filter_dict(d, function):
    out = {}
   
    for k, values in d.items():
        out[k] = []
        for v in values:
            if function(v):
                out[k].append(v)
         
    return out
    
# 58.0
# Task: Write a Python program to get all combinations of key-value pairs in a given dictionary.
my_dict = {'V': [1, 4, 6, 8], 'VI': [10, 12, 14, 16], 'VII': [18, 20, 22, 24]}
 
def all_combinations(d):
    return list(map(dict, combinations(d.items(), 2)))

# loop version
def all_combinations(d):
    items = list(d.items())
    out = {}
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            print(items[i], items[j])
    return ''

# 58.1
# Task: Write a Python program to generate all possible combinations of two keys from a dictionary using itertools.combinations.
   
def all_combinations(d):
    return list(map(dict, combinations(d.items(), 2)))

# 58.2
# Task: Write a Python program to create a list of dictionaries, each containing a unique combination of key-value pairs of a given size.
my_dict = {'V': [1, 4, 6, 8], 'VI': [10, 12, 14, 16], 'VII': [18, 20, 22, 24]}

def all_combinations(d, size):
    return list(map(dict, combinations(d.items(), size)))
 
# 58.3
# Task: Write a Python program to implement a function that returns all subsets of key-value pairs from a dictionary.
my_dict = {'V': [1, 4, 6, 8], 'VI': [10, 12, 14, 16], 'VII': [18, 20, 22, 24]}

def all_subsets(d):
    items = list(d.items())
    out = []
   
    for r in range(1, len(items) + 1):
        for combo in combinations(items, r):
            out.append(dict(combo))
   
    return out

# 58.4
# Task: Write a Python program to use recursion to generate combinations of keys and return corresponding sub-dictionaries.
my_dict = {'VI': [1, 4, 8, 12], 'VII': [14, 16, 18, 20],
           'VIII': [22, 24, 26, 28]}

def all_combos_recursive(d, r = 1, result = None):
    if result == None:
        result = []
   
    items = list(d.items())
   
    if r > len(items):
        return result
   
    for combo in combinations(items, r):
        result.append(dict(combo))
   
    return all_combos_recursive(d, r = r + 1, result = result)
       
# 59.0
# Task: Write a Python program to find the specified number of maximum values in a given dictionary.
my_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 11, 'h': 16, 'g': 6}

def find_max_vals(d, n_vals):
    return sorted(d.values())[-n_vals::]

# 59.1
# Task: Write a Python program to extract the top k key-value pairs from a dictionary using heapq.nlargest.
my_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 11, 'h': 16, 'g': 6}

#print(nlargest(3, my_dict.items(), key = lambda x: x[1]))

# 59.2
# Task: Write a Python program to sort a dictionary by its values and return a list of keys corresponding to the top k values.
my_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 11, 'h': 16, 'g': 6}

def top_keys(d, n_keys):
    sorted_dict = dict(sorted(d.items(), key = lambda x: x[1]))
   
    return list(sorted_dict.keys())[-n_keys::]

# 59.3
# Task: Write a Python function to iterate through a dictionary and maintain a list of the k largest values.
my_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 11, 'h': 16, 'g': 6}

def max_vals(d, k):
    out = []    
    max_val = 0
    values = list(d.values())
   
    for i in range(k):
        max_val = max(values)
        out.append(max_val)
       
        ind = values.index(max_val)
        del values[ind]
   
           
    return out

# 59.4
# Task: Write a Python program to use sorted() with a custom key to retrieve the top k maximum values from a dictionary.
my_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 11, 'h': 16, 'g': 6}

def find_max_vals(d, k):
    # k: Number of maximum values.
    sorted_lst = dict(sorted(d.items(), key = lambda x: x[1], reverse=False))
   
    return list(sorted_lst.values())[-k::]
   
# 60.0
# Task: Write a Python program to find the shortest list of values for the keys in a given dictionary.
my_dict = {'V': [10], 'VI': [11, 12], 'VII': [16, 12, 14],
           'VIII': [9, 8, 4, 12], 'IX': [1], 'X': [12, 19]}

def find_shortest_elements(d):
    min_list = []
    min_val = len(min(d.values(), key = lambda x: len(x)))
       
    for k, v in d.items():
        if len(v) == min_val:
            min_list.append((k, v))
   
    return [k for k in dict(min_list).keys()]

# OR list comprehension
min_val = len(min(my_dict.values(), key = lambda x: len(x)))

def find_shortest_elements(d):
    return [k for k, v in d.items() if len(v) == min_val]

# 60.1
# Task: Write a Python program to identify keys in a dictionary whose associated list has the minimum length using min().
my_dict = {'V': [10], 'VI': [11, 12], 'VII': [16, 12, 14],
           'VIII': [9, 8, 4, 12], 'IX': [1], 'X': [12, 19]}

min_length = len(min(my_dict.values(), key = lambda x: len(x)))

min_len_keys = lambda d: [k for k, v in d.items() if len(v) == min_length]

# 60.2
# Task: Write a Python program to use dictionary comprehension to filter keys with the shortest list values.
my_dict = {'V': [10], 'VI': [11, 12], 'VII': [16, 12, 14],
           'VIII': [9, 8, 4, 12], 'IX': [1], 'X': [12, 19]}

min_len_keys = lambda d: [k for k, v in d.items() if len(v) == len(min(d.values(), key = lambda x: len(x)))]

# 60.3
# Task: Write a Python program to iterate over a dictionary and return the keys corresponding to the shortest list value.
my_dict = {'V': [10], 'VI': [11, 12], 'VII': [16, 12, 14],
           'VIII': [9, 8, 4, 12], 'IX': [1], 'X': [12, 19]}

def min_len_keys(d):
    kv_list = []
    min_length = len(min(d.values(), key = lambda x: len(x)))
       
    for k, v in d.items():
        if len(v) == min_length:
            kv_list.append((k, v))
   
    return [k for k in dict(kv_list).keys()]
    
# 60.4
# Task: Write a Python program to implement a function that returns all keys that have the minimum list length in a dictionary.
my_dict = {'V': [10], 'VI': [11, 12], 'VII': [16, 12, 14],
           'VIII': [9, 8, 4, 12], 'IX': [1], 'X': [12, 19]}

min_list_len = lambda d: [k for k, v in d.items() if len(v) == len(min(d.values(), key = lambda x: len(x)))]

# 61.0
# Task: Write a Python program to count the frequency of values inside a dictionary.
my_dict  = {'V': 10, 'VI': 10, 'VII': 20, 'VIII': 20,
           'IX': 30, 'X': 30, 'XI': 35, 'XII': 40}
           
def count_values(d):
    out = {}
   
    keys = [k for k in set(d.values())]
    values = list(d.values())
       
    for k in keys:
        out[k] = 0
        for v in values:
            if v == k:
                out[k]+=1
   
    return out

# 61.1
# Task: Write a Python program to count the frequency of each value in a dictionary using collections.Counter.
def count_values(d):
    return Counter(d.values())

# 61.2
# Task: Write a Python program to iterate over dictionary values and build a new dictionary mapping each value to its occurrence count.
my_dict = {'V': 10, 'VI': 10, 'VII': 20, 'VIII': 20,
           'IX': 30, 'X': 30, 'XI': 35, 'XII': 40}

def count_values(d):
    out = {}
   
    keys = [k for k in set(d.values())]
    values = list(d.values())
   
    for k in keys:
        out[k] = 0
        for v in values:
            if v == k:
                out[k] += 1
   
    return out
   
# 61.3
# Task: Write a Python program to use dictionary comprehension to generate a frequency dictionary from the values of another dictionary.
my_dict = {'V': 10, 'VI': 20, 'VII': 10, 'VIII': 20,
           'IX': 40, 'X': 50, 'XI': 60, 'XII': 70}

def freq_table(d):
    return {k: list(d.values()).count(k) for k in set(d.values())}


# 61.4
# Task: Write a Python program to implement a function that returns the frequency distribution of dictionary values.
my_dict = {'V': 10, 'VI': 20, 'VII': 10, 'VIII': 20,
           'IX': 40, 'X': 50, 'XI': 60, 'XII': 70}

def freq_table(d):
    return {k: list(d.values().count(k) for k in set(d.values()))}

def freq_table(d):
    return Counter(d.values())

def freq_table(d):
    keys = set(d.values())
    values = d.values()
   
    out = defaultdict(int)
   
    for k in keys:
        for v in values:
            if v == k:
                out[k]+=1
   
    return out

# 62.0
# Task: Write a Python program to extract values from a given dictionary and create a list of lists from those values.
my_dicts = [{'student_id': 1, 'name': 'John Doe', 'class': 'V'},
           {'student_id': 2, 'name': 'Jane Doe', 'class': 'VI'},
           {'student_id': 3, 'name': 'Steven Smith', 'class': 'VII'},
           {'student_id': 4, 'name': 'Steve Monicker', 'class': 'VIII'},
           {'student_id': 5, 'name': 'Nick Blossom', 'class': 'IX'}]  

find_keys = lambda d: [k for k in d.keys()]
keys = find_keys(my_dicts[0]) # or manually specify

def extract_values(dicts, keys):
    return [list(d[k] for k in keys) for d in dicts]


# 62.1
# Task: Write a Python program to extract the values from a dictionary and return them as a list of lists using list().

def extract_values(dicts):
    return [list(d.values()) for d in dicts]
 
# 62.2
# Task: Write a Python program to iterate over a dictionary and collect its values into a nested list structure.
out = []

for d in my_dicts:
    out.append(list(d.values()))
       
# 62.3
# Task: Write a Python program to use dictionary.values() and convert the resulting view into a list of lists.

out = []

for d in my_dicts:
    out.append(list(d.values()))

# 62.4
# Task: Write a Python program to implement a function that returns all dictionary values as separate lists within one list.

# Function 1: d.values()
def extract_values(dicts):
    return [list(d.values()) for d in dicts]

# Function 2:
keys = [k for k in my_dicts[0].keys()]

def extract_values(dicts, keys):
    return [list(d[k] for k in keys) for d in dicts]

# 63.0
# Task: Write a Python program to convert a given list of lists to a dictionary.
my_list = [[1, 'Jean Castro', 'V'], [2, 'Steve Borello', 'VI'],
           [3, 'Nick Jenkins', 'VII'], [4, 'John Doe', 'VII']]

out = defaultdict(dict)

for item in my_list:
    out[item[0]] = item[1::]
   
# 63.1
# Task: Write a Python program to convert a list of two-element lists into a dictionary using dict().
my_list = [[1, 'V'], [2, 'VI'], [3, 'VII'], [4, 'VIII'],
           [5, 'IX'], [6, 'X'], [7, 'XI'], [8, 'XII']]

out = dict(my_list)

# 63.2
# Task: Write a Python program to iterate over a list of lists and construct a dictionary where the first element is the key and the second is the value.
my_list = [[1, 'V'], [2, 'VI'], [3, 'VII'], [4, 'VIII'],
           [5, 'IX'], [6, 'X'], [7, 'XI'], [8, 'XII'], [9, 'XIII']]

out = dict()

for l in my_list:
    out[l[0]] = l[1]

# 63.3
# Task: Write a Python program to use dictionary comprehension to transform a list of lists into a dictionary.
my_list = [[1, 'V'], [2, 'VI'], [3, 'VII'], [4, 'VIII'],
           [5, 'IX'], [6, 'X'], [7, 'XI'], [8, 'XII']]

def convert_to_dict(lst):
    return {l[0]: l[1] for l in lst}

# 63.4
# Task: Write a Python program to implement a function that creates a dictionary from a list of lists, handling duplicate keys by storing values in a list.
my_list = [[1, 'V'], [2, 'VI'], [3, 'VII'], [4, 'VIII'],
           [1, 'IX'], [6, 'X'], [2, 'XI'], [4, 'XII']]

def convert_to_dict(lst):
    out = defaultdict(list)
   
    for l in lst:
        if l[0] == l[0]:
            out[l[0]].append(l[1])
        else:
            out[l[0]] = l[1]
   
    return out

# 64.0
# Task: Write a Python program that creates key-value list pairings within a dictionary.
my_dict = {1: ['Smith Jones'], 2: ['John Doe'], 3: ['Jane Doe'],
           4: ['Michael Stevens'], 5: ['Smith Rugertz']}

def kv_pairs(d):
    return [dict(zip(d, sub)) for sub in product(*d.values())] 
    

# 64.1
# Task: Write a Python program to merge a dictionary of lists into a single dictionary by pairing each key with the first element of it's list.
my_dict = {1: ['Smith Jones', 'Jonathan Michaels'], 2: ['John Doe'], 3: ['Smith Roid'],
           4: ['John Smith'], 5: ['Michael Stevens']}
           
def kv_pairs(d):
    return {k: v for k, values in my_dict.items() for v in values}

# 64.2
# Task: Write a Python program to convert a dictionary with list values into a list containing one dictionary with key-value pairings.
my_dict = {1: ['Smith Jones', 'Jonathan Michaels'], 2: ['John Doe'], 3: ['Smith Roid'],
           4: ['John Smith'], 5: ['Michael Stevens']}

def kv_pairs(d):
    return [dict(zip(d.keys(), values)) for values in zip(*d.values())]
    

# pprint(kv_pairs(my_dict))

# 64.3
# Task: Write a Python program to iterate over a dictionary of lists and combine the key with its concatenated list elements into a new dictionary.
my_dict = {1: ['Smith Jones', 'Jonathan Michaels'], 2: ['John Doe'],
           3: ['Smith Roid', 'Michael Stevens'], 4: ['Nick Jenkins', 'Peter Parker']}

def combine_kv(d):
    out = []
   
    for k, values in d.items():
        out.append(''.join(str(k)+''.join(v for v in values)))
       

    return out

# 64.4
# Task: Write a Python program to use list comprehension to create a key-value pairing from a dictionary where each key maps to a joined string of its list.
my_dict = {1: ['Smith Jones', 'Jonathan Michaels'], 2: ['John Doe'],
           3: ['Smith Roid', 'Michael Stevens'], 4: ['Nick Jenkins', 'Peter Parker']}    
   
def combine_kv(d):
    return [(k, ''.join(v for v in values)) for k, values in d.items()]
   
# 65.0
# Task: Write a Python program to get the total length of all values in a given dictionary with string values.
my_dict = {'#687C6C': 'US Dollar', '#8F9575': 'Artichoke',
           '#D8D1CB':'Blackish White', '#CFC6B1': 'Soft Amber',
           '#C7AD75': 'Gold Tan', '#A17860': 'Mocha Mousse'}

def sum_val_len(d):
    out = 0
    for v in d.values():
        if isinstance(v, str):
            out+=len(v)
        else:
            out+=0
   
    return out

# 65.1
# Task: Write a Python program to compute the sum of the lengths of all string values in a dictionary using a for-loop.
my_dict = {'#687C6C': 'US Dollar', '#8F9575': 'Artichoke',
           '#D8D1CB':'Blackish White', '#CFC6B1': 'Soft Amber',
           '#C7AD75': 'Gold Tan', '#A17860': 'Mocha Mousse'}

def sum_val_len(d):
    out = 0
    for v in d.values():
        if isinstance(v, str):
            out+=len(v)
        elif isinstance(v, list):
            for val in v:
                if isinstance(val, str):
                    out+=len(val)
                else:
                    out+=0
        else:
            out+=0
           
    return out
       
# 65.2
# Task: Write a Python program to use dictionary comprehension to create a list of lengths and then sum them.
my_dict = {'#687C6C': 'US Dollar', '#8F9575': 'Artichoke',
           '#D8D1CB':'Blackish White', '#CFC6B1': 'Soft Amber',
           '#C7AD75': 'Gold Tan', '#A17860': 'Mocha Mousse'}

def len_lst(d):
    out = {'lengths': sum(val for val in [len(v) for v in d.values() if isinstance(v, str)])}
    return out

# 65.3
# Task: Write a Python program to iterate over dictionary values and add up the character counts for each value.
my_dict = {'#687C6C': 'US Dollar', '#8F9575': 'Artichoke',
           '#D8D1CB':'Blackish White', '#CFC6B1': 'Soft Amber',
           '#C7AD75': 'Gold Tan', '#A17860': 'Mocha Mousse'}
           
result = 0

for v in my_dict.values():
    result+=len(v)
           
# 65.4
# Task: Write a Python function that takes a dictionary with string values and returns the total length of all values.
my_dict = {'#687C6C': 'US Dollar', '#8F9575': 'Artichoke',
           '#D8D1CB':'Blackish White', '#CFC6B1': 'Soft Amber',
           '#C7AD75': 'Gold Tan', '#A17860': 'Mocha Mousse'}

def sum_val_len(d):
    out = 0
    for v in d.values():
        if isinstance(v, str):
            out+=len(v)
        else:
            out+=0
   
    return out

# 66.0
# Task: Write a Python program to check if a specific key and a value exist in a dictionary.
my_dicts = [{'student_id': 1, 'name': 'Stephen Thrill', 'class': 'V'},
           {'student_id': 2, 'name': 'John Doe', 'class': 'VI'},
           {'student_id': 3, 'name': 'Jane Doe', 'class': 'VII'},
           {'student_id': 4, 'name': 'Peter Parker', 'class': 'VIII'}]

kv_pair = ('name', 'Stephen Thrill')

contains_item = lambda dicts, kv_pair: any(kv_pair in d.items() for d in dicts)

# 66.1
# Task: Write a Python program to verify if a specific key exists in a dictionary and whether its value matches a given target.

contains_key = lambda dicts, key, v_target: any((key, v_target) in d.items() for d in dicts)

# 66.2
# Task: Write a Python program to iterate over a dictionary and return True if any entry has the specified key-value pair.
kv_pair = ('name', 'Big Ben')

def contains_item(dicts, target):
    for d in dicts:
        for k, v in d.items():
            if (k, v) == target:
                return True
   
    return False

# 66.3
# Task: Write a Python program to use the get() method to check for a key and validate its corresponding value.
kv_pair = ('name', 'Jane Doe')

result = False

for d in my_dicts:
    if d.get(kv_pair[0]) == kv_pair[1]:
        result = True

# 66.4
# Task: Write a Python function that accepts a dictionary, a key, and a value, and returns True only if the key exists and its value equals the target.
result = False

def contains_key(d, key, value):
    for k, v in d.items():
        if (k, v) == (key, value):
            return True
    return False

for d in my_dicts:
    if contains_key(d, 'name', 'Jane Doe'):
        result = True

# 67.0
# Task: Write a Python program to invert a given dictionary with non-unique hashable values.
my_dict = {'Jane Doe': 8, 'Joe Doe': 8, 'Josh Doe': 8, 'John Doe': 8, 'Smith Jenkins': 5}

def invert_dict(d):
    out = defaultdict(list)
   
    for k, v in my_dict.items():
        out[v].append(k)
       
    return dict(out)

# 67.1
# Task: Write a Python program to invert a dictionary so that each value maps to a list of keys using collections.defaultdict.
my_dict = {'Jane Doe': 8, 'Joe Doe': 8, 'Josh Doe': 8, 'John Doe': 8, 'Smith Jenkins': 5, 'Ned Jenkings': 5, 'Peter Parker': 4414}

result = defaultdict(list)

for k, v in my_dict.items():
    result[v].append(k)

# 67.2
# Task: Write a Python program to iterate over a dictionary and build an inverted dictionary where duplicate values become keys with list of original keys.
my_dict = {'Jane Doe': 8, 'Joe Doe': 8, 'Josh Doe': 8, 'John Doe': 8, 'Smith Jenkins': 5, 'Ned Jenkings': 5, 'Peter Parker': 4414}

result = defaultdict(list)

for k, v in my_dict.items():
    result[v].append(k)

result = dict(result)

# 67.3
# Task: Write a Python program to implement a function that returns the inverted dictionary for a dictionary with non-unique values.
my_dict = {'Jane Doe': 8, 'Joe Doe': 8, 'Josh Doe': 8, 'John Doe': 8, 'Smith Jenkins': 5, 'Ned Jenkings': 5, 'Peter Parker': 4414}

def invert_dict(d):
    out = defaultdict(list)
   
    for k, v in d.items():
        out[v].append(k)
   
    return dict(out)

# 67.4
# Task: Write a Python program to use dictionary comprehension to create an inverted mapping that groups keys by their values.
my_dict = {'Jane Doe': 8, 'Joe Doe': 8, 'Josh Doe': 8, 'John Doe': 8, 'Smith Jenkins': 5, 'Ned Jenkings': 5, 'Peter Parker': 4414}

def inverted_dict(d):
    return {v: [k for k in d.keys() if d[k] == v] for k, v in d.items()}

# 68.0
# Task: Write a Python program to combine two or more dictionaries, creating a list of values for each key.
my_dict1 = {'x': 200, 'y': 300, 'z': 400, 'w': 200, 'b': 600}
my_dict2 = {'a': 100, 'y': 150, 'x': 350, 'b': 450, 'k': 650}

result = defaultdict(list)

for d in [my_dict1, my_dict2]:
    for k, v in d.items():
        result[k].append(v)

# 68.1
# Task: Write a Python program to merge two dictionaries so that each key maps to a list of values from both dictionaries using defaultdict.
my_dict1 = {'x': 200, 'y': 300, 'z': 400, 'w': 200, 'b': 600}
my_dict2 = {'a': 100, 'y': 150, 'x': 350, 'b': 450, 'k': 650}

def merge_dicts(*dicts):
    out = defaultdict(list)
   
    for d in dicts:
        for k in d:
            out[k].append(d[k])
   
    return dict(out)

# 68.2
# Task: Write a Python program to combine multiple dictionaries into one by appending values for duplicate keys into lists.
my_dict1 = {'x': 200, 'y': 300, 'z': 400, 'w': 200, 'b': 600}
my_dict2 = {'a': 100, 'y': 150, 'x': 350, 'b': 450, 'k': 650}
my_dict3 = {'z': 144, 'x': 152, 'v': 111, 'b': 45, 'a': 2311}

result = defaultdict(list)

for d in [my_dict1, my_dict2, my_dict3]:
    for k in d:
        result[k].append(d[k])
       
# 68.3
# Task: Write a Python program to iterate over multiple dictionaries and construct a new dictionary where each key’s value is a list of all corresponding values.
result = defaultdict(list)

 for d in [my_dict1, my_dict2, my_dict3]:
    for k in d:
        result[k].append(d[k])
# 68.4
# Task: Write  a Python program to implement a function that takes several dictionaries and returns a combined dictionary with keys mapping to lists of values.

def combine_dicts(*dicts):
    out = defaultdict(list)
   
    for d in dicts:
        for k in d:
            out[k].append(d[k])
   
    return dict(out)

# 69.0
# Task: Write a Python program to group the elements of a given list based on the given function.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def group_vals(lst, fn):
    out = defaultdict(list)
   
    for v in lst:
        out[fn(v)].append(v)
   
    return dict(out)

# 69.1
# Task: Write a Python program to group elements of a list by applying the floor function and output a dictionary of groups.
my_list = [1, 2, 3, 4, 5, 5.4, 6, 6.3, 7, 8, 9, 10]

def group_vals(lst, fn):
    out = defaultdict(list)
   
    for k in lst:
        out[fn(k)].append(k)
   
    return dict(out)

# 69.2
# Task: Write a Python program to group words from a list by their length using a lambda function and dictionary comprehension.
my_list = ['Marine', 'Soldier', 'Navy', 'Green']

def group_vals(lst, fn):
    out = defaultdict(list)
   
    for k in lst:
        out[fn(k)].append(k)
   
    return dict(out)

# 69.3
# Task: Write a Python program to cluster list elements based on their remainder when divided by a given number.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def group_vals(lst, fn):
    out = defaultdict(list)
    for k in lst:
        out[fn(k)].append(k)
   
    return dict(out)

# 69.4
# Task: Write a Python program to use itertools.groupby to group sorted list elements by a custom function.
my_list = ['Baal', 'Diablo', 'Andariel', 'Lilith',
           'Mephisto', 'Duriel']

# Method 1: Program
length = lambda x: len(x)

#for k, g in groupby(sorted(my_list, key = length), key = length):
    #print(k, list(g))


# Method 2: Function
def group_vals(lst, Keyfun):
    out = {}
   
    for k, g in groupby(sorted(lst, key = Keyfun), key = Keyfun):
        out[k] = list(g)

    return list(out.items())

# 70.0
# Task: Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
my_list = [1, 2, 3 , 4]
 
fn = lambda x: x**2

def bind_dict(lst, fn):
    return dict(zip(lst, map(fn, lst)))

# 69.1
# Task: Write a Python program to convert a list of numbers into a dictionary where each key is the number and its value is the square of the number.
my_list = [1, 2, 3, 4] 

result = dict(zip(my_list, map(lambda x: x*x, my_list)))

# 70.2
# Task: Write a Python program to map a list of strings to a dictionary where each key is the string and the value is its length.
my_list = ['John', 'Steve', 'Mike', 'Nicholas', 'Michael']

result = dict(zip(my_list, map(lambda x: len(x), my_list)))

# 70.3
# Task: Write a Python program to implement a function that takes a list and a function, returning a dictionary mapping each element to the function’s result.
my_list = [1, 2, 3, 4, 5]

def bind_dict(lst, fn):
    return {k: fn(k) for k in lst}
   
# 70.4
# Task: Write a Python program to use dictionary comprehension to map each element of a list to its factorial value.
my_list = [1, 2, 3, 4, 5]

def factorial_2(x):
    result = 1
    for i in range(1, x+1):
        result*=i
   
    return result

result = {k: factorial_2(k) for k in my_list}

# 71.0
# Task: Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
my_dict = {
    'Carla': {
        'name': {
            'first': 'Carla ',
            'last': 'Russell'
        },
        'postIds': [1, 2, 3, 4, 5]
    }
}

def retrieve_val(d, selectors):
   
    return reduce(getitem, selectors, d)

# 71.1
# Task: Write a Python program to access a nested value in a dictionary using a list of keys as the path.

def retrieve_val(d, key_path):
    return reduce(getitem, key_path, d)

# 71.2
# Task: Write a Python program to implement a function that takes a nested dictionary and a selector list, returning the corresponding value.
 
def retrieve_val(d, key_path):
    return reduce(getitem, key_path, d)

# 71.3
# Task: Write a Python program to traverse a nested dictionary or list using recursion and a selector list to retrieve a value.

def retrieve_val(d, selector):
    if not selector:
        return d
   
    first = selector[0]
    rest = selector[1:]
   
    return retrieve_val(d[first], rest)

# 71.4
# Task: Write a Python program to use reduce() from functools to fetch a nested value based on a list of keys and indices.

def retrieve_val(d, key_path):
    return reduce(lambda current, key: current[key], key_path, d)

# 72.0
# Task: Write a Python program to invert a dictionary with unique hashable values.
my_dict = {'a': 11, 'b': 43, 'c': 7, 'd': 14}

result = {v: k for k, v in my_dict.items()}

# Method 2:
# defaultdict not necessary since we are dealing with hashable values.
def invert_dict(d):
    out = {}
   
    for k, v in d.items():
        out[v] = k
   
    return out

# 72.1
# Task: Write a Python program to invert a dictionary where each value is unique by swapping keys and values.
my_dict = {'a': 11, 'b': 33, 'c': 9, 'd': 15}

result = {v: k for k, v in my_dict.items()}

# 72.2
# Task: Write a Python program to create a new dictionary from a given dictionary with unique values, reversing the mapping using dictionary comprehension.
my_dict = {'a': 11, 'b': 33, 'c': 9, 'd': 15}

result = {v: k for k, v in my_dict.items()}

# 72.3
# Task: Write a Python program to implement a function that returns the inverse of a dictionary with unique hashable values.
my_dict = {'a': 11, 'b': 33, 'c': 9, 'd': 15}

def invert_dict(d):
    return {v: k for k, v in d.items()}

# 72.4
# Task: Write a Python program to use the items() method to construct an inverted dictionary from a unique-valued dictionary.
my_dict = {'a': 11, 'b': 33, 'c': 9, 'd': 15}

def invert_dict(d):
    out = {}
   
    for k, v in d.items():
        out[v] = k
   
    return out

# 73.0
# Task: Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
my_dicts = [{'name': 'Theodore', 'id': 1},
            {'name': 'Steven', 'id': 2},
            {'name': 'Michael', 'id': 3},
            {'name': 'Nicholas', 'id': 4},
            {'name': 'Rick', 'id': 5}]



result = lambda key: [d[key] for d in my_dicts]

# 73.1
# Task: Write a Python program to extract values corresponding to a specified key from a list of dictionaries using list comprehension.
my_dicts = [{'name': 'Theodore', 'id': 1},
            {'name': 'Steven', 'id': 2},
            {'name': 'Michael', 'id': 3},
            {'name': 'Nicholas', 'id': 4},
            {'name': 'Rick', 'id': 5}]

result = lambda key: [d[key] for d in my_dicts]

# 73.2
# Task: Write a Python program to iterate over a list of dictionaries and collect the values for a given key, handling missing keys gracefully.
my_dicts = [{'name': 'Theodore', 'id': 1},
            {'name': 'Steven', 'id': 2},
            {'name': 'Michael', 'id': 3},
            {'name': 'Nicholas', 'id': 4},
            {'name': 'Rick', 'id': 5}]

def collect_keys(dicts, key):
    out = []
    for d in dicts:
        try:
            out.append(d[key])
        except KeyError:
            return "Key not found"
   
    return out

# 73.3
# Task: Write a Python program to use the map() function to retrieve values from each dictionary for a specified key.
my_dicts = [{'name': 'Theodore', 'id': 1},
            {'name': 'Steven', 'id': 2},
            {'name': 'Michael', 'id': 3},
            {'name': 'Nicholas', 'id': 4},
            {'name': 'Rick', 'id': 5}]

def collect_keys(dicts, key):
    return list(map(lambda d: d[key], dicts))

# 73.4
# Task: Write a Python program to implement a function that returns a list of values for a given key from a list of dictionaries.
my_dicts = [{'name': 'Theodore', 'id': 1},
            {'name': 'Steven', 'id': 2},
            {'name': 'Michael', 'id': 3},
            {'name': 'Nicholas', 'id': 4},
            {'name': 'Rick', 'id': 5}]

def collect_values(dicts, key):
    return [d[key] for d in dicts]

# 74.0
# Task: Write a Python program to create a dictionary with the same keys as the given dictionary and values generated by running the given function for each value.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7}

def generate_dict(d, valFunc):
    out = {}
   
    for k, v in d.items():
        out[k] = valFunc(v)
   
    return out

# 74.1
# Task: Write a Python program to apply a given function to each value of a dictionary and return a new dictionary with the same keys and transformed values.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7}

# To apply a function you would use map()
def generate_dict(d, valFunc):
    return dict(zip(list(d.keys()),
                map(valFunc, list(d.values()))))

# 74.2
# Task: Write a Python program to use dictionary comprehension to map over a dictionary's values with a provided function.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7}
           
def generate_dict(d, valFunc):
    return dict(zip(list(d.values()),
                map(valFunc, list(d.values()))))

# 74.3
# Task: Write a Python program to implement a function that takes a dictionary and a transformation function, returning a new dictionary with updated values.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7}
           
def generate_dict(d, valFunc):
    out = {}
   
    for k, v in d.items():
        out[k] = valFunc(v)
   
   return out
 
# 74.4
# Task: Write a Python program to combine lambda functions with dictionary comprehension to modify all values in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7}

result = lambda d, valFunc: {k: valFunc(v) for k, v in d.items()}

# 75.0
# Task: Write a Python program to find all keys in a dictionary that have the given value.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}
val = 2
result = list(filter(lambda x: my_dict[x] == val, my_dict))

# 75.1
# Task: Write a Python program to iterate over a dictionary and collect all keys whose value matches a given target.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}
val = 2

#for k in my_dict:
#    if my_dict[k] == val:
#        print(k)

# 75.2
# Task: Write a Python program to use list comprehension to extract keys with a specified value from a dictionary.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}
val = 2

result = list(filter(lambda x: my_dict[x] == val, my_dict))

# 75.3
# Task: Write a Python program to implement a function that returns a list of keys with a particular value from a dictionary.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}
val = 2

def extract_key(d, val):
    return list(filter(lambda x: d[x] == val, d))

# 75.4
# Task: Write a Python program to compare each key-value pair and output keys if the value equals a specified number.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}
val = 2

#for item in my_dict.items():
#    if item[1] == val:
#        print(item[0])

# 76.0
# Task: Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.
my_list1 = ['Lilith', 'Baal', 'Diablo', 'Mephisto',
            'Duriel', 'Andariel']
my_list2 = ['Uber', 5, 4, 3, 2, 1]

result = {}

for l1, l2 in zip(my_list1, my_list2):
    result.update({l1: l2})

# 76.1
# Task: Write a Python program to combine two lists into a dictionary using the zip() function, ensuring keys are unique.
my_list1 = ['Lilith', 'Baal', 'Diablo', 'Mephisto',
            'Duriel', 'Andariel']
my_list2 = ['Uber', 5, 4, 3, 2, 1]

result = {}

for l1, l2 in zip(my_list1, my_list2):
    result.update({l1: l2})

# 76.2
# Task: Write a Python program to map elements of the first list to the corresponding elements of the second list and handle mismatched lengths.
my_list1 = ['Lilith', 'Baal', 'Diablo', 'Mephisto',
            'Duriel', 'Andariel']
my_list2 = ['Uber', 5, 4, 3, 2, 1]

result = {}

def combine_lsts(l1, l2):
    out = {}
   
    if len(l1) != len(l2):
        raise ValueError("Length mismatch: Please double-check your key-values pairs.")
   
    else:
        for k, v in zip(l1, l2):
            out.update({k: v})
   
    return out
   
# 76.3
# Task: Write a Python program to use dictionary comprehension to merge two lists into a dictionary and sort the dictionary by keys.
my_list1 = ['Lilith', 'Baal', 'Diablo', 'Mephisto',
            'Duriel', 'Andariel']
my_list2 = ['Uber', 5, 4, 3, 2, 1]

temp_dict = {}

for k, v in zip(my_list1, my_list2):
    temp_dict[k] = v

result = dict(sorted(temp_dict.items(), key = lambda x: x[0]))

# 76.4
# Task: Write a Python program to implement error checking when converting two lists to a dictionary, ensuring that all keys are hashable.
my_list1 = ['Lilith', 'Baal', 'Diablo', 'Mephisto',
            ['Duriel', 'test'], 'Andariel']
my_list2 = ['Uber', 5, 4, 3, 2, 1]

def combine_lsts(l1, l2):
    out = {}
   
    if len(l1) != len(l2):
        return (f"Value error occured: list length mismatch.")
   
    for k, v in zip(my_list1, my_list2):
        try:
            out[k] = v    
        except TypeError as e:
            print(f"Type error occured {e}. ")
            return ''

    return out

# 77.0
# Task: Write a Python program to transform a dictionary into a list of tuples.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = list(my_dict.items())

# 77.1
# Task: Write a Python program to convert a dictionary into a list of (key, value) tuples using the items() method.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = list(my_dict.items())

# 77.2
# Task: Write a Python program to use list comprehension to generate a list of tuples from a dictionary.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

def convert_to_list(d):
    return [item for item in d.items()]

# 77.3
# Task: Write a Python program to sort a dictionary's items and return them as a list of tuples.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = list(sorted(my_dict.items(),
              key = lambda t: tuple(filter(lambda v: v if isinstance(v, (int, float)) else 0, t))))

# 77.4
# Task: Write a Python program to iterate over a dictionary and append each key-value pair as a tuple to a new list.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = []

for k, v in my_dict.items():
    result.append((k, v))

# 78.0
# Task: Write a Python program to create a flat list of all the keys in a flat dictionary.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = [k for k in my_dict.keys()]

# 78.1
# Task: Write a Python program to extract all keys from a flat dictionary and store them in a list using the keys() method.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = list(my_dict.keys())

# 78.2
# Task: Write a Python program to iterate over a dictionary and build a list of keys manually.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = []

for k in my_dict:
    result.append(k)

# 78.3
# Task: Write a Python program to use list comprehension to create a list of all dictionary keys.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = [k for k in my_dict]

# 78.4
# Task: Write a Python program to implement a function that returns a sorted list of keys from a dictionary.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

def sorted_keys(d):
    return list(sorted(d))

# 79.0
# Task: Write a Python program to create a flat list of all the values in a flat dictionary.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = list(my_dict.values())

# 79.1
# Task: Write a Python program to extract all values from a flat dictionary into a list using the values() method.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = [v for v in my_dict.values()]

# 79.2
# Task: Write a Python program to use list comprehension to generate a flat list of dictionary values.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = [v for v in my_dict.values()]

# 79.3
# Task: Write a Python program to iterate over a dictionary and compile its values into a new list.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

result = []

for v in my_dict.values():
    result.append(v)

# 79.4
# Task: Write a Python program to implement a function that returns all values of a dictionary as a list, with an option to sort them.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3,'Duriel': 2, 'Andariel': 1}

def sorted_values(d, sort = False):
    if sort == False:
        return [v for v in d.values()]
    else:
        return list(sorted(d.values(),
                    key = lambda v: v if isinstance(v, (int, float)) else 0))

# 80.0
# Task: Write a Python program to find the key of the maximum value in a dictionary.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3, 'Duriel': 2, 'Andariel': 1}

max_val = max(my_dict.values(), key = lambda v: isinstance(v, (int, float)))
key = None

for k, v in my_dict.items():
    if v == max_val:
        key = k

# 80.1
# Task: Write a Python program to determine the key associated with the maximum value in a dictionary using max() with a key argument.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3, 'Duriel': 2, 'Andariel': 1}

result = max(my_dict.items(), key = lambda t: tuple(filter(lambda v: isinstance(v, (int, float)), t)))[0]

# 80.2
# Task: Write a Python program to iterate through a dictionary and return the key for which the value is highest.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3, 'Duriel': 2, 'Andariel': 1}

max_val = 0
key = None

for k, v in my_dict.items():
    if isinstance(v, (int, float)):
        if v > max_val:
            max_val = v
       
    if v == max_val:
        key = k

# 80.3
# Task: Write a Python program to implement a function that finds the key of the maximum value and returns both the key and value.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3, 'Duriel': 2, 'Andariel': 1}

def max_item(d):
    return max(d.items(), key = lambda t: tuple(filter(lambda v: isinstance(v, (int, float)), t)))
   
# 80.4
# Task: Write a Python program to use dictionary comprehension and the max() function to extract the key with the largest value.
my_dict = {'Lilith': 'Uber', 'Baal': 5, 'Diablo': 4,
           'Mephisto': 3, 'Duriel': 2, 'Andariel': 1}

def max_item(d):
    temp_dict = {k: v for k, v in d.items() if isinstance(v, (int, float))}
   
    return max(temp_dict.items(), key = lambda x: x[1])

# 81.0
# Task: Write a Python function that flattens a nested dictionary into a single-level dictionary. The keys in the flattened dictionary should be tuples representing the path to each value.
my_dict = {'Prime Evils': {'Baal': 5, 'Diablo': 4, 'Mephisto': 3},
           'Lesser Evils': {'Duriel': 2, 'Andariel': 2, 'Specials': {'Lilith': 'Uber'}}
}

def flattened_dict(d, parent_key = (), result = None):
    if result == None:
        result = {}
   
    for k, v in d.items():
        new_key = parent_key + (k, )
       
        if isinstance(v, dict):
            flattened_dict(v, new_key, result)
        else:
            result[new_key] = v
       
    return result

# 81.1
# Task: Write a Python function to merge multiple nested dictionaries, preserving the hierarchy.
my_dict1 = {'a': 1, 'b': {'x': 10}}
my_dict2 = {'c': 2, 'd': {'y': 20}}

def merge_nested_dicts(d1, d2):
    out = d1.copy()
   
    for k, v in d2.items():
        if k in out and isinstance(out[k], dict) and isinstance(v, dict):
            out[k] = merge_nested_dicts(out[k], v)
        else:
            out[k] = v
   
    return out

# 81.2
# Task: Write a Python function to count the occurrences of each unique key in a deeply nested dictionary.
my_dict = {'Prime Evils': {'Baal': 5, 'Diablo': 4, 'Mephisto': 3},
           'Lesser Evils': {'Duriel': 2, 'Andariel': 2, 'Specials': {'Lilith': 'Uber'}}
}

# Method 1:
def count_unique_keys(d):
    def flattened_dict(d, out = None):
        if out is None:
            out = {}
       
        for k, v in d.items():
            out[k] = v
           
            if isinstance(v, dict):
                flattened_dict(v, out)
               
        return out
   
    return len(set(flattened_dict(d)))

# Method 2:
def count_keys(d):
    total = 0
    for k, v in d.items():
        total+=1
        if isinstance(v, dict):
            total += count_keys(v)
   
    return total

# 81.3
# Task: Write a Python function to find and replace all occurrence  s of a given value in a nested dictionary.
my_dict = {'Prime Evils': {'Baal': 5, 'Diablo': 4, 'Mephisto': 3},
           'Lesser Evils': {'Duriel': 2, 'Andariel': 1, 'Specials': {'Lilith': 'Uber'}}
}

def replace_value(d, current_val, new_val):
    for k, v in d.items():
        if v == current_val:
            d[k] = new_val
       
        if isinstance(v, dict):
            replace_value(v, current_val, new_val)
   
    return d

# 81.4
# Task: Write a Python function to extract all paths (keys) that lead to a given value in a nested dictionary.
my_dict = {'Prime Evils': {'Baal': 5, 'Diablo': 4, 'Mephisto': 3},
           'Lesser Evils': {'Duriel': 2, 'Andariel': 1, 'Specials': {'Lilith': 'Uber'}}
}

def extract_key_path(d, target_value):
    path = []
    
    def search(d, current_path = ()):
        for k, v in d.items():
            new_path = current_path + (key, )
            
            if isinstance(v, dict):
                search(v, new_path)
            elif v == target_value:
                path.append(new_path)
    
    search(d)
    
    return path

# 82.0
# Task: Write a Python program to implement a memoization decorator that caches function results based on arguments. The decorator should handle any function 
# with any number of positional and keyword arguments. Ensure that your implementation correctly handles unhashable arguments (like lists or dictionaries).


# Define a decorator function to implement memoization for caching function results.
def memoize(func):
    """
    A decorator that caches function results based on arguments.
    Handles any function with any number of positional and keyword arguments.
    Converts unhashable arguments to hashable forms.
    
    Args:
        func: The function to memoize
        
    Returns:
        Wrapped function with memoization
    """
    # Initialize a dictionary to store cached results.
    cache = {}
    
    # Define a helper function to convert unhashable arguments into hashable forms.
    def make_hashable(arg):
        """Convert unhashable types to hashable representations."""
        # If the argument is a list or set, convert it to a tuple recursively.
        if isinstance(arg, (list, set)):
            return tuple(make_hashable(item) for item in arg)
        # If the argument is a dictionary, convert it to a sorted tuple of key-value pairs.
        elif isinstance(arg, dict):
            return tuple(sorted((k, make_hashable(v)) for k, v in arg.items()))
        # Fo all other types (e.g., integers, strings), return the argument as-is.
        else:
            return arg
    
    # Define the wrapper function that replaces the original function.
    def wrapper(*args, **kwargs):
        # Convert positional arguments into a hashable form using the `make_hashable` function.
        hashable_args = tuple(make_hashable(arg) for arg in args)
        # Convert keyword arguments into a sorted tuple of hashable key-value pairs.
        hashable_kwargs = tuple(sorted((k, make_hashable(v)) for k, v in kwargs.items()))
        # Combine hashable positional and keyword arguments into a single key.
        key = (hashable_args, hashable_kwargs)
        
        # Check if the result for the current arguments is already in the cache.
        if key not in cache:
            # If not cached, call the original function and store the result in the cache.
            cache[key] = func(*args, **kwargs)
        
        # Return the cached result.
        return cache[key]
    
    # Return the wrapper function, replacing the original function with the memoized version.
    return wrapper

 
# Example function to memoize - Fibonacci sequence calculation.
def fibonacci(n):
    # Base case: return n if n is 0 or 1.
    if n <= 1:
        return n
    # Recursive case: calculate Fibonacci(n-1) + Fibonacci(n-2).
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage with memoization applied to the Fibonacci function.
@memoize
def fibonacci_memo(n):
    # Base case: return n if n is 0 or 1.
    if n <= 1:
        return n
    # Recursive case: calculate Fibonacci(n-1) + Fibonacci(n-2) with memoization.
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)

# Test the performance of the Fibonacci function with and without memoization.
import time

# Without memoization (slow for larger values of n).
start = time.time()  # Record the start time.
result = fibonacci(30)  # Calculate Fibonacci(30) without memoization.
end = time.time()  # Record the end time.
# Print the result and the time taken.
print(f"Without memoization: {result}, Time: {end - start:.6f} seconds")

# With memoization (much faster due to caching).
start = time.time()  # Record the start time.
result = fibonacci_memo(30)  # Calculate Fibonacci(30) with memoization.
end = time.time()  # Record the end time.
# Print the result and the time taken.
print(f"With memoization: {result}, Time: {end - start:.6f} seconds")

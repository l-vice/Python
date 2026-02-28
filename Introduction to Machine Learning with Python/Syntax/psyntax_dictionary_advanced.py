from operator import itemgetter
from collections import OrderedDict, Counter, defaultdict
from functools import reduce
from math import prod
from itertools import product
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

out
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
# Task: Write a Python program to match key values in two dictionaries.
my_dict1 = {'a': 2, 'b': 3, 'c': 11, 'd': 15, 'e': 17, 'f': 12}
my_dict2 = {'a': 8, 'b': 3, 'c': 11, 'd': 18, 'e': 12, 'f': 22}

#for (key, value) in set(my_dict1.items() & my_dict2.items()):
#    print(list((key, value)))

# 37.1
# Task: Write a Python program to compare two dictionaries
# and print the keys whose values match in both.
my_dict1 = {'a': 2, 'b': 3, 'c': 11, 'd': 15, 'e': 17, 'f': 12}
my_dict2 = {'a': 8, 'b': 3, 'c': 11, 'd': 18, 'e': 12, 'f': 22}

#for (k, v) in set(my_dict1.items() & my_dict2.items()):
#    print(list(k))

# 37.2
# Task: Write a Python program to iterate over keys in one dictionary
# and check if the corresponding value in another dictionary is the same.
my_dict1 = {'a': 2, 'b': 3, 'c': 11, 'd': 15, 'e': 17, 'f': 12}
my_dict2 = {'a': 8, 'b': 3, 'c': 21, 'd': 18, 'e': 12, 'f': 22}

result = any((k, v) in my_dict2.items() for (k, v) in my_dict1.items())

# 37.3
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

# 37.4
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

# 38.0
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

# 38.1
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
   
# 38.2
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

# 38.3
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

# 38.4
# Task:

with open("data.json", "r") as f:
    data = json.load(f)

#for k, v in data.items():
#    print(f"{k:<10}: {v}")

# 39.0
# Task:
my_dict = dict(x = list(range(11, 20)), y = list(range(21, 30)), z = list(range(31, 40)))
#pprint(my_dict)

#for k, v in my_dict.items():
#    print(f"{k:<10}: {v}")

# 39.1
# Task:
my_dict = dict(x = list(range(1, 11)), y = list(range(11, 21)),
               z = list(range(21, 31)))
#pprint(my_dict)

# 39.2
# Task:
my_dict = dict(x = list(range(11, 21)), y = list(range(21, 31)), z = list(range(31, 41)))
#pprint(my_dict)
# print("\nThe fifth element: ")
# print(f"Key['x']: {my_dict['x'][4]}\nKey['y']: {my_dict['y'][4]}\nKey['z']: {my_dict['z'][4]}")

# 39.3
# Task:
my_dict = {}
user_specified_keys = list(input("Please enter your keys of choice: "))
user_specified_keys = list(filter(lambda x: x.isalpha(), user_specified_keys))

for k in range(len(user_specified_keys)):
    pair = {user_specified_keys[k]: [i*(k+1) for i in list(range(11, 21))]}
    my_dict.update(pair)

for k in my_dict:
    print(f"{my_dict[k][3]}")

# 39.4
# Task: 

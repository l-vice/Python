from operator import itemgetter
from collections import OrderedDict 
import pandas as pd
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
    
    if reverse == False:
        items.sort(key = itemgetter(1), reverse = reverse)
        
    else:
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
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #

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
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------

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
    
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------ #
# ------------------------------------------------------------------------ ##################################################################### ------------------------------------------------------------------    
    
# 6.0
# Task: Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 20

#for i in range(1,n+1):
#    print({i: i*i})

# 6.1
# Task: Write a Python script to create a dictionary with keys from 1 to n and values as the square of the keys using dictionary comprehension.

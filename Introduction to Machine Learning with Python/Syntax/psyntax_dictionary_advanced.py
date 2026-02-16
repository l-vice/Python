from operator import itemgetter
from collections import OrderedDict

# 1.0
# Task: Write a Python script to sort (ascending and descending) a dictionary by value. 
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

result = sorted(d.items(), key = lambda x: x[1])

# OR

result = sorted(d.items(), key = operator.itemgetter(1))

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

def my_sorted(input_dict):
    items = list(input_dict.items())
    
    items.sort(key = lambda x: x[1])
    
    return dict(items)
    
result = my_sorted(items)


# 1.3
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
    
    
    
                

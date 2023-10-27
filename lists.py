import random 

def is_sorted(t):
    for i in t: 
        if t[0] < t[1]:
            return True 
    return False 


def is_anagram(string1, string2):
    control = True 
    t1 = list(string1)
    t2 = list(string2)

    if len(t1) != len(t2):
        control = False 
        return control 
    else: 
        for i in t1: 
            if i in t2: 
                continue 
            else: 
                control = False 
                break 
    return control 


############################################ 

# BIRTHDAY PARADOX 

############################################ 

def has_duplicate(t):
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] == t[j]:
                return True 
    return False 

def generate_random():
    random_birth = []
    for i in range(0,23):
        random_birth.append(random.randint(1,30))
    return random_birth

def paradox_resolver():
    births = generate_random() 
    print(births)
    control = has_duplicate(births)
    return control 

############################################ 

def remove_duplicate(t): 
    t2 = []
    for i in t: 
        if i not in t2: 
            t2.append(i) 
        else: 
            continue 
    return len(t) == len(t2)


############################################

# WORDS FROM A FILE

############################################

def reader1():
    f = open("words.txt", "r")
    t = []
    for line in f: 
        t.append(line.strip())
    return t  

def reader2():
    f = open("words.txt", "r")
    t = []
    for line in f:
        t += [line.strip()]
    return t  

############################################

############################################

# SEARCHING ALGORITHMS

def linear_search(A):
    x = 5
    for i in A: 
        if i == x: 
            return True 
    return False 

def binary_search(list, item):
    if len(list) == 0:
        return False 

    low = 0 
    high = len(list) - 1 

    while low <= high:
        mid = (low + high) // 2 
        guess = list[mid] 
        if guess == item: 
            return mid 
        if guess > item: 
            high = mid - 1 
        else: 
            low = mid + 1 
    return None  


def binary_search2(word, t):
    """
    Returns True if string word is in list t.
    Uses bisection search.
    """
    
    midpoint = len(t)//2
    
    # Without this step, the function might try to access t[0], 
    # which will throw an error, since the list is empty and there
    # are no items inside of it
    
    if len(t) == 0:
        return False
    
    if t[midpoint] == word:
        return True
    elif word < t[midpoint]:
        return binary_search2(word, t[:midpoint])
    else:
        return binary_search2(word, t[midpoint + 1:])


############################################

def bisect1(t, target):
    low = 0
    high = len(t) - 1 
    while low <= high: 
        mid = (low + high) // 2 
        hit = t[mid]
        if hit == target:
            return True 
        if hit > target:
            high = mid - 1 
        else: 
            low = mid + 1 
    return False 


def bisect2(t, target):
    mid = len(t) // 2

    if len(t) == 0:
        return False 

    if t[mid] == target: 
        return True 
    elif target < t[mid]:
        return bisect2(t[:mid], target)
    else: 
        return bisect2(t[mid+1:], target)

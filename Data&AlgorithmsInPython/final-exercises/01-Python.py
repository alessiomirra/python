import random 

def generate_random_list():
    t = []
    for i in range(0,10):
        t.append(random.randint(1, 10000))
    return t 


def is_multiple(a,b):
    if a % b == 0: 
        return True 
    return False 

def is_even(n):
    if not n & 1:
        return True 
    return False 

def minmax(data):
    print(data)
    if len(data) == 0: 
        return None 
    
    min = max = data[0]
    
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i

    return (min, max)


def squares(n):
    total = 0
    for i in range(1,n):
        total += i**2 
    return total 

def squares2(n): 
    total = sum([i**2 for i in range(1,n)])
    return total 

def odd_squares(n): 
    total = 0 
    for i in range(1,n):
        if i % 2 != 0:
            total += i**2 
    return total 

def odd_squares2(n):
    total = sum([i**2 for i in range(1,n) if i % 2 != 0]) 
    return total 


def odd_pair(t):
    pairs = 0
    counter = 0
    for i in range(len(t)):
        for j in range(i+1, len(t)-1):
            pairs += 1
            if  (t[i] * t[j]) % 2 != 0:
                counter += 1 
    return "There're %s pairs which product is odd in %s pairs" % (counter, pairs)


def equal_verify(t): 
    print(t)
    for i in range(len(t)): 
        for j in range(i+1, len(t)-1):
            if t[i] == t[j]:
                return "First couple of equals number founded. %s has a duplicate" % i 
    return "No duplicates founded"


def dot_product(a,b):
    c = []
    if len(a) != len(b):
        return "Dot product not possible"
    else: 
        for i in range(len(a)): 
            c.append(a[i] * b[i])
    return c 


def index_list(t):
    try:
        while True: 
            element = int(input("Enter the index of the element to print: ")) 
            print(t[element])
    except IndexError:
        print("Don't try buffer overflow attacks in Python")
    except KeyboardInterrupt:
        print("Thanks")
    except ValueError: 
        print("The index must be an integer")


def vowels_counter(t):
    vowels = ["a", "e", "i", "o", "u"]
    t = t.lower()
    count = 0 
    for i in range(0,len(t)):
        if t[i] in vowels:
            count += 1 
    return count 

def randrange_choice(t):
    return t[random.randrange(0, len(t))]


def reverse1(t):
    reversed_list = []
    for i in range(len(t)-1, -1, -1):
        reversed_list.append(t[i])
    return reversed_list 

def reverse2(t):
    return t[::-1]

def reverse3(t):
    t.reverse()
    return t


def generate_strings(characters):
    if len(characters) == 1: 
        return characters[0]
    else: 
        results = []
        for i, char in enumerate(characters):
            remaining = characters[:i] + characters[i+1:]
            remaining_perm = generate_strings(remaining)
            for perm in remaining_perm:
                results.append(char + perm)
        return results 



def two_division(n):
    if n < 2:
        return 0 
    else: 
        return 1 + two_division(n // 2)


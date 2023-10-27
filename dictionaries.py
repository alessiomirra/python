def create_dictionary():
    d = dict()
    d["hi"] = "Hi, this is a dictionary"
    return d 

def histogram(s):
    count = dict()
    for i in s: 
        if i not in count:
            count[i] = 1 
        else: 
            count[i] += 1 
    return count 

def histogram2(s):
    count = dict() 
    for i in s: 
        count[i] = count.get(i,0) + 1
    return count  

def get_keys(d):
    return d.keys()

def print_hist(d):
    for i in d:
        print(i, d[i])

def print_hist2(d):
    key = list(d.keys())
    key.sort()
    for i in range(len(key)):
        print(key[i], d[key[i]])

def reverse_lookup(d,v):
    for k in d: 
        if d[k] == v:
            return d[k] 
    raise ValueError

h = histogram("AlessioMirra")

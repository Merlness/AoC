import hashlib

def digest(s):
    return hashlib.md5(s.encode()).hexdigest()

def mining(code, zeroes):
    suffix = 0
    begin = '0' * zeroes
        
    while True:
        if digest(code + str(suffix)).startswith(begin):
            return suffix      
        suffix += 1

print(mining('iwrupvqb', 5))
print(mining('iwrupvqb', 6))
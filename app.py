import string
import random

def generate():
    pass1 = string.ascii_uppercase

    pass2 = string.ascii_lowercase

    pass3 = string.digits
 
    pass4 = string.punctuation

    s = []
    s.extend(list(pass1))
    s.extend(list(pass2))
    s.extend(list(pass3))
    s.extend(list(pass4))
    random.shuffle(s)
    print(s)

generate()
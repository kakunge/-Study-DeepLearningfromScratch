def NOT(x):
    return not x

def AND(a, b):
    if (a and b) == True:
        return True
    else:
        return False

def OR(a, b):
    if (a or b) == True:
        return True
    else:
        return False

def NAND(a, b):
    if (a and b) == True:
        return False
    else:
        return True

def NOR(a, b):
    if (a or b) == True:
        return False
    else:
        return True

def XOR(a, b):
    if a != b:
        return True
    else:
        return False

def XNOR(a, b):
    if a != b:
        return False
    else:
        return True

def Add(a, b):
    return (int(AND(a,b)),int(XOR(a,b)))

def strReverse(s):
    return ''.join(reversed(s))


a = 0b11
b = 0b11

print(strReverse('hello'))
    
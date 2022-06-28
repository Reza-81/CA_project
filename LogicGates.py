def And(*arguments):
    result = 1
    for i in arguments:
        result = result and i
    return result

def Or(*arguments):
    result = 0
    for i in arguments:
        result = result or i
    return result

def Not(a):
    return int(not a)

def Xor(a, b):
    a_b_prim = And(a, Not(b))
    a_prim_b = And(Not(a), b)
    return Or(a_prim_b, a_b_prim)

def Nand(*arguments):
    return Not(And(*arguments))

def Nor(*arguments):
    return Not(Or(*arguments))

def Xnor(a, b):
    return Not(Xor(a, b))


def And(*arguments : int) -> int:
    result = 1
    for i in arguments:
        result = result and i
    return result

def Or(*arguments : int) -> int:
    result = 0
    for i in arguments:
        result = result or i
    return result

def Not(a : int) -> int:
    return int(not a)

def Xor(a : int, b : int) -> int:
    a_b_prim = And(a, Not(b))
    a_prim_b = And(Not(a), b)
    return Or(a_prim_b, a_b_prim)

def Nand(*arguments : int) -> int:
    return Not(And(*arguments))

def Nor(*arguments : int) -> int:
    return Not(Or(*arguments))

def Xnor(a : int, b : int) -> int:
    return Not(Xor(a, b))


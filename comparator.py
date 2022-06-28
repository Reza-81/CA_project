import LogicGates

def compare(a, b):
    result = 1
    for i in range(31, -1, -1):
        result = LogicGates.And(LogicGates.Xnor(int(a[i]), int(b[i])), result)
    return result


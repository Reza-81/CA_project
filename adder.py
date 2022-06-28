import LogicGates

def twos_complement(a):
    temp = ''
    for i in range(32):
        temp += str(LogicGates.Not(int(a[i])))
    temp = adder.adder_32_bit(temp, '00000000000000000000000000000001', 0)[0]
    return temp

def adder(a, b, carry_in):
    sum = LogicGates.Xor(LogicGates.Xor(a, b), carry_in)
    carry_out = LogicGates.Or(LogicGates.And(carry_in, LogicGates.Xor(a, b)), LogicGates.And(a, b))
    return (sum, carry_out)

def adder_subtractor_32_bit(a, b, subtract=0):
    result = ''
    carry_out = subtract
    for i in range(31, -1, -1):
        sum, carry_out = adder(int(a[i]), LogicGates.Xor(int(b[i]), subtract), carry_out)
        result = str(sum) + result
    return (result, carry_out)

# print(adder_subtractor_32_bit('00000000000000000000000000000000', '00000000000000000000000000000001', 0))

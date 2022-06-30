import LogicGates


def adder(a : int, b : int, carry_in : int) -> tuple[int, int]:
    sum = LogicGates.Xor(LogicGates.Xor(a, b), carry_in)
    carry_out = LogicGates.Or(LogicGates.And(carry_in, LogicGates.Xor(a, b)), LogicGates.And(a, b))
    return (sum, carry_out)

def adder_subtractor_32_bit(a : str, b : str, subtract : int = 0) -> tuple[int, int]:
    result = ''
    carry_out = subtract
    for i in range(31, -1, -1):
        sum, carry_out = adder(int(a[i]), LogicGates.Xor(int(b[i]), subtract), carry_out)
        result = str(sum) + result
    return (result, carry_out)

# print(adder_subtractor_32_bit('00000000000000000000000000000000', '00000000000000000000000000000000', 1))

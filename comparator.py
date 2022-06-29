import LogicGates
import adder
import mux

def twos_complement(a):
    temp = ''
    for i in range(32):
        temp += str(LogicGates.Not(int(a[i])))
    temp = adder.adder_subtractor_32_bit(temp, '00000000000000000000000000000001')[0]
    return temp

def comparator_1_bit_unsigned(a, b):
    a_less_than_b = LogicGates.And(b, LogicGates.Not(a))
    a_greater_than_b = LogicGates.And(a, LogicGates.Not(b))
    a_equal_b = LogicGates.Or(LogicGates.And(LogicGates.Not(a),LogicGates.Not(b))
                            , LogicGates.And(a, b))
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_2_bit_unsigned(a, b):
    compare_bit_0 = comparator_1_bit_unsigned(int(a[0]), int(b[0]))
    compare_bit_1 = comparator_1_bit_unsigned(int(a[1]), int(b[1]))
    
    a_less_than_b = mux.mux_2x1(compare_bit_0[0], compare_bit_1[0], compare_bit_0[2])
    a_greater_than_b = mux.mux_2x1(compare_bit_0[1], compare_bit_1[1], compare_bit_0[2])
    a_equal_b = LogicGates.And(compare_bit_0[2], compare_bit_1[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_4_bit_unsigned(a, b):
    compare_bit_0 = comparator_2_bit_unsigned(a[:2], b[:2])
    compare_bit_1 = comparator_2_bit_unsigned(a[2:], b[2:])
    
    a_less_than_b = mux.mux_2x1(compare_bit_0[0], compare_bit_1[0], compare_bit_0[2])
    a_greater_than_b = mux.mux_2x1(compare_bit_0[1], compare_bit_1[1], compare_bit_0[2])
    a_equal_b = LogicGates.And(compare_bit_0[2], compare_bit_1[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_8_bit_unsigned(a, b):
    compare_bit_0 = comparator_4_bit_unsigned(a[:4], b[:4])
    compare_bit_1 = comparator_4_bit_unsigned(a[4:], b[4:])
    
    a_less_than_b = mux.mux_2x1(compare_bit_0[0], compare_bit_1[0], compare_bit_0[2])
    a_greater_than_b = mux.mux_2x1(compare_bit_0[1], compare_bit_1[1], compare_bit_0[2])
    a_equal_b = LogicGates.And(compare_bit_0[2], compare_bit_1[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_16_bit_unsigned(a, b):
    compare_bit_0 = comparator_8_bit_unsigned(a[:8], b[:8])
    compare_bit_1 = comparator_8_bit_unsigned(a[8:], b[8:])
    
    a_less_than_b = mux.mux_2x1(compare_bit_0[0], compare_bit_1[0], compare_bit_0[2])
    a_greater_than_b = mux.mux_2x1(compare_bit_0[1], compare_bit_1[1], compare_bit_0[2])
    a_equal_b = LogicGates.And(compare_bit_0[2], compare_bit_1[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_32_bit_unsigned(a, b):
    compare_bit_0 = comparator_16_bit_unsigned(a[:16], b[:16])
    compare_bit_1 = comparator_16_bit_unsigned(a[16:], b[16:])

    a_less_than_b = mux.mux_2x1(compare_bit_0[0], compare_bit_1[0], compare_bit_0[2])
    a_greater_than_b = mux.mux_2x1(compare_bit_0[1], compare_bit_1[1], compare_bit_0[2])
    a_equal_b = LogicGates.And(compare_bit_0[2], compare_bit_1[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)

def comparator_32_bit_signed(a, b):
    result_1 = comparator_32_bit_unsigned('0'+a[1:], '0'+b[1:])
    result_2 = (int(a[0]), int(b[0]), 0)
    result_3 = [None, None, None]
    result_3[0] = mux.mux_2x1(result_1[0], result_2[0], LogicGates.Xor(int(a[0]), int(b[0])))
    result_3[1] = mux.mux_2x1(result_1[1], result_2[1], LogicGates.Xor(int(a[0]), int(b[0])))
    result_3[2] = mux.mux_2x1(result_1[2], result_2[2], LogicGates.Xor(int(a[0]), int(b[0])))
    return tuple(result_3)


# print(comparator_32_bit_signed('11000000000000000000000010000000', '01000000000000000000000010000000'))
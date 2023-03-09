from mips_cpu import LogicGates
from mips_cpu import adder
from mips_cpu import mux

def twos_complement(a : str) -> str:
    temp = ''
    for i in range(32):
        temp += str(LogicGates.Not(int(a[i])))
    temp = adder.adder_subtractor_32_bit(temp, '00000000000000000000000000000001')[0]
    return temp

def comparator_1_bit_unsigned(a : int, b : int) -> tuple[int, int, int]:
    a_less_than_b = LogicGates.And(b, LogicGates.Not(a))
    a_greater_than_b = LogicGates.And(a, LogicGates.Not(b))
    a_equal_b = LogicGates.Or(LogicGates.And(LogicGates.Not(a),LogicGates.Not(b))
                            , LogicGates.And(a, b))
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_2_bit_unsigned(a : str, b : str) -> tuple[int, int, int]:
    compare_1 = comparator_1_bit_unsigned(int(a[0]), int(b[0]))
    compare_2 = comparator_1_bit_unsigned(int(a[1]), int(b[1]))
    
    a_less_than_b = mux.mux_2x1(compare_1[0], compare_2[0], compare_1[2])
    a_greater_than_b = mux.mux_2x1(compare_1[1], compare_2[1], compare_1[2])
    a_equal_b = LogicGates.And(compare_1[2], compare_2[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_4_bit_unsigned(a : str, b : str) -> tuple[int, int, int]:
    compare_1 = comparator_2_bit_unsigned(a[:2], b[:2])
    compare_2 = comparator_2_bit_unsigned(a[2:], b[2:])
    
    a_less_than_b = mux.mux_2x1(compare_1[0], compare_2[0], compare_1[2])
    a_greater_than_b = mux.mux_2x1(compare_1[1], compare_2[1], compare_1[2])
    a_equal_b = LogicGates.And(compare_1[2], compare_2[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_8_bit_unsigned(a : str, b : str) -> tuple[int, int, int]:
    compare_1 = comparator_4_bit_unsigned(a[:4], b[:4])
    compare_2 = comparator_4_bit_unsigned(a[4:], b[4:])
    
    a_less_than_b = mux.mux_2x1(compare_1[0], compare_2[0], compare_1[2])
    a_greater_than_b = mux.mux_2x1(compare_1[1], compare_2[1], compare_1[2])
    a_equal_b = LogicGates.And(compare_1[2], compare_2[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_16_bit_unsigned(a : str, b : str) -> tuple[int, int, int]:
    compare_1 = comparator_8_bit_unsigned(a[:8], b[:8])
    compare_2 = comparator_8_bit_unsigned(a[8:], b[8:])
    
    a_less_than_b = mux.mux_2x1(compare_1[0], compare_2[0], compare_1[2])
    a_greater_than_b = mux.mux_2x1(compare_1[1], compare_2[1], compare_1[2])
    a_equal_b = LogicGates.And(compare_1[2], compare_2[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)


def comparator_32_bit_unsigned(a : str, b : str) -> tuple[int, int, int]:
    compare_1 = comparator_16_bit_unsigned(a[:16], b[:16])
    compare_2 = comparator_16_bit_unsigned(a[16:], b[16:])

    a_less_than_b = mux.mux_2x1(compare_1[0], compare_2[0], compare_1[2])
    a_greater_than_b = mux.mux_2x1(compare_1[1], compare_2[1], compare_1[2])
    a_equal_b = LogicGates.And(compare_1[2], compare_2[2])
    return (a_less_than_b, a_greater_than_b, a_equal_b)

def comparator_32_bit_signed(a : str, b : str) -> tuple[int, int, int]:
    result_1 = comparator_32_bit_unsigned('0'+a[1:], '0'+b[1:])
    result_2 = (int(a[0]), int(b[0]), 0)
    result_3 = [None, None, None]
    result_3[0] = mux.mux_2x1(result_1[0], result_2[0], LogicGates.Xor(int(a[0]), int(b[0])))
    result_3[1] = mux.mux_2x1(result_1[1], result_2[1], LogicGates.Xor(int(a[0]), int(b[0])))
    result_3[2] = mux.mux_2x1(result_1[2], result_2[2], LogicGates.Xor(int(a[0]), int(b[0])))
    return tuple(result_3)

from mips_cpu import adder
from mips_cpu import mux
from mips_cpu import shiftlogical
from mips_cpu import LogicGates
from mips_cpu import comparator


def alu(a : str, b : str, selector : str) -> tuple[str, int]:

    And = ''
    for i in range(32):
        And += str(LogicGates.And(int(a[i]), int(b[i])))
    # ------------------------------------
    Or = ''
    for i in range(32):
        Or += str(LogicGates.Or(int(a[i]), int(b[i])))
    # ------------------------------------
    add = adder.adder_subtractor_32_bit(a, b)[0]
    # ------------------------------------
    subtract = adder.adder_subtractor_32_bit(a, b, 1)[0]
    # ------------------------------------
    set_less_then = 31*'0'+str(comparator.comparator_32_bit_signed(a, b)[0])
    # ------------------------------------
    set_less_then_unsigned = 31*'0'+str(comparator.comparator_32_bit_unsigned(a, b)[0])
    # ------------------------------------
    shift_right = shiftlogical.shift_right(b, a)
    # ------------------------------------
    shift_left = shiftlogical.shift_left(b, a)
    # ------------------------------------
    nor = ''
    for i in range(32):
        nor += str(LogicGates.Not(int(Or[i])))
    # ------------------------------------
    zero = LogicGates.Not(LogicGates.Or(*(map(int, subtract))))
    # ------------------------------------
    result = ''
    for i in range(32):
        result += str(mux.mux_16x1(int(And[i]), int(Or[i]), int(add[i]), int(subtract[i])
                                , int(set_less_then[i]), int(set_less_then_unsigned[i]), int(shift_right[i]), int(shift_left[i])
                                , int(nor[i]), 0, 0, 0, 0, 0, 0, 0, selector))

    return (result, zero)

import adder
import mux
import shiftlogical

def alu(a, b, selector):
    sum = adder.adder_subtractor_32_bit(a, b)[0]
    subtract = adder.adder_subtractor_32_bit(a, b, 1)[0]
    shift_right = shiftlogical.shift(a, b)
    shift_left = shiftlogical.shift(a, b, 0)
    And = None
    Or = None
    # compare
    # less then

    result = ''
    for i in range(32):
        result += str(mux.mux_4x1(int(sum[i]), int(subtract[i]), int(shift_right[i]), int(shift_left[i]), selector))
    return result

# print(alu('10000000000000000000000000000000', '00000000000000000000000000000001', '10'))
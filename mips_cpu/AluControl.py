from mips_cpu import LogicGates
from mips_cpu import mux


def alu_control(funct_code : str, alu_op : str) -> str:
    # and -> 0000
    # or -> 0001
    # add -> 0010
    # subtract -> 0011
    # set less than -> 0100
    # set less than u -> 0101
    # shift right -> 0110
    # shift left -> 0111
    # nor -> 1000
    # ----------------------------------------------------------
    # add -> add -> R
    # jr -> None
    # addi -> add
    # and -> and -> R
    # andi -> and
    # beq -> compare
    # bne -> compare
    # lbu -> add
    # lhu -> add
    # lh -> add
    # lb -> add
    # lw -> add
    # nor -> nor -> R
    # or -> or -> R
    # ori -> or
    # slt -> set_less_than -> R
    # sltu -> set_less_than_unsigned -> R
    # sll -> shift left logical -> R
    # sll -> shift right logical -> R
    # sb -> add
    # sh -> add
    # sw -> add
    # sub -> subtract -> R
    # ---------------------------------------------------------- ghanona
    # alu_op:(110 nabashe)
        # 000 -> add
        # 010 -> and                                           ===> mishe avale ina ye 111 ezafe kard
        # 001 -> compare_equal -> subtract (bit Zero)
        # 011 -> or
        # 101 -> set_less_than
    # alu_op:(110 bashe)
        # 100000 -> add
        # 100001 -> add
        # 100100 -> and
        # 100111 -> nor
        # 100101 -> or
        # 101010 -> set_less_than
        # 101011 -> set_less_than_unsigen
        # 100010 -> subtract
        # 000000 -> shift_left_logical
        # 000010 -> shift_right_logical
        # 001000 -> jump_register -> lazem nist bere to alu -> kodesh ham 1001
    # ----------------------------------------------------------
    # 111000 -> 0010
    # 111010 -> 0000
    # 111001 -> xxxx
    # 111011 -> 0001
    # 111101 -> 0100
    # 100000 -> 0010
    # 100001 -> 0010
    # 100100 -> 0000
    # 100111 -> 1000
    # 100101 -> 0001
    # 101010 -> 0100
    # 101011 -> 0101
    # 100010 -> 0011
    # 000000 -> 0111
    # 000010 -> 0110
    # 001000 -> 1001
    selector = LogicGates.And(int(alu_op[0]), int(alu_op[1]), LogicGates.Not(int(alu_op[2])))
    signal_1 = '111'+alu_op
    signal_2 = funct_code
    signal = ''
    for i in range(6):
        signal = signal + str(mux.mux_2x1(int(signal_1[i]), int(signal_2[i]), selector))
    
    result_bit_3 = LogicGates.Or(LogicGates.And(LogicGates.Not(int(signal[0])), LogicGates.Not(int(signal[1]))
                                              , int(signal[2]), LogicGates.Not(int(signal[3])), LogicGates.Not(int(signal[4]))
                                              , LogicGates.Not(int(signal[5])))
                                , LogicGates.And(int(signal[0]), LogicGates.Not(int(signal[1]))
                                               , LogicGates.Not(int(signal[2])), int(signal[3]), int(signal[4]), int(signal[5])))
    
    result_bit_2 = LogicGates.Or(LogicGates.Not(LogicGates.Or(int(signal[0]), int(signal[1]), int(signal[2])
                                                            , int(signal[3]), int(signal[5])))
                               , LogicGates.And(int(signal[0]), LogicGates.Not(int(signal[1])), int(signal[2])
                                              , LogicGates.Not(int(signal[3])), int(signal[4]))
                               , LogicGates.And(int(signal[0]), int(signal[1]), int(signal[2]), int(signal[3])
                                              , LogicGates.Not(int(signal[4])), int(signal[5])))

    result_bit_1 = LogicGates.Or(LogicGates.Not(LogicGates.Or(int(signal[1]), int(signal[2]), int(signal[3]), int(signal[5])))
                               , LogicGates.Not(LogicGates.Or(LogicGates.Not(int(signal[0])), int(signal[1])
                                                            , int(signal[2]), int(signal[3]), int(signal[4])))
                               , LogicGates.And(int(signal[0]), int(signal[1]), int(signal[2])
                                              , LogicGates.Not(int(signal[3])), LogicGates.Not(int(signal[4]))
                                              , LogicGates.Not(int(signal[5]))))
    
    result_bit_0 = LogicGates.Or(LogicGates.Not(LogicGates.Or(int(signal[0]), int(signal[1]), int(signal[3])
                                                            , int(signal[4]), int(signal[5])))
                              , LogicGates.And(int(signal[0]), int(signal[2]), LogicGates.Not(int(signal[3]))
                                             , int(signal[4]), int(signal[5]))
                              , LogicGates.And(int(signal[0]), LogicGates.Not(int(signal[1])), LogicGates.Not(int(signal[2]))
                                             , LogicGates.Not(int(signal[3])), int(signal[4]), LogicGates.Not(int(signal[5])))
                              , LogicGates.And(int(signal[0]), LogicGates.Not(int(signal[1])), LogicGates.Not(int(signal[2]))
                                             , int(signal[3]), LogicGates.Not(int(signal[4])), int(signal[5])))

    return f'{result_bit_3}{result_bit_2}{result_bit_1}{result_bit_0}'

# print(alu_control('100000', '101'))
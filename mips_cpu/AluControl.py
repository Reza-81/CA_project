from mips_cpu import LogicGates
from mips_cpu import mux


def alu_control(funct_code : str, alu_op : str) -> str:
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

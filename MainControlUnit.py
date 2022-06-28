import LogicGates


def control_unit(opcode):
    reg_dst = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[2])))

    jump = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                        , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[3])), int(opcode[4]))
    
    branch = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                          , LogicGates.Not(int(opcode[2])), int(opcode[3]), LogicGates.Not(int(opcode[4]))
                          , LogicGates.Not(int(opcode[5])))

    mem_read = LogicGates.Or(LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                           , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[4])))
                           , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                           , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[3]))
                           , int(opcode[5])))

    mem_to_reg_bit_1 = LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                    , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[4])))
    
    mem_to_reg_bit_0 = LogicGates.Or(LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                   , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[4]))
                                   , LogicGates.Not(int(opcode[5])))
                                   , LogicGates.And(int(opcode[0])
                                   , LogicGates.Not(int(opcode[1])), LogicGates.Not(int(opcode[2]))
                                   , LogicGates.Not(int(opcode[3])), int(opcode[4]), int(opcode[5])))
    
    mem_write = LogicGates.Or(LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                              , int(opcode[2]), LogicGates.Not(int(opcode[3]))
                              , LogicGates.Not(int(opcode[4])))
                              , LogicGates.And(int(opcode[0])
                              , LogicGates.Not(int(opcode[1])), int(opcode[2])
                              , LogicGates.Not(int(opcode[3])), int(opcode[5])))

    alu_src_bit_1 = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                 , int(opcode[2]), int(opcode[3]), LogicGates.Not(int(opcode[4])))

    alu_src_bit_0 = LogicGates.Or(LogicGates.And(LogicGates.Not(int(opcode[1])), int(opcode[2])
                                , LogicGates.Not(int(opcode[3])), LogicGates.Not(int(opcode[4])))
                                , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[4])))
                                , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                , LogicGates.Not(int(opcode[3])), int(opcode[5]))
                                , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                , int(opcode[2]), LogicGates.Not(int(opcode[3])), LogicGates.Not(int(opcode[5]))))
    
    reg_write = LogicGates.Or(LogicGates.And(int(opcode[3]), int(opcode[4]))
                            , LogicGates.And(LogicGates.Not(int(opcode[0])), int(opcode[1]))
                            , LogicGates.And(int(opcode[1]), LogicGates.Not(int(opcode[3])))
                            , LogicGates.And(int(opcode[1]), int(opcode[5]))
                            , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[2])))
                            , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[3]))
                            , LogicGates.Not(int(opcode[4])))
                            , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[3])), int(opcode[5]))
                            , LogicGates.And(int(opcode[2]), int(opcode[4]), LogicGates.Not(int(opcode[5])))
                            , LogicGates.And(LogicGates.Not(int(opcode[1])), int(opcode[2]), int(opcode[3])))
    
    alu_op_bit_1 = None

    alu_op_bit_0 = LogicGates.Or(LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                               , LogicGates.Not(int(opcode[2])), int(opcode[3]), LogicGates.Not(int(opcode[4])))
                               , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                               , int(opcode[3]), LogicGates.Not(int(opcode[4])), int(opcode[5]))
                               , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                               , int(opcode[2]), LogicGates.Not(int(opcode[3])), int(opcode[4]), LogicGates.Not(int(opcode[5]))))

    return {'reg_dst': reg_dst
          , 'jump': jump
          , 'branch': branch
          , 'mem_read': mem_read
          , 'mem_to_reg': str(mem_to_reg_bit_1) + str(mem_to_reg_bit_0)
          , 'mem_write': mem_write
          , 'alu_src': str(alu_src_bit_1) + str(alu_src_bit_0)
          , 'reg_write': reg_write}

print(control_unit('100011'))
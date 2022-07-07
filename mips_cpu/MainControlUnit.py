from mips_cpu import LogicGates


def control_unit(opcode : str) -> dict[int, int, int, int, str, int, str, int, str, int]:
    reg_dst = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[2])))

    jump = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                        , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[3])), int(opcode[4]))
    
    branch_equal = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                          , LogicGates.Not(int(opcode[2])), int(opcode[3]), LogicGates.Not(int(opcode[4]))
                          , LogicGates.Not(int(opcode[5])))

    branch_not_euqal = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                          , LogicGates.Not(int(opcode[2])), int(opcode[3]), LogicGates.Not(int(opcode[4]))
                          , int(opcode[5]))

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
                                   , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                                  , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[3]))
                                                  , int(opcode[4]), int(opcode[5])))
    
    mem_write = LogicGates.Or(LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                           , int(opcode[2]), LogicGates.Not(int(opcode[3]))
                                           , LogicGates.Not(int(opcode[4])))
                            , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                           , int(opcode[2]), LogicGates.Not(int(opcode[3]))
                                           , int(opcode[5])))

    alu_src_bit_1 = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                 , int(opcode[2]), int(opcode[3]), LogicGates.Not(int(opcode[4])))

    alu_src_bit_0 = LogicGates.Or(LogicGates.And(LogicGates.Not(int(opcode[1])), int(opcode[2])
                                               , LogicGates.Not(int(opcode[3])), LogicGates.Not(int(opcode[4])))
                                               , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                               , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[4])))
                                , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1]))
                                               , LogicGates.Not(int(opcode[3])), int(opcode[5]))
                                               , LogicGates.And(LogicGates.Not(int(opcode[0]))
                                               , LogicGates.Not(int(opcode[1]))
                                               , int(opcode[2]), LogicGates.Not(int(opcode[3]))
                                               , LogicGates.Not(int(opcode[5]))))
    
    reg_write = LogicGates.Or(LogicGates.And(int(opcode[3]), int(opcode[4]))
                            , LogicGates.And(LogicGates.Not(int(opcode[0])), int(opcode[1]))
                            , LogicGates.And(int(opcode[1]), LogicGates.Not(int(opcode[3])))
                            , LogicGates.And(int(opcode[1]), int(opcode[5]))
                            , LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[2])))
                            , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[3]))
                                           , LogicGates.Not(int(opcode[4])))
                            , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[3]))
                                           , int(opcode[5]))
                            , LogicGates.And(int(opcode[2]), int(opcode[4]), LogicGates.Not(int(opcode[5])))
                            , LogicGates.And(LogicGates.Not(int(opcode[1])), int(opcode[2]), int(opcode[3])))
    
    alu_op_bit_2 = LogicGates.Or(LogicGates.Not(LogicGates.Or(int(opcode[0]), int(opcode[1]), int(opcode[2])
                                              , int(opcode[3]), int(opcode[4]), int(opcode[5])))
                               , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                              , int(opcode[2]), LogicGates.Not(int(opcode[3])), int(opcode[4])
                                              , LogicGates.Not(int(opcode[5]))))

    alu_op_bit_1 = LogicGates.Or(LogicGates.Not(LogicGates.Or(int(opcode[0]), int(opcode[1]), int(opcode[2])
                                                            , int(opcode[3]), int(opcode[4]), int(opcode[5])))
                               , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                              , int(opcode[2]), int(opcode[3]), LogicGates.Not(int(opcode[4]))))

    alu_op_bit_0 = LogicGates.Or(LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                              , LogicGates.Not(int(opcode[2])), int(opcode[3])
                                              , LogicGates.Not(int(opcode[4])))
                               , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                              , int(opcode[3]), LogicGates.Not(int(opcode[4])), int(opcode[5]))
                               , LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                              , int(opcode[2]), LogicGates.Not(int(opcode[3])), int(opcode[4])
                                              , LogicGates.Not(int(opcode[5]))))
    
    jump_and_link = LogicGates.And(LogicGates.Not(int(opcode[0])), LogicGates.Not(int(opcode[1]))
                                 , LogicGates.Not(int(opcode[2])), LogicGates.Not(int(opcode[3]))
                                 , int(opcode[4]), int(opcode[5]))
    
    load_half = LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1])), LogicGates.Not(int(opcode[2]))
                             , LogicGates.Not(int(opcode[3])), LogicGates.Not(int(opcode[4])), int(opcode[5]))

    load_half_unsigned = LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1])), LogicGates.Not(int(opcode[2]))
                                      , int(opcode[3]), LogicGates.Not(int(opcode[4])), int(opcode[5]))

    load_byte = LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1])), LogicGates.Not(int(opcode[2]))
                             , LogicGates.Not(int(opcode[3])), LogicGates.Not(int(opcode[4]))
                             , LogicGates.Not(int(opcode[5])))

    load_byte_unsigned = LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1])), LogicGates.Not(int(opcode[2]))
                             , int(opcode[3]), LogicGates.Not(int(opcode[4])), LogicGates.Not(int(opcode[5])))

    store_half = LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1])), int(opcode[2])
                              , LogicGates.Not(int(opcode[3])), LogicGates.Not(int(opcode[4])), int(opcode[5]))

    store_byte = LogicGates.And(int(opcode[0]), LogicGates.Not(int(opcode[1])), int(opcode[2])
                              , LogicGates.Not(int(opcode[3])), LogicGates.Not(int(opcode[4]))
                              , LogicGates.Not(int(opcode[5])))

    return {'reg_dst': reg_dst
          , 'jump': jump
          , 'branch_equal': branch_equal
          , 'branch_not_euqal': branch_not_euqal
          , 'mem_read': mem_read
          , 'mem_to_reg': LogicGates.Or(mem_to_reg_bit_1, mem_to_reg_bit_0)
          , 'mem_write': mem_write
          , 'alu_src': LogicGates.Or(alu_src_bit_1 ,alu_src_bit_0)
          , 'reg_write': reg_write
          , 'alu_op': str(alu_op_bit_2) + str(alu_op_bit_1) + str(alu_op_bit_0)
          , 'jump_and_link': jump_and_link
          , 'load_half': load_half
          , 'load_half_unsigned': load_half_unsigned
          , 'load_byte': load_byte
          , 'load_byte_unsigned': load_byte_unsigned
          , 'store_half': store_half
          , 'store_byte': store_byte}

# print(control_unit('100100'))
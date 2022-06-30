def alu_control(funct_code, alu_op):
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
    pass
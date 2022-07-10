from mips_cpu import RegisterFile
from mips_cpu import Memory
from mips_cpu import MainControlUnit
from mips_cpu import Extended
from mips_cpu import Alu
from mips_cpu import mux
from mips_cpu import AluControl
from mips_cpu import adder
from mips_cpu import shiftlogical
from mips_cpu import LogicGates

def run():
    pc = RegisterFile.Register(32)

    counter = 0
    while(True):
        # gereftane instruction
        instruction = Memory.InstructionMemory.read_instruction(int(pc.read_data(), 2))
        if instruction == 32*'0':
            break
        print('instruction:', int(pc.read_data(), 2)//4 + 1, '     counter:', counter + 1)
        
        # sakhte signal haye control unit
        control_unit_signals = MainControlUnit.control_unit(instruction[0:6])

        # khondane register haye havi data
        register_1 = RegisterFile.RegisterFile.read_data(int(instruction[6:11], 2))
        register_2 = RegisterFile.RegisterFile.read_data(int(instruction[11:16], 2))

        # alu control
        alu_control_signals = AluControl.alu_control(instruction[26:], control_unit_signals['alu_op'])

        # sign extended 16 -> 32
        sign_extended_immediate = Extended.sign_extended_16_32(instruction[16:])

        # alu
        signal_for_read_data_1 = LogicGates.Or(LogicGates.And(LogicGates.Not(int(alu_control_signals[0])), int(alu_control_signals[1])
                                                            , int(alu_control_signals[2]), (LogicGates.Not(int(alu_control_signals[3]))))
                                            , LogicGates.And(LogicGates.Not(int(alu_control_signals[0])), int(alu_control_signals[1])
                                                            , int(alu_control_signals[2]), int(alu_control_signals[3])))
        read_data_1 = ''
        shamt = 27*'0' + instruction[21:26]
        for i in range(32):
            read_data_1 += str(mux.mux_2x1(int(register_1[i]), int(shamt[i]), signal_for_read_data_1))
        read_data_2 = ''
        for i in range(32):
            read_data_2 += str(mux.mux_2x1(int(register_2[i]), int(sign_extended_immediate[i]), int(control_unit_signals['alu_src'])))
        alu_result = Alu.alu(read_data_1, read_data_2, alu_control_signals)

        # write in memory
        store_half = Extended.sign_extended_16_32(register_2[16:])
        store_byte = Extended.sign_extended_8_32(register_2[24:])
        write_data = ''
        for i in range(32):
            write_data += str(mux.mux_4x1(int(register_2[i]), int(store_byte[i]), int(store_half[i]), 0
                                    , f'{control_unit_signals["store_half"]}{control_unit_signals["store_byte"]}'))
        if control_unit_signals['mem_write']:
            Memory.DataMemory.write_data(write_data, int(alu_result[0], 2))
        
        # read from memory
        read_memory_data = Memory.DataMemory.read_data(int(alu_result[0], 2))
        load_half = Extended.sign_extended_16_32(read_memory_data[16:])
        load_half_unsigned = Extended.unsign_extended_16_32(read_memory_data[16:])
        load_byte = Extended.sign_extended_8_32(read_memory_data[24:])
        load_byte_unsigned = Extended.unsign_extended_8_32(read_memory_data[24:])
        mem_to_reg_data = ''
        for i in range(32):
            mem_to_reg_data += str(mux.mux_16x1(int(read_memory_data[i]), int(load_half[i]), int(load_half_unsigned[i]), 0
                                            , int(load_byte[i]), 0, 0, 0, int(load_byte_unsigned[i]), 0, 0, 0, 0, 0, 0, 0
                                            , str(control_unit_signals['load_byte_unsigned'])+str(control_unit_signals['load_byte'])
                                            + str(control_unit_signals['load_half_unsigned'])+str(control_unit_signals['load_half'])))
        write_data_to_register = ''
        for i in range(32):
            write_data_to_register += str(mux.mux_2x1(int(alu_result[0][i]), int(mem_to_reg_data[i]), int(control_unit_signals['mem_to_reg'])))
        
        # write back to register file
        return_address = adder.adder_subtractor_32_bit(pc.read_data(), '00000000000000000000000000000100')[0]
        data_to_reg = ''
        for i in range(32):
            data_to_reg += str(mux.mux_2x1(int(write_data_to_register[i]), int(return_address[i]), control_unit_signals['jump_and_link']))
        destination_register_number = ''
        for i in range(5):
            destination_register_number += str(mux.mux_4x1(int(instruction[11:16][i]), int(instruction[16:21][i]), 0, 1
                                                        , str(control_unit_signals['jump_and_link'])+str(control_unit_signals['reg_dst'])))
        if control_unit_signals['reg_write']:
            RegisterFile.RegisterFile.write_data(data_to_reg, int(destination_register_number, 2))

        # update pc
        pc_next = adder.adder_subtractor_32_bit(pc.read_data(), '00000000000000000000000000000100')[0]
        j_target = shiftlogical.shift_left(6*'0'+instruction[6:], '00000000000000000000000000000010')
        j_target = pc_next[:4] + j_target[4:]
        sign_extended_immediate = shiftlogical.shift_left(sign_extended_immediate, '00000000000000000000000000000010')
        selector_jr = LogicGates.And(int(alu_control_signals[0]), LogicGates.Not(int(alu_control_signals[1]))
                                , LogicGates.Not(int(alu_control_signals[2])), int(alu_control_signals[3]))
        pc_next_or_jr = ''
        for i in range(32):
            pc_next_or_jr += str(mux.mux_2x1(int(pc_next[i]), int(register_1[i]), selector_jr))
        pc_next = pc_next_or_jr
        branch_target = adder.adder_subtractor_32_bit(pc_next, sign_extended_immediate)[0]
        selector_for_branch = LogicGates.Or(LogicGates.And(control_unit_signals['branch_equal'], alu_result[1])
                                        , LogicGates.And(control_unit_signals['branch_not_euqal'], LogicGates.Not(alu_result[1])))
        pc_next_or_branch = ''
        for i in range(32):
            pc_next_or_branch += str(mux.mux_2x1(int(pc_next[i]), int(branch_target[i]), selector_for_branch))
        pc_next = pc_next_or_branch
        pc_next_or_jump = ''
        for i in range(32):
            pc_next_or_jump += str(mux.mux_2x1(int(pc_next[i]), int(j_target[i]), control_unit_signals['jump']))
        pc_next = pc_next_or_jump
        pc.write_data(pc_next)
        counter += 1

    print('finihsed :)')
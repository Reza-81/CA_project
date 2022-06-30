import RegisterFile
import Memory
import MainControlUnit
import Extended
import Alu
import mux
import AluControl
import adder

# 000000 00000 00000 0000000000 000000

pc = RegisterFile.Register(32)

while(True):
    # gereftane instruction
    instruction = Memory.InstructionMemory().read_instruction(pc)
    
    # sakhte signal haye control unit
    control_unit_signals = MainControlUnit.control_unit(instruction[0:6])

    # khondane register haye havi data
    register_1 = RegisterFile.RegisterFile().read_data(int(instruction[11:16], 2))
    register_2 = RegisterFile.RegisterFile().read_data(int(instruction[6:11], 2))

    # alu control
    alu_control_signals = AluControl.alu_control(instruction[26:], control_unit_signals['alu_op'])

    # sign extended 16 -> 32
    extended_immediate = Extended.sign_extended_16_32(instruction[16:])

    # alu
    read_data_2 = ''
    for i in range(32):
        read_data_2 += mux.mux_2x1(register_2[i], extended_immediate[i], control_unit_signals['alu_src'])
    alu_result = Alu.alu(register_1, read_data_2, alu_control_signals)

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
        mem_to_reg_data += str(mux.mux_16x1(read_memory_data, load_half, load_half_unsigned, 0, load_byte, 0, 0, 0, load_byte_unsigned
                                          , str(control_unit_signals['load_half'])+str(control_unit_signals['load_half_unsigned'])
                                          + str(control_unit_signals['load_byte'])+str(control_unit_signals['load_byte_unsigned'])))
    write_data_to_register = ''
    for i in range(32):
        write_data_to_register += str(mux.mux_2x1(alu_result[0][i], mem_to_reg_data[i], control_unit_signals['mem_to_reg']))
    
    # write back to register file
    data_to_reg = ''
    return_address = adder.adder_subtractor_32_bit(pc.read_data(), '00000000000000000000000000000100')[0]
    for i in range(32):
        data_to_reg += str(mux.mux_2x1(write_data_to_register, return_address, control_unit_signals['jump_and_link']))
    destination_register_number = ''
    for i in range(5):
        destination_register_number += str(mux.mux_2x1(instruction[11:16]), instruction[16:21], control_unit_signals['reg_dst'])
    RegisterFile.RegisterFile.write_data(data_to_reg, int(destination_register_number, 2))

    # update pc




from assembler import assembler
from mips_cpu import DataPath, Memory, RegisterFile

# assembler
# assembly_file_name = input('/>enter the assembly file name: ').lower()
assembly_file_name = 'assembly.txt'
machine_code = assembler.read_file(assembly_file_name)

# load instructions to memory
for index, i in enumerate(machine_code):
    Memory.InstructionMemory.write_instruction(i, 4*index)
del(machine_code)

# data path
DataPath.run()

# memory
data_memory = Memory.DataMemory.memory()
instruction_memory = Memory.InstructionMemory.memory()
registers = RegisterFile.RegisterFile.registers()
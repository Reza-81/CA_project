import os
import json
from assembler import Jtype
from assembler import Itype
from assembler import Rtype


def read_file(assembly_file_name):
    machine_code_list = []
    assembly_code = []
    if assembly_file_name in os.listdir():
        labels = dict()
        # check for label
        with open(assembly_file_name) as f:
            for number, line in enumerate(f):
                if ':' in line:
                    line = line.split(':')
                    labels[line[0]] = number
                    if line[1].strip() != '':
                        assembly_code.append(line[1])
                else:
                    assembly_code.append(line)
        # read instructions
        for number, line in enumerate(assembly_code):
            # check for label
            if ':' in line:
                line = line.split(':', 1)[1].strip().split(' ', 1)
            else:
                line = line.strip().split(' ', 1)
            if line != ['']:
                with open('assembler/instructions.json', 'r') as json_file:
                    instructions = json.load(json_file)
                    # check the instruction type
                    if line[0] in instructions:
                        # r type instruction
                        if instructions[line[0]]['type'] == 'r':
                            temp = line.pop(1)
                            line += temp.replace(' ', '').split(',')
                            if len(line) == 4:
                                if line[0] == 'sll' or line[0] == 'srl':
                                    machine_code = Rtype.r_type_instruction(instructions[line[0]]['funct'], '$zero', line[2], line[1], int(line[3]))
                                else:
                                    machine_code = Rtype.r_type_instruction(instructions[line[0]]['funct'], line[2], line[3], line[1], 0)
                                if not machine_code:
                                    print(f'this instruction is not correct: line {number+1}')
                                    return []
                            elif len(line) == 2:
                                machine_code = Rtype.r_type_instruction(instructions[line[0]]['funct'], line[1], '$zero', '$zero', 0)
                                if not machine_code:
                                    print(f'this instruction is not correct: line {number+1}')
                                    return []
                            else:
                                print(f'this instruction is not correct: line {number+1}')
                                return []
                        # i type instruction
                        elif instructions[line[0]]['type'] == 'i':
                            temp = line.pop(1)
                            if '(' in temp:
                                temp = temp.replace('(', ',')
                                temp = temp.replace(')', '')
                                line += temp.replace(' ', '').split(',')
                                line[2], line[3] = line[3], line[2]
                            else:
                                line += temp.replace(' ', '').split(',')
                            if len(line) == 4:
                                try:
                                    machine_code = Itype.i_type_instruction(instructions[line[0]]['opcode'], line[2], line[1], int(line[3]))
                                except:
                                    machine_code = Itype.i_type_instruction(instructions[line[0]]['opcode'], line[2], line[1], labels[line[3]]-number)
                                if not machine_code:
                                    print(f'this instruction is not correct: line {number+1}')
                                    return []
                            else:
                                print(f'this instruction is not correct: line {number+1}')
                                return []
                        # j type instruction
                        elif instructions[line[0]]['type'] == 'j':
                            if len(line) == 2:
                                machine_code = Jtype.j_type_instruction(instructions[line[0]]['opcode'], line[1].replace(' ', ''), labels)
                                if not machine_code:
                                    print(f'this instruction is not correct: line {number+1}')
                                    return []
                            else:
                                print(f'this instruction is not correct: line {number+1}')
                                return []
                    else:
                        print(f'this instruction is not correct: line {number+1}')
                        return []
                machine_code_list.append(machine_code)
        return machine_code_list
    else:
        print('sorry! there is no such file.')
        return []
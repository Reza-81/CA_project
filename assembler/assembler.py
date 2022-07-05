import os
import json
import Jtype
import Itype
import Rtype


def read_file():
    machine_code_list = []
    assembly_file_name = input('/>enter the assembly file name: ').lower()
    if assembly_file_name in os.listdir():
        labels = dict()
        with open(assembly_file_name) as f:
            for number, line in enumerate(f):
                # check for label
                line = line[:-1].split(' ', 1)
                if ':' in line[0]:
                    labels[line[0][:-1]] = number
                    line = line[1].split(' ', 1)
                with open('instructions.json', 'r') as json_file:
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
                                    print(f'this instruction is not correct: line {number}')
                                    return []
                            elif len(line) == 2:
                                machine_code = Rtype.r_type_instruction(instructions[line[0]]['funct'], line[1], '$zero', '$zero', 0)
                                if not machine_code:
                                    print(f'this instruction is not correct: line {number}')
                                    return []
                            else:
                                print(f'this instruction is not correct: line {number}')
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
                                machine_code = Itype.i_type_instruction(instructions[line[0]]['opcode'], line[2], line[1], int(line[3]))
                                if not machine_code:
                                    print(f'this instruction is not correct: line {number}')
                                    return []
                            else:
                                print(f'this instruction is not correct: line {number}')
                                return []
                        # j type instruction
                        elif instructions[line[0]]['type'] == 'j':
                            if len(line) == 2:
                                machine_code = Jtype.j_type_instruction(instructions[line[0]]['opcode'], line[1].replace(' ', ''), labels)
                                if not machine_code:
                                    print(f'this instruction is not correct: line {number}')
                                    return []
                            else:
                                print(f'this instruction is not correct: line {number}')
                                return []
                    else:
                        print(f'this instruction is not correct: line {number}')
                        return []
                machine_code_list.append(machine_code)
        return machine_code_list
    else:
        print('sorry! there is no such file.')
        return []




machine_code = read_file()
for i in machine_code:
    print(i)
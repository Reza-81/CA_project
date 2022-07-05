import json


def i_type_instruction(opcode, rs, rt, immediate):
    with open('registers.json', 'r') as json_file:
        registers = json.load(json_file)
    if rs in registers and rt in registers:
        immediate = bin(immediate)[2:]
        return opcode + registers[rs] + registers[rt] + + (16-len(immediate))*'0' + immediate
    return None
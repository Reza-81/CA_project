import json


def r_type_instruction(funct, rs, rt, rd, shamt):
    with open('assembler/registers.json', 'r') as json_file:
            registers = json.load(json_file)
    if rs in registers and rt in registers and rd in registers:
        shamt = bin(shamt if shamt>0 else shamt+(1<<32))[2:][-5:]
        return 6*'0' + registers[rs] + registers[rt] + registers[rd] + (5-len(shamt))*'0' + shamt + funct


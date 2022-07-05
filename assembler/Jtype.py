def j_type_instruction(opcode, label, labels):
    if label in labels:
        immediate = bin(labels[label])[2:]
        return opcode + (26-len(immediate))*'0' + immediate
    return None
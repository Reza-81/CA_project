def j_type_instruction(opcode, label, labels):
    try:
        label = int(label)
        immediate = bin(label if label>0 else label+(1<<32))[2:][-26:]
        return opcode + (26-len(immediate))*'0' + immediate
    except:
        if label in labels:
            immediate = bin(labels[label] if labels[label]>0 else labels[label]+(1<<32))[2:][-26:]
            return opcode + (26-len(immediate))*'0' + immediate
    return None
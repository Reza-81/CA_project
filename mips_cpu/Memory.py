class DataMemory():
    __memory_cell_list = [32*'0'] * 100
    
    @classmethod
    def write_data(cls, data, index):
        index //= 4
        if index < len(DataMemory.__memory_cell_list):
            DataMemory.__memory_cell_list[index] = data
    
    @classmethod
    def read_data(cls, index):
        index //= 4
        if index < len(DataMemory.__memory_cell_list):
            return DataMemory.__memory_cell_list[index]
        return 32*'0'
    
    @classmethod
    def memory(cls):
        return DataMemory.__memory_cell_list


class InstructionMemory():
    __memory_cell_list = [32*'0'] * 100
    
    @classmethod
    def write_instruction(cls, data, index):
        index //= 4
        if index < len(InstructionMemory.__memory_cell_list):
            InstructionMemory.__memory_cell_list[index] = data
    
    @classmethod
    def read_instruction(cls, index):
        index //= 4
        if index < len(InstructionMemory.__memory_cell_list):
            return InstructionMemory.__memory_cell_list[index]
        return 32*'0'
    
    @classmethod
    def memory(cls):
        return InstructionMemory.__memory_cell_list
class DataMemory():
    __memory_cell_list = [32*'0'] * 100
    
    @classmethod
    def write_data(cls, data, index):
        DataMemory.__memory_cell_list[index//4] = data
    
    @classmethod
    def read_data(cls, index):
        return DataMemory.__memory_cell_list[index//4]
    
    @classmethod
    def memory(cls):
        return DataMemory.__memory_cell_list


class InstructionMemory():
    __memory_cell_list = [32*'0'] * 100
    
    @classmethod
    def write_instruction(cls, data, index):
        InstructionMemory.__memory_cell_list[index//4] = data
    
    @classmethod
    def read_instruction(cls, index):
        return InstructionMemory.__memory_cell_list[index//4]
    
    @classmethod
    def memory(cls):
        return InstructionMemory.__memory_cell_list
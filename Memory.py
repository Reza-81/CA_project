class DataMemory():
    __memory_cell_list = [None] * 100
    
    @classmethod
    def write_data(cls, data, index):
        DataMemory.__memory_cell_list[index/4] = data
    
    @classmethod
    def read_data(cls, index):
        return DataMemory.__memory_cell_list[index/4]



class InstructionMemory():
    __memory_cell_list = [None] * 100
    
    @classmethod
    def write_instruction(cls, data, index):
        DataMemory.__memory_cell_list[index/4] = data
    
    @classmethod
    def read_instruction(cls, index):
        return DataMemory.__memory_cell_list[index/4]
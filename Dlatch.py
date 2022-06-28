import LogicGates


class SRlatch():
    def __init__(self):
        self.__input_r = 1
        self.__input_s = 0
    
    def run(self):
        and_r = LogicGates.And(self.__input_r, 1)
        and_s = LogicGates.And(self.__input_s, 1)
        nor_r = LogicGates.Nor(and_r, 0)
        nor_s = LogicGates.Nor(and_s, 0)
        return (nor_r, nor_s)
    
    def get_input(self, input_s, input_r):
        self.__input_r = input_r
        self.__input_s = input_s


class Dlatch():
    def __init__(self):
        self.sr_latch = SRlatch()
    
    def get_input(self, input):
        self.sr_latch.get_input(input, LogicGates.Not(input))

    def run(self):
        return self.sr_latch.run()

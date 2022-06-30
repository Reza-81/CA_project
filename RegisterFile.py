class Register():
    def __init__(self, register_number):
        self.__register_number = register_number
        self.__value = 0

    def write_data(self, data):
        self.__value = data
    
    def read_data(self):
        return self.__value

    def number(self):
        return self.__register_number


class RegisterFile():
    __register_list = []
    for i in range(32):
        Register.__register_list.append(Register(i))
    
    @classmethod
    def write_data(cls, data, register_number):
        for register in RegisterFile.__register_list:
            if register.number() == register_number:
                register.write_data(data)
    
    @classmethod
    def read_data(cls, register_number):
        for register in RegisterFile.__register_list:
            if register.number() == register_number:
                return register.read_data()

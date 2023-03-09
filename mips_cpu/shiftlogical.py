from mips_cpu import Dlatch

def shift_right(a : str, b : str) -> str:
    b = int(b[-5:], 2)
    list_d_latch = []
    for i in range(0, 32):
        d_latch = Dlatch.Dlatch()
        d_latch.get_input(int(a[i]))
        list_d_latch.append(d_latch)

    for _ in range(b):
        for i in range(31, 0, -1):
            list_d_latch[i].get_input(list_d_latch[i-1].run()[0])
        list_d_latch[0].get_input(0)

    result = ''
    for i in list_d_latch:
        result += str(i.run()[0])
    return result

def shift_left(a : str, b : str) -> str:
    b = int(b[-5:], 2)
    list_d_latch = []
    for i in range(0, 32):
        d_latch = Dlatch.Dlatch()
        d_latch.get_input(int(a[i]))
        list_d_latch.append(d_latch)
    
    for _ in range(b):
        for i in range(0, 31):
            list_d_latch[i].get_input(list_d_latch[i+1].run()[0])
        list_d_latch[31].get_input(0)
    
    result = ''
    for i in list_d_latch:
        result += str(i.run()[0])
    return result

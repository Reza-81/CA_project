import LogicGates

def mux_2x1(a : int, b : int, selector : int) -> int:
    return LogicGates.Or(LogicGates.And(b, selector), LogicGates.And(a, LogicGates.Not(selector)))

def mux_4x1(a : int, b : int, c : int, d : int, selector : str) -> int:
    mux_1 = mux_2x1(a, b, int(selector[1]))
    mux_2 = mux_2x1(c, d, int(selector[1]))
    mux_3 = mux_2x1(mux_1, mux_2, int(selector[0]))
    return mux_3

def mux_8x1(a : int, b : int, c : int, d : int, e : int, f : int, g : int, h : int, selector : str) -> int:
    mux_1 = mux_4x1(a, b, c, d, selector[1:])
    mux_2 = mux_4x1(e, f, g, h, selector[1:])
    mux_3 = mux_2x1(mux_1, mux_2, int(selector[0]))
    return mux_3

def mux_16x1(a : int, b : int, c : int, d : int, e : int, f : int, g : int, h : int
           , i : int, j : int, k : int, l : int, m : int, n : int, o : int, p : int, selector : str) -> int:
    mux_1 = mux_8x1(a, b, c, d, e, f, g, h, selector[1:])
    mux_2 = mux_8x1(i, j, k, l, m, n, o, p, selector[1:])
    mux_3 = mux_2x1(mux_1, mux_2, int(selector[0]))
    return mux_3

# print(mux_2x1(1, 0, 0))
# print(mux_16x1(1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,'0001'))

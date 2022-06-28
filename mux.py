import LogicGates

def mux_2x1(a, b, selector):
    return LogicGates.Or(LogicGates.And(b, selector), LogicGates.And(a, LogicGates.Not(selector)))

def mux_4x1(a, b, c, d, selector):
    mux_1 = mux_2x1(a, b, int(selector[1]))
    mux_2 = mux_2x1(c, d, int(selector[1]))
    mux_3 = mux_2x1(mux_1, mux_2, int(selector[0]))
    return mux_3

# print(mux_4x1(0,0,1,1,'11'))

print("..\nz0   z1   z2\n------------\nz3   z4   z5\n------------\nz6   z7   z8\n ..")

"""
    z0   z1   z2
    ------------
    z3   z4   z5
    ------------
    z6   z7   z8

"""

def NOT(x):
    return int(not x)

def AND(x1, x2):
    return int(x1 and x2)

def XOR(x1, x2):
    return int(x1 != x2)

def OR(x1, x2):
    return int(x1 or x2)

def HA(x1, x2):
    c = AND(x1, x2)
    s = XOR(x1, x2)
    return (c, s)

def FA(x1, x2, x3):
    c = OR(AND(x1, x2), AND(XOR(x1, x2), x3))
    s = XOR(XOR(x1, x2), x3)
    return (c, s)

def PG(g1, p1, g2, p2):
    g = OR(g2, AND(p2, g1))
    p = AND(p2, p1)
    return (g, p)

def MX(c, x0, x1):
    if c:
        return x1
    else:
        return x0



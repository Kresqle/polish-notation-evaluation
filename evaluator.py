from enums import *
from pile import Pile
from errors import *

class Evaluator:
    def __init__(self, ev, nty = NotationType.POSTFIX):
        self.ev = ev.split()
        self.nty = nty
    
    def __repr__(self):
        return " ".join(self.ev)
    
    op = {
        "+": lambda x, y : x + y,
        "-": lambda x, y : x - y,
        "*": lambda x, y : x * y,
        "/": lambda x, y : x / y,
        "%": lambda x, y : x % y
    }

    def eval(self):
        p = Pile()
        r = 0
        for i in range(len(self.ev)):
            c = self.ev[i]
            if c in Token.OPERAND:
                ts = list()
                for _ in range(2):
                    if p.isEmpty():
                        raise MissingValue(i)
                    ts.append(p.unstack())  
                p.stack(self.op.get(c, None)(ts[1], ts[0]))
            elif c.isnumeric():
                p.stack(int(c))
            else:
                raise InvalidOperand(i)

        if len(p.values) > 1:
            raise MissingOperand()
        return p.values[0]
from enums import *
from pile import Pile
from errors import *

class Evaluator:
    def __init__(self, ev, nty = NotationType.POSTFIX):
        self.ev = ev.split()
        self.nty = nty
        self.checkExpression()
    
    def __repr__(self):
        return " ".join(self.ev)

    def checkExpression(self):
        if self.ev[-1].replace('.', '', 1).isnumeric():
            raise EvaluationEndingByANumber()

    def postfix(self):
        p = Pile()
        r = 0
        for i in range(len(self.ev)):
            c = self.ev[i]
            if c in Token.OPERANDS:
                ts = list()
                for _ in range(2):
                    if p.isEmpty():
                        raise MissingValue(i)
                    ts.append(p.unstack())
                p.stack(Token.OPERANDS.get(c, None)(ts[1], ts[0]))
            elif c.replace('.', '', 1).isnumeric():
                p.stack(float(c))
            elif c.replace('.', '').isnumeric():
                raise InvalidValue(c)
            else:
                raise InvalidCharacter(c)

        if len(p.values) > 1:
            raise MissingOperand()
        return p.values[0]

    def eval(self):
        func = getattr(self, self.nty)
        return func()

class Token:
    def __init__(self,v,t):
        #print('criou',v,t)
        self.type = t
        self.value=v
class Node:
    def __init__(self,v,filhos):
        self.value = v
        self.filhos: [Node]= filhos

class UnOp(Node):
    def evaluate(self):
        #print('Unop',self.value, [type(x)for x in self.filhos])
        if self.value == 'minus': 
            return - self.filhos[0].evaluate()
        else:
            return self.filhos[0].evaluate()

class Binop(Node):
    def evaluate(self):
        #print('Biop',self.value, [type(x)for x in self.filhos])
        if self.value == 'minus': 
            return self.filhos[0].evaluate() - self.filhos[1].evaluate()
        elif self.value == 'plus':
            return self.filhos[0].evaluate() + self.filhos[1].evaluate()
        elif self.value == 'times':
            return self.filhos[0].evaluate() * self.filhos[1].evaluate()
        elif self.value == 'div':
            return self.filhos[0].evaluate() // self.filhos[1].evaluate()
class Intvar(Node):
    def evaluate(self):
        #print('Intvar',self.value, [type(x)for x in self.filhos])
        return int(self.value)

class NoOp(Node):
    def evaluate(self):
        pass
# Binop
# UnOp
# Intvar
# NoOp
# .
# .
# .


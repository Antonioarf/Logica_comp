class SymbolClass:

    def __init__(self):
        ## private varibale or property in Python
        self.tabela={}

    def getter(self, valor):
        if valor in self.tabela.keys():
            return self.tabela[valor]
        else:
            raise('Chave invalida')
    def setter(self, chave, valor):
        self.tabela[chave] = valor

tabela = SymbolClass()
class Token:
    def __init__(self,v,t):
        #print('criou',v,t)
        self.type = t
        self.value=v
class Node:
    def __init__(self,v,filhos):
        self.value = v
        self.filhos: [Node]= filhos

class Readln(Node):
    def evaluate(self):
         return int(input())


class UnOp(Node):
    def evaluate(self):
        #print('Unop',self.value, [type(x)for x in self.filhos])
        if self.value == 'minus': 
            return - self.filhos[0].evaluate()
        elif self.value == 'plus':
            return self.filhos[0].evaluate()
        elif self.value == 'not':
            return not self.filhos[0].evaluate()

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
        elif self.value == 'and':
            return self.filhos[0].evaluate() and self.filhos[1].evaluate()
        elif self.value == 'or':
            return self.filhos[0].evaluate() or self.filhos[1].evaluate()
        elif self.value == 'comp':
            return self.filhos[0].evaluate() == self.filhos[1].evaluate()
        elif self.value == 'menor':
            return self.filhos[0].evaluate() < self.filhos[1].evaluate()
        elif self.value == 'maior':
            return self.filhos[0].evaluate() > self.filhos[1].evaluate()
        elif self.value == 'concat':
            return str(self.filhos[0].evaluate()) + str(self.filhos[1].evaluate())
class IfOp(Node):
    def evaluate(self):
        #print('If',self.value, [type(x)for x in self.filhos])
        if self.filhos[0].evaluate():
            self.filhos[1].evaluate()
        elif len(self.filhos) == 3:
            self.filhos[2].evaluate()
class WhileOp(Node):
    def evaluate(self):
        #print('While',self.value, [type(x)for x in self.filhos])
        while self.filhos[0].evaluate():
            self.filhos[1].evaluate()
            
class Intvar(Node):
    def evaluate(self):
        #print('Intvar',self.value, [type(x)for x in self.filhos])
        return int(self.value)

class NoOp(Node):
    def evaluate(self):
        pass


class Identifier(Node): 
    # value=nome da variavel
    # 0 filhos
    def evaluate(self):
        #print('ident-getter',self.value, [type(x)for x in self.filhos])
        return tabela.getter(self.value)

class Println(Node):
    #valor = nada
    #filho= parseexpression 
    def evaluate(self):
        print (self.filhos[0].evaluate())

class Assigment(Node):
    #2 filhos:
    #esquerda= Identifier pra criar
    #direita= expression do valor
    def evaluate(self):
        tabela.setter(self.filhos[0].value,self.filhos[1].evaluate())

class Block(Node):
    #criado na funcao raiz BLOCK
    #um filho pra cada linha => append de filho
    def evaluate(self):
        for filho in self.filhos:
            filho.evaluate()

class SymbolClass:

    def __init__(self):
        ## private varibale or property in Python
        self.tabela={}

    def getter(self, valor):
        if valor in self.tabela.keys():
            return self.tabela[valor]
        else:
            raise('Chave invalida')
    def setter(self, chave,tipo, valor=None):
        if chave in self.tabela.keys():
            self.tabela[chave] = (valor,tipo)
        else:
            self.tabela[chave] = (valor,tipo)

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
        # print('Biop',self.value, [x.evaluate() for x in self.filhos])
        if self.value == 'minus': 
            return (self.filhos[0].evaluate()[0] - self.filhos[1].evaluate()[0], 'int')
        elif self.value == 'plus':
            return (self.filhos[0].evaluate()[0] + self.filhos[1].evaluate()[0], 'int')
        elif self.value == 'times':
            return (self.filhos[0].evaluate()[0] * self.filhos[1].evaluate()[0], 'int')
        elif self.value == 'div':
            return (self.filhos[0].evaluate()[0] // self.filhos[1].evaluate()[0], 'int')
        elif self.value == 'and':
            return (self.filhos[0].evaluate()[0] and self.filhos[1].evaluate()[0],'int')
        elif self.value == 'or':
            return (self.filhos[0].evaluate()[0] or self.filhos[1].evaluate()[0],'int')
        elif self.value == 'comp':
            return (self.filhos[0].evaluate()[0] == self.filhos[1].evaluate()[0],'int')
        elif self.value == 'menor':
            return (self.filhos[0].evaluate()[0] < self.filhos[1].evaluate()[0],'int')
        elif self.value == 'maior':
            return (self.filhos[0].evaluate()[0] > self.filhos[1].evaluate()[0],'int')
        elif self.value == 'concat':
            return (str(self.filhos[0].evaluate()[0]) + str(self.filhos[1].evaluate()[0]),'string')
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

class Stringvar(Node):
    def evaluate(self):
        #print('Stringvar',self.value, [type(x)for x in self.filhos])
        return str(self.value)

class NoOp(Node):
    def evaluate(self):
        pass

class Println(Node):
    #valor = nada
    #filho= parseexpression 
    def evaluate(self):
        print (self.filhos[0].evaluate()[0])

class Identifier(Node): 
    # value=nome da variavel
    # 0 filhos
    def evaluate(self):
        #print('ident-getter',self.value, [type(x)for x in self.filhos])
        return tabela.getter(self.value)
class Assigment(Node):
    #2 filhos:
    #esquerda= Identifier pra criar
    #direita= expression do valor
    def evaluate(self):
        if len(self.filhos) == 2:
            if len(self.filhos[0].value)==2:
                tabela.setter(self.filhos[0].value[0],self.filhos[0].value[1],self.filhos[1].evaluate())
            else:
                tabela.setter(self.filhos[0].value[0],tabela.getter(self.filhos[0].value[0])[1]  ,self.filhos[1].evaluate())
        else:
            tabela.setter(self.filhos[0].value[0],self.filhos[0].value[1])

class Block(Node):
    #criado na funcao raiz BLOCK
    #um filho pra cada linha => append de filho
    def evaluate(self):
        for filho in self.filhos:
            filho.evaluate()

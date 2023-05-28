class SymbolClass:

    def __init__(self):
        ## private varibale or property in Python
        self.tabela={}
    def verifica(self, valor):
        return valor in self.tabela.keys()

    def getter(self, valor):
        if valor in self.tabela.keys():
            return self.tabela[valor]
        else:
            # print(self.tabela, valor)
            raise('Chave invalida',valor)
        
    def setter(self, chave,tipo, valor=None):
        if chave in self.tabela.keys():
            self.tabela[chave] = (valor,tipo)
        else:
            self.tabela[chave] = (valor,tipo)

class Token:
    def __init__(self,v,t):
        self.type = t
        self.value=v
class Node:
    def __init__(self,v,filhos):
        # print('Node',type(self))
        self.value = v
        self.filhos: [Node]= filhos




class Readln(Node):
    def evaluate(self):
         return (int(input()),'Int')

class UnOp(Node):
    def evaluate(self, symbol):
        #print('Unop',self.value, [type(x)for x in self.filhos])
        if self.value == 'minus': 
            return (-self.filhos[0].evaluate(symbol), 'Int')
        elif self.value == 'plus':
            return (self.filhos[0].evaluate(symbol), 'Int')
        elif self.value == 'not':
            return (int(not self.filhos[0].evaluate(symbol)), 'Int')

class Binop(Node):
    def evaluate(self,symbol):
        # print('Biop',self.value, [x.evaluate() for x in self.filhos])
        if (self.filhos[0].evaluate(symbol)[1] != self.filhos[1].evaluate(symbol)[1]) and (self.value in ['plus','minus','times','div']):
            raise Exception('Tipos diferentes1')
        if self.value == 'minus': 
            return (self.filhos[0].evaluate(symbol)[0] - self.filhos[1].evaluate(symbol)[0], 'Int')
        elif self.value == 'plus':
            return (self.filhos[0].evaluate(symbol)[0] + self.filhos[1].evaluate(symbol)[0], 'Int')
        elif self.value == 'times':
            return (self.filhos[0].evaluate(symbol)[0] * self.filhos[1].evaluate(symbol)[0], 'Int')
        elif self.value == 'div':
            return (self.filhos[0].evaluate(symbol)[0] // self.filhos[1].evaluate(symbol)[0], 'Int')
        elif self.value == 'and':
            return (int(self.filhos[0].evaluate(symbol)[0] and self.filhos[1].evaluate(symbol)[0]),'Int')
        elif self.value == 'or':
            return (int(self.filhos[0].evaluate(symbol)[0] or self.filhos[1].evaluate(symbol)[0]),'Int')
        elif self.value == 'comp':
            return (int(self.filhos[0].evaluate(symbol)[0] == self.filhos[1].evaluate(symbol)[0]),'Int')
        elif self.value == 'menor':
            return (int(self.filhos[0].evaluate(symbol)[0] < self.filhos[1].evaluate(symbol)[0]),'Int')
        elif self.value == 'maior':
            return (int(self.filhos[0].evaluate(symbol)[0] > self.filhos[1].evaluate(symbol)[0]),'Int')
        elif self.value == 'concat':
            return (str(self.filhos[0].evaluate(symbol)[0]) + str(self.filhos[1].evaluate(symbol)[0]),'String')

class IfOp(Node):
    def evaluate(self,symbol):
        #print('If',self.value, [type(x)for x in self.filhos])
        if self.filhos[0].evaluate(symbol):
            self.filhos[1].evaluate(symbol)
        elif len(self.filhos) == 3:
            self.filhos[2].evaluate(symbol)
class WhileOp(Node):
    def evaluate(self,symbol):
        # print('While',self.value, [x.value for x in self.filhos])
        while self.filhos[0].evaluate(symbol)[0]:
            self.filhos[1].evaluate(symbol)
            
            
class Intvar(Node):
    def evaluate(self,symbol):
        #print('Intvar',self.value, [type(x)for x in self.filhos])
        return (int(self.value),'Int')

class Stringvar(Node):
    def evaluate(self,symbol):
        #print('Stringvar',self.value, [type(x)for x in self.filhos])
        return (str(self.value),'String')

class NoOp(Node):
    def evaluate(self,symbol):
        pass

class Println(Node):
    #valor = nada
    #filho= parseexpression 
    def evaluate(self,symbol):
        print (self.filhos[0].evaluate(symbol)[0])

class Identifier(Node): 
    # value=nome da variavel
    # 0 filhos
    def evaluate(self,symbol):
        #print('ident-getter',self.value, [type(x)for x in self.filhos])
        return symbol.getter(self.value)
    
class Assigment(Node):
    #2 filhos:
    #esquerda= Identifier pra criar
    #direita= expression do valor
    def evaluate(self,symbol):
        # print('assigment',self.value, [x.evaluate() for x in self.filhos])
        # print('assigment',self.value, [type(x) for x in self.filhos])
        if type(self.filhos[0])==Identifier:
            chave = self.filhos[0].value
        elif type(self.filhos[0])==Createvar:
            chave = self.filhos[0].evaluate(symbol)[0]
        resul = self.filhos[1].evaluate(symbol)
        if resul[1] != symbol.getter(chave)[1]:
            print(resul[1],symbol.getter(chave)[1])
            raise Exception('Tipos diferentes2')

        symbol.setter(chave=chave,tipo=resul[1],valor=resul[0])

class Createvar(Node):
    def evaluate(self,symbol):
        #print('createvar',self.value, [type(x)for x in self.filhos])
        #valor = tipo
        #filho = identifier
        if not symbol.verifica(self.filhos[0].value):
            symbol.setter(chave = self.filhos[0].value,tipo = self.value)
            return (self.filhos[0].value,self.value)
        else:
            raise Exception('Variavel ja declarada',self.filhos[0].value)
    

class Block(Node):
    #criado na funcao raiz BLOCK
    #um filho pra cada linha => append de filho
    def evaluate(self,symbol):
        for filho in self.filhos:
            if type(filho) == ReturnOp:
                return filho.evaluate(symbol)
            filho.evaluate(symbol)

functable ={}
class FuncDec(Node):
    def evaluate(self,symbol):
        # tipo = self.value
        nome = self.filhos[0].value
        functable[nome] = self


class FuncCall(Node):
    def evaluate(self,symbol):
        funcao = functable[self.value]
        tabela = SymbolClass()
        for recebido, passado  in zip(funcao.filhos[1:-1],self.filhos):
            if type(passado)== Identifier:
                tabela.setter(chave=recebido.filhos[0].value,tipo=symbol.getter(passado.value)[1],valor=symbol.getter(passado.value)[0])
            else:
                tabela.setter(chave=recebido.filhos[0].value,tipo=passado.evaluate(symbol)[1],valor=passado.evaluate(symbol)[0])

        # print("tabela",tabela.tabela)
        return funcao.filhos[-1].evaluate(tabela)
        

class ReturnOp(Node):
    def evaluate(self,symbol):
        return self.filhos[0].evaluate(symbol)
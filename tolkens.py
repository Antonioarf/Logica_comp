class SymbolClass:

    def __init__(self):
        ## private varibale or property in Python
        self.tabela={}
        self.contador = 1
    def verifica(self, valor):
        return valor in self.tabela.keys()

    def getter(self, valor):
        if valor in self.tabela.keys():
            return self.tabela[valor]
        else:
            # print(self.tabela, valor)
            raise('Chave invalida')
    def setter(self, chave,tipo, valor=None): #agora só pra itens novos
            self.tabela[chave] = ((self.contador)*4,tipo)
            self.contador += 1

class Assembler:
    def __init__(self):
        self.code = []
    def get_header(self):
        with open('header.asm','r') as f:
            return f.read()
    def get_footer(self):
        with open('footer.asm','r') as f:
            return f.read()
        
    def add(self,code):
        self.code.append(code)

    def write(self,nome):
        self.nome = nome.split('.')[0] + '.asm'
        with open(self.nome,'w') as f:
            f.write(self.get_header())
            for line in self.code:
                f.write(line+'\n')   
            f.write(self.get_footer())   
                  

tabela = SymbolClass()
assembler = Assembler()
class Token:
    def __init__(self,v,t):
        #print('criou',v,t)
        self.type = t
        self.value=v
class Node:
    def __init__(self,v,filhos):
        # print('criou',v, [type(x)for x in filhos])
        self.value = v
        self.filhos: [Node]= filhos
#==============================================================================

class NoOp(Node):
    def evaluate(self, id):
        pass

class Readln(Node):
    def evaluate(self):
         return (int(input()),'Int')
    
class Println(Node):
    #valor = nada
    #filho= parseexpression 
    def evaluate(self, id):
        print('print',id)
        # print (self.filhos[0].evaluate(id+1)[0])
        self.filhos[0].evaluate(id+1)
        assembler.add(f"push ebx ;{id}")
        assembler.add(f"CALL print ;{id}")
        assembler.add(f"pop ebx ;{id}")
#==============================================================================
class Block(Node):
    #criado na funcao raiz BLOCK
    #um filho pra cada linha => append de filho
    def evaluate(self, id):
        print("block" , id)
        atual = id+100
        for filho in self.filhos:
            filho.evaluate(atual)
            atual += 1
#==============================================================================
class IfOp(Node):
    def evaluate(self, id):
        print('if',id)
        #print('If',self.value, [type(x)for x in self.filhos])
        self.filhos[0].evaluate(id+1)
        assembler.add('cmp ebx, 1 ; COMP IF')
        assembler.add('je endIF{}'.format(id))
        if len(self.filhos) == 3:
            self.filhos[2].evaluate(id+2)
        assembler.add('jmp endBloco{}'.format(id))    
        assembler.add('endIF{}:'.format(id))
        self.filhos[1].evaluate(id+1)
        assembler.add('endBloco{}:'.format(id))

class WhileOp(Node):
    def evaluate(self, id):
        print('while',id)
        # print('While',self.value, [x.value for x in self.filhos])
        # while self.filhos[0].evaluate(id+1)[0]:
        #     self.filhos[1].evaluate(id+1)
        assembler.add('while{}:'.format(id))
        self.filhos[0].evaluate(id+1)
        assembler.add('cmp ebx, 0 ; COMP WHILE')
        assembler.add('je endwhile{}'.format(id))
        self.filhos[1].evaluate(id+2)
        assembler.add('jmp while{}'.format(id))
        assembler.add('endwhile{}:'.format(id))
#==============================================================================
class Intvar(Node):
    def evaluate(self, id):
        print('intvar',id)
        # print(f'Intvar{id}',self.value, [type(x)for x in self.filhos])
        #return (int(self.value),'Int')
        assembler.add('mov ebx, {} ; {}'.format(self.value,id))

class Stringvar(Node):
    def evaluate(self, id):
        #print('Stringvar',self.value, [type(x)for x in self.filhos])
        return (str(self.value),'String')

#==============================================================================
class UnOp(Node):
    def evaluate(self, id):
        #print('Unop',self.value, [type(x)for x in self.filhos])
        if self.value == 'minus': 
            return (-self.filhos[0].evaluate(id+1), 'Int')
        elif self.value == 'plus':
            return (self.filhos[0].evaluate(id+1), 'Int')
        elif self.value == 'not':
            return (int(not self.filhos[0].evaluate(id+1)), 'Int')

class Binop(Node):
    def evaluate(self, id):
        print("biop",id)
        # print('Biop',self.value, [x.evaluate(id+1) for x in self.filhos])
        self.filhos[0].evaluate(id+1)
        assembler.add(f'push ebx ;{id}')
        self.filhos[1].evaluate(id+2)
        assembler.add(f'pop eax ;{id}')
        if self.value == 'minus': 
            assembler.add(f'sub eax, ebx ;{id}')
            assembler.add(f'mov ebx, eax ;{id}')
        elif self.value == 'plus':
            assembler.add(f'add eax, ebx ;{id}')
            assembler.add(f'mov ebx, eax ;{id}')
        elif self.value == 'times':
            assembler.add(f'mov al, eax ;{id}')
            assembler.add(f'imul ebx ;{id}')
        elif self.value == 'div':
            assembler.add(f'div eax, ebx ;{id}')
            assembler.add(f'mov ebx, eax ;{id}')
        elif self.value == 'and':
            assembler.add(f'and eax, ebx ;{id}')
            assembler.add(f'mov ebx, eax ;{id}')
        elif self.value == 'or':
            assembler.add(f'or eax, ebx ;{id}')
            assembler.add(f'mov ebx, eax ;{id}')
        elif self.value == 'comp':
            assembler.add(f'cmp eax, ebx ;{id}')
            assembler.add(f'call binop_je ;{id}')
        elif self.value == 'menor':
            assembler.add(f'cmp eax, ebx ;{id}')
            assembler.add(f'call binop_jl ;{id}')
        elif self.value == 'maior':
            assembler.add(f'cmp eax, ebx ;{id}')
            assembler.add(f'call binop_jg ;{id}')
        # elif self.value == 'concat':
        #     return (str(self.filhos[0].evaluate(id+1)[0]) + str(self.filhos[1].evaluate(id+1)[0]),'String')


#==============================================================================         




class Identifier(Node): 
    # value=nome da variavel
    # 0 filhos
    def evaluate(self, id):
        print("identifier",id)
        # print('ident-getter',self.value, [type(x)for x in self.filhos])
        # return tabela.getter(self.value)
        valor = tabela.getter(self.value)[0]
        assembler.add('mov ebx,  [ebp- {}] ; {}'.format(valor,id))
    
class Assigment(Node):
    #2 filhos:
    #esquerda= Identifier pra criar
    #direita= expression do valor
    def evaluate(self, id):
        print("assin",id)
        # print('assigment',self.value, [x.evaluate(id+1) for x in self.filhos])
        print(f'assigment{id}',self.value, [type(x) for x in self.filhos])
        if type(self.filhos[0])== Createvar:
            self.filhos[0].evaluate(id+1)
            chave = tabela.getter(self.filhos[0].filhos[0].value)[0]
        else:
            chave = tabela.getter(self.filhos[0].value)[0]
        self.filhos[1].evaluate(id+1)
        assembler.add('mov [ebp- {}], ebx'.format(chave))

class Createvar(Node):
    def evaluate(self, id):
        print("creare",id)
        print('createvar',self.value, [type(x)for x in self.filhos])
        #valor = tipo
        #filho = identifier
        if not tabela.verifica(self.filhos[0].value):
            assembler.add('PUSH DWORD 0')
            tabela.setter(chave = self.filhos[0].value,tipo = self.value)
        else:
            raise Exception('Variavel ja declarada')
    



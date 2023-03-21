from Tolkenizer import *
# PARSE BLOCK => while not EOF roda o STATMEMNT
# PARSE STATMEMNT if entre print, atribuicao e nada
class Parser:
    tolk = Tolkenizer()
    abriu = False
    def filtra(linha:str):
        return linha.split('#')[0].strip()

    def leitura(nome:str):
        with open(nome) as f:
            contents = f.read()
        #print(contents)
        #print('--------------------------------------')
        return contents

    def parseBlock():
        filhos = []
        Parser.tolk.selectNext()
        while Parser.tolk.next.type != 'EOF':
            filhos.append(Parser.parseStatment())
            Parser.tolk.selectNext()
        return Block('',filhos)
        
    def parseStatment():
        if Parser.tolk.next.type == 'var':
            valor = Parser.tolk.next.value
            Parser.tolk.selectNext()
            if Parser.tolk.next.type == 'igual':
                Parser.tolk.selectNext()
                filho = Parser.parseExepresion()
                return Assigment('',[Identifier(valor,[]),filho])
            else:
                raise ('VAR SEM IGUAL DEPOIS')
        elif Parser.tolk.next.type == 'print':
            Parser.tolk.selectNext()
            filho = Parser.parseFactor()
            Parser.tolk.selectNext()
            return Println('',[filho])

    def parseExepresion():
        filho1 = Parser.parseTerm()
        while True:   
            
            if (Parser.tolk.next.type == 'plus') or (Parser.tolk.next.type == 'minus'):
                tipo = Parser.tolk.next.type
                Parser.tolk.selectNext() 
                filho2 =Parser.parseTerm()
                atual  =Binop (tipo,[filho1,filho2])

            elif (Parser.tolk.next.type in ['EOF','break']) or ((Parser.tolk.next.type == 'C_par')and(Parser.abriu)):
                atual=filho1
                break     
            else:
                    raise Exception(Parser.tolk.next.type,Parser.tolk.next.value)
            filho1 = atual
        return atual

    def parseTerm():
        filho1 = Parser.parseFactor()
        while True:
            Parser.tolk.selectNext()
            if (Parser.tolk.next.type == 'div') or (Parser.tolk.next.type == 'times'):
                tipo = Parser.tolk.next.type
                Parser.tolk.selectNext() 
                filho2 =Parser.parseFactor()
                atual  =Binop (tipo,[filho1,filho2])    
            else:
                atual = filho1
                break
            filho1 = atual
        return atual

    def parseFactor():

        if Parser.tolk.next.type == 'int':
            return Intvar(int(Parser.tolk.next.value),[])
        elif Parser.tolk.next.type == 'var':
            return Identifier(Parser.tolk.next.value,[])

        elif (Parser.tolk.next.type == 'minus') or (Parser.tolk.next.type == 'plus'):
            tipo = Parser.tolk.next.type
            Parser.tolk.selectNext()
            return UnOp(tipo, [Parser.parseFactor()])
        elif  Parser.tolk.next.type == 'O_par':
                Parser.abriu =True
                Parser.tolk.selectNext()
                salva = Parser.parseExepresion()
                if (Parser.tolk.next.type == 'C_par'):
                    return salva
                else:
                    raise Exception("s",Parser.tolk.next.type,Parser.tolk.next.value)


            
        

        
    def run(self, s):
        ss = Parser.leitura(s)
        l = Parser.filtra(ss)
        Parser.tolk.cria(l)
        return Parser.parseBlock()

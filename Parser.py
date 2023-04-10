from Tolkenizer import *
import re

class Parser:
    tolk = Tolkenizer()
    abriu = False
    def filtra(linha:str):
        return linha.split('#')[0].strip()

    def leitura(nome:str):
        with open(nome) as f:
            contents=''
            for line in f:
                contents += Parser.filtra(line)+'\n'

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
                filho = Parser.parseRelExpr()
                return Assigment('',[Identifier(valor,[]),filho])
            else:
                raise ('VAR SEM IGUAL DEPOIS')
        elif Parser.tolk.next.type == 'print':
            Parser.tolk.selectNext()
            filho = Parser.parseFactor()
            Parser.tolk.selectNext()
            return Println('',[filho])
        
        elif Parser.tolk.next.type == 'if':
            Parser.tolk.selectNext()
            condicao = Parser.parseRelExpr()
            print(condicao.filhos, condicao.value)
            Parser.tolk.selectNext()
            filhos = []
            while (Parser.tolk.next.type != 'end' )or (Parser.tolk.next.type != 'else'):
                filhos.append(Parser.parseStatment())
                Parser.tolk.selectNext()
            filho1= Block('',filhos)
            if Parser.tolk.next.type == 'else':
                Parser.tolk.selectNext()
                filhos = []
                while Parser.tolk.next.type != 'end':
                    print('2222222222222222')
                    filhos.append(Parser.parseStatment())
                    Parser.tolk.selectNext()
                filho2= Block('',filhos)
                return IfOp('',[condicao,filho1,filho2])
            else:
                return IfOp('',[condicao,filho1])
        elif Parser.tolk.next.type == 'while':
            Parser.tolk.selectNext()
            condicao = Parser.parseRelExpr()
            Parser.tolk.selectNext()
            filhos = []
            while Parser.tolk.next.type != 'end':
                print('333333333333333333')
                filhos.append(Parser.parseStatment())
                Parser.tolk.selectNext()
            filho1= Block('',filhos)
            return WhileOp('',[condicao,filho1])    
        
        elif Parser.tolk.next.type == 'break':
            return NoOp('',[])
    
    
    def parseRelExpr():
        filho1 = Parser.parseExepresion()
        while True:   
            
            if (Parser.tolk.next.type == 'comp') or (Parser.tolk.next.type == 'maior') or (Parser.tolk.next.type == 'menor'):
                tipo = Parser.tolk.next.type
                Parser.tolk.selectNext() 
                filho2 =Parser.parseExepresion()
                atual  =Binop (tipo,[filho1,filho2])

            elif (Parser.tolk.next.type in ['EOF','break','end']) or ((Parser.tolk.next.type == 'C_par')and(Parser.abriu)):
                atual=filho1
                break     
            else:
                    raise Exception(Parser.tolk.next.type,Parser.tolk.next.value)
            filho1 = atual
        return atual
        
    def parseExepresion():
        filho1 = Parser.parseTerm()
        while True:   
            if (Parser.tolk.next.type == 'plus') or (Parser.tolk.next.type == 'minus') or (Parser.tolk.next.type == 'or'):
                tipo = Parser.tolk.next.type
                Parser.tolk.selectNext() 
                filho2 =Parser.parseTerm()
                atual  =Binop (tipo,[filho1,filho2])

            else:
                atual = filho1
                break
            filho1 = atual
            filho1 = atual
        return atual

    def parseTerm():
        filho1 = Parser.parseFactor()
        while True:
            Parser.tolk.selectNext()
            if (Parser.tolk.next.type == 'div') or (Parser.tolk.next.type == 'times') or (Parser.tolk.next.type == 'and'):
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

        elif (Parser.tolk.next.type == 'minus') or (Parser.tolk.next.type == 'plus') or (Parser.tolk.next.type == 'not'):
            tipo = Parser.tolk.next.type
            Parser.tolk.selectNext()
            return UnOp(tipo, [Parser.parseFactor()])
        elif Parser.tolk.next.type == 'read':
            Parser.tolk.selectNext()
            if  Parser.tolk.next.type == 'O_par':
                Parser.tolk.selectNext()
                if (Parser.tolk.next.type == 'C_par'):
                    return Readln('',[])
                else:
                    raise Exception("s",Parser.tolk.next.type,Parser.tolk.next.value)
        elif  Parser.tolk.next.type == 'O_par':
                Parser.abriu =True
                Parser.tolk.selectNext()
                salva = Parser.parseRelExpr()
                if (Parser.tolk.next.type == 'C_par'):
                    return salva
                else:
                    raise Exception("s",Parser.tolk.next.type,Parser.tolk.next.value)


            
        
    def run(self, s):
        ss = Parser.leitura(s)
        l = Parser.filtra(ss)
        Parser.tolk.cria(l)
        return Parser.parseBlock()

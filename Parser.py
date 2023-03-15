from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    tipo_atual = "plus"
    abriu = False
    def filtra(linha:str):
        return linha.split('#')[0].strip()

    def leitura(nome:str):
        with open(nome) as f:
            contents = f.read()
        return contents


    def parseExepresion():
        filho1 = Parser.parseTerm()
        #print('filho1', type(filho1))
        ##print(filho1)
        while True:   
            
            if Parser.tolk.next.type == 'plus':
                Parser.tolk.selectNext() 
                filho2 =Parser.parseTerm()
                atual  =Binop('plus',[filho1,filho2])

            elif Parser.tolk.next.type == 'minus':
                Parser.tolk.selectNext() 
                filho2 =Parser.parseTerm()
                atual  =Binop('minus',[filho1,filho2])
            elif (Parser.tolk.next.type == 'EOF'):
                atual=filho1
                break
            elif (Parser.tolk.next.type == 'C_par'):
                if Parser.abriu:
                    atual=filho1
                    return atual
            elif  Parser.tolk.next.type == 'O_par':
                Parser.abriu =True
                salva = Parser.parseExepresion()
                if (Parser.tolk.next.type == 'C_par')or (Parser.tolk.next.type == 'EOF'):
                    Parser.tolk.selectNext()
                    return salva
            else:
                    raise Exception("sla T2",Parser.tolk.next.type,Parser.tolk.next.value)

            
            filho1 = atual
        return atual

    def parseTerm():
        
        filho1 = Parser.parseFactor()
        #print('filho2', type(filho1))
        while True:
            Parser.tolk.selectNext()
            if Parser.tolk.next.type == 'times':
                Parser.tolk.selectNext() 
                filho2 =Parser.parseFactor()
                atual  =Binop('times',[filho1,filho2])
            elif Parser.tolk.next.type == 'div': 
                Parser.tolk.selectNext() 
                filho2 =Parser.parseFactor()
                atual  =Binop('div',[filho1,filho2])
            #elif Parser.tolk.next.type  in  ["EOF",'plus', 'minus','C_par']:
            elif (Parser.tolk.next.type == 'C_par'):
                if Parser.abriu:
                    atual=filho1
                    return atual
                else:
                    raise Exception("sla T2")
            else:
                atual = filho1
                break
            Parser.tipo_atual = Parser.tolk.next.type
            filho1 = atual
        return atual

    def parseFactor():

        if Parser.tolk.next.type == 'int':
            Parser.tipo_atual= 'int'
            return Intvar(int(Parser.tolk.next.value),[])

        elif Parser.tolk.next.type == 'minus':
            Parser.tolk.selectNext()
            return UnOp("minus", [Parser.parseFactor()])
        elif Parser.tolk.next.type == 'plus':
            Parser.tolk.selectNext()
            return UnOp("plus", [Parser.parseFactor()])
        elif  Parser.tolk.next.type == 'O_par':
                Parser.abriu =True
                
                Parser.tolk.selectNext()
                salva = Parser.parseExepresion()
                if (Parser.tolk.next.type == 'C_par'):
                    return salva
                else:
                    raise Exception("s",Parser.tolk.next.type,Parser.tolk.next.value)
        elif  Parser.tolk.next.type == 'EOF':
            return

        else:
            raise Exception("SLA2",Parser.tolk.next.type,Parser.tolk.next.value)

            
        

        
    def run(self, s):
        ss = Parser.leitura(s)
        l = Parser.filtra(ss)
        Parser.tolk.cria(l)
        return Parser.parseExepresion()

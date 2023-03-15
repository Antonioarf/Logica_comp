from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    abriu = False
    def filtra(linha:str):
        return linha.split('#')[0].strip()

#parenteses
#leitura de arquivo
    def parseExepresion():
            filho1 = Parser.parseTerm()
        
            if Parser.tolk.next.type == 'plus':
                valor_ex = 'plus'
                Parser.tolk.selectNext()
                filho2 =  Parser.parseTerm()
            elif Parser.tolk.next.type == 'minus':
                Parser.tolk.selectNext()
                valor_ex = 'minus'
                filho2 = Parser.parseTerm()
            elif (Parser.tolk.next.type == 'EOF'):
                return Binop('plus',[filho1,Intvar(0,[])])
            elif (Parser.tolk.next.type == 'C_par'):
                if not Parser.abriu:
                    raise Exception("NAO ABRIU") 
            else:
                    raise Exception("SLA",Parser.tolk.next.type,Parser.tolk.next.value)
            return Binop(valor_ex,[filho1,filho2])

    def parseTerm():       
            filho1 = Parser.parseFactor()            
            if Parser.tolk.next.type == 'times':
                Parser.tolk.selectNext()
                valor_term = 'times'
                filho2 =  Parser.parseFactor()
            elif Parser.tolk.next.type == 'div':
                Parser.tolk.selectNext()
                valor_term = 'div'
                filho2= Parser.parseFactor()
            elif Parser.tolk.next.type =="EOF":
                return filho1
            elif (Parser.tolk.next.type in ['plus', 'minus']):
                return Binop(Parser.tolk.next.type,[filho1,Parser.parseExepresion()])
            elif (Parser.tolk.next.type == 'C_par'):
                if not Parser.abriu:
                    raise Exception("NAO ABRIU") 
            else:
                raise Exception("SLA2",Parser.tolk.next.type,Parser.tolk.next.value) 
            




    def parseFactor():
        
        if Parser.tolk.next.type == 'int':
            s = int(Parser.tolk.next.value)
            Parser.tolk.selectNext()
            return Intvar(s,[])

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
                # Parser.tolk.selectNext()
                if Parser.tolk.next.type == 'C_par':
                    Parser.tolk.selectNext()
                    return salva
                else:
                    raise Exception("NAO FECHOU") 
        else:
                raise Exception("SLA3",Parser.tolk.next.type,Parser.tolk.next.value)

    def run(self, s):
        s = Parser.filtra(s)
        Parser.tolk.cria(s)
        return Parser.parseExepresion()


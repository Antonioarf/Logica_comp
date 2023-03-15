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
            print(contents)
            return contents


    def parseExepresion():
        filho1 = Parser.parseTerm()
        while True:   
            
            if Parser.tolk.next.type == 'plus':
                filho2 =Parser.parseTerm()
                atual  =Binop('plus',[filho1,filho2])

            elif Parser.tolk.next.type == 'minus':
                filho2 =Parser.parseTerm()
                atual  =Binop('minus',[filho1,filho2])
            elif (Parser.tolk.next.type == 'EOF'):
                atual=filho1
                break
            elif (Parser.tolk.next.type == 'C_par'):
                if Parser.abriu:
                    atual=filho1
                    break
                else:
                    raise Exception("sla T2") 
            
            filho1 = atual
        return atual

    def parseTerm():
        Parser.tolk.selectNext()
        filho1 = Parser.parseFactor()
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
            elif Parser.tolk.next.type  in  ["EOF",'plus', 'minus','C_par']:
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
                salva = Parser.parseExepresion()
                if Parser.tolk.next.type == 'C_par':
                    Parser.tolk.selectNext()
                    return salva
                else:
                    raise Exception("sla") 
        else:
            raise Exception("SLA2",Parser.tolk.next.type,Parser.tolk.next.value)

            
        

        
    def run(self, s):
        s = Parser.filtra(s)
        Parser.tolk.cria(s)
        return Parser.parseExepresion()


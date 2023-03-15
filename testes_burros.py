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
        while True:          
            if (Parser.tolk.next.type == 'plus') or (Parser.tolk.next.type == 'minus'):
                tipo = Parser.tolk.next.type
                Parser.tolk.selectNext() 
                filho2 =Parser.parseTerm()
                atual  =Binop (tipo,[filho1,filho2])
   
            elif (Parser.tolk.next.type == 'EOF') or (Parser.tolk.next.type == 'C_par'):
                atual=filho1
                break
            filho1 = atual
        return atual

    def parseTerm():
        
        filho1 = Parser.parseFactor()
        while True:
            Parser.tolk.selectNext()
            if (Parser.tolk.next.type == 'div') or (Parser.tolk.next.type == 'times'):
                tipo = Parser.tolk.next.type
                Parser.tolk.selectNext() 
                filho2 =Parser.parseTerm()
                atual  =Binop (tipo,[filho1,filho2])        
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
        else:
            raise Exception("SLA2",Parser.tolk.next.type,Parser.tolk.next.value)

            
        

        
    def run(self, s):
        ss = Parser.leitura(s)
        l = Parser.filtra(ss)
        Parser.tolk.cria(l)
        return Parser.parseExepresion()

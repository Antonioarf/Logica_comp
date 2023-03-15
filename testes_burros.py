from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    tipo_atual = "plus"
    abriu = False
    def filtra(linha:str):
        return linha.split('#')[0].strip()


    def parseExepresion():
        filho1 = Parser.parseTerm()
        print("filho_exp",filho1.value)
        while True:            
            print('1')
            if Parser.tolk.next.type == 'plus':
                valor = 'plus'
                filho2 = Parser.parseTerm()
            elif Parser.tolk.next.type == 'minus':
                valor = 'minus'
                filho2 = Parser.parseTerm()
            elif (Parser.tolk.next.type == 'EOF'):
                break
            elif (Parser.tolk.next.type == 'C_par'):
                if Parser.abriu:
                    break
            else:
                raise Exception("NAO ABRIU") 
        return Binop(valor,[filho1,filho2])

    def parseTerm():
        filho1 = Parser.parseFactor()
        print("filho_term",filho1.value)
        while True:            
            if Parser.tolk.next.type == 'times':
                valor = 'times'
                filho2 = Parser.parseFactor()
            elif Parser.tolk.next.type == 'div':
                valor = 'div'
                filho2 = Parser.parseFactor()
            elif (Parser.tolk.next.type in  ["EOF",'plus', 'minus']):
                break
            elif (Parser.tolk.next.type == 'C_par'):
                if Parser.abriu:
                    break
                else:
                    raise Exception("NAO ABRIU") 
        return Binop(valor,[filho1,filho2])

    def parseFactor():
        print('@!!!!!!!')
        if Parser.tolk.next.type == 'int':
            print('1')
            Parser.tipo_atual= 'int'
            return Intvar(Parser.tolk.next.value,[])
        elif Parser.tolk.next.type == 'minus':
            print('2')
            Parser.tolk.selectNext()
            return UnOp("minus", [Parser.parseFactor()])
        elif Parser.tolk.next.type == 'plus':
            print('3')
            Parser.tolk.selectNext()
            return UnOp("plus", [Parser.parseFactor()])
        #FAZER PARENTESES - NAO ENTENDI O PULO
        elif  Parser.tolk.next.type == 'O_par':
                Parser.abriu =True
                salva = Parser.parseExepresion()
                if Parser.tolk.next.type == 'C_par':
                    Parser.tolk.selectNext()
                    return salva
                else:
                    raise Exception("NAO FECHOU") 
        else:
            raise Exception("Tipo errado aqui embaixo") 

    def run(self, s):
        s = Parser.filtra(s)
        Parser.tolk.cria(s)
        return Parser.parseExepresion()

    def fodase():
        prod = 1
        Parser.tipo_atual= 'times'
        while Parser.tipo_atual not in  ["EOF",'plus', 'minus','C_par']:

            Parser.tolk.selectNext()
            if Parser.tolk.next.type == Parser.tipo_atual:
                raise Exception("Tipo repetido!!!!: {}".format(Parser.tipo_atual))


            if Parser.tipo_atual == 'times':
                prod *= Parser.parseFactor() 
            elif Parser.tipo_atual == 'div': 
                prod //= Parser.parseFactor()
                
            Parser.tipo_atual = Parser.tolk.next.type
        return prod
from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    tipo_atual = "plus"
    def filtra(linha:str):
        return linha.split('#')[0]


    def parseExepresion():
        soma = 0
        while Parser.tipo_atual != "EOF":
            Parser.tolk.selectNext()
            if Parser.tolk.next.type == Parser.tipo_atual:
                raise Exception("Tipo repetido")
            else:
                if Parser.tipo_atual == "EOF":
                    break

            if Parser.tipo_atual == 'plus':
                soma += int(Parser.parseTerm())
            elif Parser.tipo_atual == 'minus': 
                soma -= int(Parser.parseTerm())

            Parser.tipo_atual = Parser.tolk.next.type

            print("SOMA:", soma, '!!!!')
        return soma


    def parseTerm():
        soma = 1
        Parser.tipo_atual= 'times'
        print('-----------')
        print(Parser.tipo_atual)
        print(Parser.tolk.next.type)
        print('-----------')
        print('-----------')
        print('-----------')

        while Parser.tipo_atual not in  ["EOF",'plus', 'minus']:
            print('-----------')
            print(Parser.tolk.next.value)
            print(Parser.tolk.next.type)
            print('-----------')
            
            if Parser.tolk.next.type == Parser.tipo_atual:
                raise Exception("Tipo repetido")
            else:
                if Parser.tipo_atual == "EOF":
                    break

            if Parser.tipo_atual == 'times':
                soma *= int(Parser.tolk.next.value)
            elif Parser.tipo_atual == 'div': 
                soma /= int(Parser.tolk.next.value)

            Parser.tipo_atual = Parser.tolk.next.type

            print("SOMA:", soma, '@@@@')
            Parser.tolk.selectNext()
        return soma

    
        
    def run(self, s):
        s = Parser.filtra(s)
        Parser.tolk.cria(s)
        return Parser.parseExepresion()


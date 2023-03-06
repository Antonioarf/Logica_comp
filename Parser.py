from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    tipo_atual = "plus"
    def filtra(linha:str):
        return linha.split('#')[0]


    def parseExepresion():
        soma = Parser.parseTerm()
        #print('soma:@@@@',soma)
        while True:
            #print('@@@@@@@@@@@@')
            
            if Parser.tolk.next.type == 'plus':
                soma +=  Parser.parseTerm()
            elif Parser.tolk.next.type == 'minus':
                soma -=  Parser.parseTerm()
            elif Parser.tolk.next.type == 'EOF':
                break
        return soma

    def parseTerm():
        soma = 1
        Parser.tipo_atual= 'times'

        while Parser.tipo_atual not in  ["EOF",'plus', 'minus']:
            Parser.tolk.selectNext()
            # print('----------')
            # print("teste",Parser.tipo_atual)
            # print('t2',Parser.tolk.next.type )
            if Parser.tolk.next.type == Parser.tipo_atual:
                raise Exception("Tipo repetido!!!!: {}".format(Parser.tipo_atual))


            if Parser.tipo_atual == 'times':
                soma *= int(Parser.tolk.next.value)
            elif Parser.tipo_atual == 'div': 
                soma /= int(Parser.tolk.next.value)
                
            Parser.tipo_atual = Parser.tolk.next.type

            #print('soma::',soma)
            #print(Parser.tipo_atual)
        #print('!!!!!!!!1',Parser.tolk.next.type)
        return soma

    
        
    def run(self, s):
        s = Parser.filtra(s)
        Parser.tolk.cria(s)
        return Parser.parseExepresion()


from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    tipo_atual = "plus"
    def filtra(linha:str):
        return linha.split('#')[0].strip()


    def parseExepresion():
        soma = Parser.parseTerm()
        while True:            
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
            #print(Parser.tolk.next.type, '@@@@@@@@@@@@')
            #print(soma,'soma','@@@@@@')
            #print(Parser.tolk.next.value)
            if Parser.tolk.next.type == Parser.tipo_atual:
                raise Exception("Tipo repetido!!!!: {}".format(Parser.tipo_atual))


            if Parser.tipo_atual == 'times':
                soma *= Parser.parseFactor() #passa a ser Parser.parseFactor
            elif Parser.tipo_atual == 'div': 
                soma //= Parser.parseFactor()
                
            Parser.tipo_atual = Parser.tolk.next.type

        return soma
    def parseFactor():
        #print(Parser.tolk.next.type, '!!!!!!!')
        if Parser.tolk.next.type == 'minus':
            Parser.tolk.selectNext()
            return  - Parser.parseFactor()
        if Parser.tolk.next.type == 'plus':
            Parser.tolk.selectNext()
            return + Parser.parseFactor()
        if Parser.tolk.next.type == 'int':
            #print('devolvendo',int(Parser.tolk.next.value))
            return int(Parser.tolk.next.value)


        #recursivo: if numero retorna numero
        #elif - retorna (-parseFactor)
        #elif + retorna (parseFactor)
        #fazer recursao tipo rashi e ai o ultimo elif
        #elif () chama o parseExpression return depois de tirar o ) (se n fechar da erro)
        
    def run(self, s):
        s = Parser.filtra(s)
        Parser.tolk.cria(s)
        return Parser.parseExepresion()


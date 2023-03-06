from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    tipo_atual = "plus"
    abriu = False
    def filtra(linha:str):
        return linha.split('#')[0].strip()


    def parseExepresion():
        #print('#######')
        #print(Parser.tolk.next.type )
        #print(Parser.tolk.next.value )
        #print('--------------------')
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
        #print('@@@@@@')
        #print(Parser.tolk.next.type )
        #print(Parser.tolk.next.value )
        #print('--------------------')
        prod = 1
        Parser.tipo_atual= 'times'
        while Parser.tipo_atual not in  ["EOF",'plus', 'minus']:
            Parser.tolk.selectNext()
            if Parser.tolk.next.type == Parser.tipo_atual:
                raise Exception("Tipo repetido!!!!: {}".format(Parser.tipo_atual))


            if Parser.tipo_atual == 'times':
                prod *= Parser.parseFactor() #passa a ser Parser.parseFactor
            elif Parser.tipo_atual == 'div': 
                prod //= Parser.parseFactor()
                
            Parser.tipo_atual = Parser.tolk.next.type

        return prod
    def parseFactor():
        #print('!!!!!!!!!')
        #print(Parser.tolk.next.type )
        #print(Parser.tolk.next.value )
        #print('--------------------')
        
        if Parser.tolk.next.type == 'int':
            return int(Parser.tolk.next.value)

        elif Parser.tolk.next.type == 'minus':
            Parser.tolk.selectNext()
            return  - Parser.parseFactor()
        elif Parser.tolk.next.type == 'plus':
            Parser.tolk.selectNext()
            return + Parser.parseFactor()

        elif Parser.tolk.next.type == 'O_par':
            #print('ABRIUUUUUUUUUU')
            Parser.tolk.selectNext()
            Parser.abriu = True
            salva =  Parser.parseExepresion()
            return salva
        elif Parser.tolk.next.type == 'C_par':
            #print('FECHOUUUUUUUUUUUUu')
            if Parser.abriu:
                return 1
            else:
                raise Exception("FECHOU SEM ABRIR!!!!: ")

        #recursivo: if numero retorna numero
        #elif - retorna (-parseFactor)
        #elif + retorna (parseFactor)
        #fazer recursao tipo rashi e ai o ultimo elif
        #elif () chama o parseExpression return depois de tirar o ) (se n fechar da erro)
        
    def run(self, s):
        s = Parser.filtra(s)
        Parser.tolk.cria(s)
        return Parser.parseExepresion()


from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    tipo_atual = "plus"
    abriu = False
    def filtra(linha:str):
        return linha.split('#')[0].strip()


    def parseExepresion():
        soma = Parser.parseTerm()
        while True:            
            if Parser.tolk.next.type == 'plus':
                soma +=  Parser.parseTerm()
            elif Parser.tolk.next.type == 'minus':
                soma -=  Parser.parseTerm()
            elif (Parser.tolk.next.type == 'EOF')or (Parser.tolk.next.type == 'C_par'):
                break

            #print('soma',soma)
        return soma

    def parseTerm():
        prod = 1
        Parser.tipo_atual= 'times'
        while Parser.tipo_atual not in  ["EOF",'plus', 'minus','C_par']: #,'O_par','C_par'
            #print(Parser.tolk.next.value, '@@@@@@')
            #print(Parser.tipo_atual, '@@@@@@')
            Parser.tolk.selectNext()
            if Parser.tolk.next.type == Parser.tipo_atual:
                raise Exception("Tipo repetido!!!!: {}".format(Parser.tipo_atual))


            if Parser.tipo_atual == 'times':
                prod *= Parser.parseFactor() #passa a ser Parser.parseFactor
            elif Parser.tipo_atual == 'div': 
                prod //= Parser.parseFactor()
                
            Parser.tipo_atual = Parser.tolk.next.type
        #print('prod',prod)
        return prod
    def parseFactor():
        #print(Parser.tolk.next.value, '!!!!!!!!!!')

        if Parser.tolk.next.type == 'int':
            Parser.tipo_atual= 'int'
            return int(Parser.tolk.next.value)

        elif Parser.tolk.next.type == 'minus':
            Parser.tolk.selectNext()
            return  - Parser.parseFactor()
        elif Parser.tolk.next.type == 'plus':
            Parser.tolk.selectNext()
            return + Parser.parseFactor()

        elif  Parser.tolk.next.type == 'O_par':
                salva = Parser.parseExepresion()
                if Parser.tolk.next.type == 'C_par':
                    Parser.tolk.selectNext()
                    return salva
                else:
                    raise Exception("sla") 
                    #print(Parser.tolk.next.type)
                    #print('11111111')
            
        

        #recursivo: if numero retorna numero
        #elif - retorna (-parseFactor)
        #elif + retorna (parseFactor)
        #fazer recursao tipo rashi e ai o ultimo elif
        #elif () chama o parseExpression return depois de tirar o ) (se n fechar da erro)
        
    def run(self, s):
        s = Parser.filtra(s)
        Parser.tolk.cria(s)
        return Parser.parseExepresion()


from Tolkenizer import *
class Parser:
    tolk = Tolkenizer()
    def parseExepresion():
        pass
        
    def run(self, s):
        tolk = Tolkenizer()
        tolk.cria(s)
        
        tipo_atual = "plus"
        soma = 0
        while tipo_atual != "EOF":
            tolk.selectNext()
            if tolk.next.type == tipo_atual:
                raise Exception("Tipo repetido")
            else:
                if tipo_atual == "EOF":
                    break

            if tipo_atual == 'plus':
                soma+= int(tolk.next.value)
            elif tipo_atual == 'minus': 

                soma-= int(tolk.next.value)
            tipo_atual = tolk.next.type
        print(soma)


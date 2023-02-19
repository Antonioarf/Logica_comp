from sys import argv


class Token:
    def __init__(self,v,t):
        self.type = t
        self.value=v

class Tolkenizer:
    def cria(self,s):
        self.source= s 
        self.position= 0
        self.next = Token('','plus') 
    def selectNext(self):
        ultimo_n= False
        index= self.position
        while index < len(self.source):    
            pulo = 0
            if self.source[index].isnumeric():
                
                while self.source[index+pulo].isnumeric():
                    pulo+=1
                    if index+pulo>= len(self.source): 
                        break
                numero = self.source[index:index+pulo]
                self.next = Token(numero,'int')

            elif self.source[index] =='+':
                self.next = Token('','plus')
                ultimo_n=False
                pulo+=1
            elif self.source[index]=='-':
                self.next = Token('','minus')
                ultimo_n=False
                pulo+=1
            elif self.source[index]==' ':
                pass
            else:
                raise Exception("Invalid Char",self.source,self.source[index])
            index+=pulo
            self.position = index
            return self.next

        self.next = Token('','EOF')
        return self.next

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



argv.pop(0)
programa = "".join(argv)

roda = Parser()
roda.run(programa)

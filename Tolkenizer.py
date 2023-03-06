class Token:
    def __init__(self,v,t):
        self.type = t
        self.value=v

class Tolkenizer:
    def cria(self,s):
        self.source= s 
        self.position= 0
        self.next = Token('','times') 

    def selectNext(self):
        ultimo_n= False
        index= self.position
        while index < len(self.source):    
            pulo = 0
            while self.source[index]==' ':
                if  index >= len(self.source): 
                    break
                index+=1 
            if self.source[index].isnumeric():
                
                while self.source[index+pulo].isnumeric():
                    pulo+=1
                    if index+pulo>= len(self.source): break
                numero = self.source[index:index+pulo]
                self.next = Token(numero,'int')

            elif self.source[index] =='+':
                self.next = Token('sinal','plus')
                ultimo_n=False
                pulo+=1
            elif self.source[index]=='-':
                self.next = Token('sinal','minus')
                ultimo_n=False
                pulo+=1
            elif self.source[index]=='*':
                self.next = Token('sinal','times')
                ultimo_n=False
                pulo+=1
            elif self.source[index]=='/':
                self.next = Token('sinal','div')
                ultimo_n=False
                pulo+=1
            else:
                raise Exception("Invalid Char", self.source[index])
            index+=pulo
            self.position = index
            return self.next

        self.next = Token('teste','EOF')
        return self.next

from tolkens import *

class Tolkenizer:
    def cria(self,s):
        self.source= s 
        self.position= 0
        self.next:Token

    def selectNext(self):
        ultimo_n= False
        index= self.position
        reservadas = ['println']
        while index < len(self.source): 
            pulo = 0
            while self.source[index]==' ':
                index+=1 
            if self.source[index].isnumeric():    
                while self.source[index+pulo].isnumeric():
                    pulo+=1
                    if index+pulo>= len(self.source): break
                numero = self.source[index:index+pulo]
                self.next = Token(numero,'int')

            elif self.source[index].isalpha():    
                while (self.source[index+pulo].isalnum())or (self.source[index+pulo] =='_'):
                    pulo+=1
                    if index+pulo>= len(self.source): break
                nome = self.source[index:index+pulo]
                if nome not in reservadas:
                    self.next = Token(nome,'var')
                elif nome == 'println':
                    self.next = Token('print','print')
            
            
            elif ord(self.source[index]) ==10:
                self.next = Token('break','break')
                ultimo_n=False
                pulo+=1

            elif self.source[index:(index+2)] =='==' :
                self.next = Token('rel','comp')
                ultimo_n=False
                pulo+=2
            elif self.source[index] =='<':
                self.next = Token('rel','menor')
                ultimo_n=False
                pulo+=1
            elif self.source[index] =='>':
                self.next = Token('rel','maior')
                ultimo_n=False
                pulo+=1
            
            elif self.source[index:(index+2)] =='&&':
                self.next = Token('log','and')
                ultimo_n=False
                pulo+=2
            elif self.source[index:(index+2)] =='||':
                self.next = Token('log','or')
                ultimo_n=False
                pulo+=2
            elif self.source[index] =='!':
                self.next = Token('log','not')
                ultimo_n=False
                pulo+=1

            
            elif self.source[index] =='=':
                self.next = Token('sinal','igual')
                ultimo_n=False
                pulo+=1
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
            elif self.source[index]=='(':
                self.next = Token('par','O_par')
                ultimo_n=False
                pulo+=1
            elif self.source[index]==')':
                self.next = Token('par','C_par')
                ultimo_n=False
                pulo+=1
            else:
                raise Exception("Invalid Char", self.source[index])
            index+=pulo
            self.position = index
            return self.next

        self.next = Token('teste','EOF')
        return self.next

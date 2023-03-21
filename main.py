from sys import argv
from Parser import *

arq = argv[1]
# arq = " ".join(argv)

roda = Parser()
resul = roda.run(arq)
resul.evaluate()


#FALTA:
# ajeitar indentificador pra atribuir e pra buscar 



#adcionar classe Symbol Table com geeter e setter pra manipular o dic
#sett: ve ja existe ou cria
#get: raise se n tiver sido criada
#atribuição eh fora do expression



# criar print (novo tipo de nó) => pode entrar qualquer coisa(expression) menos atribuicao (evaluate = print(evaluete(filho)))
# ParseFactor vai criar tolken pra get variavel 
# no tolkenizer=> ler palavra e ai ver se eh reservado (atualmente só tem o println) ou var






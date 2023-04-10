from sys import argv
from Parser import *

arq = argv[1]
roda = Parser()
resul = roda.run(arq)
resul.evaluate()







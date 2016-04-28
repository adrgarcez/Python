'''Implementar um programa que receba um nome de arquivo e gere estatísticas sobre o
arquivo (número de caracteres, número de linhas e número de palavras)'''

from collections import Counter

def geraRelatorio (file):
    arquivo = open(file,'r')
    linha = caracter = palavras = 0
    for linhas in arquivo.readlines():
        linha+=1
        caracter+=len(linhas)
        palavras+=len(linhas.split())
    arquivo.close()
    return (linha, caracter, palavras)


lineCounter, charCounter, wordCounter = geraRelatorio('python.txt')
print("Quantidade de linhas: %d\nQuantidade de caracteres: %d\nQuantidade de palavras: %d\n" % (lineCounter, charCounter, wordCounter))

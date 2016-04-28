'''
Faça um script que:
▪ Leia um arquivo texto.
▪ Conte as ocorrências de cada palavra.
▪ Mostre os resultados ordenados pelo número de ocorrências.
'''

from collections import Counter

def contaOcorrencia (file):
    arquivo = open ('python.txt','r')
    lista = []
    for linhas in arquivo.readlines():
        frase = linhas.split()
        for linhas in frase:
            lista.append(linhas)
    return lista


palavras = contaOcorrencia('python.txt')
count = Counter(palavras)
print(count)

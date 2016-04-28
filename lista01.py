# Faça um Programa que leia uma lista de 5 números inteiros e mostre-os. 

#MANEIRA 1
print('QUESTAO 01')
lista = [1, 2, 5, 78, 9]
print ('LISTA =',lista)
print('\n')
#MANEIRA 2
lista = []
for inicio in range (5):
    lista.append(int(input('Digite um numero:')))
print ('LISTA =',lista)

'''------------------------------------------------------------------------------------------------'''
# Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

#MANEIRA 1
print('QUESTAO 02')
lista = [1, 2, 5, 78, 9, 48, 75, 26, 3, 100]
lista.reverse()
print ('ORDEM INVERSA =',lista)

#MANEIRA 2
lista = []
for inicio in range (10):
    lista.append(int(input('Digite um numero:')))
lista.reverse()
print ('LISTA =',lista)

print('\n')

'''------------------------------------------------------------------------------------------------'''
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 

print('QUESTAO 03')
#MANEIRA 1
lista = [10, 9.5, 9, 8]
soma = 0
for inicio in lista:
    print (inicio)
    soma = soma + inicio
media = soma / len(lista)
print ('MEDIA =',media)

#MANEIRA 2
lista = []
media = soma = 0
for inicio in range(4):
    lista.append(float(input('Digite nota:')))
for inicio in lista:
    print (inicio)
    soma = soma + inicio
media = soma / len(lista)
print ('SOMA =',soma)
print ('MEDIA =',media)

print('\n')

'''------------------------------------------------------------------------------------------------'''
# Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 

#MANEIRA 1
print('QUESTAO 04')
lista = ['w','t','u','m','a','y','p','o','b','e']
vogais = 'aeiou'
contador = 0
for inicio in lista:
    if inicio not in vogais:
        print (inicio)
        contador = contador + 1
print ('TOTAL DE CONSOANTES =',contador)

#MANEIRA 2
lista = []
contador = 0
for inicio in range(10):
    lista.append(input('Digite caracter:'))
for inicio in lista:
    if inicio not in vogais:
        print (inicio)
        contador = contador + 1
print ('TOTAL DE CONSOANTES =',contador)

print('\n')

'''------------------------------------------------------------------------------------------------'''
# Faça um Programa que leia 20 números inteiros e armazene-os numa lista. 
# Armazene os números pares na listar PAR e os números IMPARES na lista impar. Imprima os três vetores. 

#MANEIRA 1
print('QUESTAO 05')
numeros = [2,4,5,8,96,35,78,41,25,698,52,17,100,256,968,632,547,852,301,605]
impar = []
par = []
for inicio in numeros:
    if (inicio % 2 == 0):
        par.append(inicio)
    else:
        impar.append(inicio)
print('LISTA =',numeros,'\nPAR =',par,'\nIMPAR =',impar)

#MANEIRA 2
numeros = []
impar = []
par = []
for inicio in range(20):
    numeros.append(int(input('Digite um numero:')))
for inicio in numeros:
    if (inicio % 2 == 0):
        par.append(inicio)
    else:
        impar.append(inicio)
print('LISTA =',numeros,'\nPAR =',par,'\nIMPAR =',impar)

print('\n')

'''------------------------------------------------------------------------------------------------'''
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0. 

print('QUESTAO 06')
lista = []
nota = media = count = 0
for inicio in range(10):
    print('Aluno (%d)'%(inicio+1))
    media = 0
    for inicio in range (4):
        nota = (float(input('Nota %d = '%(inicio+1))))
        media = media + nota
    media = media/4
    lista.append(media)
for inicio in lista:
    print ("MEDIAS = %.2f"%inicio)
    if (inicio>=7):
        count+=1
print('QUANTIDADE DE ALUNOS COM MEDIA IGUAL OU MAIOR QUE 7 =',count)

print('\n')

'''------------------------------------------------------------------------------------------------'''
# Faça um Programa que leia duas listas com 10 elementos cada. 
# Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas. 

print('QUESTAO 07')
lista1 = [1, 20, 10, 48, 7, 59, 638, 85, 72, 93]
lista2 = [24, 69, 874, 32, 64, 51, 28, 60, 37, 2]
lista3 = []
for inicio,inicio2 in zip(lista1,lista2):
    lista3.append(inicio)
    lista3.append(inicio2)
print ("LISTA 1:",lista1)
print ("LISTA 2:",lista2)
print ("LISTA INTERCALADA:",lista3)

print('\n')

'''------------------------------------------------------------------------------------------------'''
# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). 

print('QUESTAO 08')
temperaturas = []
numero = 1
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print('Entre com as temperaturas em cada mes')
media = 0
for inicio in range(12):
    temperaturas.append(float(input('%d - %s: ' %((inicio+1),(mes[inicio])))))
    media += temperaturas[inicio]
media = media/len(temperaturas)
print("MEDIA = %.2f"%media)
for inicio in range(len(temperaturas)):
    if (temperaturas[inicio] > media):
        print('%d - %s - %.2f' %((numero),(mes[inicio]),(temperaturas[inicio])))
        numero+=1

print('\n')

'''------------------------------------------------------------------------------------------------'''
'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
a) "Telefonou para a vítima?" 
b) "Esteve no local do crime?" 
c) "Mora perto da vítima?" 
d) "Devia para a vítima?" 
e) "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente". 
'''

print('QUESTAO 09')
perguntas=["Telefonou para a vitima?","Esteve no local do crime?","Mora perto da vitima?","Devia para a vitima?","Ja trabalhou com a vitima?"]
contador = 0
for inicio in perguntas:
    resposta = input(str(inicio) + " - S ou N: ")
    if (resposta == 'S'):
        contador+=1
print("Classificação sobre a participação da pessoa no crime")
if (contador==2):
    print("Resultado: %d - Suspeita"%contador)
elif (contador==3 or contador==4):
    print("Resultado: %d - Cumplice"%contador)
elif (contador==5):
    print("Resultado: %d - Assassino"%contador)
elif (contador<2):
    print("Resultado: %d - Inocente"%contador)

print('\n')

'''------------------------------------------------------------------------------------------------'''
'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça: 
a) Mostre a quantidade de valores que foram lidos; 
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; 
d) Calcule e mostre a soma dos valores; 
e) Calcule e mostre a média dos valores; 
f) Calcule e mostre a quantidade de valores acima da média calculada; 
g) Calcule e mostre a quantidade de valores abaixo de sete; 
h) Encerre o programa com uma mensagem;
'''

print('QUESTAO 10')
notas=[]
nota=soma=contador=0
while True:
    nota =(float(input("Digite nota: ")))
    if (nota==-1):
        break
    notas.append(nota)
print("A - Quantidade de valores que foram lidos: ",len(notas))
print("B - Valores na ordem em que foram informados: ",notas)
print("C - Valores na ordem inversa à que foram informados, um abaixo do outro:")
notas.reverse()
for inicio in notas:
    print(inicio)
    soma+=inicio
print("D - Soma dos valores: ",soma)
media=soma/len(notas)
print("D - Média dos valores: ",media)
for inicio in notas:
    if (inicio>media):
        contador+=1
print("E - Quantidade de valores acima da média calculada: ",contador)
contador = 0
for inicio in notas:
    if (inicio<7):
        contador+=1
print("F - Quantidade de valores abaixo de sete: ",contador)
print("Fim")

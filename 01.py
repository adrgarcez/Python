#ADRIELE GARCEZ DE FARIAS

def stringCaract (string, caracter=""):
    if (caracter!=""):
        lista = []
        for item in string:
            for letra in item:
                lista.append(letra)
        

        indices = []
        for item in range(len(lista)):
            if (lista[item] == caracter):
                indices.append(int(item))
        print(indices)
    else:
        print("\nO caracter nao foi especificado!\n")

historico = []
for string in range(3):
    frase = input("Digite a frase: ")
    historico.append(frase)
    caracter = input ("Digite caracter: ")
    stringCaract(frase, caracter)

print(historico)

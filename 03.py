#ADRIELE GARCEZ DE FARIAS

def valorPagamento(prestacao, dias):
    valor = 0
    if (dias!=0):
        valor = prestacao + (prestacao*0.03) + (0.1*int(dias))
        print("O valor a ser pago é %.2f"%valor)
        return valor
    else:
        print("O valor a ser pago é %d"%int(prestacao))
        return prestacao

prestacao=-1
quantidade = valorTotal = 0
lista = []
while(prestacao!=0):
    prestacao = int(input("Digite valor da prestacao: "))
    if (prestacao!=0):
        quantidade+=1
        dias = int(input("Digite valor de dias de atraso: "))
        valorTotal += valorPagamento(prestacao,dias)    
    else:
        print("\n\nQuantidade de prestações pagas no dia = %d"%int(quantidade))
        print("Valor total pago = %.2f\n"%valorTotal)

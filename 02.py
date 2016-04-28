#ADRIELE GARCEZ DE FARIAS

def troco(valorDaConta, pagamento):
    troco=notas1=notas2=notas5=notas10=notas20=notas50=0
    if (pagamento > valorDaConta):
        troco = int(pagamento) - int(valorDaConta)

        if(troco>=50):
            notas50+=1
            print("%d nota de 50"%notas50)
            troco-=50
        if(troco>=20):
            notas20+=1
            print("%d nota de 20"%notas20)
            troco-=20
        if(troco>=10):
            notas10+=1
            print("%d nota de 10"%notas10)
            troco-=10
        if(troco>=5):
            notas5+=1
            print("%d nota de 5"%notas5)
            troco-=5
        if(troco>=2):
            notas2+=1
            print("%d nota de 2"%notas2)
            troco-=2
        if(troco>=1):
            notas1+=1
            print("%d nota de 1"%notas1)
            troco-=1

        #print("%d notas de 1\n%d notas de 2\n%d notas de 5\n%d notas de 10\n%d notas de 20\n%d notas de 50"%(notas1,notas2,notas5,notas10,notas20,notas50))

valorDaConta = int(input("Valor da conta: "))
pagamento = int(input("Pagamento: "))
troco(valorDaConta,pagamento)

validade=False
cpf=(input())
cpfNovo=[]
numCresc=['10','9','8','7','6','5','4','3','2']
numCresc1=['11','10','9','8','7','6','5','4','3','2']
resultado=[]

for i in cpf:
    valor = i
    cpfNovo.append(valor)
cpfNovo.pop(3),cpfNovo.pop(6),cpfNovo.pop(9)

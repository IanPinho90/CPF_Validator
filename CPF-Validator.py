cpfNovo=[]
numCresc=["10","9","8","7","6","5","4","3","2"]
numCresc1=["11","10","9","8","7","6","5","4","3","2"]
resultado=[]
print("Digite aqui seu CPF com um '.' a cada 3 números e um '-' antes dos 2 ultimos dígitos.")
cpf=input()

def resultado (numCresc,cpfNovo,cpf):
    for i in cpf:
        valor = i
        cpfNovo.append(valor)
    cpfNovo.pop(3),cpfNovo.pop(6),cpfNovo.pop(9)
    resultado = list(map(lambda x,y: int(x)*int(y) ,numCresc,cpfNovo))
    soma=sum(resultado)
    resto = soma%int(numCresc1[0])
    numero1=int(numCresc1[0])-int(resto)
    resultado2 = list(map(lambda x,y: int(x)*int(y) ,numCresc1,cpfNovo))
    resto2=sum(resultado2)%int(numCresc1[0])
    numero2=int(numCresc1[0])-int(resto2)
    if int(numero1) ==int(cpfNovo[9]) and int(numero2) ==int(cpfNovo[10]):
        return True
    else:
        return False

while not resultado(numCresc,cpfNovo,cpf):
    print("CPF inválido, por favor digite novamente")
    cpf=input()
    cpfNovo=[]
    resultado(numCresc,cpfNovo,cpf)
print("CPF válido!")
alunos = []

while True:

    try:
        nome =(input("Digite o nome do aluno: "))
        for letra in nome:
            if letra >="0" and letra<= "9":
                raise ValueError
            break

        idade = int(input("Digite a idade do aluno: "))
        if idade < 0:
            raise ValueError
        nota = float(input("Digite a nota do aluno: "))
        if nota < 0 or nota > 10:
            raise ValueError

        aluno = {
            "nome": nome,
            "idade": idade,
            "nota": nota
            }

        alunos.append(aluno)

        continuar = input("Deseja continuar? (s/n): ").lower()

        if continuar == "n":
                break
        
    except ValueError:
        print("Erro nos dados. Tente novamente.")

def classificacao(nota):
    if nota >= 7:
        print("Aprovado")
    elif nota >=5:
        print("Recuperação")
    else:
        print("Reprovado")

def media(alunos):
    soma = 0 

    for alunos in alunos:
        soma = soma + alunos["nota"]
        media = soma / len(alunos)
    print("Média da sala:", media)


print("\nAlunos Cadastrados")

for aluno in alunos:
    print("Nome:", aluno["nome"])

print("\nSituação dos alunos")

for aluno in alunos:

    print("Nome:", aluno["nome"])
    classificacao(aluno["nota"])

aprovados = 0
recuperacao = 0 
reprovados = 0 

for aluno in alunos:

    if aluno["nota"]>=7:
        aprovados +=1

    elif aluno["nota"]>=5:
        recuperacao +=1
    
    else:
        reprovados +=1

print("\nQuantidade de aprovados: ", aprovados)
print("Quantidade de recuperação: ", recuperacao)
print("Quantidade de reprovados: ", reprovados)

maior_aluno = alunos[0]
menor_aluno = alunos[0]

for aluno in alunos:

    if aluno["nota"] > maior_aluno["nota"]:
        maior_aluno = aluno

    if aluno["nota"] < menor_aluno["nota"]:
        menor_aluno = aluno

print("\nAluno com maior nota:", maior_aluno["nome"])

print("Aluno com menor nota:", menor_aluno["nome"])
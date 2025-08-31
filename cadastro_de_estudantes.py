import sys
import os

def add_aluno():
    print("Você escolheu adicionar um aluno\n")
    nome = input("Insira um nome:\n ")
    nomes.append(nome)
    
    with open("estudantes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")
    
    print("Nome cadastrado!")
    os.system("pause")

def lista_alunos():
    print("Lista de alunos:\n")
    for i in nomes:
        print(f"- {i}")
    os.system("pause")

def apagar_estudante():
    print("Você escolheu apagar um estudante!\n")
    apagar = input("Qual estudante você deseja apagar?\n")
            
    if apagar in nomes:
        print("Estudante encontrado! Apagando...")
        nomes.remove(apagar)
        os.system("pause")
        
        with open("estudantes.txt", "w", encoding="utf-8") as arquivo:
            for aluno in nomes:
                arquivo.write(aluno + "\n")
    else:
        print("Estudante não encontrado")
        os.system("pause")

def saida():
    out = input("Você escolheu sair? Sim/Não\n").strip().lower() #ignora espaços maiusculas e minusculas
            
    if out in ["não", "nao", "n"]:
        print("Voltando...")
        os.system("pause")
    else:
        print("Saindo...")
        sys.exit()

def opcao_inexistente():
    print("Por favor digite uma opção adequada!")
    os.system("pause")

nomes= []

try:
    with open("estudantes.txt", "r", encoding="utf-8") as arquivo:
        nomes = [linha.strip() for linha in arquivo]
except FileNotFoundError:
    nomes = []


while True:
    print("====Cadastro de estudantes====\n")

    escolha = (input("Selecione uma opção:--->\n1 - Cadastrar estudante\n2 - Lista de estudantes\n3 - Apagar um estudante\n4 - Sair\n"))

    match escolha:
        case "1":
            add_aluno()
        case "2":
            lista_alunos()
        case "3":
            apagar_estudante()
        case "4":
            saida()
        case _:
            opcao_inexistente()
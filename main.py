import functions

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar
[q] Sair

=> """
print("\n================ BANCO PYTHÔNICO ================")
print("Bem-vindo ao Banco Pythônico!")
usuario = input("Informe o número de sua conta: ")

while True:
    print("Selecione uma das opções abaixo:")

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: ").replace(',', '.')) #O replace permite que o usuário informe o valor com vírgula OU ponto sem gerar erro.
        resultado, saldo, extrato = functions.depositar(valor)
        print(resultado)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: ").replace(',', '.'))
        resultado, saldo, extrato = functions.sacar(valor)
        print(resultado)

    elif opcao == "e":
        print(functions.obter_extrato())

    elif opcao == "q":
        print("Obrigado por utilizar o Banco Pythônico! Até logo!")
        break

    elif opcao == "c":
        print("Seja bem-vindo(a) ao cadastro de clientes do Banco Pythônico!")
        cpf = input("Informe o seu CPF (apenas números): ")
        if functions.cpf_existe(functions.dic_cadastrados, cpf):
            print("CPF já cadastrado. Por favor, tente novamente com outro CPF.")
        
        nome = input("Informe o seu nome completo: ")
        data_nascimento = input("Informe a sua data de nascimento (DD/MM/AAAA): ")
        logradouro = input("Informe o seu logradouro (rua, avenida, etc.): ")
        num_casa = input("Informe o número de sua residência: ")
        bairro = input("Informe o seu bairro: ")
        cidade = input("Informe sua cidade com a sigla de seu estado (ex. São José dos Campos - SP): ")
        endereço = logradouro + ", " + num_casa + ", " + bairro + ", " + cidade
        resultado = functions.criar_conta(nome, data_nascimento, cpf, endereço)
        print(resultado)

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
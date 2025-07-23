from classes import PessoaFisica, ContaCorrente, Saque, Deposito
clientes = []
contas = []

def encontrar_conta(numero):
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None

def encontrar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar
[q] Sair

=> """

print("\n================ BANCO PYTHÔNICO ================")
print("Bem-vindo ao Banco Pythônico!")

while True:
    print("Selecione uma das opções abaixo:")
    opcao = input(menu)

    match opcao:
        case "c":
            print("Seja bem-vindo(a) ao cadastro de clientes do Banco Pythônico!")
            cpf = input("Informe o seu CPF (apenas números): ")
            if encontrar_cliente_por_cpf(cpf):
                print("CPF já cadastrado. Por favor, tente novamente com outro CPF.")
                continue
            nome = input("Informe o seu nome completo: ")
            data_nascimento = input("Informe a sua data de nascimento (DD/MM/AAAA): ")
            endereco = input("Informe seu endereço completo: ")
            cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
            clientes.append(cliente)
            numero_conta = len(contas) + 1
            conta = ContaCorrente(numero_conta, cliente)
            cliente.adicionar_conta(conta)
            contas.append(conta)
            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

        
        case "d":
            numero = input("Informe o número da sua conta: ")
            try:
                numero_conta = int(numero)
            except ValueError:
                print("Número invalido!")
                continue

            conta = encontrar_conta(numero_conta)
            if not conta:
                print("Conta não encontrada.")
                continue
            valor = float(input("Informe o valor do depósito: ").replace(',', '.'))
            transacao = Deposito(valor)
            conta.cliente.realizar_transacao(conta, transacao)


        case "s":
            numero = input("Informe o número da sua conta: ")
            try:
                numero_conta = int(numero)
            except ValueError:
                print("Número invalido!")
                continue

            conta = encontrar_conta(numero_conta)
            if not conta:
                print("Conta não encontrada.")
                continue
            valor = float(input("Informe o valor do saque: ").replace(',', '.'))
            transacao = Saque(valor)
            conta.cliente.realizar_transacao(conta, transacao)

        case "e":
            numero = input("Informe o número da sua conta: ")
            try:
                numero_conta = int(numero)
            except ValueError:
                print("Número invalido!")
                continue

            conta = encontrar_conta(numero_conta)
            if not conta:
                print("Conta não encontrada.")
                continue
            print("\n=== Extrato ===")
            for t in conta.historico.transacoes:
                print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
            print(f"Saldo atual: R$ {conta.saldo:.2f}")

        case "q":
            print("Obrigado por utilizar o Banco Pythônico! Até logo!")
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
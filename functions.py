#variáveis globais - a serem modificadas pelas funções

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
ultima_conta = 0
agência = "0001"  # Agência padrão do Banco Pythônico
dic_cadastrados = {}  # Dicionário para armazenar os clientes cadastrados

# Funções para o Banco Pythônico
def depositar(valor):
    global saldo, extrato

    verificar_numero = str(valor).split('.')[1]            #Verifica se o usuário digitou um valor válido para centavos
    if len(verificar_numero) > 2:
        return "Operação falhou! O valor informado é inválido para os centavos."
        
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return f"Depósito de {valor:.2f} realizado com sucesso! Saldo atual: R$ {saldo:.2f}", saldo, extrato

    else:
        return "Operação falhou! O valor informado é inválido."

def sacar(valor):
    global saldo, numero_saques, limite_saques, extrato

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        return "Operação falhou! Você não tem saldo suficiente.", saldo, extrato

    elif excedeu_limite:
        return "Operação falhou! O valor do saque excede o limite.", saldo, extrato

    elif excedeu_saques:
        return "Operação falhou! Número máximo de saques por período excedido.", saldo, extrato

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return "Sucesso!\nAguarde o processamento do saque e retire seu dinheiro!", saldo, extrato

    else:
        return "Operação falhou! O valor informado é inválido.", saldo, extrato

def obter_extrato():
    if extrato:
        return f"\n================ EXTRATO ================\n{extrato}Saldo: R$ {saldo:.2f}\n=========================================="
    else:
        return f"\n================ EXTRATO ================\nNão foram realizadas movimentações.\nSaldo: R$ {saldo:.2f}\n=========================================="
    
def criar_conta(nome, data_nascimento, cpf, endereço):
    global ultima_conta, dic_cadastrados
    ultima_conta += 1

    dic_cadastrados[ultima_conta] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereço": endereço,
        "agência": agência,
        "saldo": 0
    }
    return f"Conta criada com sucesso! Número da conta: {ultima_conta}, Agência: {agência}. Bem-vindo(a) ao Banco Pythônico, {nome}!"

def cpf_existe(dic_cadastrados, cpf):
    for cliente in dic_cadastrados.values():
        if cliente["cpf"] == cpf:
            return True
    return False
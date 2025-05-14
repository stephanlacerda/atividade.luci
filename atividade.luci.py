pessoas = []
contas = []
movimentacoes = []

def achar_pessoa(cpf):
    for p in pessoas:
        if p['cpf'] == cpf:
            return p
    return None

def achar_conta(numero):
    for c in contas:
        if c['numero'] == numero:
            return c
    return None

def nova_pessoa():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    end = input("Endereço: ")
    tel = input("Telefone: ")
    pessoa = {'cpf': cpf, 'nome': nome, 'end': end, 'tel': tel}
    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso.")

def mudar_pessoa():
    cpf = input("Digite o CPF da pessoa: ")
    pessoa = achar_pessoa(cpf)
    if pessoa:
        pessoa['nome'] = input("Novo nome: ")
        pessoa['end'] = input("Novo endereço: ")
        pessoa['tel'] = input("Novo telefone: ")
        print("Dados atualizados.")
    else:
        print("Pessoa não encontrada.")

def mostrar_pessoas():
    for p in pessoas:
        print(p)

def apagar_pessoa():
    cpf = input("CPF da pessoa a remover: ")
    pessoa = achar_pessoa(cpf)
    if pessoa:
        pessoas.remove(pessoa)
        print("Pessoa removida.")
    else:
        print("Pessoa não achada.")

def nova_conta():
    numero = input("Número da conta: ")
    agencia = input("Agência: ")
    cpf_dono = input("CPF do dono: ")
    if achar_pessoa(cpf_dono):
        conta = {'numero': numero, 'agencia': agencia, 'cpf': cpf_dono, 'saldo': 0}
        contas.append(conta)
        print("Conta criada.")
    else:
        print("CPF não cadastrado.")

def mudar_conta():
    numero = input("Número da conta: ")
    conta = achar_conta(numero)
    if conta:
        conta['agencia'] = input("Nova agência: ")
        print("Conta atualizada.")
    else:
        print("Conta não encontrada.")

def mostrar_contas():
    for c in contas:
        print(c)

def apagar_conta():
    numero = input("Número da conta: ")
    conta = achar_conta(numero)
    if conta:
        contas.remove(conta)
        print("Conta excluída.")
    else:
        print("Conta inválida.")

def fazer_deposito():
    numero = input("Conta para depósito: ")
    conta = achar_conta(numero)
    if conta:
        valor = float(input("Valor: "))
        conta['saldo'] += valor
        movimentacoes.append({'tipo': 'depósito', 'conta': numero, 'valor': valor})
        print("Depósito feito.")
    else:
        print("Conta não encontrada.")

def fazer_saque():
    numero = input("Conta para saque: ")
    conta = achar_conta(numero)
    if conta:
        valor = float(input("Valor: "))
        if conta['saldo'] >= valor:
            conta['saldo'] -= valor
            movimentacoes.append({'tipo': 'saque', 'conta': numero, 'valor': valor})
            print("Saque feito.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta inválida.")

def fazer_transferencia():
    origem = input("Conta de origem: ")
    destino = input("Conta de destino: ")
    valor = float(input("Valor: "))
    c1 = achar_conta(origem)
    c2 = achar_conta(destino)
    if c1 and c2:
        if c1['saldo'] >= valor:
            c1['saldo'] -= valor
            c2['saldo'] += valor
            movimentacoes.append({'tipo': 'pix', 'de': origem, 'para': destino, 'valor': valor})
            print("Transferência concluída.")
        else:
            print("Sem saldo.")
    else:
        print("Alguma conta está errada.")

def ver_extrato():
    numero = input("Conta: ")
    conta = achar_conta(numero)
    if conta:
        print(f"Saldo atual: R$ {conta['saldo']:.2f}")
        for m in movimentacoes:
            if m.get('conta') == numero or m.get('de') == numero or m.get('para') == numero:
                print(m)
    else:
        print("Conta não encontrada.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar pessoa")
        print("2. Atualizar pessoa")
        print("3. Listar pessoas")
        print("4. Remover pessoa")
        print("5. Criar conta")
        print("6. Editar conta")
        print("7. Ver contas")
        print("8. Excluir conta")
        print("9. Depositar")
        print("10. Sacar")
        print("11. Transferir")
        print("12. Extrato")
        print("13. Sair")
        op = input("Escolha: ")

        if op == '1': nova_pessoa()
        elif op == '2': mudar_pessoa()
        elif op == '3': mostrar_pessoas()
        elif op == '4': apagar_pessoa()
        elif op == '5': nova_conta()
        elif op == '6': mudar_conta()
        elif op == '7': mostrar_contas()
        elif op == '8': apagar_conta()
        elif op == '9': fazer_deposito()
        elif op == '10': fazer_saque()
        elif op == '11': fazer_transferencia()
        elif op == '12': ver_extrato()
        elif op == '13':
            print("Encerrado.")
            break
        else:
            print("Opção inválida.")

menu()
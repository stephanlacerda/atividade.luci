usuarios = []
livros = []
registros = []

def achar_usuario(cpf):
    for u in usuarios:
        if u['cpf'] == cpf:
            return u
    return None

def achar_livro(codigo):
    for l in livros:
        if l['codigo'] == codigo:
            return l
    return None

def novo_usuario():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    end = input("Endereço: ")
    tel = input("Telefone: ")
    usuario = {'cpf': cpf, 'nome': nome, 'end': end, 'tel': tel}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

def mudar_usuario():
    cpf = input("Digite o CPF do usuário: ")
    usuario = achar_usuario(cpf)
    if usuario:
        usuario['nome'] = input("Novo nome: ")
        usuario['end'] = input("Novo endereço: ")
        usuario['tel'] = input("Novo telefone: ")
        print("Dados atualizados.")
    else:
        print("Usuário não encontrado.")

def mostrar_usuarios():
    for u in usuarios:
        print(u)

def apagar_usuario():
    cpf = input("CPF do usuário a remover: ")
    usuario = achar_usuario(cpf)
    if usuario:
        usuarios.remove(usuario)
        print("Usuário removido.")
    else:
        print("Usuário não achado.")

def novo_livro():
    codigo = input("Código do livro: ")
    titulo = input("Título: ")
    cpf_dono = input("CPF do responsável: ")
    if achar_usuario(cpf_dono):
        livro = {'codigo': codigo, 'titulo': titulo, 'cpf': cpf_dono, 'status': 'disponível'}
        livros.append(livro)
        print("Livro cadastrado.")
    else:
        print("CPF não cadastrado.")

def mudar_livro():
    codigo = input("Código do livro: ")
    livro = achar_livro(codigo)
    if livro:
        livro['titulo'] = input("Novo título: ")
        print("Livro atualizado.")
    else:
        print("Livro não encontrado.")

def mostrar_livros():
    for l in livros:
        print(l)

def apagar_livro():
    codigo = input("Código do livro: ")
    livro = achar_livro(codigo)
    if livro:
        livros.remove(livro)
        print("Livro removido.")
    else:
        print("Livro inválido.")

def registrar_emprestimo():
    codigo = input("Código do livro: ")
    livro = achar_livro(codigo)
    if livro and livro['status'] == 'disponível':
        livro['status'] = 'emprestado'
        registros.append({'tipo': 'empréstimo', 'livro': codigo})
        print("Empréstimo registrado.")
    else:
        print("Livro não disponível ou não encontrado.")

def registrar_devolucao():
    codigo = input("Código do livro: ")
    livro = achar_livro(codigo)
    if livro and livro['status'] == 'emprestado':
        livro['status'] = 'disponível'
        registros.append({'tipo': 'devolução', 'livro': codigo})
        print("Devolução registrada.")
    else:
        print("Livro não encontrado ou não está emprestado.")

def registrar_transferencia():
    origem = input("Código do livro de origem: ")
    destino = input("Código do livro de destino: ")
    descricao = input("Motivo da transferência: ")
    l1 = achar_livro(origem)
    l2 = achar_livro(destino)
    if l1 and l2:
        registros.append({'tipo': 'transferência', 'de': origem, 'para': destino, 'motivo': descricao})
        print("Transferência registrada.")
    else:
        print("Algum código está incorreto.")

def ver_historico():
    codigo = input("Código do livro: ")
    livro = achar_livro(codigo)
    if livro:
        print(f"Status atual: {livro['status']}")
        for r in registros:
            if r.get('livro') == codigo or r.get('de') == codigo or r.get('para') == codigo:
                print(r)
    else:
        print("Livro não encontrado.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar usuário")
        print("2. Atualizar usuário")
        print("3. Listar usuários")
        print("4. Remover usuário")
        print("5. Cadastrar livro")
        print("6. Editar livro")
        print("7. Ver livros")
        print("8. Excluir livro")
        print("9. Registrar empréstimo")
        print("10. Registrar devolução")
        print("11. Registrar transferência")
        print("12. Ver histórico do livro")
        print("13. Sair")
        op = input("Escolha: ")

        if op == '1': novo_usuario()
        elif op == '2': mudar_usuario()
        elif op == '3': mostrar_usuarios()
        elif op == '4': apagar_usuario()
        elif op == '5': novo_livro()
        elif op == '6': mudar_livro()
        elif op == '7': mostrar_livros()
        elif op == '8': apagar_livro()
        elif op == '9': registrar_emprestimo()
        elif op == '10': registrar_devolucao()
        elif op == '11': registrar_transferencia()
        elif op == '12': ver_historico()
        elif op == '13':
            print("Encerrado.")
            break
        else:
            print("Opção inválida.")

menu()

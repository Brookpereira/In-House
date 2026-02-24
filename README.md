

usuarios = []

while True:
    print('=== Sistema de Cadastro ===')
    print('1 - Cadastrar usuário')
    print('2 - listar usuários')
    print('0 - sair')
    opcao=input('Escolha uma opção.')
    if opcao == "1":
        nome=input('digite seu nome')
        email=input('digite seu e-mail')
        senha=input('Digite sua senha')
       
        usuario = {
            "nome": nome,
            "e-mail": email,
            "senha": senha
        }
        usuarios.append(usuario)
        print('Usuario cadastrado com sucesso!')
    elif opcao =='2':
        print("---usuarios cadastrados---")
        for u in usuarios:
            print('Nome:', u["nome"], '|E-mail:', u,["e-mail"])
    elif opcao == "0":
        print('Sistema encerrado.')
        break
    else:
        print('Opção invalida.')

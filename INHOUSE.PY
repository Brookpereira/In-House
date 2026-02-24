email_existe = False

for u in usuarios:
    if u["email"] == email:
        email_existe = True
        break

    if email_existe:
        print("Esse email já está cadastrado!")
        else:
        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha
        }

        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
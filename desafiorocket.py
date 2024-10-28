def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {'contato': nome_contato, 'telefone': telefone_contato, 'email': email_contato, 'favorito': False}
    contatos.append(contato)
    print(f'Contato de {nome_contato} foi adicionado com sucesso!')
    return

def ver_contatos(contatos):
    print('Lista de contatos:')
    for indice, contato in enumerate(contatos, start=1):
        status = '★' if contato['favorito'] else ' '
        nome_contato = contato['contato']
        telefone_contato = contato['telefone']
        email_contato = contato['email']
        print(f'{indice}. {status} Nome: {nome_contato} \n     Telefone: {telefone_contato} \n     Email: {email_contato}')
    return

def atualizar_contato(contatos, indice_contatos, novo_nome_contato):
    indice_contato_ajustado = int(indice_contatos) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]['contato'] = novo_nome_contato
        print(f'O contato de índice [{indice_contatos}] foi atualizado para {novo_nome_contato}')
    else:
        print('Índice de contato invalido.')
    return

def atualizar_numero(contatos, indice_contatos, novo_numero_contato):
    indice_contato_ajustado = int(indice_contatos) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]['telefone'] = novo_numero_contato
        print(f'O numero de índice [{indice_contatos}] foi atualizado para {novo_numero_contato}')
    else:
        print('Índice de contato invalido.')
    return
    
def atualizar_email(contatos, indice_contatos, novo_email_contato):
    indice_contato_ajustado = int(indice_contatos) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]['email'] = novo_email_contato
        print(f'O email de índice [{indice_contatos}] foi atualizado para {novo_email_contato}')
    else:
        print('Índice de contato invalido.')
    return

def atualizar_num_email(contatos, indice_contatos, novo_numero_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contatos) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]['telefone'] = novo_numero_contato
        print(f'O numero de índice [{indice_contatos}] foi atualizado para {novo_numero_contato}')
        contatos[indice_contato_ajustado]['email'] = novo_email_contato
        print(f'O email de índice [{indice_contatos}] foi atualizado para {novo_email_contato}')
    else:
        print('Índice de contato invalido.')
    return

def favoritar_contato(contatos, indice_contatos):
    indice_contato_ajustado = int(indice_contatos) - 1
    contatos[indice_contato_ajustado]['favorito'] = True
    print(f'Contato de índice [{indice_contatos}] favoritado com sucesso!')
    return

def desfavoritar_contato(contatos, indice_contatos):
    indice_contato_ajustado = int(indice_contatos) - 1
    contatos[indice_contato_ajustado]['favorito'] = False
    print(f'Contato de índice [{indice_contatos}] desfavoritado com sucesso!')
    return

def contatos_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato['favorito'] is True]
    ver_contatos(favoritos)
    return

def indice_valido(contatos, mensagem):
    if len(contatos) <= 0:
        print("A lista de contatos está vazia!")
        return 0
    indice_contatos = 0
    while indice_contatos <= 0 or indice_contatos > len(contatos):
        try:
            indice_contatos = int(input(mensagem))
            if indice_contatos <= 0 or indice_contatos > len(contatos):
                print("Índice de contato inválido! Tente novamente.\n")
        except Exception as e:
            print(f"Exceção: {e}")
    return indice_contatos

def deletar_contato(contatos, indice_contatos):
    indice_contato_deletar = int(indice_contatos) - 1
    contatos.pop(indice_contato_deletar)
    print(f"Contato {indice_contatos} deletado!")  
    return

contatos = []

while True:
    print('==========================================')
    print('1. Adicionar um contato')
    print('2. Lista de Contatos')
    print('3. Editar um Contato')
    print('4. Marcar como Favorito')
    print('5. Desmarcar como Favorito')
    print('6. Lista de Contatos Favoritos')
    print('7. Apagar um Contato')
    print('8. Sair')
    print('==========================================')
    escolha = input('Digite sua escolha: ')
    print('==========================================')

    if escolha == '1':
       nome_contato = input('Digite o nome do contato que você deseja adicionar: ')
       telefone_contato = input('Digite o telefone: ')
       email_contato = input('Digite um email: ')
       adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == '2':
        ver_contatos(contatos)
    elif escolha == '3':
        ver_contatos(contatos)
        print('=========================')
        print('1. Mudar o nome')
        print('2. Mudar o telefone')
        print('3. Mudar o email')
        print('4. Mudar telefone e email')
        print('=========================')
        escolha_alteracao = input('Digite sua escolha: ')
        print('=========================')

        if escolha_alteracao == '1':
            ver_contatos(contatos)
            print('==========================================')
            indice_contatos = input('Digite o indice do contato que deseja atualizar: ')
            print('------------------------------------------')
            novo_nome_contato = input('Digite o novo nome do contato: ')
            print('------------------------------------------')
            atualizar_contato(contatos, indice_contatos, novo_nome_contato)
        elif escolha_alteracao == '2':
            ver_contatos(contatos)
            print('==========================================')
            indice_contatos = input('Digite o indice do contato que deseja atualizar: ')
            print('------------------------------------------')
            novo_numero_contato = input('Digite o novo número do contato: ')
            print('------------------------------------------')    
            atualizar_numero(contatos, indice_contatos, novo_numero_contato)
        elif escolha_alteracao == '3':
            ver_contatos(contatos)
            print('==========================================')
            indice_contatos = input('Digite o indice do contato que deseja atualizar: ')
            print('------------------------------------------')
            novo_email_contato = input('Digite o novo email do contato: ')
            print('------------------------------------------')
            atualizar_email(contatos, indice_contatos, novo_email_contato)
        elif escolha_alteracao == '4':
            ver_contatos(contatos)
            print('==========================================')
            indice_contatos = input('Digite o indice do contato que deseja atualizar: ')
            print('------------------------------------------')
            novo_numero_contato = input('Digite o novo número do contato: ')
            print('------------------------------------------')
            novo_email_contato = input('Digite o novo email do contato: ')
            print('------------------------------------------')
            atualizar_num_email(contatos, indice_contatos, novo_numero_contato, novo_email_contato)
    
    elif escolha == '4':
        ver_contatos(contatos)
        print('==========================================')
        indice_contatos = input('Digite o índice do contato que deseja favoritar: ')
        print('------------------------------------------')
        favoritar_contato(contatos, indice_contatos)
    
    elif escolha == '5':
        ver_contatos(contatos)
        print('==========================================')
        indice_contatos = input('Digite o índice do contato que deseja desfavoritar: ')
        print('------------------------------------------')
        desfavoritar_contato(contatos, indice_contatos)
    
    elif escolha == '6':
        contatos_favoritos(contatos)

    elif escolha == '7':
        ver_contatos(contatos)
        mensagem = "Digite o índice do contato a ser excluído: "
        indice_contatos = indice_valido(contatos, mensagem)
        if indice_contatos == 0:
            continue
        deletar_contato(contatos, indice_contatos)
    
    elif escolha == '8':
        break
print('Programa Finalizado.')
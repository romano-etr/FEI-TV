import os
import difflib

ARQ_USUARIOS = "FeiTV/arquivos_txt/usuarios.txt"
ARQ_FILMES = "FeiTV/arquivos_txt/filmes.txt"
ARQ_CURTIDAS = "FeiTV/arquivos_txt/curtidas.txt"
ARQ_FAVORITOS = "FeiTV/arquivos_txt/favoritos.txt"

# Função para cadastrar os filmes
def cadastrar_filmes_iniciais():
    with open(ARQ_FILMES, "r", encoding="utf-8") as arq:
        conteudo = arq.readlines()

    if len(conteudo) == 0:
        filmes = [
            "1;Guerra Mundial Z;Ação;1:55\n",
            "2;Mãos Talentosas;Biografia;1:30\n",
            "3;A Vida Em Um Ano;Romance;1:47\n",
            "4;Bastardos Inglórios;Guerra;2:33\n",
            "5;A Lenda Do Cavaleiro Sem Cabeça;Terror;1:45\n",
            "6;Piratas Do Caribe;Aventura;2:23\n",
            "7;Gente Grande;Comédia;1:42\n",
            "8;A Origem;Ficção Científica;2:28\n"
        ]

        with open(ARQ_FILMES, "w", encoding="utf-8") as arq:
            arq.writelines(filmes)


# Função para cadastrar o usuário 
def cadastrar_usuario():
    print("\n=== CADASTRO ===")

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    with open(ARQ_USUARIOS, "r", encoding="utf-8") as arq:
        usuarios = arq.readlines()

    for linha in usuarios:
        dados = linha.strip().split(";")

        if dados[0] == usuario:
            print("Usuário já existe.")
            return

    with open(ARQ_USUARIOS, "a", encoding="utf-8") as arq:
        arq.write(usuario + ";" + senha + "\n")

    print("Usuário cadastrado com sucesso!")

# Função para fazer o login
def login():
    print("\n=== LOGIN ===")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    with open(ARQ_USUARIOS, "r", encoding="utf-8") as arq:
        usuarios = arq.readlines()

    for linha in usuarios:
        dados = linha.strip().split(";")

        if dados[0] == usuario and dados[1] == senha:
            print("Login realizado com sucesso!")
            return usuario

    print("Usuário ou senha incorretos.")
    return None

# Função para listar os filmes
def listar_filmes():
    print("\n=== LISTA DE FILMES ===")

    with open(ARQ_FILMES, "r", encoding="utf-8") as arq:
        filmes = arq.readlines()

    for linha in filmes:
        dados = linha.strip().split(";")

        print("----------------------")
        print("ID:", dados[0])
        print("Nome:", dados[1])
        print("Gênero:", dados[2])
        print("Duração:", dados[3])

# Função para buscar o filme
def buscar_filme():
    nome = input("\nDigite o nome do filme: ").lower()

    encontrado = False

    with open(ARQ_FILMES, "r", encoding="utf-8") as arq:
        filmes = arq.readlines()

    for linha in filmes:
        dados = linha.strip().split(";")

        if nome in dados[1].lower():
            encontrado = True

            print("\nFilme encontrado!")
            print("ID:", dados[0])
            print("Nome:", dados[1])
            print("Gênero:", dados[2])
            print("Duração:", dados[3])

    if not encontrado:
        print("Nenhum filme encontrado.")

# Função para curtir o filme
def curtir_filme(usuario):
    listar_filmes()

    filme_id = input("\nDigite o ID do filme para curtir: ")

    with open(ARQ_CURTIDAS, "r", encoding="utf-8") as arq:
        curtidas = arq.readlines()

    for linha in curtidas:
        dados = linha.strip().split(";")

        if dados[0] == usuario and dados[1] == filme_id:
            print("Você já curtiu esse filme.")
            return

    with open(ARQ_CURTIDAS, "a", encoding="utf-8") as arq:
        arq.write(usuario + ";" + filme_id + "\n")

    print("Filme curtido com sucesso!")

# Função para descurtir o filme
def descurtir_filme(usuario):
    listar_filmes()

    filme_id = input("\nDigite o ID do filme para descurtir: ")

    with open(ARQ_CURTIDAS, "r", encoding="utf-8") as arq:
        curtidas = arq.readlines()

    novas_curtidas = []

    removido = False

    for linha in curtidas:
        dados = linha.strip().split(";")

        if dados[0] == usuario and dados[1] == filme_id:
            removido = True
        else:
            novas_curtidas.append(linha)

    with open(ARQ_CURTIDAS, "w", encoding="utf-8") as arq:
        arq.writelines(novas_curtidas)

    if removido:
        print("Curtida removida.")
    else:
        print("Você não curtiu esse filme.")

# Função para criar uma lista de filmes favoritos
def criar_lista_favoritos(usuario):
    nome_lista = input("\nNome da lista de favoritos: ")

    with open(ARQ_FAVORITOS, "a", encoding="utf-8") as arq:
        arq.write(usuario + ";" + nome_lista + ";\n")

    print("Lista criada com sucesso!")

# Função para mostrar a lista de filmes favoritos
def mostrar_listas(usuario):
    with open(ARQ_FAVORITOS, "r", encoding="utf-8") as arq:
        listas = arq.readlines()

    print("\n=== SUAS LISTAS ===")

    encontrou = False

    for linha in listas:
        dados = linha.strip().split(";")

        if dados[0] == usuario:
            encontrou = True
            print("Lista:", dados[1])

    if not encontrou:
        print("Nenhuma lista encontrada.")

# Função para adicionar um filme a sua lista de filmes favoritos
def adicionar_filme_lista(usuario):
    mostrar_listas(usuario)
    listar_filmes()

    nome_lista = input("\nDigite o nome da lista: ")
    filme_id = input("Digite o ID do filme: ")

    with open(ARQ_FAVORITOS, "r", encoding="utf-8") as arq:
        listas = arq.readlines()

    novas_linhas = []

    for linha in listas:
        dados = linha.strip().split(";")

        if dados[0] == usuario and dados[1] == nome_lista:

            filmes = dados[2]

            if filmes == "":
                filmes = filme_id
            else:
                filmes += "," + filme_id

            nova_linha = usuario + ";" + nome_lista + ";" + filmes + "\n"

            novas_linhas.append(nova_linha)

        else:
            novas_linhas.append(linha)

    with open(ARQ_FAVORITOS, "w", encoding="utf-8") as arq:
        arq.writelines(novas_linhas)

    print("Filme adicionado na lista!")

# Função para ver a lista de filmes favoritos
def ver_favoritos(usuario):
    with open(ARQ_FAVORITOS, "r", encoding="utf-8") as arq:
        listas = arq.readlines()

    print("\n=== FAVORITOS ===")

    for linha in listas:
        dados = linha.strip().split(";")

        if dados[0] == usuario:

            print("\nLista:", dados[1])

            if dados[2] == "":
                print("Lista vazia.")
            else:
                ids = dados[2].split(",")

                with open(ARQ_FILMES, "r", encoding="utf-8") as filmes_arq:
                    filmes = filmes_arq.readlines()

                for fil in ids:
                    for linha_filme in filmes:
                        dados_filme = linha_filme.strip().split(";")

                        if dados_filme[0] == fil:
                            print("-", dados_filme[1])

# Função para excluir a lista de filmes favoritos
def excluir_lista(usuario):
    mostrar_listas(usuario)

    nome_lista = input("\nDigite o nome da lista que deseja excluir: ")

    with open(ARQ_FAVORITOS, "r", encoding="utf-8") as arq:
        listas = arq.readlines()

    novas_linhas = []

    removido = False

    for linha in listas:
        dados = linha.strip().split(";")

        if dados[0] == usuario and dados[1] == nome_lista:
            removido = True
        else:
            novas_linhas.append(linha)

    with open(ARQ_FAVORITOS, "w", encoding="utf-8") as arq:
        arq.writelines(novas_linhas)

    if removido:
        print("Lista removida.")
    else:
        print("Lista não encontrada.")

# Função para o menu do usuário
def menu_usuario(usuario):

    while True:

        print("\n========================")
        print("FEItv")
        print("Usuário:", usuario)
        print("========================")

        print("1 - Listar filmes")
        print("2 - Buscar filme")
        print("3 - Curtir filme")
        print("4 - Descurtir filme")
        print("5 - Criar lista de favoritos")
        print("6 - Adicionar filme na lista de favoritos")
        print("7 - Ver lista de favoritos")
        print("8 - Excluir lista de favoritos")
        print("0 - Logout")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_filmes()

        elif opcao == "2":
            buscar_filme()

        elif opcao == "3":
            curtir_filme(usuario)

        elif opcao == "4":
            descurtir_filme(usuario)

        elif opcao == "5":
            criar_lista_favoritos(usuario)

        elif opcao == "6":
            adicionar_filme_lista(usuario)

        elif opcao == "7":
            ver_favoritos(usuario)

        elif opcao == "8":
            excluir_lista(usuario)

        elif opcao == "0":
            print("Logout realizado.")
            break

        else:
            print("Opção inválida.")

# Função para o menu principal
def menu_principal():

    cadastrar_filmes_iniciais()

    while True:

        print("\n========================")
        print("BEM-VINDO AO FEItv")
        print("========================")

        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":

            usuario = login()

            if usuario != None:
                menu_usuario(usuario)

        elif opcao == "0":
            print("FEItv desligado.")
            break

        else:
            print("Opção inválida.")


menu_principal()
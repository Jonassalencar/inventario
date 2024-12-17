from produtos.eletronico import Eletronico
from produtos.roupa import Roupa
from produtos.alimento import Alimento

# Lista de produtos
produtos = []

def adicionar_produto():
    print("\nAdicionar Produto")
    print("1. Eletrônico")
    print("2. Roupa")
    print("3. Alimento")
    tipo = input("Escolha o tipo de produto (1-3): ")
    
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))
    categoria = input("Categoria do produto: ")

    if tipo == "1":
        garantia = input("Garantia (meses): ")
        produto = Eletronico(nome, preco, quantidade, categoria, garantia)
    elif tipo == "2":
        tamanho = input("Tamanho: ")
        material = input("Material: ")
        produto = Roupa(nome, preco, quantidade, categoria, tamanho, material)
    elif tipo == "3":
        validade = input("Data de validade (YYYY-MM-DD): ")
        peso = float(input("Peso (kg): "))
        produto = Alimento(nome, preco, quantidade, categoria, validade, peso)
    else:
        print("Tipo inválido!")
        return

    produtos.append(produto)
    print(f"Produto {nome} adicionado com sucesso!")

def remover_produto():
    print("\nRemover Produto")
    nome = input("Digite o nome do produto a ser removido: ")
    for produto in produtos:
        if produto.nome.lower() == nome.lower():
            produtos.remove(produto)
            print(f"Produto {nome} removido com sucesso!")
            return
    print(f"Produto {nome} não encontrado!")

def listar_produtos():
    print("\nLista de Produtos")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print(produto)

def aplicar_desconto():
    print("\nAplicar Desconto")
    nome = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto.nome.lower() == nome.lower():
            percentual = float(input("Digite o percentual de desconto: "))
            produto.aplicar_desconto(percentual)
            return
    print(f"Produto {nome} não encontrado!")

def menu():
    while True:
        print("\n--- Sistema de Inventário ---")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Aplicar desconto")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            aplicar_desconto()
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

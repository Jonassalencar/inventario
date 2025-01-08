# main.py
import json
from produtos.produto import Produto
from produtos.eletronico import Eletronico
from produtos.roupa import Roupa
from produtos.alimento import Alimento

def salvar_produtos(produtos, arquivo="produtos.json"):
    """Salva uma lista de objetos Produto em um arquivo JSON."""
    produtos_dict = [produto.to_dict() for produto in produtos]
    with open(arquivo, "w") as f:
        json.dump(produtos_dict, f, indent=4)
    print(f"Produtos salvos em {arquivo}")

def carregar_produtos(arquivo="produtos.json"):
    """Carrega os produtos de um arquivo JSON e retorna uma lista de objetos Produto."""
    try:
        with open(arquivo, "r") as f:
            produtos_dict = json.load(f)
        
        produtos = []
        for produto_data in produtos_dict:
            categoria = produto_data['categoria']
            if categoria == "Eletrônicos":
                produtos.append(Eletronico.from_dict(produto_data))
            elif categoria == "Roupas":
                produtos.append(Roupa.from_dict(produto_data))
            elif categoria == "Alimentos":
                produtos.append(Alimento.from_dict(produto_data))
            else:
                produtos.append(Produto.from_dict(produto_data))
        
        return produtos
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Retornando lista vazia.")
        return []

def main():
    # Exemplo de como adicionar produtos
    produto1 = Eletronico("TV", 1200.0, 10, "Eletrônicos", 24)
    produto2 = Roupa("Camiseta", 50.0, 50, "Roupas", "M", "Algodão")
    produto3 = Alimento("Arroz", 30.0, 100, "Alimentos", "2025-12-31", 5.0)

    produtos = [produto1, produto2, produto3]

    # Salvar produtos em um arquivo JSON
    salvar_produtos(produtos)

    # Carregar produtos do arquivo JSON
    produtos_carregados = carregar_produtos()

    # Listar produtos carregados
    for produto in produtos_carregados:
        print(produto)

if __name__ == "__main__":
    main()

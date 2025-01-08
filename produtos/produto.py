
class Produto:
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade
        self.categoria = categoria

    def to_dict(self):
        return {
            'nome': self.nome,
            'preco': self.preco,
            'quantidade_estoque': self.quantidade_estoque,
            'categoria': self.categoria
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['nome'], data['preco'], data['quantidade_estoque'], data['categoria'])

    def __str__(self):
        return (f"Produto: {self.nome}, Preço: {self.preco}, "
                f"Estoque: {self.quantidade_estoque}, Categoria: {self.categoria}")

    # Métodos adicionais conforme necessário...

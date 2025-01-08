from produtos.produto import Produto


class Alimento(Produto):
    def __init__(self, nome, preco, quantidade, categoria, validade, peso):
        super().__init__(nome, preco, quantidade, categoria)
        self.validade = validade
        self.peso = peso

    def to_dict(self):
        data = super().to_dict()
        data['validade'] = self.validade
        data['peso'] = self.peso
        return data

    @classmethod
    def from_dict(cls, data):
        produto = produto.from_dict(data)
        return cls(produto.nome, produto.preco, produto.quantidade_estoque, produto.categoria, data['validade'], data['peso'])

    def __str__(self):
        return f"{super().__str__()}, Validade: {self.validade}, Peso: {self.peso}kg"

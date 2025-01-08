from produtos.produto import Produto


class Eletronico(Produto):
    def __init__(self, nome, preco, quantidade, categoria, garantia):
        super().__init__(nome, preco, quantidade, categoria)
        self.garantia = garantia

    def to_dict(self):
        data = super().to_dict()
        data['garantia'] = self.garantia
        return data

    @classmethod
    def from_dict(cls, data):
        produto = produto.from_dict(data)
        return cls(produto.nome, produto.preco, produto.quantidade_estoque, produto.categoria, data['garantia'])

    def __str__(self):
        return f"{super().__str__()}, Garantia: {self.garantia} meses"

from produtos.produto import Produto


class Roupa(Produto):
    def __init__(self, nome, preco, quantidade, categoria, tamanho, material):
        super().__init__(nome, preco, quantidade, categoria)
        self.tamanho = tamanho
        self.material = material

    def to_dict(self):
        data = super().to_dict()
        data['tamanho'] = self.tamanho
        data['material'] = self.material
        return data

    @classmethod
    def from_dict(cls, data):
        produto = produto.from_dict(data)
        return cls(produto.nome, produto.preco, produto.quantidade_estoque, produto.categoria, data['tamanho'], data['material'])

    def __str__(self):
        return f"{super().__str__()}, Tamanho: {self.tamanho}, Material: {self.material}"

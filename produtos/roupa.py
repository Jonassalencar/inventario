from produtos.produto import Produto

class Roupa(Produto):
    def __init__(self, nome, preco, quantidade, categoria, tamanho, material):
        super().__init__(nome, preco, quantidade, categoria)
        self.tamanho = tamanho
        self.material = material

    def __str__(self):
        return (f"{super().__str__()}, Tamanho: {self.tamanho}, "
                f"Material: {self.material}")

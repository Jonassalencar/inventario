from produtos.produto import Produto

class Eletronico(Produto):
    def __init__(self, nome, preco, quantidade, categoria, garantia):
        super().__init__(nome, preco, quantidade, categoria)
        self.garantia = garantia

    def __str__(self):
        return f"{super().__str__()}, Garantia: {self.garantia} meses"

from produtos.produto import Produto

class Alimento(Produto):
    def __init__(self, nome, preco, quantidade, categoria, validade, peso):
        super().__init__(nome, preco, quantidade, categoria)
        self.validade = validade
        self.peso = peso

    def __str__(self):
        return (f"{super().__str__()}, Validade: {self.validade}, "
                f"Peso: {self.peso}kg")

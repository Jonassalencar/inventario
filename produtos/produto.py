class Produto:
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade  # Correto
        self.categoria = categoria
    
    def __str__(self):
        return (f"Produto: {self.nome}, Preço: {self.preco}, "
                f"Estoque: {self.quantidade_estoque}, Categoria: {self.categoria}")  # Corrigido

    def adicionar_estoque(self, qtd):
        self.quantidade_estoque += qtd

    def remover_estoque(self, qtd):
        if qtd <= self.quantidade_estoque:
            self.quantidade_estoque -= qtd
        else:
            print("Estoque insuficiente!")

    def exibir_informacoes(self):
        return f"Produto: {self.nome}, Preço: {self.preco}, Estoque: {self.quantidade_estoque}, Categoria: {self.categoria}"

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem / 100)
        self.preco -= desconto
        print(f"Desconto aplicado! Novo preço: {self.preco}")

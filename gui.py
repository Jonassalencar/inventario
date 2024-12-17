import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from produtos.produto import Produto
from produtos.eletronico import Eletronico
from produtos.roupa import Roupa
from produtos.alimento import Alimento

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventário")
        self.produtos = []

        # Criando a interface
        self.criar_widgets()

    def criar_widgets(self):
        # Título
        self.titulo = tk.Label(self.root, text="Sistema de Inventário", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Botões
        self.botao_adicionar = tk.Button(self.root, text="Adicionar Produto", command=self.adicionar_produto)
        self.botao_adicionar.pack(pady=5)

        self.botao_listar = tk.Button(self.root, text="Listar Produtos", command=self.listar_produtos)
        self.botao_listar.pack(pady=5)

        self.botao_aplicar_desconto = tk.Button(self.root, text="Aplicar Desconto", command=self.aplicar_desconto)
        self.botao_aplicar_desconto.pack(pady=5)

    def adicionar_produto(self):
        # Tela para adicionar um produto
        adicionar_janela = tk.Toplevel(self.root)
        adicionar_janela.title("Adicionar Produto")

        tk.Label(adicionar_janela, text="Nome do Produto:").pack()
        nome_entry = tk.Entry(adicionar_janela)
        nome_entry.pack()

        tk.Label(adicionar_janela, text="Preço do Produto:").pack()
        preco_entry = tk.Entry(adicionar_janela)
        preco_entry.pack()

        tk.Label(adicionar_janela, text="Quantidade em Estoque:").pack()
        quantidade_entry = tk.Entry(adicionar_janela)
        quantidade_entry.pack()

        tk.Label(adicionar_janela, text="Categoria do Produto:").pack()
        categoria_entry = tk.Entry(adicionar_janela)
        categoria_entry.pack()

        tk.Label(adicionar_janela, text="Tipo de Produto:").pack()
        tipo_var = tk.StringVar()
        tipo_var.set("Eletrônico")

        tipo_menu = tk.OptionMenu(adicionar_janela, tipo_var, "Eletrônico", "Roupa", "Alimento")
        tipo_menu.pack()

        def salvar_produto():
            nome = nome_entry.get()
            preco = float(preco_entry.get())
            quantidade = int(quantidade_entry.get())
            categoria = categoria_entry.get()
            tipo_produto = tipo_var.get()

            if tipo_produto == "Eletrônico":
                garantia = tk.simpledialog.askinteger("Garantia", "Meses de garantia?")
                produto = Eletronico(nome, preco, quantidade, categoria, garantia)
            elif tipo_produto == "Roupa":
                tamanho = tk.simpledialog.askstring("Tamanho", "Tamanho da roupa?")
                material = tk.simpledialog.askstring("Material", "Material da roupa?")
                produto = Roupa(nome, preco, quantidade, categoria, tamanho, material)
            else:
                validade = tk.simpledialog.askstring("Validade", "Data de validade?")
                peso = float(tk.simpledialog.askstring("Peso", "Peso do produto em kg"))
                produto = Alimento(nome, preco, quantidade, categoria, validade, peso)

            self.produtos.append(produto)
            messagebox.showinfo("Sucesso", f"{nome} foi adicionado com sucesso!")
            adicionar_janela.destroy()

        tk.Button(adicionar_janela, text="Salvar", command=salvar_produto).pack()

    def listar_produtos(self):
        # Tela para listar os produtos
        listar_janela = tk.Toplevel(self.root)
        listar_janela.title("Lista de Produtos")

        for produto in self.produtos:
            produto_info = produto.__str__()
            tk.Label(listar_janela, text=produto_info).pack()

    def aplicar_desconto(self):
        # Tela para aplicar desconto
        desconto_janela = tk.Toplevel(self.root)
        desconto_janela.title("Aplicar Desconto")

        tk.Label(desconto_janela, text="Produto (Escolha índice):").pack()
        produto_var = tk.StringVar()
        produto_menu = tk.OptionMenu(desconto_janela, produto_var, *[produto.nome for produto in self.produtos])
        produto_menu.pack()

        tk.Label(desconto_janela, text="Porcentagem de desconto:").pack()
        desconto_entry = tk.Entry(desconto_janela)
        desconto_entry.pack()

        def aplicar():
            produto_nome = produto_var.get()
            desconto = float(desconto_entry.get())

            for produto in self.produtos:
                if produto.nome == produto_nome:
                    produto.aplicar_desconto(desconto)
                    break

            desconto_janela.destroy()

        tk.Button(desconto_janela, text="Aplicar", command=aplicar).pack()

# Inicializando a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()

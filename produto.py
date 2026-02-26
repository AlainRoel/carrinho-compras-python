class Produto:
    def __init__(self, nome, preco, quantidade=1):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.preco * self.quantidade

    def __str__(self):
        return f"{self.nome} | R$ {self.preco:.2f} | Qtd: {self.quantidade} | Subtotal: R$ {self.calcular_subtotal():.2f}"

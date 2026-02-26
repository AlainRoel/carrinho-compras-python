from produto import Produto


class Carrinho:
    def __init__(self):
        self.produtos = []  # Lista de produtos
        self.desconto = 0

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():
                self.produtos.remove(produto)
                return True
        return False

    def calcular_total(self):
        total = sum(produto.calcular_subtotal() for produto in self.produtos)
        return total - self.desconto

    def aplicar_desconto(self, valor):
        self.desconto = valor

    def gerar_nota_fiscal(self):
        print("\n========= NOTA FISCAL =========")
        for produto in self.produtos:
            print(produto)
        print("--------------------------------")
        print(f"Desconto: R$ {self.desconto:.2f}")
        print(f"TOTAL FINAL: R$ {self.calcular_total():.2f}")
        print("================================\n")

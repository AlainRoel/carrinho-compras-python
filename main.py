from produto import Produto
from carrinho import Carrinho


def menu():
    carrinho = Carrinho()

    while True:
        print("1 - Adicionar Produto")
        print("2 - Remover Produto")
        print("3 - Aplicar Desconto")
        print("4 - Ver Nota Fiscal")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: ").replace(",", "."))
            quantidade = int(input("Quantidade: "))
            produto = Produto(nome, preco, quantidade)
            carrinho.adicionar_produto(produto)
            print("Produto adicionado com sucesso!\n")

        elif opcao == "2":
            nome = input("Digite o nome do produto a remover: ")
            if carrinho.remover_produto(nome):
                print("Produto removido!\n")
            else:
                print("Produto não encontrado!\n")

        elif opcao == "3":
            desconto = float(input("Valor do desconto: "))
            carrinho.aplicar_desconto(desconto)
            print("Desconto aplicado!\n")

        elif opcao == "4":
            carrinho.gerar_nota_fiscal()

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    menu()

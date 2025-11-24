def mostrar_produtos(catalogo):
    """Mostra todos os produtos disponíveis e o preço."""
    print("\n--- PRODUTOS DISPONÍVEIS ---")
    # O ciclo 'for' percorre o dicionário. 'item' é o nome, 'preco' é o valor.
    for item, preco in catalogo.items():
        # f-string ajuda a formatar o texto bonitinho
        print(f"- {item}: R$ {preco:.2f}")
    print("----------------------------")


def calcular_total(carrinho):
    """Soma os preços de tudo o que está no carrinho."""
    total = sum(carrinho)  # A função sum() soma todos os números de uma lista
    return total


def main():
    # 1. Criação do Catálogo (Dicionário: Nome -> Preço)
    catalogo = {
        "Camiseta": 29.90,
        "Calça": 89.90,
        "Tênis": 120.00,
        "Boné": 15.00,
        "Meias": 9.50
    }

    # 2. Criação do Carrinho (Lista vazia para começar)
    carrinho_precos = []
    carrinho_nomes = []

    print("Bem-vindo à Loja Python!")

    while True:
        # Menu principal
        print("\nO que deseja fazer?")
        print("1. Ver Produtos")
        print("2. Adicionar Produto ao Carrinho")
        print("3. Ver Meu Carrinho")
        print("4. Finalizar Compra (Sair)")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            mostrar_produtos(catalogo)

        elif opcao == "2":
            mostrar_produtos(catalogo)
            escolha = input("Digite o nome do produto que quer comprar: ").capitalize()
            # .capitalize() ajuda se a pessoa escrever 'camiseta' minúsculo.

            if escolha in catalogo:
                preco = catalogo[escolha]
                carrinho_nomes.append(escolha)  # Guarda o nome
                carrinho_precos.append(preco)  # Guarda o preço
                print(f"Sucesso! {escolha} adicionado por R$ {preco:.2f}")
            else:
                print("Erro: Produto não encontrado. Verifique a ortografia.")

        elif opcao == "3":
            print("\n--- SEU CARRINHO ---")
            if not carrinho_nomes:
                print("O carrinho está vazio.")
            else:
                for i in range(len(carrinho_nomes)):
                    print(f"{carrinho_nomes[i]} - R$ {carrinho_precos[i]:.2f}")
                print(f"Total parcial: R$ {sum(carrinho_precos):.2f}")

        elif opcao == "4":
            total = calcular_total(carrinho_precos)
            print("\n--- NOTA FISCAL ---")
            print(f"Você comprou {len(carrinho_nomes)} itens.")
            print(f"TOTAL A PAGAR: R$ {total:.2f}")
            print("Obrigado por comprar connosco!")
            break  # O 'break' para o loop while e encerra o programa

        else:
            print("Opção inválida. Tente novamente.")


# Esta linha faz o programa começar
if __name__ == "__main__":
    main()

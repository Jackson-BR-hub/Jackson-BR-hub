def exibir_menu():
    print("=== Gerenciador de Estoque ===")
    print("1. Adicionar produto")
    print("2. Atualizar quantidade")
    print("3. Remover produto")
    print("4. Visualizar estoque")
    print("5. Sair")

def adicionar_produto(estoque):
    produto = input("Digite o nome do produto: ")
    if produto in estoque:
        print(f"O produto '{produto}' já existe no estoque.")
    else:
        quantidade = int(input("Digite a quantidade do produto: "))
        estoque[produto] = quantidade
        print(f"Produto '{produto}' adicionado com sucesso.")

def atualizar_quantidade(estoque):
    produto = input("Digite o nome do produto: ")
    if produto in estoque:
        quantidade = int(input("Digite a nova quantidade do produto: "))
        estoque[produto] = quantidade
        print(f"Quantidade do produto '{produto}' atualizada para {quantidade}.")
    else:
        print(f"O produto '{produto}' não existe no estoque.")

def remover_produto(estoque):
    produto = input("Digite o nome do produto: ")
    if produto in estoque:
        del estoque[produto]
        print(f"Produto '{produto}' removido com sucesso.")
    else:
        print(f"O produto '{produto}' não existe no estoque.")

def visualizar_estoque(estoque):
    if estoque:
        print("=== Estoque Atual ===")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade}")
    else:
        print("O estoque está vazio.")

def main():
    estoque = {}
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            atualizar_quantidade(estoque)
        elif opcao == '3':
            remover_produto(estoque)
        elif opcao == '4':
            visualizar_estoque(estoque)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

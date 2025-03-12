from registrationAnalyzer import load_csv, add_person, update_person, delete_person, find_person, analyze_data, list_people

# Menu principal
def menu():
    try:
        records = load_csv()  # Carrega dados do arquivo
    except Exception as e:
        print(f"Erro ao carregar registros: {e}")
        records = []  # Inicializa uma lista vazia em caso de erro

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar pessoa")
        print("2. Alterar pessoa")
        print("3. Apagar pessoa")
        print("4. Buscar pessoa")
        print("5. Analisar dados")
        print("6. Listar pessoas")
        print("7. Sair")
        option = input("Escolha uma opção: ")

        try:
            if option == '1':
                add_person(records)  # Adiciona uma nova pessoa
            elif option == '2':
                update_person(records)  # Altera os dados de uma pessoa
            elif option == '3':
                delete_person(records)  # Apaga uma pessoa
            elif option == '4':
                find_person(records)  # Busca uma pessoa
            elif option == '5':
                analyze_data(records)  # Analisa os dados
            elif option == '6':
                list_people(records)  # Lista todas as pessoas
            elif option == '7':
                break  
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Erro durante a execução: {e}")

# Executar o programa
if __name__ == "__main__":
    menu()

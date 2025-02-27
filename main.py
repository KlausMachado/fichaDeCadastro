from registrationAnalyzer import load_records, add_record, update_record, delete_record, find_record, analyze_data, list_records

# Menu principal
def menu():
    try:
        records = load_records()  # Carrega dados do arquivo
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
                add_record(records)  # Adiciona uma nova pessoa
            elif option == '2':
                update_record(records)  # Altera os dados de uma pessoa
            elif option == '3':
                delete_record(records)  # Apaga uma pessoa
            elif option == '4':
                find_record(records)  # Busca uma pessoa
            elif option == '5':
                analyze_data(records)  # Analisa os dados
            elif option == '6':
                list_records(records)  # Lista todas as pessoas
            elif option == '7':
                break  
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Erro durante a execução: {e}")

# Executar o programa
if __name__ == "__main__":
    menu()
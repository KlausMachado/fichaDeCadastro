import csv
import os
from form import Register

# Cria arquivo CSV com os dados
def save_records(records, file='records.csv'):
    try:
        with open(file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Code', 'Name', 'Age', 'Gender'])  # Cabeçalho
            for record in records:
                writer.writerow([record.code, record.name, record.age, record.gender])
    except PermissionError:
        print("Erro: Sem permissão para escrever no arquivo.")
    except Exception as e:
        print(f"Erro ao salvar registros: {e}")

# Carrega os dados do arquivo CSV
def load_records(file='records.csv'):
    records = []
    try:
        if os.path.exists(file):  # Verifica se o arquivo existe
            with open(file, mode='r') as file:  # Faz a leitura
                reader = csv.reader(file)  # Lê os dados
                next(reader)  # Pula o cabeçalho
                for row in reader:
                    try:
                        records.append(Register(int(row[0]), row[1], int(row[2]), row[3]))
                    except (ValueError, IndexError):
                        print(f"Erro: Formato inválido no arquivo na linha: {row}")
        else:
            print("Arquivo não encontrado. Criando um novo arquivo.")
    except PermissionError:
        print("Erro: Sem permissão para ler o arquivo.")
    except Exception as e:
        print(f"Erro ao carregar registros: {e}")
    return records

# Adiciona um novo registro
def add_record(records):
    try:
        while True:
            code = int(input("Digite o código: "))

            # Verifica se o código já existe
            codigo_existente = False
            for record in records:
                if record.code == code:
                    print("Erro: Código já existe. Por favor, insira um código único.")
                    code_exist = True
                    break

            if not code_exist:
                break  # Sai do loop se o código for novo

        name = input("Digite o nome: ")
        age = int(input("Digite a idade: "))
        gender = input("Digite o gênero: ")

        # Adiciona o novo registro
        records.append(Register(code, name, age, gender))
        save_records(records)
        print("Pessoa adicionada com sucesso!")
    except ValueError:
        print("Erro: Idade e código devem ser números.")
    except Exception as e:
        print(f"Erro ao adicionar pessoa: {e}") #{e} exibe o erro

# Altera um registro existente
def update_record(records):
    try:
        code = int(input("Digite o código da pessoa que deseja alterar: "))
        for record in records:
            if record.code == code:
                record.name = input("Novo nome: ")
                record.age = int(input("Nova idade: "))
                record.gender = input("Novo gênero: ")
                save_records(records)
                print("Pessoa alterada com sucesso!")
                return
        print("Pessoa não encontrada.")
    except ValueError:
        print("Erro: Código e idade devem ser números.")
    except Exception as e:
        print(f"Erro ao alterar pessoa: {e}")

# Remove um registro
def delete_record(records):
    try:
        code = int(input("Digite o código da pessoa que deseja apagar: "))
        for record in records:
            if record.code == code:
                records.remove(record)
                save_records(records)
                print("Pessoa apagada com sucesso!")
                return
        print("Pessoa não encontrada.")
    except ValueError:
        print("Erro: Código deve ser um número.")
    except Exception as e:
        print(f"Erro ao apagar pessoa: {e}")

# Busca um registro
def find_record(records):
    try:
        code = int(input("Digite o código da pessoa que deseja encontrar: "))
        for record in records:
            if record.code == code:
                print(record)
                return
        print("Pessoa não encontrada.")
    except ValueError:
        print("Erro: Código deve ser um número.")
    except Exception as e:
        print(f"Erro ao buscar pessoa: {e}")

# Analisa os dados
def analyze_data(records):
    try:
        if not records:
            print("Nenhum dado para analisar.")
            return

        # Ordena por idade
        sorted_records = sorted(records, key=lambda x: x.age) #função lambda retorna dados de idade
        print("\nDados ordenados por idade:")
        for record in sorted_records:
            print(record)

        # Identifica o mais velho e o mais novo
        oldest = max(records, key=lambda x: x.age)
        youngest = min(records, key=lambda x: x.age)
        print(f"\nPessoa mais velha: {oldest.name} ({oldest.age} anos)")
        print(f"Pessoa mais nova: {youngest.name} ({youngest.age} anos)")
    except Exception as e:
        print(f"Erro ao analisar dados: {e}")

# Lista todos os registros
def list_records(records):
    try:
        if not records:
            print("Nenhum registro encontrado.")
        else:
            print("\nLista de pessoas cadastradas:")
            for record in records:
                print(record)
    except Exception as e:
        print(f"Erro ao listar registros: {e}")
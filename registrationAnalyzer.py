import csv
import os
from datetime import datetime
from form import Register

current_year = datetime.now().year

def validate_born_year(year):
    #validando se o ano de nascimneto é maior que 1900 e menor que o ano atual
    return 1900 <= year <= current_year
    
def validate_code(code, records):
    #verificando se código ja existe na lista
    return any(record.code == code for record in records)
    
#funções de analise de dados:
def analyze_gender(records):

    if not records:
        print("Nenhum dado para analisar.")
        return
        
    #ordena por genero
    sorted_records_gender = sorted(records, key=lambda x: x.gender)

    # Dicionário para agrupar pessoas por gênero
    grupos_genero = {
        'F': "As mulheres listadas no arquivo são:",
        'MT': "As mulheres listadas no arquivo são:",
        'NB': "As pessoas não binárias listadas no arquivo são:",
        'M': "Os homens listados no arquivo são:",
        'HT': "Os homens listados no arquivo são:",
    }

    # Exibe os resultados agrupados por gênero
    print("\nDados ordenados por gênero:")
    genero_atual = None
    for record in sorted_records_gender:
        if record.gender != genero_atual:
            genero_atual = record.gender
            print(f"\n{grupos_genero.get(genero_atual, f'As pessoas do gênero {genero_atual} listadas são:')}")
        print(f"Código: {record.code}, Nome: {record.name}")    

def analyze_age(records):
    if not records:
        print("Nenhum dado para analisar.")
        return

    # Ordena por idade
    sorted_records_age = sorted(records, key=lambda x: x.age) #função lambda retorna dados de idade
    print("\nDados ordenados por idade:")
    for record in sorted_records_age:
        print(f"Código: {record.code}, Nome: {record.name}, Idade: {record.age}")            
        
    # Identifica o mais velho e o mais novo
    oldest = max(records, key=lambda x: x.age)
    youngest = min(records, key=lambda x: x.age)
    print(f"\nPessoa mais velha: {oldest.name} ({oldest.age} anos)")
    print(f"Pessoa mais nova: {youngest.name} ({youngest.age} anos)")    


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
        code = int(input("Digite o código: "))

        # Verifica se o código já existe
        if validate_code(code, records):
            print("Erro: Código já existe. Por favor, insira um código único.")
            return        

        name = input("Digite o nome: ")
        year = int(input("Digite o ano de nascimento (2000): "))
        if not validate_born_year(year):
            print("Erro: Ano de nascimento invalido.")
            return    
        age = current_year - year
            
        gender = input("Digite o gênero: (\nF = Mulher cis;\nM = Homem cis;\nNB = Não binarie;\nMT = Mulher Trans;\nHT = Homem Trans;\nGQ = Genero Queer;) ").upper().strip()

        # Adiciona o novo registro
        records.append(Register(code, name, age, gender))
        save_records(records)
        print("Pessoa adicionada com sucesso!")
    except ValueError:
        print("Erro:Ano e código devem ser números.")
    except Exception as e:
        print(f"Erro ao adicionar pessoa: {e}") #{e} exibe o erro

# Altera um registro existente
def update_record(records):
    try:
        code = int(input("Digite o código da pessoa que deseja alterar: "))
        for record in records:
            if record.code == code:                        
                record.name = input("Novo nome: ")
                year = int(input("Novo ano de nascimento: "))
                if not validate_born_year(year):
                    print("Erro: Ano de nascimento invalido.")
                    return
                    
                age = current_year - year
                record.gender = input("Novo gênero: ").upper().strip()
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
        analyze_age(records)
        analyze_gender(records)

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

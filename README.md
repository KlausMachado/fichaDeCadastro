# 📋 Sistema de Cadastro e Análise de Pessoas

Este é um projeto em Python que permite cadastrar, gerenciar e analisar dados de pessoas. O sistema oferece funcionalidades como adicionar, alterar, apagar, buscar e listar registros, além de realizar análises como ordenação por idade e identificação da pessoa mais velha e mais nova.

---

## 🚀 Funcionalidades

- **Adicionar pessoa**: Cadastra uma nova pessoa com código, nome, idade e gênero.
- **Alterar pessoa**: Atualiza os dados de uma pessoa existente.
- **Apagar pessoa**: Remove uma pessoa do cadastro.
- **Buscar pessoa**: Localiza uma pessoa pelo código.
- **Listar pessoas**: Exibe todas as pessoas cadastradas.
- **Analisar dados**: Ordena as pessoas por idade e identifica a mais velha e a mais nova.
- **Armazenamento em CSV**: Os dados são salvos em um arquivo CSV para persistência.

---

## 📂 Estrutura do Projeto

O projeto é organizado em três arquivos principais:

1. **`forms.py`**: Contém a classe `Register`, que representa uma pessoa cadastrada.
2. **`registrationAnalyzer.py`**: Contém as funções para manipulação dos dados (CRUD) e análise.
3. **`main.py`**: Contém o menu principal e a lógica de interação com o usuário.

---

## 🛠️ Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.
- Biblioteca `csv` (já incluída na biblioteca padrão do Python).

### Passos para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```

4. Siga as instruções do menu para interagir com o sistema.

---

## 🧩 Exemplo de Uso

### Menu Principal

```
--- Menu ---
1. Adicionar pessoa
2. Alterar pessoa
3. Apagar pessoa
4. Buscar pessoa
5. Analisar dados
6. Listar pessoas
7. Sair
Escolha uma opção:
```

### Adicionar uma Pessoa

```
Digite o código: 1
Digite o nome: João
Digite a idade: 25
Digite o gênero: Masculino
Pessoa adicionada com sucesso!
```

### Listar Pessoas

```
Lista de pessoas cadastradas:
Codigo: 1
Nome: João
Idade: 25
Genero: Masculino
```

### Analisar Dados

```
Dados ordenados por idade:
Codigo: 1
Nome: João
Idade: 25
Genero: Masculino

Pessoa mais velha: João (25 anos)
Pessoa mais nova: João (25 anos)
```

---

## 🛑 Tratamento de Erros

O sistema inclui tratamento de erros para garantir uma experiência robusta e amigável. Alguns exemplos de erros tratados:

- **Código duplicado**: Impede a adição de um código já existente.
- **Entradas inválidas**: Valida se o usuário digitou números onde esperado (por exemplo, código e idade).
- **Arquivo não encontrado**: Cria um novo arquivo CSV se ele não existir.
- **Permissões de arquivo**: Exibe mensagens claras em caso de problemas de leitura/escrita.

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

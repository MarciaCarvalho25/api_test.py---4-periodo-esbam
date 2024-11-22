# Testes de API

Este repositório contém testes automatizados para várias APIs, como APIs de 
livros, jogos, feriados, horóscopos e receitas. Os testes foram realizados 
utilizando a biblioteca (pytest) e a ferramenta (responses) para simular 
respostas da API.

## Explicação dos Comentários:
Comentando o propósito do teste: Em cada função de teste, os comentários 
explicam o que está sendo testado. Por exemplo, no teste de "Busca por título 
de livro", ele verifica se a resposta da API retorna corretamente o título e o autor.

Simulação de Respostas: Usei a biblioteca responses para simular a resposta da API.
Isso é feito para garantir que os testes não dependam de uma API real e que possam 
ser executados em qualquer ambiente.

Verificação de Status Code: Cada teste começa verificando se a resposta tem o status
code correto (normalmente 200 para sucesso e 400 para erro).

Validação de Dados: A validação de dados envolve verificar se os dados retornados pela 
API estão no formato esperado, como garantir que o "signo" no horóscopo seja correto ou 
que a lista de ingredientes de uma receita contenha o item esperado.

# No Windows
python -m venv venv
.\venv\Scripts\activate

# Dependências do projeto
pip install -r requirements.txt

# Arquivos de Configuração
requirements.txt

# Este arquivo contém as bibliotecas necessárias para rodar os testes, aqui:
pytest==8.3.3
responses==0.22.0
requests==2.31.0

- requirements.txt

- Contém as versões exatas das bibliotecas necessárias para o funcionamento dos testes. 
As bibliotecas principais incluem: 

- pytest: para rodar os testes.
- responses: para simular as respostas das APIs durante os testes.
- requests: para fazer as requisições HTTP durante os testes.


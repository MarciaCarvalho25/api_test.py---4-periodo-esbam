import pytest
import responses
import requests

# Teste para busca por título de livro
@responses.activate
def test_busca_por_titulo_sucesso():
    # Simula a resposta da API com um livro fictício
    responses.add(responses.GET, 'https://api.exemplo-de-livros.com/api/v1/livros',
                  json={'titulo': 'Harry Potter', 'autor': 'J.K. Rowling'}, status=200) 

    # Faz a requisição para a API
    response = requests.get('https://api.exemplo-de-livros.com/api/v1/livros')

    # Verifica se a resposta foi bem-sucedida (status code 200)
    assert response.status_code == 200

    # Verifica se o título do livro retornado é "Harry Potter"
    assert response.json()['titulo'] == 'Harry Potter'

    # Verifica se o autor retornado é "J.K. Rowling"
    assert response.json()['autor'] == 'J.K. Rowling'


# Teste para verificar os jogos populares
@responses.activate
def test_jogos_populares_sucesso():
    # Simula a resposta da API para jogos populares
    responses.add(responses.GET, 'https://api.exemplo-de-jogos.com/api/v1/jogos/populares',
                  json=[{'nome': 'The Witcher 3'}, {'nome': 'Cyberpunk 2077'}], status=200)

    # Faz a requisição para a API
    response = requests.get('https://api.exemplo-de-jogos.com/api/v1/jogos/populares')

    # Verifica se a resposta foi bem-sucedida (status code 200)
    assert response.status_code == 200

    # Verifica se "The Witcher 3" está na lista de jogos populares
    assert 'The Witcher 3' in [jogo['nome'] for jogo in response.json()]


# Teste para buscar feriados por país e ano
@responses.activate
def test_feriados_por_pais_e_ano():
    # Simula a resposta da API com dados de feriados para o ano de 2024 nos EUA
    responses.add(responses.GET, 'https://api.exemplo-de-feriados.com/api/v1/feriados/US/2024',
                  json=[{'data': '2024-01-01', 'descricao': 'New Year\'s Day'}], status=200)

    # Faz a requisição para a API
    response = requests.get('https://api.exemplo-de-feriados.com/api/v1/feriados/US/2024')

    # Verifica se a resposta foi bem-sucedida (status code 200)
    assert response.status_code == 200

    # Verifica se o feriado "New Year\'s Day" está presente na resposta
    assert 'New Year\'s Day' in [feriado['descricao'] for feriado in response.json()]


# Teste para buscar horóscopo do dia
@responses.activate
def test_horoscopo_hoje():
    # Simula a resposta da API com o horóscopo para o signo de Áries
    responses.add(responses.GET, 'https://api.exemplo-de-horoscopo.com/api/v1/horoscopo/aries',
                  json={'signo': 'Áries', 'previsao': 'Hoje será um bom dia!'}, status=200)

    # Faz a requisição para a API
    response = requests.get('https://api.exemplo-de-horoscopo.com/api/v1/horoscopo/aries')

    # Verifica se a resposta foi bem-sucedida (status code 200)
    assert response.status_code == 200

    # Verifica se a previsão contém a mensagem "Hoje será um bom dia!"
    assert 'Hoje será um bom dia!' in response.json()['previsao']


# Teste para buscar receitas por ingredientes
@responses.activate
def test_receitas_por_ingredientes():
    # Simula a resposta da API com receitas contendo "tomate" como ingrediente
    responses.add(responses.GET, 'https://api.exemplo-de-receitas.com/api/v1/receitas?ingredientes=tomate',
                  json=[{'nome': 'Salada de Tomate', 'ingredientes': ['tomate', 'cebola']}], status=200)

    # Faz a requisição para a API
    response = requests.get('https://api.exemplo-de-receitas.com/api/v1/receitas?ingredientes=tomate')

    # Verifica se a resposta foi bem-sucedida (status code 200)
    assert response.status_code == 200

    # Verifica se a receita contém "tomate" nos ingredientes
    assert 'tomate' in response.json()[0]['ingredientes']


# Teste para verificar erro de ano inválido nos feriados
@responses.activate
def test_erro_ano_invalido_feriados():
    # Simula a resposta de erro da API quando o ano fornecido é inválido
    responses.add(responses.GET, 'https://api.exemplo-de-feriados.com/api/v1/feriados/US/invalid_year',
                  json={'erro': 'Ano inválido'}, status=400)

    # Faz a requisição para a API
    response = requests.get('https://api.exemplo-de-feriados.com/api/v1/feriados/US/invalid_year')

    # Verifica se o status code é 400 (erro de requisição)
    assert response.status_code == 400

    # Verifica se a resposta contém a mensagem de erro 'Ano inválido'
    assert 'Ano inválido' in response.json()['erro']


# Teste para verificar signo inválido no horóscopo
@responses.activate
def test_signo_invalido_horoscopo():
    # Simula a resposta de erro da API quando o signo fornecido é inválido
    responses.add(responses.GET, 'https://api.exemplo-de-horoscopo.com/api/v1/horoscopo/invalid_signo',
                  json={'erro': 'Signo inválido'}, status=400)

    # Faz a requisição para a API
    response = requests.get('https://api.exemplo-de-horoscopo.com/api/v1/horoscopo/invalid_signo')

    # Verifica se o status code é 400 (erro de requisição)
    assert response.status_code == 400

    # Verifica se a resposta contém a mensagem de erro 'Signo inválido'
    assert 'Signo inválido' in response.json()['erro']


# Teste para verificar parâmetro inválido na busca de livros
@responses.activate
def test_parametro_invalido_livros():
    # Simula a resposta de erro da API quando o parâmetro de busca é inválido
    responses.add(responses.GET, 'https://api.exemplo-de-livros.com/api/v1/livros?titulo=',
                  json={'erro': 'Parâmetro inválido'}, status=400)

    # Faz a requisição para a API
    response = requests.get('https://api.exemplo-de-livros.com/api/v1/livros?titulo=')

    # Verifica se o status code é 400 (erro de requisição)
    assert response.status_code == 400

    # Verifica se a resposta contém a mensagem de erro 'Parâmetro inválido'
    assert 'Parâmetro inválido' in response.json()['erro']

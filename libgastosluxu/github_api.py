import requests

def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github

    :param usuario: str com o nome de usuário no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

def busca_cep(nro_cep):
    """
        Busca as informações de um determinado CEP

        :param usuario: int numero do cep
        :return: str informações do logradouro
    """
    url = f'http://www.viacep.com.br/ws/{nro_cep}/json'
    resp = requests.get(url)
    return resp.json()['logradouro']

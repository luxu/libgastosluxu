import requests


def busca_cep(nro_cep):
    """
        Busca as informações de um determinado CEP

        :param usuario: int numero do cep
        :return: str informações do logradouro
    """
    url = f'http://www.viacep.com.br/ws/{nro_cep}/json'
    resp = requests.get(url)
    return resp.json()['logradouro']

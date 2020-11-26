from unittest.mock import Mock

from libgastosluxu import github_api


def test_busca_logradouro_com_mock():
    nro_cep = '19013060'
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'cep': '19013060',
        'logradouro': 'Avenida Marechal Deodoro',
        'bairro': 'Vila São Jorge',
        'localidade': 'Presidente Prudente'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    cep = github_api.busca_cep(nro_cep)
    assert 'Avenida Marechal Deodoro' == cep

def test_busca_logradouro_sem_mock():
    nro_cep = '19013060'
    assert 'Avenida Marechal Deodoro' == github_api.busca_cep(nro_cep)

from unittest.mock import Mock

from libgastosluxu import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'luxu',
        'id': 1096573,
        'avatar_url': 'https://avatars0.githubusercontent.com/u/1096573?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('luxu')
    assert 'https://avatars0.githubusercontent.com/u/1096573?v=4' == url

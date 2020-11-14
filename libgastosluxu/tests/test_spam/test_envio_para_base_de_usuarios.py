import pytest

from libgastosluxu.spam.enviador_de_email import Enviador
from libgastosluxu.spam.main import EnviadorDeSpam
from libgastosluxu.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Luciano', email='contato@luxu.com.br'),
            Usuario(nome='Renzo', email='contato@luxu.com.br')
        ],
        [
            Usuario(nome='Luciano', email='contato@luxu.com.br'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'contato@luxu.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Luciano', email='contato@luxu.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'publicarnowordpress@luxu.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'publicarnowordpress@luxu.com.br',
        'contato@luxu.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

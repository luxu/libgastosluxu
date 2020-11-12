import pytest

from libgastosluxu.spam.spam.test_enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['contato@luxu.com.br', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'zicadopv@gmail.com',
        'Cursos Python Pro',
        'Turma Jessica Ferrari'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'contato']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'zicadopv@gmail.com',
            'Cursos Python Pro',
            'Turma Jessica Ferrari'
        )

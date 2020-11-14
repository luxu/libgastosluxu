from libgastosluxu.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Luciano', email='contato@luxu.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Luciano', email='contato@luxu.com.br'),
        Usuario(nome='Renzo', email='contato@luxu.com.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

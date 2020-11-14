from libgastosluxu.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Luciano')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Luciano'),
        Usuario(nome='Renzo')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

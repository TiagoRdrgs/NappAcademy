from ecommerce.classes.Cliente import Cliente
import pytest

class TestCliente:
    def test_class_declared(self):
        objeto = Cliente(nome='John Doe')
        assert isinstance(objeto, Cliente)

    def test_instanciar_objeto(self):
        objeto = Cliente(nome='José da Silva')
        assert objeto.nome, 'José da Silva'

    def test_instanciar_objeto_2(self):
        objeto = Cliente(nome='José da Silva', idade=19)
        assert objeto.nome, 'José da Silva'
        assert objeto.idade == 19
        assert objeto.rg == ''


    def test_setter(self):
        objeto = Cliente(nome='José da Silva')
        assert objeto.nome == 'José da Silva'
        objeto.nome = 'José da Silva Júnior'
        assert objeto.nome == 'José da Silva Júnior'

    def test_setter_2(self):
        objeto = Cliente(nome='José da Silva', idade=23)
        assert objeto.nome == 'José da Silva'
        assert objeto.idade == 23
        objeto.nome = 'José da Silva Júnior'
        objeto.idade = 22
        assert objeto.nome == 'José da Silva Júnior'
        assert objeto.idade == 22

    def test_str_repr(self):
        cliente = Cliente(nome='José da Silva')
        assert str(cliente) == 'José da Silva'
        assert repr(cliente) == 'Cliente: José da Silva'

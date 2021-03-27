from rh.classes.Departamento import Departamento
from datetime import date, timedelta

class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento(nome_setor='Departamento XYZ')
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento(nome_setor='Departamento XYZ')
        assert objeto.nome == 'Departamento XYZ'
        assert objeto.responsavel == 'José da Silva'

    def test_str_repr(self):
        objeto = Departamento(nome_setor='Departamento XYZ')
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento(nome_setor='Curadoria')
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'

    def test_properties(self):
        objeto = Departamento(nome_setor='Departamento XYZ')
        assert objeto.nome == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento(nome_setor='Departamento XYZ')
        departamento.informar_responsavel('José da Silva','Departamento XYZ', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'

    def test_responsavel_substituido(self):
        departamento = Departamento(nome_setor='Departamento XYZ')        
        assert departamento.responsavel == 'José da Silva'
        departamento.informar_responsavel('João Oliveira', 'Departamento XYZ', 1, 1, 1990)
        assert departamento.responsavel == 'João Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento(nome_setor='Departamento XYZ')
        departamento.informar_responsavel('José da Silva', 'Departamento XYZ',1, 1, 1990)
        departamento.add_colaborador('João Oliveira', 'Departamento XYZ', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 'Departamento XYZ', 18, 4, 1993)
        assert len(departamento.colaboradores) == 2

    def test_verificar_aniversariantes(self):
        retorno = [('João Oliveira', '1992-03-27' , 'Departamento XYZ'),
                   ('Luis Fernando', '2000-03-27' , 'Departamento XYZ')]
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        depto = Departamento(nome_setor='Departamento XYZ')
        depto.informar_responsavel('José da Silva', 'Departamento XYZ', dt1.day, dt1.month, 1990)
        depto.add_colaborador('João Oliveira', 'Departamento XYZ', hoje.day, hoje.month, 1992)
        depto.add_colaborador('José da Silva', 'Departamento XYZ', dt1.day, dt1.month, 1990)
        depto.add_colaborador('Pedro Mendonça', 'Departamento XYZ', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', 'Departamento XYZ', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', 'Departamento XYZ', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list

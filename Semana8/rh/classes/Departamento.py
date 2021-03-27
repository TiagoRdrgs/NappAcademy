from rh.classes.Colaborador import Colaborador


class Departamento:
    def __init__(self, **kwargs):
        self._nome_setor = kwargs.get('nome_setor', '')
        self._responsavel = kwargs.get('responsavel', 'José da Silva')
        self._colaboradores = []

    @property
    def nome(self):
        return self._nome_setor

    @nome.setter
    def nome(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        if self._responsavel is None:
            return None
        return str(self._responsavel)

    @property
    def colaboradores(self):
        return self._colaboradores

    def informar_responsavel(self, nome, nome_setor, dia, mes, ano):
        self._responsavel = Colaborador(nome, nome_setor, dia, mes, ano)

    def add_colaborador(self, nome, nome_setor, dia, mes, ano):
        self._colaboradores.append(Colaborador(nome, nome_setor, dia, mes, ano))

    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
                lista.append((colaborador.nome, colaborador.aniversario, colaborador.nome_setor))
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor

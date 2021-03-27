from datetime import date


class Colaborador:
    def __init__(self, nome, nome_setor=None, dia=None, mes=None, ano=None):
        self._nome = nome
        self._nome_setor = nome_setor
        self._ano = ano
        self._mes = mes
        self._dia = dia
        try:
            self._aniversario = date(ano, mes, dia)
        except TypeError:
            raise TypeError('Informe dia, mês e ano')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def aniversario(self):
        return self._aniversario.isoformat()

    @property
    def nome_setor(self):
        return self._nome_setor

    @nome_setor.setter
    def nome_setor(self, value):
        self._nome_setor = value

    def aniversario_hoje(self):
        hoje = date.today()
        if self._aniversario.day == hoje.day:
            if self._aniversario.month == hoje.month:
                return True
        return False

    def __str__(self):
        return self._nome

    def __repr__(self):
        return 'Colaborador: ' + self._nome

class Cliente:
    def __init__(self, **kwargs):        
        self._name = kwargs.get('nome', '')
        if kwargs.get('idade', 0) > 100:
            raise ValueError('x')
        self._age = kwargs.get('idade', 0)
        self._rg = kwargs.get('rg', '')

    @property
    def nome(self):
        return self._name

    @property
    def idade(self):
        return self._age

    @property
    def rg(self):
        return self._rg

    @nome.setter
    def nome(self, value):
        self._name = value

    @idade.setter
    def idade(self, value):        
        self._age = value

    @rg.setter
    def rg(self, value):
        self._rg = value

    def __str__(self):
        return self._name

    def __repr__(self):
        return f'Cliente: {self._name}'
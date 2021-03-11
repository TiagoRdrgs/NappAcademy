class Conta:
    def __init__(self, **kwargs):      
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        saldo = kwargs.get('saldo', 0)
        if saldo < 0:
            raise ValueError('Saldo negativo')
        self.saldo = saldo
        self.extrato.append(('I', saldo))

    def deposito(self, valor):        
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo = self.saldo + valor
            self.extrato.append(('D', valor))
            return
        raise TypeError('O depósito precisa ser numérico')

    def get_extrato(self):
        return self.extrato
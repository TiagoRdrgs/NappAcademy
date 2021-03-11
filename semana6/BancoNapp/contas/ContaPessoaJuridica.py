from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):    
    def __init__(self, **kwargs):
        self.empresa = kwargs.get('empresa', '')
        self.nome = kwargs.get('nome', '')
        self.saldo = kwargs.get('saldo', '')
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 1500)    

    def saque(self, valor):       
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo e seu limite')
                return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')

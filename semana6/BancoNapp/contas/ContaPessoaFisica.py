from BancoNapp.contas.Conta import Conta


class ContaPessoaFisica(Conta):   
    def __init__(self,  **kwargs):       
        self.profissao = kwargs.get('profissao', '')
        super(ContaPessoaFisica, self).__init__(**kwargs)

    def saque(self, valor):      
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo e seu limite')
                return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')
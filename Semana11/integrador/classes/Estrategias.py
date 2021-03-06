from abc import ABC, abstractmethod
from contextlib import closing
import sqlite3
import csv


class Estrategia(ABC):
    """
    Classe Base para as estratégias (algoritmos)

    """
    @abstractmethod
    def execute(self, dados):
        """ Método em que o algoritmo é contido.
        Implementação do algoritmo na classe filha deve
        sobreescrever este método."""
        pass

    @abstractmethod
    def parametros_necessarios(self):
        """Sobreescrever este método para que retorne uma tupla
        com a lista de parâmetros necessários.
        Exemplo:
        ('algoritmo', 'dbname', 'host', 'user', 'password')
        """
        pass

    @abstractmethod
    def nome(self):
        """Sobreescrever este método para que
        retorne o nome do algoritmo utilizado."""
        pass


class Estrategia_SQLite(Estrategia):
    def execute(self, dados):
        lista_registros = []
        db = dados['db']
        with closing(sqlite3.connect(db)) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas;")
            for linha in cursor.fetchall():
                lista_registros.append(linha)
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'db')

    def nome(self):
        return 'Algoritmo SQLite'


class Estrategia_CSV(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_registros.append(line)
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo CSV'

class Estrategia_TEXTO1(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']        
        file1 = open(arquivo, 'r')
        Lines = file1.readlines()
        for line in Lines:
            if line.startswith('2'):
                data = line.split()    
                final = [data[4] + ' ' + data[5], data[3], data[0]]
                lista_registros.append(final)
        return lista_registros
        
    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo TXT1'

class Estrategia_TEXTO2(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']        
        file1 = open(arquivo, 'r')
        Lines = file1.readlines()
        for line in Lines:
            if line.startswith('2'):
                data = line.split()    
                final = [data[1] + ' ' + data[2], data[3], data[0]]
                lista_registros.append(final)
        return lista_registros
        
    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo TXT2'



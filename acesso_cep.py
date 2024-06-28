import requests


class BuscarEndereço:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('Cep inválido')
            
    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False


    def __str__(self):
        return self.format_cep()


    def format_cep(self):
        return '{}-{}'.format(self.cep[:4],self.cep[4:])


    def acesso_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        print(url)
        r = requests.get(url)
        return r


    def cidade_estado(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        print(url)
        r = requests.get(url)

        return (r.json()['bairro'],r.json()['localidade'],r.json()['uf'])

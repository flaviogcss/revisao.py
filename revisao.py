class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

class Paciente(Pessoa):
    def __init__(self, sintoma, nome, idade, genero):
        super().__init__(nome, idade, genero)
        self.sintoma = sintoma
        
    def imprimir_sintoma(self):
        print('SINTOMA: ' + self.sintoma)

    def imprimir_dados(self):
        print(f'Nome: {self.nome}')
        print('Idade: ' + self.idade)
        print('Genero: ' + self.genero)

class Medico(Pessoa):
    def __init__(self, nome, idade, genero, crm, especialidade):
        super().__init__(nome, idade, genero)
        self.crm = crm
        self.especialidade = especialidade                                                                                                                                                                                                                               

    def imprimir_crm(self):
        return print('CRM: ' + self.crm)

    def imprimir_especialidade(self):
        return print('ESPECIALIDADE: ' + self.especialidade)

    def imprimir_doutor(self):
        print('Nome: ' + self.nome)
        print('Especialidade: ' + self.especialidade)

print('____Paciente____')
paciente = Paciente('Sintoma Tal', 'Nome Tal', '16', 'Genero Tal')
paciente_dois = Paciente('Caganeira', 'Zeze', '16', 'M')
paciente.imprimir_dados()
paciente.imprimir_sintoma()

print('____Medico____')
medico = medico('Crm', 'Especialidade')

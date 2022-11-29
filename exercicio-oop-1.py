from datetime import datetime, date
from enum import Enum
from random import randint

class Escola():
  def __init__(self, nome, cnpj):
    self.nome = nome
    self.cnpj = cnpj
    self.alunos = []

    self.pagamentos = {}

  def get_qntdd_alunos(self):
    """Documentação da função? Assistir Aula - https://programandoseuemprego.com.br/plataforma/aulas/curso-python-intermediario/funcoes-documentacao/
    """
    return len(self.alunos)

  # Melhorar parametrização. Separar ano e mês em parâmetros diferentes
  # Melhorar os nomes dos parâmetros
  # Mais observações no final
  def calcula_faturamento_mes(self, anomes):
    """Inserir Documentação"""
    return sum(self.pagamentos[anomes])


# Separar em módulos
class Aluno():
  def __init__(self, nome, cpf, email, telefone, escola): #<< escola n estava no UML, mas posso incluir??
    self.nome = nome
    self.cpf = cpf
    self.email = email
    self.telefone = telefone
    self.escola = escola
    self.escola.alunos.append(self)

    ## get_valor_pagamento

# Separar em módulos
class Contrato():
  def __init__(self, aluno, data_inicio, valor, data_vencimento):
    self.aluno = aluno
    self.data_inicio = data_inicio
    self.valor = valor
    self.data_vencimento = data_vencimento
    self.template = f"""
      ##### Contrato Prestação de Serviço #####
      Eu, {self.aluno.nome} com CPF número {self.aluno.cpf} contrato os serviços da escola {self.aluno.escola.nome} com CNPJ número {self.aluno.escola.cnpj} por R${self.valor} mensais, vencimentos todo dia {self.data_vencimento} a partir de {self.data_inicio}.
      """
    
  # Retorno faz sentido com o nome do médo?
  def imprime_contrato(self):
    """ Documentação """
    contrato = f"""
    ##### Contrato Prestação de Serviço #####
    Eu, {self.aluno.nome} com CPF número {self.aluno.cpf} contrato os serviços da escola {self.aluno.escola.nome} com CNPJ número {self.aluno.escola.cnpj} por R${self.valor} mensais, vencimentos todo dia {self.data_vencimento} a partir de {self.data_inicio}.
    """
    print(contrato)

  def gera_contrato(self):
    """ Documentação """
    contrato = f"""
    ##### Contrato Prestação de Serviço #####
    Eu, {self.aluno.nome} com CPF número {self.aluno.cpf} contrato os serviços \
    da escola {self.aluno.escola.nome} com CNPJ número {self.aluno.escola.cnpj} \
    por R${self.valor} mensais, vencimentos todo dia {self.data_vencimento} a \
    partir de {self.data_inicio}.
    """
    return contrato


class StatusPagamento(Enum):
  # https://docs.python.org/3/library/enum.html
  PAGO = 1
  ABERTO = 2
  ATRASADO = 3

class Pagamento():
  def __init__(self, data_pagamento, contrato):
    self.contrato = contrato
    self.valor = self.contrato.valor # Ideia Exercício: e se tiver juros? 

    # data que precisa ser paga ou data efetiva do pagamento?
    # considerei data que precisa ser pago
    # datetime é a melhor opção? Usar Date pode ser mais eficiente nesse cenário
    self.data_pagamento = datetime.strptime(data_pagamento, '%d/%m/%Y')

    #Implementar caso pagamento realizado (status pago)
    self.is_pago = False
    self.status = self.get_status_pagamento()
    
    # Dicionários não permitem duplicação de chaves. Datas de ANOMES repetidas serão apagadas
    #Melhorar o nome da variável
    anomes = int(str(self.data_pagamento.year)+str(self.data_pagamento.month))

    # Verificar se a possibilidade de já iniciar 
    try:
      self.contrato.aluno.escola.pagamentos[anomes].append(self.valor)
    except:
      self.contrato.aluno.escola.pagamentos[anomes]=[self.valor]

  def get_status_pagamento(self):
    status_pagamento = None

    if self.is_pago == True:
      status_pagamento = StatusPagamento.PAGO

    elif self.data_pagamento.date() > date.today():
      status_pagamento = StatusPagamento.ABERTO

    elif self.data_pagamento.date() <= date.today():
      status_pagamento = StatusPagamento.ATRASADO

    if not status_pagamento:
      raise Exception("Erro ao processar status de Pagamento")

    return status_pagamento



escola = Escola('Escola Mogi', 123456)

### Usar mais as chaves dos parâmetros. Difícil de ler a declaração dos objetos
aluno_a = Aluno(
    nome='Joao', 
    cpf=1, 
    email='joao@joao',
    telefone=randint(100, 999),
    escola=escola
    )
aluno_b = Aluno('Gustavo', 4, 'guss@guss', randint(100, 999), escola)
aluno_c = Aluno('Paulo', 5, 'paulo@paulo', randint(100, 999), escola)

assert escola.get_qntdd_alunos() == 3


contrato_aluno_a = Contrato(aluno_a, '26/11/2022', 160, 10)
contrato_aluno_b = Contrato(aluno_b, '26/11/2022', 160, 10)
contrato_aluno_c = Contrato(aluno_c, '26/11/2022', 160, 10)

# print(contrato_aluno_a.template)

pagto_1 = Pagamento('15/11/2022', contrato_aluno_a)
assert pagto_1.get_status_pagamento() == StatusPagamento.ATRASADO

pagto_2 = Pagamento('27/12/2023', contrato_aluno_b)
assert pagto_2.get_status_pagamento() == StatusPagamento.ABERTO

pagto_3 = Pagamento('20/11/2022', contrato_aluno_c)
assert pagto_3.get_status_pagamento() == StatusPagamento.ATRASADO

escola.calcula_faturamento_mes(202211)

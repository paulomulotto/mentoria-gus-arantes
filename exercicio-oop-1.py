from datetime import datetime

class Escola():
  def __init__(self, nome, cnpj):
    self.nome = nome
    self.cnpj = cnpj
    self.lista_alunos = []

    self.dict_receb = {}

  def get_qntdd_alunos(self):
    return f'Total de alunos: {len(self.lista_alunos)}'

  def calcula_faturamento_mes(self, anomes):
    return f'Faturamento do mês {anomes} foi de R${sum(self.dict_receb[anomes])}'



class Aluno():
  def __init__(self, nome, cpf, email, telefone, escola): #<< escola n estava no UML, mas posso incluir??
    self.nome = nome
    self.cpf = cpf
    self.email = email
    self.telefone = telefone
    self.escola = escola
    self.escola.lista_alunos.append(self.cpf)

    ## get_valor_pagamento

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
    

  def imprime_contrato(self):
    ################################ contrato tem q estar assim??? sem self?
    contrato = f"""
    ##### Contrato Prestação de Serviço #####
    Eu, {self.aluno.nome} com CPF número {self.aluno.cpf} contrato os serviços da escola {self.aluno.escola.nome} com CNPJ número {self.aluno.escola.cnpj} por R${self.valor} mensais, vencimentos todo dia {self.data_vencimento} a partir de {self.data_inicio}.
    """
    return print(contrato)

class Pagamento():
  def __init__(self, data_pagamento, contrato): #, status):
    self.contrato = contrato
    self.valor = self.contrato.valor
    self.data_pagamento = data_pagamento
    # self.status = status ## n tentendi o status
    
    data_pagamento = datetime.strptime(self.data_pagamento, '%d/%m/%Y')
    anomes = int(str(data_pagamento.year)+str(data_pagamento.month))
    try:
      self.contrato.aluno.escola.dict_receb[anomes].append(self.valor)
    except:
      self.contrato.aluno.escola.dict_receb[anomes]=[self.valor]



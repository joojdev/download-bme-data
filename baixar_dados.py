from tinydb import TinyDB
import inquirer

banco_de_dados = TinyDB('medicoes.json')

chaves = set()

for entradas in banco_de_dados.all():
  for chave in entradas.keys():
    if chave == 'timestamp': continue
    chaves.add(chave)

pergunta = inquirer.Checkbox('chaves',
                             message='Quais campos você quer baixar?',
                             choices=chaves)

respostas = inquirer.prompt([pergunta])
chaves_selecionadas = respostas['chaves']

lista_entradas = []

for entradas in banco_de_dados.all():
  chaves_sem_timestamp = [_ for _ in entradas if _ != 'timestamp']
  if set(chaves_selecionadas) == set(chaves_sem_timestamp):
    lista_entradas.append(entradas)

try:
  assert(len(lista_entradas))
except AssertionError:
  print('Não existem entradas com esses campos exatamente!')
  exit()

cabecalho = f'Timestamp,{",".join(chaves_selecionadas)}\n'
arquivo_csv = cabecalho

for entradas in lista_entradas:
  linha_csv = str(entradas['timestamp'])

  for chave in chaves_selecionadas:
    linha_csv += f',{entradas[chave]}'

  linha_csv += '\n'
  arquivo_csv += linha_csv

pergunta = inquirer.Path('caminho',
                         message='Onde eu salvo esses dados?',
                         default='resultado.csv')

respostas = inquirer.prompt([pergunta])
caminho = respostas['caminho']

with open(caminho, 'w') as arquivo:
  arquivo.write(arquivo_csv)
  arquivo.close()
from tinydb import TinyDB
from classes import Registro

banco_de_dados = TinyDB('medicoes.json')

def registrar(medicao):
  assert(type(medicao) == Registro)

  banco_de_dados.insert(medicao.informacoes)

def pegar():
  return banco_de_dados.all()
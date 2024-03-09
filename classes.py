class Registro:
  def __init__(self, timestamp, informacoes):
    self.__informacoes = informacoes
    self.timestamp = timestamp

  @property
  def informacoes(self):
    temp = self.__informacoes
    temp['timestamp'] = self.timestamp
    return temp
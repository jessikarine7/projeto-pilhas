from functools import total_ordering

# python .\pilhas.py
class PilhaArray:
  def __init__(self):
    self._pilha = []
  
  def verPilha(self):
    return self._pilha

  def __len__(self):
    return len(self._pilha)

  def size(self):
    return self.__len__()

  def is_empty(self):
    return len(self._pilha) == 0

  def push(self, e):
    self._pilha.append(e)

  def top(self):
    if self.is_empty():
      raise PilhaVazia('A pilha está vazia')
    return self._pilha[-1]

  def pop(self):
    if self.is_empty():
      raise PilhaVazia('A pilha está vazia')
    return self._pilha.pop()
  
  def sort(self):
    # sort(reverse=True)
    self._pilha.sort()
  
#---------outra class----------
class PilhaVazia(Exception):
  pass
#---------resposta----------

@total_ordering
class Carta():
  def __init__(self, nome, id):
    self.id = id
    self.nome = nome

  # x < y
  def __lt__(self, other):
    return self.id < other.id;

  # x > y
  def __gt__(self, other):
    return self.id > other.id;

def ordenacao():
  p = PilhaArray()

  carta1 = Carta('umPaus', 1)
  carta2 = Carta('doisPaus', 2)
  carta3 = Carta('tresPaus', 3)
  carta4 = Carta('quatroPaus', 4)
  carta5 = Carta('cincoPaus', 5)
  carta6 = Carta('seisPaus', 6)
  carta7 = Carta('setePaus', 7)
  carta8 = Carta('oitoPaus', 8)
  carta9 = Carta('novePaus', 9)
  carta10 = Carta('dezPaus', 10)

  p.push(carta2)
  p.push(carta1)
  p.push(carta8)
  p.push(carta5)
  p.push(carta3)
  p.push(carta6)
  p.push(carta9)
  p.push(carta10)
  p.push(carta7)
  p.push(carta4)

  # corrigir
  p.sort()

  for e in p.verPilha():
    print(e.nome)

ordenacao()
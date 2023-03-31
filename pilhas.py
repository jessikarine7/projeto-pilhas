from functools import total_ordering

# python .\pilhas.py
class PilhaVazia(Exception):
  pass

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
  
  def sortCrescente(self):
    self._pilha.sort()

  def sortDecrescente(self):
    self._pilha.sort(reverse=True)
    
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
  #---------cartas de copas----------
  carta1 = Carta("Ás de Copas", 1)
  carta2 = Carta("2 de Copas", 2)
  carta3 = Carta("3 de Copas", 3)
  carta4 = Carta("4 de Copas", 4)
  carta5 = Carta("5 de Copas", 5)
  carta6 = Carta("6 de Copas", 6)
  carta7 = Carta("7 de Copas", 7)
  carta8 = Carta("8 de Copas", 8)
  carta9 = Carta("9 de Copas", 9)
  carta10 = Carta("10 de Copas", 10)
  carta11 = Carta("Valete de Copas", 11)
  carta12 = Carta("Rainha de Copas", 12)
  carta13 = Carta("Rei de Copas", 13)
  #---------cartas de espadas----------
  carta14 = Carta("Ás de Espadas", 14)
  carta15 = Carta("2 de Espadas", 15)
  carta16 = Carta("3 de Espadas", 16)
  carta17 = Carta("4 de Espadas", 17)
  carta18 = Carta("5 de Espadas", 18)
  carta19 = Carta("6 de Espadas", 19)
  carta20 = Carta("7 de Espadas", 20)
  carta21 = Carta("8 de Espadas", 21)
  carta22 = Carta("9 de Espadas", 22)
  carta23 = Carta("10 de Espadas", 23)
  carta24 = Carta("Valete de Espadas", 24)
  carta25 = Carta("Rainha de Espadas", 25)
  carta26 = Carta("Rei de Espadas", 26)
  #---------cartas de ouros----------
  carta27 = Carta("Ás de Ouros", 27)
  carta28 = Carta("2 de Ouros", 28)
  carta29 = Carta("3 de Ouros", 29)
  carta30 = Carta("4 de Ouros", 30)
  carta31 = Carta("5 de Ouros", 31)
  carta32 = Carta("6 de Ouros", 32)
  carta33 = Carta("7 de Ouros", 33)
  carta34 = Carta("8 de Ouros", 34)
  carta35 = Carta("9 de Ouros", 35)
  carta36 = Carta("10 de Ouros", 36)
  carta37 = Carta("Valete de Ouros", 37)
  carta38 = Carta("Rainha de Ouros", 38)
  carta39 = Carta("Rei de Ouros", 39)
  #---------cartas de paus----------
  carta40 = Carta("Ás de Paus", 40)
  carta41 = Carta("2 de Paus", 41)
  carta42 = Carta("3 de Paus", 42)
  carta43 = Carta("4 de Paus", 43)
  carta44 = Carta("5 de Paus", 44)
  carta45 = Carta("6 de Paus", 45)
  carta46 = Carta("7 de Paus", 46)
  carta47 = Carta("8 de Paus", 47)
  carta48 = Carta("9 de Paus", 48)
  carta49 = Carta("10 de Paus", 49)
  carta50= Carta("Valete de Paus", 50)
  carta51= Carta("Rainha de Paus", 51)
  carta52= Carta("Rei de Paus", 52)

  p.push(carta4)
  p.push(carta9)
  p.push(carta10)
  p.push(carta11)
  p.push(carta1)
  p.push(carta12)
  p.push(carta13)
  p.push(carta14)
  p.push(carta17)
  p.push(carta8)
  p.push(carta15)
  p.push(carta16)
  p.push(carta6)
  p.push(carta2)
  p.push(carta19)
  p.push(carta20)
  p.push(carta21)
  p.push(carta18)
  p.push(carta7)
  p.push(carta22)
  p.push(carta3)
  p.push(carta23)
  p.push(carta24)
  p.push(carta25)
  p.push(carta26)
  p.push(carta27)
  p.push(carta30)
  p.push(carta28)
  p.push(carta31)
  p.push(carta29)
  p.push(carta32)
  p.push(carta33)
  p.push(carta34)
  p.push(carta35)
  p.push(carta36)
  p.push(carta38)
  p.push(carta5)
  p.push(carta40)
  p.push(carta43)
  p.push(carta37)
  p.push(carta41)
  p.push(carta39)
  p.push(carta42)
  p.push(carta44)
  p.push(carta45)
  p.push(carta46)
  p.push(carta50)
  p.push(carta47)
  p.push(carta48)
  p.push(carta49)
  p.push(carta52)
  p.push(carta51)

  ordem = int(input('Escolha entre 1 => Crescente ou 2 => Decrescente: '))

  if ordem == 1:
    p.sortCrescente()
  else:
    p.sortDecrescente()

  for e in p.verPilha():
    print(e.nome)

ordenacao()
# Clase base listas doblemente enlazadas

import random

class NodeD:
  __slots__ = ('__value','__next', '__prev')

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("prev debe ser un objeto tipo nodo ó None")
    self.__prev = node


class DoublyLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @head.setter
  def head(self, newHead):
    if newHead is not None and not isinstance(newHead,NodeD):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = newHead

  @property
  def tail(self):
    return self.__tail

  @tail.setter
  def tail(self, newTail):
    if newTail is not None and not isinstance(newTail,NodeD):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = newTail

  @property
  def size(self):
    return self.__size

  @size.setter
  def size(self, newSize):
    if not isinstance(newSize,int):
      raise TypeError("Size debe ser un objeto numero entero")
    self.__size = newSize

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def prepend(self, value):

    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      newnode.next = self.__head #enlazo nuevo nodo
      self.head.prev = newnode
      self.__head = newnode
    self.__size += 1

  def append(self,value):
    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      newnode.prev = self.__tail
      self.__tail = newnode

    self.__size += 1

  def getbyindex(self, index):
    if index < 0 or index > self.__size:
      return "Error, indice fuera de rango"

    cont = 0
    for currentNode in self:
      if cont == index:
        return currentNode
      cont += 1


  def insertinindex(self, value, index):

    if index == 0:
      self.prepend(value)
    elif index == -1 or index == self.__size:
      self.append(value)
    else:
      prevNode = self.getbyindex(index-1)
      nextNode = prevNode.next
      #nextNode = self.getbyindex(index)
      newNode = NodeD(value)
      newNode.next = prevNode.next #Enlazo el next del nuevo nodo, que es el next del previo
      prevNode.next = newNode
      newNode.prev = prevNode
      nextNode.prev = newNode
      self.__size +=1

      print("prev_new_node :",newNode.prev)
      print("prev_next_node :",nextNode.prev)

  def searchbyvalue(self, valuetosearch):
    for currentNode in self:
      if currentNode.value == valuetosearch:
        return True

    return False

  def setnewvalue(self, valuetochange, newvalue):
    for currentNode in self:
      if currentNode.value == valuetochange:
        currentNode.value = newvalue
        return True

    return False


  def pop(self):
    tempNode = self.__head
    if self.__head is None:
       print("Lista vacia, no hay elementos a eliminar")
       return None
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      poppednode = self.__tail
      prevnode = self.__tail.prev
      print("prevnode",prevnode)
      prevnode.next = None
      self.__tail = prevnode
      self.__size -= 1
      poppednode.prev = None
      return poppednode

  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.head.prev = None
      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode


  def generate(self, n, minvalue, maxvalue):
    for i in range(n):
      self.append(random.randint(minvalue, maxvalue))
    return self

customLL = DoublyLinkedList()


# Clase vehiculo


class Vehiculo:
    def __init__(self, placa, tipo, prioridad):
        self.placa = placa
        self.tipo = tipo
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.placa} | {self.tipo} | Prioridad {self.prioridad}"


def insertar_vehiculos(via):
    via.append(Vehiculo("ABC123", "auto", 2))
    via.append(Vehiculo("XYZ111", "moto", 1))
    via.append(Vehiculo("JKL222", "camion", 4))
    via.append(Vehiculo("MNO333", "moto", 1))
    via.append(Vehiculo("PQR444", "auto", 3))
    via.append(Vehiculo("STU555", "camion", 5))
    via.append(Vehiculo("VWX666", "auto", 2))
    via.append(Vehiculo("HJU652", "moto", 5))
    via.append(Vehiculo("SAR210", "camion", 3))
    print("Vehículos insertados en la vía:")
    mostrar_via(via)


def mostrar_via(via):
  for nodo in via:
    print(nodo.value)
  print("-" * 40)

def paso_preferencial(via):
    actual = via.head
    while actual:
        siguiente = actual.next
        if actual.value.tipo == "moto" and actual.value.prioridad == 1 and actual != via.head:
            nodo_moto = actual
            prev = nodo_moto.prev
            nxt = nodo_moto.next
            if prev:
                prev.next = nxt
            if nxt:
                nxt.prev = prev
            if nodo_moto == via.tail:
                via.tail = prev
            nodo_moto.prev = None
            nodo_moto.next = via.head
            via.head.prev = nodo_moto
            via.head = nodo_moto
        actual = siguiente
    print("Después del paso preferencial (motos prioridad 1):")
    mostrar_via(via)


def eliminar_camiones(via):
    actual = via.head
    while actual:
        siguiente = actual.next
        if actual.value.tipo == "camion" and actual.value.prioridad > 3:
            prev = actual.prev
            nxt = actual.next
            if prev:
                prev.next = nxt
            else:
                via.head = nxt
            if nxt:
                nxt.prev = prev
            else:
                via.tail = prev
            via.size -= 1
        actual = siguiente
    print("Después de eliminar camiones con prioridad > 3:")
    mostrar_via(via)


def accidente(via, placa1, placa2):
    nodo1 = nodo2 = None
    actual = via.head
    while actual:
        if actual.value.placa == placa1:
            nodo1 = actual
        elif actual.value.placa == placa2:
            nodo2 = actual
        actual = actual.next

    if not nodo1 or not nodo2:
        print("Una de las placas no existe en la vía.")
        return

   
    actual = via.head
    primero, segundo = None, None
    while actual:
        if actual == nodo1:
            primero = nodo1
            segundo = nodo2
            break
        elif actual == nodo2:
            primero = nodo2
            segundo = nodo1
            break
        actual = actual.next

    actual = primero
    while actual and actual != segundo:
        siguiente = actual.next
        prev = actual.prev
        nxt = actual.next
        if prev:
            prev.next = nxt
        else:
            via.head = nxt
        if nxt:
            nxt.prev = prev
        else:
            via.tail = prev
        via.size -= 1
        actual = siguiente


    if segundo:
        prev = segundo.prev
        nxt = segundo.next
        if prev:
            prev.next = nxt
        else:
            via.head = nxt
        if nxt:
            nxt.prev = prev
        else:
            via.tail = prev
        via.size -= 1

    print(f"Después del accidente entre {placa1} y {placa2}:")
    mostrar_via(via)


def invertir_si_mas_autos(via):
    cont_autos = 0
    cont_motos = 0
    for nodo in via:
        if nodo.value.tipo == "auto":
            cont_autos += 1
        elif nodo.value.tipo == "moto":
            cont_motos += 1

    if cont_autos > cont_motos:
        actual = via.head
        via.head, via.tail = via.tail, via.head
        while actual:
            actual.next, actual.prev = actual.prev, actual.next
            actual = actual.prev
        print("Vía invertida (más autos que motos):")
    else:
        print("No se invierte, hay igual o más motos que autos.")

    mostrar_via(via)


def reorganizar_prioridad(via):
    actual = via.head
    while actual:
        min_nodo = actual
        buscador = actual.next
        while buscador:
            if buscador.value.prioridad < min_nodo.value.prioridad:
                min_nodo = buscador
            buscador = buscador.next
        if min_nodo != actual:
            actual.value, min_nodo.value = min_nodo.value, actual.value
        actual = actual.next
    print("Vía reorganizada por prioridad (1 a 5):")
    mostrar_via(via)


def main():
    via = DoublyLinkedList() 
    insertar_vehiculos(via)
    paso_preferencial(via)
    eliminar_camiones(via)
    accidente(via, "XYZ111", "PQR444")
    invertir_si_mas_autos(via)
    reorganizar_prioridad(via)


main()

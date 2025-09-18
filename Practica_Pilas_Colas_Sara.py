import random

class Queue():

  def __init__(self):
    self.__list = []

  def __str__(self):
    return '--'.join(map(str,self.__list))


  def enqueue(self,e):
    self.__list.append(e)
    return True

  def dequeue(self):
    if self.is_empty():
      return "Error no es posible desencolar, no hay elementos"

    return self.__list.pop(0)

  def first(self):
    if self.is_empty():
      return "Error no es posible leer el primer elemento, no hay elementos"

    return self.__list[0]


  def is_empty(self):
    return len(self.__list) == 0

  def len(self):
    return len(self.__list)

  def generate(self,num, min, max):
   for i in range(0,num):
    self.enqueue(random.randint(min,max))


customQ = Queue()

import random

class Stack():

  def __init__(self):
    self.__list = []

  def __str__(self):
    return '--'.join(map(str,reversed(self.__list)))


  def push(self,e):
    self.__list.append(e)
    return True

  def pop(self):
    if self.is_empty():
      return "Error no es posible desencolar, no hay elementos"

    return self.__list.pop()

  def top(self):
    if self.is_empty():
      return "Error no es posible leer el primer elemento, no hay elementos"

    return self.__list[-1]


  def is_empty(self):
    return len(self.__list) == 0

  def len(self):
    return len(self.__list)

  def generate(self,num, min, max):
   for i in range(0,num):
    self.push(random.randint(min,max))


customS = Stack()



class Atraccion:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.visitors = Stack()

    def __str__(self):
        return f"{self.name} (Capacidad: {self.capacity}) -> {str(self.visitors)}"

    def mostrar_visitantes_recursivo(self, stack=None):
        if stack is None:
            stack = self.visitors
        if stack.is_empty():
            return ""
        v = stack.pop()
        res = str(v) + " " + self.mostrar_visitantes_recursivo(stack)
        stack.push(v)
        return res


class ParqueDiversiones:
    def __init__(self):
        self.attractions = Queue()
        self.turn = 1

    def inicializar_defecto(self):
        self.agregar_atraccion("Montaña Rusa", 3)
        self.agregar_atraccion("Carros Chocones", 2)
        self.agregar_atraccion("Rueda de la Fortuna", 2)
        self.agregar_atraccion("Casa del Terror", 2)

    def agregar_atraccion(self, name, capacity):
        self.attractions.enqueue(Atraccion(name, capacity))

    def eliminar_atraccion(self, name):
        tempQ = Queue()
        removed = None
        while not self.attractions.is_empty():
            atr = self.attractions.dequeue()
            if atr.name == name:
                removed = atr
            else:
                tempQ.enqueue(atr)
        self.attractions = tempQ
        if removed:
            if not self.attractions.is_empty():
                next_atr = self.attractions.first()
                while not removed.visitors.is_empty():
                    next_atr.visitors.push(removed.visitors.pop())
        return removed

    def agregar_visitante(self, visitor):
        if not self.attractions.is_empty():
            first = self.attractions.first()
            first.visitors.push(visitor)

    def ejecutar_turno(self):
        if self.attractions.is_empty():
            print("No hay atracciones en el sistema.")
            return
        print(f"\n=== TURNO {self.turn} ===")
        tempQ = Queue()
        while not self.attractions.is_empty():
            atr = self.attractions.dequeue()
            print(f"\n[{atr.name}]")
            processed = Stack()
            for _ in range(atr.capacity):
                if not atr.visitors.is_empty():
                    processed.push(atr.visitors.pop())
            if not self.attractions.is_empty():
                next_atr = self.attractions.first()
                while not processed.is_empty():
                    next_atr.visitors.push(processed.pop())
            else:
                while not processed.is_empty():
                    v = processed.pop()
                    print(f" → {v} salió del parque")
            print("Visitantes esperando:", atr.mostrar_visitantes_recursivo())
            tempQ.enqueue(atr)
        self.attractions = tempQ
        self.turn += 1

    def mostrar_estado(self):
        print("\n--- Estado del Sistema ---")
        self._mostrar_estado_recursivo(self.attractions)

    def _mostrar_estado_recursivo(self, queue, tempQ=None):
        if tempQ is None:
            tempQ = Queue()
        if queue.is_empty():
            while not tempQ.is_empty():
                queue.enqueue(tempQ.dequeue())
            return
        atr = queue.dequeue()
        print(f"{atr.name}: {atr.mostrar_visitantes_recursivo()}")
        tempQ.enqueue(atr)
        self._mostrar_estado_recursivo(queue, tempQ)


if __name__ == "__main__":
    parque = ParqueDiversiones()
    parque.inicializar_defecto()


    visitantes = ["A1", "N1", "A2", "N2", "A3", "A4", "N3", "G5", "R7", "E90"]
    for v in visitantes:
        parque.agregar_visitante(v)

    parque.mostrar_estado()


    parque.ejecutar_turno()
    parque.ejecutar_turno()
    parque.ejecutar_turno()
    parque.ejecutar_turno()


    parque.mostrar_estado()


    parque.eliminar_atraccion("Rueda de la Fortuna")
    parque.mostrar_estado()


    parque.agregar_atraccion("Simulador 4D", 2)
    parque.mostrar_estado()

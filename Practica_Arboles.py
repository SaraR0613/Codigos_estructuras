class BinaryTreeNode:

  def __init__(self, data):
    self.data = data
    self.leftchild = None
    self.rightchild = None


  def __str__(self, level=0):
    ret = "  " *level + str(self.data) + "\n"
    if self.leftchild:
       ret += self.leftchild.__str__(level+1)
    if self.rightchild:
       ret += self.rightchild.__str__(level+1)
    return ret


def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)

def inorder(root):

  if root is None:
    return

  inorder(root.leftchild)
  print(root.data)
  inorder(root.rightchild)

def insertNodeBST(root, newValue):

  if root is None:
    return BinaryTreeNode(newValue)

  if newValue <= root.data:
    root.leftchild = insertNodeBST(root.leftchild, newValue)
  else:
    root.rightchild = insertNodeBST(root.rightchild, newValue)

  return root

def searchBST(root, valuetofind):

  if root is None:
    return "el nodo con valor {} NO fue encontrado".format(valuetofind)

  print("Recorrido/Visitados: ", root.data)
  if valuetofind == root.data:
    return "el nodo con valor {} SI fue encontrado".format(valuetofind)
  elif valuetofind < root.data:
    return searchBST(root.leftchild,valuetofind)
  else:
    return searchBST(root.rightchild,valuetofind)

  def deleteNodeBST(root, valuetoDelete):
    if root is None:
      return "Arbol vacio/nodo no encontrado"

    if valuetoDelete < root.data:
      root.leftchild = deleteNodeBST(root.leftchild, valuetoDelete)
    elif valuetoDelete > root.data:
      root.rightchild = deleteNodeBST(root.rightchild, valuetoDelete)
    else:
      #caso 1, nodo a eliminar es una hoja
      if root.leftchild is None and root.rightchild is None:
        return None
      #caso 2, nodo a eliminar tiene hijo a la izquiera e hijo a la derecha
      elif root.leftchild and root.rightchild:
        succesor_node = minsucessor(root.rightchild)
        value_succesor_temp = succesor_node.data
        deleteNodeBST(root, value_succesor_temp)
        root.data = value_succesor_temp
      #caso 3, nodo a eliminar tiene 1 hijo a la izquierda
      elif root.leftchild:
        return root.leftchild
      #caso 4, nodo a eliminar tiene 1 hijo a la derecha
      else:
        return root.rightchild

    return root


def minsucessor(root):
  if root.leftchild:
    return minsucessor(root.leftchild)
  return root

def maxsucessor(root):
  if root.rightchild:
    return maxsucessor(root.rightchild)
  return root

root1bst = None
printTree(root1bst)

"_____"

import random

class Queue:
    def __init__(self):
        self.__list = []

    def __str__(self):
        return '--'.join(map(str, self.__list))

    def enqueue(self, e):
        self.__list.append(e)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        return self.__list.pop(0)

    def first(self):
        if self.is_empty():
            return None
        return self.__list[0]

    def is_empty(self):
        return len(self.__list) == 0

    def len(self):
        return len(self.__list)

    def generate(self, num, min, max):
        for i in range(0, num):
            self.enqueue(random.randint(min, max))

"_____"
class Paciente:
    def __init__(self, id, nombre, nivel_emergencia, orden_llegada):
        self.id = id
        self.nombre = nombre
        self.nivel_emergencia = nivel_emergencia
        self.orden_llegada = orden_llegada

    def __lt__(self, other):
        if self.nivel_emergencia == other.nivel_emergencia:
            return self.orden_llegada < other.orden_llegada
        return self.nivel_emergencia < other.nivel_emergencia

    def __str__(self):
        return f"{self.nombre} | Nivel {self.nivel_emergencia} | Llegada {self.orden_llegada}"


def insertPaciente(root, paciente):
    new_node = BinaryTreeNode(paciente)
    if root is None:
        return new_node

    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        actual = q.dequeue()
        if actual.leftchild is None:
            actual.leftchild = new_node
            break
        elif actual.rightchild is None:
            actual.rightchild = new_node
            break
        else:
            q.enqueue(actual.leftchild)
            q.enqueue(actual.rightchild)

    heapifyUp(root, new_node)
    return root


def findParent(root, node):
    if root is None or root == node:
        return None
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        current = q.dequeue()
        if current.leftchild == node or current.rightchild == node:
            return current
        if current.leftchild:
            q.enqueue(current.leftchild)
        if current.rightchild:
            q.enqueue(current.rightchild)
    return None


def heapifyUp(root, node):
    parent = findParent(root, node)
    if parent and node.data < parent.data:
        node.data, parent.data = parent.data, node.data
        heapifyUp(root, parent)


def getLastNode(root):
    q = Queue()
    q.enqueue(root)
    last = None
    while not q.is_empty():
        last = q.dequeue()
        if last.leftchild:
            q.enqueue(last.leftchild)
        if last.rightchild:
            q.enqueue(last.rightchild)
    return last


def deleteLastNode(root, last_node):
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        current = q.dequeue()
        if current.leftchild == last_node:
            current.leftchild = None
            return
        elif current.rightchild == last_node:
            current.rightchild = None
            return
        if current.leftchild:
            q.enqueue(current.leftchild)
        if current.rightchild:
            q.enqueue(current.rightchild)


def heapifyDown(node):
    if node is None:
        return
    smallest = node
    if node.leftchild and node.leftchild.data < smallest.data:
        smallest = node.leftchild
    if node.rightchild and node.rightchild.data < smallest.data:
        smallest = node.rightchild
    if smallest != node:
        node.data, smallest.data = smallest.data, node.data
        heapifyDown(smallest)


def programarCirugia(root):
    if root is None:
        print("No hay pacientes en espera.")
        return None, None

    min_paciente = root.data
    last_node = getLastNode(root)

    if last_node == root:
        return None, min_paciente

    root.data = last_node.data
    deleteLastNode(root, last_node)
    heapifyDown(root)

    return root, min_paciente


def mostrarPacientes(root):
    if not root:
        print("No hay pacientes en espera.")
        return
    print("Pacientes en espera:")
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        current = q.dequeue()
        print(current.data)
        if current.leftchild:
            q.enqueue(current.leftchild)
        if current.rightchild:
            q.enqueue(current.rightchild)


def mostrarPorNivel(root, nivel):
    if not root:
        print("Árbol vacío.")
        return
    print(f"Pacientes con nivel de emergencia {nivel}:")
    q = Queue()
    q.enqueue(root)
    found = False
    while not q.is_empty():
        current = q.dequeue()
        if current.data.nivel_emergencia == nivel:
            print(current.data)
            found = True
        if current.leftchild:
            q.enqueue(current.leftchild)
        if current.rightchild:
            q.enqueue(current.rightchild)
    if not found:
        print("Ninguno con ese nivel.")


"___N__"

def reportePacientes(root, contador_atendidos):
    total_registrados = contarPacientes(root)
    print(f"Total pacientes registrados: {total_registrados + contador_atendidos}")
    print(f"Pacientes en espera: {total_registrados}")
    print(f"Pacientes atendidos: {contador_atendidos}")

def contarPacientes(root):
    if not root:
        return 0
    q = Queue()
    q.enqueue(root)
    count = 0
    while not q.is_empty():
        current = q.dequeue()
        count += 1
        if current.leftchild:
            q.enqueue(current.leftchild)
        if current.rightchild:
            q.enqueue(current.rightchild)
    return count

def actualizarEmergencia(root, id_paciente, nuevo_nivel):
    if root is None:
        print("No hay pacientes registrados.")
        return root

    q = Queue()
    q.enqueue(root)
    encontrado = None
    while not q.is_empty():
        current = q.dequeue()
        if current.data.id == id_paciente:
            encontrado = current
            break
        if current.leftchild:
            q.enqueue(current.leftchild)
        if current.rightchild:
            q.enqueue(current.rightchild)

    if encontrado:
        encontrado.data.nivel_emergencia = nuevo_nivel
        print(f"Nivel de emergencia actualizado para {encontrado.data.nombre} a {nuevo_nivel}")
        heapifyUp(root, encontrado)
        heapifyDown(root)
    else:
        print("No se encontró el paciente con ese ID.")

    return root

    def buscarPaciente(root, id_paciente): 
        print("1. Buscar paciente por ID o por nombre")
        if not root:
            print("No hay pacientes registrados.")
            return
        q = Queue()
        q.enqueue(root)
        while not q.is_empty():
            actual = q.dequeue()
            if actual.data.id == id_paciente:
                print(actual.data)
                return
            if actual.leftchild:
                q.enqueue(actual.leftchild)
            if actual.rightchild:
                q.enqueue(actual.rightchild)
        print("Paciente no encontrado.")

    def mostrarOrdenPrioridad(root): 
        print("2. Mostrar los pacientes en orden de prioridad (ordenado sin eliminar)")
        lista = []
        q = Queue()
        if root:
            q.enqueue(root)
        while not q.is_empty():
            actual = q.dequeue()
            lista.append(actual.data)
            if actual.leftchild:
                q.enqueue(actual.leftchild)
            if actual.rightchild:
                q.enqueue(actual.rightchild)
        lista.sort(key=lambda x: (x.nivel_emergencia, x.orden_llegada))
        for p in lista:
            print(p)

    def registrarVarios(root, lista_pacientes): 
        print("3. Registrar varios pacientes automáticamente (simular llegada)")
        for p in lista_pacientes:
            root = insertPaciente(root, p)
        return root

    def conteoPorNivel(root): 
        print("4. Ver cuántos pacientes hay por cada nivel de emergencia")
        niveles = {1:0,2:0,3:0,4:0,5:0}
        q = Queue()
        if root:
            q.enqueue(root)
        while not q.is_empty():
            actual = q.dequeue()
            niveles[actual.data.nivel_emergencia] += 1
            if actual.leftchild:
                q.enqueue(actual.leftchild)
            if actual.rightchild:
                q.enqueue(actual.rightchild)
        for n, c in niveles.items():
            print(f"Nivel {n}: {c} pacientes")
    
    def pacienteMenorPrioridad(root): 
        print("3. Mostrar el paciente con menor prioridad (último del heap)")
        if not root:
            print("No hay pacientes.")
            return
        ultimo = getLastNode(root)
        print("Paciente menos urgente:", ultimo.data)
    
    def contarCriticos(root): 
        print("6. Contar cuántos pacientes están en estado crítico (nivel 1 o 2)")
        if not root:
            return 0
        q = Queue()
        q.enqueue(root)
        criticos = 0
        while not q.is_empty():
            current = q.dequeue()
            if current.data.nivel_emergencia <= 2:
                criticos += 1
            if current.leftchild:
                q.enqueue(current.leftchild)
            if current.rightchild:
                q.enqueue(current.rightchild)
        print(f"Pacientes críticos (niveles 1 y 2): {criticos}")



# ---------------- DEMOSTRACIÓN ---------------- #

"""root = None
contador_atendidos = 0

root = insertPaciente(root, Paciente(1, "Ana", 2, 1))
root = insertPaciente(root, Paciente(2, "Luis", 1, 2))
root = insertPaciente(root, Paciente(3, "María", 3, 3))
root = insertPaciente(root, Paciente(4, "Pedro", 1, 4))

print("\n--- Lista de pacientes ---")
mostrarPacientes(root)

reportePacientes(root, contador_atendidos)

print("\n--- Actualizando emergencia de María (ID 3) a nivel 1 ---")
root = actualizarEmergencia(root, 3, 1)
mostrarPacientes(root)

print("\n--- Programar cirugía ---")
root, atendido, contador_atendidos = programarCirugia(root, contador_atendidos)
print("Paciente atendido:", atendido)

reportePacientes(root, contador_atendidos)"""

root = None
root = insertPaciente(root, Paciente(1, "Ana", 2, 1))
root = insertPaciente(root, Paciente(2, "Luis", 1, 2))
root = insertPaciente(root, Paciente(3, "María", 3, 3))
root = insertPaciente(root, Paciente(4, "Pedro", 1, 4))

print("\n--- Lista de pacientes ---")
mostrarPacientes(root)

print("\n--- Siguiente paciente para cirugía ---")
print(root.data)

root, atendido = programarCirugia(root)
print("\nPaciente atendido:", atendido)

print("\n--- Lista actualizada ---")
mostrarPacientes(root)

print("\n--- Pacientes con nivel de emergencia 1 ---")
mostrarPorNivel(root, 1)
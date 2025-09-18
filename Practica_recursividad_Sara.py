productos = [
    {"codigo": "001", "nombre": "Anillo de oro", "categoria": "accesorio", "precio": 1000000},
    {"codigo": "006", "nombre": "Bola de nieve", "categoria": "artesania", "precio": 90000},
    {"codigo": "008", "nombre": "Consola", "categoria": "juguetes", "precio": 7000},
    {"codigo": "002", "nombre": "Cadena de plata", "categoria": "accesorio", "precio": 800000},
    {"codigo": "003", "nombre": "Gorra", "categoria": "accesorio", "precio": 45000},
    {"codigo": "007", "nombre": "Jean", "categoria": "ropa", "precio": 35000},
    {"codigo": "009", "nombre": "Manilla", "categoria": "accesorio", "precio": 25000},
    {"codigo": "004", "nombre": "Muñeca bebe", "categoria": "juguetes", "precio": 10000},
    {"codigo": "005", "nombre": "Plato de cerámica", "categoria": "artesania", "precio": 75000},
    {"codigo": "010", "nombre": "Vestido", "categoria": "ropa", "precio": 50000},
]

def busqueda_producto(productos, nombre, i=0, final=None):
    if final is None:
        final = len(productos) - 1
    if i > final:
        return None
    inmitad = (i + final) // 2

    if productos[inmitad]["nombre"].lower() == nombre.lower():
        return productos[inmitad]
    if nombre.lower() < productos[inmitad]["nombre"].lower():
        return busqueda_producto(productos, nombre, i, inmitad - 1)
    else:
        return busqueda_producto(productos, nombre, inmitad + 1, final)

def calculo_total(productos, i=0, cont=0):
    if i == len(productos):
        return cont
    return calculo_total(productos, i + 1, cont + productos[i]["precio"])

def calculo_precio_promedio(productos, categoria, i=0, suma=0, cont1=0):
    if i == len(productos):
        if cont1 == 0:
            return 0
        return round(suma / cont1)
    if productos[i]["categoria"].lower() == categoria.lower():
        return calculo_precio_promedio(productos, categoria, i + 1,
                                       suma + productos[i]["precio"], cont1 + 1)
    else:
        return calculo_precio_promedio(productos, categoria, i + 1, suma, cont1)

def particionar(lista, pivote, i=0, menores=None, mayores=None, ascendente=True):
    if menores is None: menores = []
    if mayores is None: mayores = []

    if i == len(lista):
        return menores, mayores

    actual = lista[i]
    if ascendente:
        if actual["precio"] <= pivote["precio"]:
            menores.append(actual)
        else:
            mayores.append(actual)
    else:
        if actual["precio"] >= pivote["precio"]:
            menores.append(actual)
        else:
            mayores.append(actual)

    return particionar(lista, pivote, i + 1, menores, mayores, ascendente)

def ordenamiento_precio(productos, ascendente=True):
    if len(productos) <= 1:
        return productos
    pivote = productos[0]
    menores, mayores = particionar(productos[1:], pivote, ascendente=ascendente)
    return ordenamiento_precio(menores, ascendente) + [pivote] + ordenamiento_precio(mayores, ascendente)

def busqueda_de_rangos(productos, minimo, maximo, i=0):
    if i == len(productos):
        return []
    resto = busqueda_de_rangos(productos, minimo, maximo, i + 1)
    if minimo <= productos[i]["precio"] <= maximo:
        return [productos[i]] + resto
    else:
        return resto

def generar_recomenda(productos, producto_referencia, i=0):
    if i == len(productos):
        return []
    resto = generar_recomenda(productos, producto_referencia, i + 1)
    if (productos[i]["categoria"].lower() == producto_referencia["categoria"].lower() and 
        productos[i]["nombre"].lower() != producto_referencia["nombre"].lower()):
        return [productos[i]] + resto
    else:
        return resto

def imprimir_lista(productos, i=0):
    if i == len(productos):
        return
    print(f"- {productos[i]['nombre'].title()} | ${productos[i]['precio']} | {productos[i]['categoria']}")
    imprimir_lista(productos, i + 1)

if __name__ == "__main__":
    print("🔍 BÚSQUEDAS")
    for nombre in ["Anillo de oro", "Vestido", "Camiseta"]:
        p = busqueda_producto(productos, nombre)
        if p:
            print(f"- {p['nombre'].title()} | ${p['precio']} | {p['categoria']}")
        else:
            print(f"- {nombre} no encontrado")

    print(f"\n💰 PRECIO TOTAL: ${calculo_total(productos)}")

    print("\n📊 PROMEDIOS POR CATEGORÍA")
    categorias = set(p["categoria"] for p in productos)
    for categoria in categorias:
        promedio = calculo_precio_promedio(productos, categoria)
        print(f"{categoria}: ${promedio}")

    print("\n⬆️ ORDENAMIENTO ASCENDENTE")
    ordenados_asc = ordenamiento_precio(productos, ascendente=True)
    imprimir_lista(ordenados_asc)

    print("\n⬇️ ORDENAMIENTO DESCENDENTE")
    ordenados_desc = ordenamiento_precio(productos, ascendente=False)
    imprimir_lista(ordenados_desc)

    print("\n🎯 PRODUCTOS EN RANGO $10,000 - $50,000")
    productos_rango = busqueda_de_rangos(productos, 10000, 50000)
    imprimir_lista(productos_rango)

    print("\n💡 RECOMENDACIONES")
    producto_ref = busqueda_producto(productos, "gorra")
    if producto_ref:
        recomendaciones = generar_recomenda(productos, producto_ref)
        imprimir_lista(recomendaciones)
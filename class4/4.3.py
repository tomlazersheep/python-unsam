
# Ejercicio 4.3: Propagar por vecinos
# El siguiente código propaga el fuego de cáda fósforo encendido a sus 
# vecinos inmediatos(si son fósforos nuevos) a lo largo de toda la lista.
# Y repite esta operación mientras sea necesario. ¿Te animás a estimar cuántas 
# operaciones puede tener que hacer, en el peor caso?

def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i, e in enumerate(l):
        if e == 1 and i < n-1 and l[i+1] == 0:
            l[i+1] = 1
            modif = True
        if e == 1 and i > 0 and l[i-1] == 0:
            l[i-1] = 1
            modif = True
    return modif


def propagar(l):
    m = l.copy()
    veces = 0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")
    print(f"Y obtuve  {l}")
    return m


propagar([0, 0, 0, 0, 1])
propagar([0, 0, 1, 0, 0])
propagar([1, 0, 0, 0, 0])

# Preguntas:

# ¿Por qué los tests l[i+1] == 0 y l[i-1] == 0 de la función propagar_al_vecino no causan un IndexError en los bordes de la lista?
# Porque antes hay tests que checkean que i > 0  e i < n-1 con "and" de modo que si alguno de estos da falso el intérprete no sigue evaluando

# ¿Por qué propagar([0, 0, 0, 0, 1]) y propagar([1, 0, 0, 0, 0]), siendo entradas perfectamente simétricas, no generan la misma cantidad de repeticiones de llamadas a la función propagar_al_vecino?
# Por la dirección en que recorro los fósforos, si voy propagando un fósforo delante del iterador cada vez que checkeo el siguiente ya se propagó, por lo que en un ciclo termina de propagar
# En cambio si propago hacia atrás tengo que volver a empezar para toparme con el nuevo fósforo encendido

# Sobre la complejidad. Si te sale, calculá:

# ¿Cuántas veces como máximo se puede repetir el ciclo while en una lista de largo n?
# En el peor de los casos n+1 veces, si tuviera que propagar en contra del sentido en que recorro
# y agrego un ciclo más para determinar que no se deben realizar más cambios

# ¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n?

# Entonces, ¿cuántas operaciones hace como máximo esta versión de propagar en una lista de largo n? ¿Es un algoritmo de complejidad lineal o cuadrática?

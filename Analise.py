import heapq
import timeit


startNode = '1'
Nnode = 150
NnodeNegativo = 7

import random


def gerarGrafoPositivo(n):
    grafo = {}
    for i in range(1, n+1):
        grafo[str(i)] = {}
        for j in range(1, n+1):
            if i == j:
                grafo[str(i)][str(j)] = 0
            else:
                if random.random() < 0.4:
                    grafo[str(i)][str(j)] = float('inf')
                else:
                    distancia = random.randint(1, 10)
                    grafo[str(i)][str(j)] = distancia
    return grafo

def gerarGrafoNegativo(n):
    grafo = {}
    for i in range(1, n+1):
        grafo[str(i)] = {}
        for j in range(1, n+1):
            if i == j:
                grafo[str(i)][str(j)] = 0
            else:
                if random.random() < 0.2:
                    grafo[str(i)][str(j)] = float('inf')
                else:
                    if (random.random() < 0.1):
                        distancia = random.randint(-5, -1)
                    else:
                        distancia = random.randint(1, 10)
                    grafo[str(i)][str(j)] = distancia

    return grafo

def gerarGrafoDenso(n):
    grafo = {}
    for i in range(1, n+1):
        grafo[str(i)] = {}
        for j in range(1, n+1):
            if i != j:
                distancias = random.randint(1, 30)
                grafo[str(i)][str(j)] = distancias
        grafo[str(i)][str(i)] = 0  
    return grafo


grafo1 = gerarGrafoPositivo(Nnode)

grafo2 = gerarGrafoNegativo(NnodeNegativo)

grafo3 = gerarGrafoDenso(Nnode)

#for node in grafo2:
#    custos = " ".join(str(grafo2[node][vizinho]) for vizinho in grafo2[node])
#    print(f"{node}: {custos}")



def dijkstra(grafoDijkstra, startNode):
    distancias = {node: float('inf') for node in grafoDijkstra}
    distancias[startNode] = 0
    listaPrioridade = [(0, startNode)]
    
    while listaPrioridade:
        distanciaAtual, current = heapq.heappop(listaPrioridade)
        if distanciaAtual > distancias[current]:
            continue

        for vizinho, custo in grafoDijkstra[current].items():

            distancia = distanciaAtual + custo

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(listaPrioridade, (distancia, vizinho))
    
    return distancias


def floyd_warshall(grafoFloyd):
    distancias = grafoFloyd.copy()
    
    for k in grafoFloyd:
        for i in grafoFloyd:
            for j in grafoFloyd:
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
    
    return distancias


def bellman_ford(grafoBelman, startNode):
    distancias = {node: float('inf') for node in grafoBelman}
    distancias[startNode] = 0
    
    for _ in range(len(grafoBelman) - 1):
        for node in grafoBelman:
            for vizinho, custo in grafoBelman[node].items():
                if distancias[node] + custo < distancias[vizinho]:
                    distancias[vizinho] = distancias[node] + custo

    for node in grafoBelman:
        for vizinho, custo in grafoBelman[node].items():
            if distancias[node] + custo < distancias[vizinho]:
                raise ValueError("O grafo contém ciclos negativos.")
            
    return distancias



inicioDijk = timeit.default_timer()

print("\nDijkstra:")

inicioDijkPositivo = timeit.default_timer()
dijkPositivo       = dijkstra(grafo1, startNode)
finalDijkPositivo  = timeit.default_timer()
print('Dijkstra tempo para grafo apenas positivo: ', finalDijkPositivo-inicioDijkPositivo )


inicioDijkDenso    = timeit.default_timer()
dijkDenso          = dijkstra(grafo3, startNode)
finalDijkDenso     = timeit.default_timer()

print('Dijkstra tempo para grafo denso: ', finalDijkDenso-inicioDijkDenso)


finalDijk = timeit.default_timer()
print('Dijkstra tempo total: ', finalDijk-inicioDijk )


#print("\nDistâncias a partir do nó inicial", startNode + ":")
#for node, distancia in ##########.items():
#    print("Nó:", node, "Distância:", distancia)


inicioBellman = timeit.default_timer()

print("\nBellman Ford:")


inicioBellmanPositivo = timeit.default_timer()
bellmanPositivo       = bellman_ford(grafo1, startNode)
finalBellmanPositivo  = timeit.default_timer()
print('Bellman tempo para grafo apenas positivo: ', finalBellmanPositivo-inicioBellmanPositivo )

inicioBellmanNegativo = timeit.default_timer()
bellmanNegativo       = bellman_ford(grafo2, startNode)
finalBellmanNegativo  = timeit.default_timer()
print('Bellman tempo para grafo com numeros negativos: ', finalBellmanNegativo-inicioBellmanNegativo )

inicioBellmanDenso    = timeit.default_timer()
bellmanDenso          = bellman_ford(grafo3, startNode)
finalBellmanDenso     = timeit.default_timer()
print('Bellman tempo para grafo denso: ', finalBellmanDenso-inicioBellmanDenso)


finalBellman = timeit.default_timer()
print('Bellmantempo total: ', finalBellman-inicioBellman )


#print("\nDistâncias a partir do nó inicial", startNode + ":")
#for node, distancia in ###########.items():
#    print("Nó:", node, "Distância:", distancia)    




inicioFloid = timeit.default_timer()

print("\nFloyd warshall:")

inicioFloydPositivo = timeit.default_timer()
floydPositivo       = floyd_warshall(grafo1)
finalFloydPositivo  = timeit.default_timer()
print('Floyd tempo para grafo apenas positivo: ', finalFloydPositivo-inicioFloydPositivo)


inicioFloydNegativo = timeit.default_timer()
floydNegativo       = floyd_warshall(grafo2)
finalFloydNegativo  = timeit.default_timer()
print('Floyd tempo para grafo com numeros negativos: ', finalFloydNegativo-inicioFloydNegativo)


inicioFloydDenso    = timeit.default_timer()
floydDenso          = floyd_warshall(grafo3)
finalFloydDenso     = timeit.default_timer()
print('Floyd tempo para grafo denso: ', finalFloydDenso-inicioFloydDenso)


finalFloid = timeit.default_timer()
print('Floyd: ', finalFloid-inicioFloid )


#print("\nMatriz de distâncias:")
#for i in &&&&&&&&&&:
#    row = [str(##########[i][j]) if ##########[i][j] != float('inf') else 'inf' for j in &&&&&&&&&&]
#    print(' '.join(row))


print('\nAnalise grafo Positivo:\n')
print('Dijkstra: ', finalDijkPositivo-inicioDijkPositivo )
print('Bellman: ', finalBellmanPositivo-inicioBellmanPositivo )
print('Floyd: ', finalFloydPositivo-inicioFloydPositivo)

print('\nAnalise grafo Negativo:\n')
print('Bellman: ', finalBellmanNegativo-inicioBellmanNegativo )
print('Floyd: ', finalFloydNegativo-inicioFloydNegativo)

print('\nAnalise grafo Denso:\n')
print('Dijkstra: ', finalDijkDenso-inicioDijkDenso )
print('Bellman: ', finalBellmanDenso-inicioBellmanDenso )
print('Floyd: ', finalFloydDenso-inicioFloydDenso)
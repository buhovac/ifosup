from __future__ import annotations
from typing import Any, Dict, List, Tuple
import heapq
import math

Node = Any
AdjList = Dict[Node, List[Tuple[float, Node]]]  # (weight, neighbor)


def arcs_sortants(P: AdjList, u: Node) -> List[Tuple[float, Node]]:
    return P.get(u, [])


def dijkstra(P: AdjList, depart: Node, arrivee: Node) -> Tuple[List[Node], float]:
    dist = {node: math.inf for node in P}
    prev = {node: None for node in P}
    visited = set()

    dist[depart] = 0
    pq = [(0, depart)]

    while pq:
        d_u, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        if u == arrivee:
            break

        for w, v in arcs_sortants(P, u):
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    # Ako nema puta
    if math.isinf(dist[arrivee]):
        return [], math.inf

    # Rekonstrukcija puta
    path = []
    cur = arrivee
    while cur is not None:
        path.append(cur)
        if cur == depart:
            break
        cur = prev[cur]

    path.reverse()
    return path, dist[arrivee]


# ----------------------------
# MAIN — ISPIS U KONZOLU
# ----------------------------
if __name__ == "__main__":

    graph = {
        "A": [(2, "B"), (5, "C")],
        "B": [(10, "E")],
        "C": [(3, "D")],
        "D": [(2, "E")],
        "E": []
    }

    depart = "A"
    arrivee = "E"

    chemin, distance = dijkstra(graph, depart, arrivee)

    print("===== DIJKSTRA RESULT =====")
    print(f"Start : {depart}")
    print(f"Goal  : {arrivee}")

    if chemin:
        print("Chemin le plus court :")
        print(" -> ".join(chemin))
        print(f"Distance totale : {distance}")
    else:
        print("Aucun chemin trouvé")

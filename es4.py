from typing import Container


class Graph:
    def __init__(self, dim: int):
        self._matrix = []
        for i in range(dim):
            self._matrix.append([False for i in range(dim)])

    def connect(self, node_1: int, node_2: int) -> None:
        self._matrix[node_1][node_2] = True
        self._matrix[node_2][node_1] = True

    def are_connected(self, node_1: int, node_2: int) -> bool:
        return self._matrix[node_1][node_2]

    def get_connected(self, node: int) -> Container[int]:
        return [i for i in range(len(self)) if self._matrix[node][i]]

    def __len__(self) -> int:
        return len(self._matrix)

    def __str__(self) -> str:
        mtx = []
        for row in self._matrix:
            mtx.append(" ".join([str(1) if i else str(0) for i in row]))
        return "\n".join(mtx)


def main():
    # creo un grafo con 10 nodi
    g = Graph(dim=10)

    # controllo dimensione
    print(len(g))

    # connetto i nodi
    g.connect(0, 2)
    g.connect(1, 2)
    g.connect(1, 3)
    g.connect(2, 3)
    g.connect(2, 5)
    g.connect(3, 4)
    g.connect(3, 6)
    g.connect(6, 8)
    g.connect(5, 8)
    g.connect(4, 9)
    g.connect(3, 9)
    g.connect(7, 2)

    # controllo simmetria connessione
    print(g.are_connected(2, 5), g.are_connected(5, 2))
    print(g.are_connected(0, 7), g.are_connected(7, 0))

    # ottengo nodi connessi
    print(g.get_connected(2))

    # stampo matrice di adiacenze
    print(str(g))


if __name__ == "__main__":
    main()

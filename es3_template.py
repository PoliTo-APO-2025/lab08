from typing import Any


class BinaryTree:

    def add(self, key: Any) -> None:
        pass

    def min(self) -> Any:
        pass

    def __repr__(self) -> str:
        pass

    def __len__(self) -> int:
        pass


def main():
    # creo albero vuoto e stamp
    b = BinaryTree()
    print(b)  # []

    # aggiungo elementi all'albero
    keys = [3, 10, 7, 1, 2, 3, 3, 9, 3, 4, 5, 4, 3, 2, 5]
    for key in keys:
        b.add(key)

    # numero elementi
    print(len(b))  # 15

    # stampo albero in modo ordinato
    print(b)  # [1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 7, 9, 10]

    # trovo il minimo
    print(b.min())  # 1


if __name__ == "__main__":
    main()

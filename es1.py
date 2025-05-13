class SortableCouple:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __lt__(self, other):
        return self._a + self._b < other.get_a() + other.get_b()

    def __repr__(self):
        return "({}, {})".format(self._a, self._b)


class CoupleSorter:
    def __call__(self, elm):
        return elm.get_a() - elm.get_b()


def main():
    a = SortableCouple(3, 3)
    b = SortableCouple(1, 5)
    c = SortableCouple(5, 0)

    couple_list = [a, b, c]

    couple_list.sort()
    print(couple_list)

    couple_list.sort(key=lambda x: x.get_a() * x.get_b())
    print(couple_list)

    couple_list.sort(key=CoupleSorter())
    print(couple_list)


if __name__ == "__main__":
    main()

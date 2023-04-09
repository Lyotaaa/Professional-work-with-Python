class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iterator = [iter(self.list_of_list)]
        self.result = []
        return self

    def __next__(self):
        while self.iterator:
            i = self.iterator.pop()
            try:
                while True:
                    data = next(i)
                    if isinstance(data, list):
                        self.iterator.append(i)
                        i = iter(data)
                    else:
                        self.result.append(data)
            except StopIteration:
                pass

        return self.result


def test_3():
    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
        "!",
    ]

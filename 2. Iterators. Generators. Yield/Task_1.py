class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.external_counter = 0
        self.internal_counter = 0
        return self

    def __next__(self):
        if self.external_counter == len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.external_counter][self.internal_counter]
        if self.internal_counter >= len(self.list_of_list[self.external_counter]) - 1:
            self.internal_counter = 0
            self.external_counter += 1
        else:
            self.internal_counter += 1

        return item


def test_1():
    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
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
    ]

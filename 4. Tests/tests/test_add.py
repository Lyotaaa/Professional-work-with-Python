from unittest import TestCase
from parameterized import parameterized
import pytest
from src.add import (
    human_output,
    document_output,
    output_all_documents,
    add_new_document,
    delete_document,
    creating_new_shelf,
)


class Test_Add_Unittest(TestCase):
    @parameterized.expand(
        [
            ["2207 876234", "Василий Гупкин"],
            ["11-2", "Геннадий Покемонов"],
            ["10006", "Аристарх Павлов"],
            [112, None],
        ]
    )
    def test_human_output(sefl, query, expected):
        sefl.assertEqual(human_output(query), expected)

    @parameterized.expand(
        [["2207 876234", "1"], ["11-2", "1"], ["10006", "2"], [112, None]]
    )
    def test_document_output(sefl, query, expected):
        sefl.assertEqual(document_output(query), expected)

    def test_output_all_documents(self):
        expected = "\npassport 2207 876234 Василий Гупкин\ninvoice 11-2 Геннадий Покемонов\ninsurance 10006 Аристарх Павлов\n"
        self.assertEqual(output_all_documents(), expected)


class Test_Add_Pytest:
    def test_addadd_new_document(self):
        assert add_new_document("+7-912", "invoice", "Иван Иванов", "4") == "4"
        assert add_new_document("+7-912", "invoice", "Иван Иванов", 4) != "4"

    @pytest.mark.parametrize(
        "query, expected",
        (
            ["2207 876234", (True, True, "2207 876234")],
            ["11-2", (True, True, "11-2")],
            ["10006", (True, True, "10006")],
            [10006, (False, False, 10006)],
        ),
    )
    def test_delete_document(self, query, expected):
        assert delete_document(query) == expected

    @pytest.mark.parametrize(
        "query, expected",
        (["1", False], ["2", False], ["3", False], ["5", True], [7, True]),
    )
    def test_creating_new_shelf(self, query, expected):
        assert creating_new_shelf(query) == expected

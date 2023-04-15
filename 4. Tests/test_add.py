from unittest import TestCase
from parameterized import parameterized
import pytest
from src.add import (
    human_output,
    document_output,
    output_all_documents,
    add_new_document,
    delete_document,
    document_migration,
    creating_new_shelf,
)


class TestAdd(TestCase):
    @parameterized.expand(
        [
            ["2207 876234", "Василий Гупкин"],
            ["11-2", "Геннадий Покемонов"],
            ["10006", "Аристарх Павлов"],
            [112, None],
        ]
    )
    def test_human_output(sefl, input_, expected):
        sefl.assertEqual(human_output(input_), expected)

    @parameterized.expand(
        [
            ["2207 876234", "1"],
            ["11-2", "1"],
            ["10006", "2"],
            [112, None]
        ]
    )
    def test_document_output(sefl, input_, expected):
        sefl.assertEqual(document_output(input_), expected)

    def test_output_all_documents(self):
        expected = "\npassport 2207 876234 Василий Гупкин\ninvoice 11-2 Геннадий Покемонов\ninsurance 10006 Аристарх Павлов\n"
        self.assertEqual(output_all_documents(), expected)

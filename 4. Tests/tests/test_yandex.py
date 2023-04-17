from unittest import TestCase
import pytest
from src.yandex import YandexDisk, yandex_info

res_YA = yandex_info()


class Test_Add_Unittest(TestCase):
    def test_get_folder(self):
        expected_1 = (False, "1")
        expected_2 = (True, 200)
        self.assertEqual(res_YA.get_folder("1"), expected_1)
        self.assertEqual(res_YA.get_folder("!Test"), expected_2)

    def test_create_a_folder(self):
        expected_1 = (False, "1")
        expected_2 = (True, 201)
        self.assertEqual(res_YA.create_a_folder("1"), expected_2)
        self.assertEqual(res_YA.create_a_folder("1"), expected_1)

    def test_ddelete_folder(self):
        expected_1 = (False, "1")
        expected_2 = (True, 204)
        self.assertEqual(res_YA.delete_folder("1"), expected_2)
        self.assertEqual(res_YA.delete_folder("1"), expected_1)


class Test_Yandex_Pytest:
    def test_get_folder(self):
        assert res_YA.get_folder("1") == (False, "1")
        assert res_YA.get_folder("test") == (True, 200)

    def test_create_a_folder(self):
        assert res_YA.create_a_folder("1") == (True, 201)
        assert res_YA.create_a_folder("1") == (False, "1")

    def test_delete_folder(self):
        assert res_YA.delete_folder("test") == (True, 204)
        assert res_YA.delete_folder("2") == (False, "2")

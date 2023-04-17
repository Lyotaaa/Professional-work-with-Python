from src.HW_4 import (
    list_filtering,
    get_unique_id,
    get_sales,
    get_distribution,
    sort_dict,
)
from unittest import TestCase
from parameterized import parameterized
import pytest


class Test_HW_4_Pytest:
    @pytest.mark.parametrize(
        "expected",
        (
            {
                "visit1": ["Москва", "Россия"],
                "visit3": ["Владимир", "Россия"],
                "visit7": ["Тула", "Россия"],
                "visit8": ["Тула", "Россия"],
                "visit9": ["Курск", "Россия"],
                "visit10": ["Архангельск", "Россия"],
            },
        ),
    )
    def test_list_filtering(self, expected):
        geo_logs = list_filtering()
        result = {}
        for i in geo_logs:
            for key, value in i.items():
                result[key] = value
        assert result == expected

    def test_get_unique_id(self):
        result = get_unique_id()
        assert result == [15, 35, 54, 98, 119, 213]

    def test_get_sales(self):
        result = get_sales()
        assert result == "yandex"

    def test_get_distribution(self):
        result = get_distribution()
        assert result == [("2", "42.9"), ("3", "57.1")]

    def test_sort_dict(self):
        result = sort_dict()
        assert result == {
            "2018-01-01": {
                "yandex": {"cpc": {100: {400: {"kek": {2022: "Hello World"}}}}}
            }
        }

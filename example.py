from typing import Any
import pytest


class TestDict:
    test_data_update_dict = [
        pytest.param(
            {0: "zero"},
            {1: "one"},
            {0: "zero", 1: "one"}
        ),
        pytest.param(
            {},
            {},
            {}
        ),
        pytest.param(
            {0: "zero"},
            {},
            {0: "zero"}
        ),
        pytest.param(
            {},
            {0: "zero"},
            {0: "zero"}
        )
    ]

    def test_add_item_to_dict(self):
        test_dict = {}

        test_dict[1] = "one"

        assert test_dict[1] == "one"

    @pytest.mark.parametrize(
        "dict1, dict2, expected",
        test_data_update_dict
    )
    def test_update_dict(
        self,
        dict1: dict[Any, Any],
        dict2: dict[Any, Any],
        expected: dict[Any, Any]
    ):
        dict1.update(dict2)

        assert dict1 == expected

    def test_item_by_non_existing_key(self):
        test_dict = {}
        with pytest.raises(KeyError):
            test_dict[1]


class TestInt:
    def test_type_after_division(self):
        number_one = 10
        number_two = 5
        division_result = number_one / number_two

        assert isinstance(division_result,
                          float), f" {type(division_result)} не float"

    def test_bit_left_step(self):
        number = 5
        step = 8
        result = number << step
        expected_result = 1280

        assert result == expected_result, f"битовый оператор '<<' отрабатывает с ошибкой," \
                                          f" результат {result} отличен от ожидаемого {expected_result}"


class TestString:
    @pytest.mark.parametrize(
        ("proc", "final"),
        [("", []), ("a", ["a"]), ("a b", ["a", "b"]), ("ab c", ["ab", "c"])],
    )
    def test_split(self, proc, final):
        assert proc.split() == final

    def test_lower(self):
        assert "AaBbCcDd12".lower() == "aabbccdd12"

    def test_negative_str_plus_int(self):
        with pytest.raises(TypeError) as exc:
            "123" + 1
        assert str(exc.value) == 'нельзя прибавлять к строке не строковый элемент'
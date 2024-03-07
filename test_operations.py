from main import Length
import pytest


@pytest.mark.parametrize("first, second, result", [(Length("20 m"), 7, "27.0 m"),
                                                    (Length("15000"), 5, "15.005 km"),
                                                    (Length("20 km"), 35000, "55.0 km"),
                                                    (Length("0.01 m"), 0.5, "5.1 dm"),
                                                    (Length("150 cm"), 0.4, "1.9 m")])
def test_add(first, second, result):
    assert str(Length.__add__(first, second)) == result


@pytest.mark.parametrize("first, second, result", [(Length("20 m"), 7, "13.0 m"),
                                                    (Length("15000"), 5, "14.995 km"),
                                                    (Length("35 km"), 20000, "15.0 km"),
                                                    (Length(0.5), 0.1, "4.0 dm"),
                                                    (Length("150 cm"), 0.4, "1.1 m")])
def test_sub(first, second, result):
    assert str(Length.__sub__(first, second)) == result



@pytest.mark.parametrize("left_operand, factor, result", [(Length("20 m"), 3, "60.0 m"), 
                                                          (Length("150 cm"), 5, "7.5 m"), 
                                                          (Length("0.2 km"), 2, "400.0 m")])
def test_mul(left_operand, factor, result):
    assert str(Length.__mul__(left_operand, factor)) == result


@pytest.fixture
def example_data():
    return [
        {
            "numerator": Length("20 m"),
            "denominator": 4,
            "result": "5.0 m"
        },
        {
            "numerator": Length("150 cm"),
            "denominator": 25,
            "result": "6.0 cm"
        }
    ]


def test_div(example_data):
    for element_dict in example_data:
        if element_dict.get('denominator') == 0:
            assert ZeroDivisionError()
        elif type(element_dict.get('denominator')) != int:
            assert TypeError()
        else:
            assert str(Length.__truediv__(element_dict.get('numerator'), element_dict.get('denominator'))) == element_dict.get('result')























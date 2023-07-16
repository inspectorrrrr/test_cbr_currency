import pytest


@pytest.mark.parametrize('get_cbr_rates', ['15/07/1023'], indirect=True)
def test_response_code(get_cbr_rates):
    assert get_cbr_rates.status_code == 200
    #  Проверка некорректной даты
    assert "Error in parameters" in get_cbr_rates.text, "Ошибка: некорректная дата"

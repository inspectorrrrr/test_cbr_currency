import pytest

"""
Проверка времени выполнения запроса: Измерьте время выполнения запроса и установите предельные значения для времени 
ответа, чтобы убедиться, что сервис работает достаточно быстро.
"""


@pytest.mark.parametrize('get_cbr_rates', ['15/07/2023'], indirect=True)
def test_api_response_time(get_cbr_rates):
    assert get_cbr_rates.elapsed.total_seconds() < 1.0  # Проверка времени выполнения менее 1 секунды

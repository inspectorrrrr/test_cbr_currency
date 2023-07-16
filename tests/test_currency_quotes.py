import pytest


@pytest.mark.parametrize('get_cbr_rates', ['15/07/2023'], indirect=True)
def test_currency_quotes(get_cbr_rates):
    assert get_cbr_rates.status_code == 200, "Ошибка: невозможно получить доступ к API"
    assert get_cbr_rates.headers["Content-Type"] == "application/xml; charset=windows-1251", "Ошибка: неверный " \
                                                                                             "формат ответа"
    # Проверяем, что ответ содержит все необходимые поля
    xml = get_cbr_rates.content.decode("windows-1251")
    assert "<ValCurs" in xml, "Ошибка: отсутствует элемент ValCurs"
    assert "<Valute" in xml, "Ошибка: отсутствует элемент Valute"
    assert "<NumCode" in xml, "Ошибка: отсутствует элемент NumCode"
    assert "<CharCode>" in xml, "Ошибка: отсутствует элемент CharCode"
    assert "<Nominal>" in xml, "Ошибка: отсутствует элемент Nominal"
    assert "<Name>" in xml, "Ошибка: отсутствует элемент Name"
    assert "<Value>" in xml, "Ошибка: отсутствует элемент Value"

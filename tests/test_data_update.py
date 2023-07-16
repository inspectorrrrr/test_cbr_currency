import pytest
import xml.etree.ElementTree as xml_et
import datetime


"""
Проверка обновления данных. Добавьте проверку на то, что данные обновляются регулярно. Для этого можно сохранять 
дату последнего обновления данных и проверять, что она не старше определенного периода (например, 24 часа).
"""


@pytest.mark.parametrize('get_cbr_rates', ['15/07/2023'], indirect=True)
def test_data_update(get_cbr_rates):
    assert get_cbr_rates.status_code == 200, "Ошибка: невозможно получить доступ к API"
    root = xml_et.fromstring(get_cbr_rates.content)
    date_str = root.get("Date")
    date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
    assert datetime.datetime.now() - date < datetime.timedelta(days=2), "Ошибка: данные не были обновлены за " \
                                                                        "последние 48 часа"

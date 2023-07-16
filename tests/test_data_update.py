import pytest
import xml.etree.ElementTree as xml_et
import datetime

"""
Проверка обновления данных. Добавьте проверку на то, что данные обновляются регулярно. Для этого можно сохранять 
дату последнего обновления данных и проверять, что она не старше определенного периода (например, 24 часа).
"""


def test_data_update(get_cbr_rates_last_date):
    assert get_cbr_rates_last_date.status_code == 200, "Ошибка: невозможно получить доступ к API"
    root = xml_et.fromstring(get_cbr_rates_last_date.content)
    date_str = root.get("Date")
    date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
    assert datetime.datetime.now() - date < datetime.timedelta(days=2), "Ошибка: данные не были обновлены за " \
                                                                        "последние 48 часа"

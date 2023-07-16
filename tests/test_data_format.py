import pytest
import xml.etree.ElementTree as xml_et


@pytest.mark.parametrize('get_cbr_rates', ['15/07/2023'], indirect=True)
def test_data_format(get_cbr_rates):
    root = xml_et.fromstring(get_cbr_rates.text)
    values = [float(valute.find('Value').text.replace(',', '.')) for valute in root.findall('Valute')]
    assert isinstance(values[0], float)  # Проверяем, что числовые значения являются действительными числами

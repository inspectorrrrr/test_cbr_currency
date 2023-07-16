import pytest
import lxml.etree as lx_et


@pytest.mark.parametrize('get_cbr_rates', ['15/07/2023'], indirect=True)
def test_xml_valid(get_cbr_rates):
    # Проверяем статус-код ответа
    assert get_cbr_rates.status_code == 200, "Ошибка: невозможно получить доступ к API"
    # Проверяем, что ответ содержит валидный XML
    schema_url = "http://www.cbr.ru/StaticHtml/File/92172/ValCurs.xsd"
    schema = lx_et.XMLSchema(lx_et.parse(schema_url))
    xml = lx_et.fromstring(get_cbr_rates.text.encode('windows-1251'))
    assert schema.validate(xml), "Ошибка: невалидный XML-ответ"

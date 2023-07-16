import requests
import pytest

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


@pytest.fixture
def get_cbr_rates(request):
    date = request.param
    url = f'{URL}?date_req={date}'
    # Отправляем запрос на получение курсов валют
    response = requests.get(url)
    return response


"""
@pytest.fixture
def get_cbr_xml():
    url = 'http://www.cbr.ru/StaticHtml/File/92172/ValCurs.xsd'
    # Отправляем запрос на получение схемы XSD
    response = requests.get(url)
    return response
"""

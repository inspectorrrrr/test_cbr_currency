import requests
import pytest

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


@pytest.fixture
def get_cbr_rates(request):
    date = request.param
    url = f'{URL}?date_req={date}'
    # Отправляем запрос на получение курсов валют на определенную дату
    response = requests.get(url)
    return response


@pytest.fixture
def get_cbr_rates_last_date():
    # Отправляем запрос на получение курсов валют на последнюю дату
    response = requests.get(URL)
    return response

import pytest
import xml.etree.ElementTree as xml_et


@pytest.mark.parametrize('get_cbr_rates', ['15/07/2023'], indirect=True)
def test_currency_codes(get_cbr_rates):
    root = xml_et.fromstring(get_cbr_rates.text)
    codes = [valute.find('CharCode').text for valute in root.findall('Valute')]
    # Проверяем, что все коды валют соответствуют реальным кодам валют
    currency_codes = ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR',
                      'KZT', 'CAD', 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT',
                      'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY']
    for i in currency_codes:
        assert i in codes

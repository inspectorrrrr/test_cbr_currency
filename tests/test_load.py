import pytest


@pytest.mark.parametrize('get_cbr_rates', ['15/07/2023'], indirect=True)
def test_load(get_cbr_rates):
    for i in range(100):
        assert get_cbr_rates.status_code == 200

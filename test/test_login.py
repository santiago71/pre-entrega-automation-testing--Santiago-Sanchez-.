import pytest
from utils.data_reader import read_csv


@pytest.mark.parametrize("username,password,expected,error_message", read_csv("data/login.csv"))
def test_login(login_p, username, password, expected, error_message):

    login_p.login(username, password)

    if expected:

        assert "inventory.html" in login_p.driver.current_url

    else:

        actual_error = login_p.get_error_message()

        assert actual_error == error_message

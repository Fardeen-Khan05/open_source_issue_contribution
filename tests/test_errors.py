from fixit import cli

def test_invalid_json_returns_1():
    assert cli.main(["json", "{bad"]) == 1

def test_invalid_password_returns_1():
    assert cli.main(["password", "--length", "0"]) == 1

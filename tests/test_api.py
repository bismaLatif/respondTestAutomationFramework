import allure

@allure.feature("API Feature")
def test_get_user(api_client, login_data):
    # Perform the login to get the token
    login_response = api_client.login(login_data["valid_email"], login_data["valid_password"])
    assert login_response.status_code == 200



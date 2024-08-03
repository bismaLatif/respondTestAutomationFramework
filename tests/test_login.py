import allure
from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Login Feature")
def test_login(driver, login_data):
    login_page = LoginPage(driver)
    login_page.login(login_data["valid_email"], login_data["valid_password"])
    wait = WebDriverWait(driver, 20)  # Adjust timeout as needed
    # Wait for the URL to contain "dashboard"
    wait.until(EC.url_contains("dashboard"))
    expected_url = login_data["dashboard_url"]
    assert driver.current_url == expected_url, f"Expected URL {expected_url}, but got {driver.current_url}"
    login_page.click_signout()
    assert driver.current_url == login_data["login_url"]


def test_invalid_login(driver, login_data):
    login_page = LoginPage(driver)
    login_page.login(login_data["invalid_email"], login_data["valid_password"])
    alert = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(login_page.alert))
    assert "Invalid username or password" in alert.text




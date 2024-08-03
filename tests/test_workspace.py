import pytest
import allure
from pages.login_page import LoginPage
from pages.workspace_page import WorkspacePage


@allure.feature("WorkFlow Feature")
def test_workspace_functionality(driver, login_data):
    # Perform login
    login_page = LoginPage(driver)
    login_page.login(login_data['valid_email'], login_data['valid_password'])
    workspace_page = WorkspacePage(driver)
    workspace_page.navigate_to_workspace_action()
    workspace_page.add_workspace_screen()
    current_url = driver.current_url
    assert "workflows" in current_url, f"Expected 'workflows' in URL, but got {current_url}"
    workspace_page.click_add_workflow_button()
    workspace_page.click_start_from_scratch()

    # workspace_page.fill_modal_form("test", "test")
    # workspace_page.get_page_text()
    # assert workspace_page.get_truncated_text() == "test"

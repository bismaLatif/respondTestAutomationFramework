from pages.login_page import LoginPage
from pages.workspace_page import WorkspacePage



def test_workspace_functionality(driver, login_data):
    # Perform login
    login_page = LoginPage(driver)
    login_page.login(login_data['valid_email'], login_data['valid_password'])
    workspace_page = WorkspacePage(driver)
    workspace_page.navigate_to_workspace()
    current_url = driver.current_url
    assert "workflows" in current_url, f"Expected 'workflows' in URL, but got {current_url}"
    workspace_page.click_add_workflow_button()
    workspace_page.click_start_from_scratch()
    workspace_page.enter_workflow_name("t88st")
    workspace_page.enter_workflow_description("testttt")
    workspace_page.click_create_button()
    workspace_page.verify_text_presence("tst")


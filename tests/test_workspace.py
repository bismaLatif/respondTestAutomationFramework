import uuid

import pytest

from pages.login_page import LoginPage
from pages.workspace_page import WorkspacePage


@pytest.mark.description("Verifies the functionality of workflow creation.")
def test_workspace_functionality(driver, login_data, workflow_data):
    # Perform login
    login_page = LoginPage(driver)
    login_page.login(login_data['valid_email'], login_data['valid_password'])
    workspace_page = WorkspacePage(driver)
    workspace_page.navigate_to_workspace()
    current_url = driver.current_url
    assert "workflows" in current_url, f"Expected 'workflows' in URL, but got {current_url}"
    workspace_page.click_add_workflow_button()
    workspace_page.click_start_from_scratch()
    unique_suffix = uuid.uuid4().hex[:6]  # Generating a short unique suffix
    workflow_name = workflow_data['workflow_name']+unique_suffix  # Or use any other format you prefer
    workspace_page.enter_workflow_name(workflow_name)
    workspace_page.enter_workflow_description(workflow_data['workflow_description'])
    workspace_page.click_create_button()
    workspace_page.verify_text_presence(workflow_name)





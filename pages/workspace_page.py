import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class WorkspacePage(BasePage):
    # Define locators for the workspace page
    new_workspace_button = (By.CSS_SELECTOR, '.dls-text-text-selected.dls-txt-button')
    add_workspace = (By.XPATH,
                     '//div[text()="My New Workspace" and contains(@class, "dls-text-text-selected") and contains(@class, "dls-txt-button")]')
    add_workflow_button = (By.CSS_SELECTOR, 'button[data-pw="btn-add-workflow"]')
    start_from_scratch_button = (By.XPATH, '//button[.//span[text()="Start From Scratch"]]')
    input_name = (By.ID, "input-144")
    input_description = (By.ID, "input-146")
    create_workflow_button = (By.CSS_SELECTOR, 'span.dls-txt-button.dls-inline-flex')
    modal_locator = (By.XPATH, "//div[contains(text(), 'Add Workflow')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_workspace_action(self):
        # Use locator directly without unpacking
        self.wait.until(EC.visibility_of_element_located(self.new_workspace_button)).click()

    def add_workspace_screen(self):
        # Use locator directly without unpacking
        self.wait.until(EC.visibility_of_element_located(self.add_workspace)).click()
        self.driver.get("https://app.respond.io/space/241198/workflows")

    def click_add_workflow_button(self):
        # Use locator directly without unpacking
        self.wait.until(EC.element_to_be_clickable(self.add_workflow_button)).click()

    def click_start_from_scratch(self):
        self.wait.until(EC.element_to_be_clickable(self.start_from_scratch_button)).click()
    def fill_modal_form(self, name, description):
        # Fill in the input fields in the modal
        name_input = self.wait.until(EC.visibility_of_element_located(self.input_name))
        name_input.clear()
        name_input.send_keys(name)

        description_input = self.wait.until(EC.visibility_of_element_located(self.input_description))
        description_input.clear()
        description_input.send_keys(description)
        # Click the create workflow button
        create_button = self.wait.until(EC.element_to_be_clickable(self.create_workflow_button))
        create_button.click()
    def get_page_text(self):
            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.dls-max-w-[300px].dls-truncate'))
        )
            return element.text

    def test_truncated_text(driver):
        assert driver.get_page_text() == "test"





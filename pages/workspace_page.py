import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class WorkspacePage(BasePage):
    # Define locators for the workspace page
    add_workflow_button = (By.CSS_SELECTOR, 'button[data-pw="btn-add-workflow"]')
    navigate_to_workflow_screen = (By.CSS_SELECTOR,
                                   "a[href='/space/241150/workflows'] .v-list-item__append svg.dls-h-icon-md.dls-w-icon-md.dls-text-icon-md.dls-text-icon-primary.dls-fill-icon-primary")
    start_from_scratch_button = (By.XPATH, '//button[.//span[text()="Start From Scratch"]]')
    input_name = (By.CSS_SELECTOR, "input[placeholder='Name your workflow (only visible internally)']")
    input_description = (By.CSS_SELECTOR, "input[placeholder='Briefly describe your workflow for internal reference']")
    create_workflow_button = (By.XPATH, "//span[text()='Create']")
    modal_locator = (By.XPATH, "//div[contains(text(), 'Add Workflow')]")
    actual_workflow_name = (By.XPATH, "//div[@class='dls-max-w-[300px] dls-truncate']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    def navigate_to_workspace(self):
        # Wait until the element is present and visible, then click it
        svg_element = self.wait.until(
            EC.presence_of_element_located(self.navigate_to_workflow_screen)
        )
        svg_element.click()
        time.sleep(2)

    def click_add_workflow_button(self):
        # Use locator directly without unpacking
        self.wait.until(EC.element_to_be_clickable(self.add_workflow_button)).click()

    def click_start_from_scratch(self):
        self.wait.until(EC.element_to_be_clickable(self.start_from_scratch_button)).click()

    def enter_workflow_name(self, name):
        # Wait for the input element to be present
        name_element = self.wait.until(
            EC.presence_of_element_located(self.input_name)
        )
        # Clear the input field if needed and enter the new name

        name_element.send_keys(name)

    def enter_workflow_description(self, description):
        # Wait for the input element to be present using the placeholder text
        description_element = self.wait.until(
            EC.presence_of_element_located(self.input_description)
        )
        description_element.send_keys(description)

    def click_create_button(self):
        # Wait for the button with the text "Create" to be clickable
        create_button = self.wait.until(
            EC.element_to_be_clickable(self.create_workflow_button)
        )
        create_button.click()

    def verify_text_presence(self, expected_workflow_name):
        # Wait for the div with the specified text to be present
        self.wait.until(
            EC.text_to_be_present_in_element(self.actual_workflow_name
                                             ,
                                             expected_workflow_name
                                             )
        )

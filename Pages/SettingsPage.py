from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "Settings.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.settings_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.settings = {
            "settingsLink": (By.XPATH, '//a[@href="#/Settings"]'),
            "radiologySubmodule": (By.XPATH, '//a[@href="#/Settings/RadiologyManage" and contains(text(),"Radiology")]'),
            "addImagingTypeButton": (By.XPATH, '//a[text()="Add Imaging Type"]'),
            "imagingItemNameField": (By.ID, 'ImagingTypeName'),
            "addButton": (By.ID, 'Add'),
            "searchBar": (By.ID, 'quickFilterInput'),
            "dynamicTemplates": (By.XPATH, '(//a[@href="#/Settings/DynamicTemplates"])[2]'),
            "addTemplateButton": (By.XPATH, '//a[@id="id_btn_template_newTemplate"]'),
            "templateName": (By.XPATH, '//input[@placeholder="template name"]'),
            "templateType": (By.ID, 'TemplateTypeId'),
            "templateCode": (By.XPATH, '//input[@placeholder="enter template code"]'),
            "iframeLocator": (By.CSS_SELECTOR, 'iframe[title="Rich Text Editor, editor1"]'),
            "textField": (By.CSS_SELECTOR, 'html[dir="ltr"] body'),
            "typeOption": (By.XPATH, '//span[text()="Discharge Summary"]')
        }

    def verify_dynamic_templates(self):
        """
        /**
        * @Test5
        * @description This method verifies the creation of dynamic templates in the Settings module.
        * It navigates to the Dynamic Templates submodule, fills out the template details including
        * template type, name, code, and text field, and ensures the template is added successfully.
        * @expected
        * The template should be created successfully and appear in the templates list.
        */
        """
        try:
            wait = WebDriverWait(self.driver, 10)

            text_field = self.settings_data["Templates"][0]["TextField"]
            template_name = self.settings_data["Templates"][1]["TemplateName"]
            template_code = self.settings_data["Templates"][2]["TemplateCode"]
            template_type = self.settings_data["Templates"][3]["TemplateType"]

            # Navigate to Settings module
            self.driver.find_element(*self.settings["settingsLink"]).click()
            time.sleep(2)

            # Click on Dynamic Templates submodule
            self.driver.find_element(*self.settings["dynamicTemplates"]).click()
            time.sleep(2)

            # Click on Add Template button
            self.driver.find_element(*self.settings["addTemplateButton"]).click()
            time.sleep(2)

            # Select Template Type
            select = Select(self.driver.find_element(*self.settings["templateType"]))
            select.select_by_visible_text(template_type)

            # Enter Template Name
            self.driver.find_element(*self.settings["templateName"]).send_keys(template_name)

            # Enter Template Code
            self.driver.find_element(*self.settings["templateCode"]).send_keys(template_code)

            # Switch to iframe before interacting with the text field
            iframe = wait.until(EC.presence_of_element_located(self.settings["iframeLocator"]))
            self.driver.switch_to.frame(iframe)

            # Enter text in the text field
            self.driver.find_element(*self.settings["textField"]).click()
            self.driver.find_element(*self.settings["textField"]).send_keys(text_field)

            self.driver.switch_to.default_content()

            # Click Add Button
            self.driver.find_element(*self.settings["addButton"]).click()
            time.sleep(2)

            # Verify if the template is added successfully
            success_message = wait.until(EC.visibility_of_element_located(self.settings["successMessage"]))
            if success_message:
                print("Template added successfully.")
                return True

            print("Failed to add template.")
            return False

        except Exception as e:
            print(f"Error verifying dynamic templates: {e}")
            return False


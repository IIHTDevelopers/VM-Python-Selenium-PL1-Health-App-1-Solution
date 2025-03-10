from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import os
import time

class SubStorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "SubStore.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.substore_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")
        
        self.ward_supply_link = (By.CSS_SELECTOR, 'a[href="#/WardSupply"]')
        self.substore = (By.XPATH, '//i[text()="Accounts"]')
        self.inventory_requisition_tab = (By.XPATH, '//a[text()="Inventory Requisition"]')
        self.create_requisition_button = (By.XPATH, '//span[text()="Create Requisition"]')
        self.target_inventory_dropdown = (By.XPATH, '//input[@id="activeInventory"]')
        self.item_name_field = (By.XPATH, '//input[@placeholder="Item Name"]')
        self.request_button = (By.XPATH, '//input[@value="Request"]')
        self.success_message = (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Requisition is Generated and Saved"]')
        self.account_btn = (By.XPATH, '//span[contains(@class, "report-name")]/i[contains(text(), "Accounts")]')
        self.print_button = (By.XPATH, '//button[@id="printButton"]')
        self.consumption_link = (By.XPATH, '(//a[@href="#/WardSupply/Inventory/Consumption"])')
        self.new_consumption_btn = (By.XPATH, '//span[contains(@class, "glyphicon") and contains(@class, "glyphicon-plus")]')
        self.input_item_name = (By.ID, "itemName0")
        self.save_btn = (By.ID, "save")
        self.success_message1 = (By.XPATH, '//p[contains(text()," Success ")]/../p[text()="Consumption completed"]')
        self.report_link = (By.XPATH, '(//a[@href="#/WardSupply/Inventory/Reports"])')
        self.consumption_report = (By.XPATH, '//span[contains(@class, "report-name")]/i[contains(text(), "Consumption Report")]')
        self.sub_category = (By.XPATH, '//select[@id="selectedCategoryName"]')
        self.show_report = (By.XPATH, '//button[contains(text(),"Show Report")]')
        self.issue_field = (By.XPATH, "//input[@placeholder='Issue No']")
        self.from_date = (By.XPATH, '(//input[@id="date"])[1]')

    def create_inventory_requisition(self):
        """
        /**
        * @Test6
        * @description This method verifies the creation of an inventory requisition in the Ward Supply module.
        * It navigates to the Substore section, selects a target inventory, adds an item, and submits the requisition.
        * The method ensures the requisition is successfully created by verifying the success message.
        * @expected
        * The inventory requisition should be successfully created and a success message should be displayed.
        */
        """
        try:
            wait = WebDriverWait(self.driver, 10)

            target_inventory = self.substore_data["SubStore"][0]["TargetInventory"]
            item_name = self.substore_data["SubStore"][1]["ItemName"]

            self.driver.find_element(*self.ward_supply_link).click()
            self.driver.find_element(*self.substore).click()
            self.driver.find_element(*self.inventory_requisition_tab).click()
            self.driver.find_element(*self.create_requisition_button).click()
            time.sleep(2)  # Wait for the modal to appear

            # Select target inventory
            self.driver.find_element(*self.target_inventory_dropdown).click()
            self.driver.find_element(*self.issue_field).click()
            self.driver.find_element(*self.target_inventory_dropdown).send_keys(target_inventory)
            self.driver.find_element(*self.target_inventory_dropdown).send_keys("\n")  # Press Enter
            time.sleep(2)

            # Add item
            self.driver.find_element(*self.item_name_field).send_keys(item_name)
            self.driver.find_element(*self.item_name_field).send_keys("\n")  # Press Enter
            time.sleep(2)

            # Submit requisition
            self.driver.find_element(*self.request_button).click()
            time.sleep(2)

            # Verify success message
            success_message = wait.until(EC.visibility_of_element_located(self.success_message))
            if success_message:
                print("Inventory requisition created successfully.")
                return True

            print("Failed to create inventory requisition.")
            return False

        except Exception as e:
            print(f"Error creating inventory requisition: {e}")
            return False

    def creating_consumption_section(self):
        """
        /**
        * @Test11
        * @description This method creates a new consumption section. It navigates through the Ward Supply module,
        * accesses the account and consumption sections, and opens the "New Consumption" form.
        * The function enters the item name, submits the form, and verifies the successful creation of the consumption
        * section by asserting that a success message becomes visible.
        * @return True if the consumption section is successfully created, otherwise False.
        */
        """
        try:
            item_name = self.substore_data['SubStore'][1]['ItemName']

            self.driver.find_element(*self.ward_supply_link).click()
            self.driver.find_element(*self.account_btn).click()
            self.driver.find_element(*self.consumption_link).click()
            self.driver.find_element(*self.new_consumption_btn).click()
            self.driver.find_element(*self.input_item_name).send_keys(item_name)
            self.driver.find_element(*self.input_item_name).send_keys("\n")  # Press Enter
            self.driver.find_element(*self.save_btn).click()

            # Wait for the success message to appear
            success_visible = self.wait.until(EC.visibility_of_element_located(self.success_message1))

            if success_visible.is_displayed():
                print("Consumption section created successfully.")
                return True
            else:
                print("Success message not displayed.")
                return False

        except Exception as error:
            print(f"Error creating consumption section: {error}")
            return False  # Return False in case of an error

    def creating_report_section(self):
        """
        /**
        * @Test12
        * @description This method creates a new report section in the Ward Supply module. It navigates through
        * the report section and selects the specified item name from the subcategory dropdown. After generating
        * the report, the function verifies if the selected item name is displayed in the report grid.
        * @return True if the item name is found in the report, otherwise False.
        */
        """
        try:
            item_name = self.substore_data['SubStore'][1]['ItemName']

            self.driver.find_element(*self.ward_supply_link).click()
            self.driver.find_element(*self.account_btn).click()
            self.driver.find_element(*self.report_link).click()
            self.driver.find_element(*self.consumption_report).click()

            element = self.wait.until(EC.visibility_of_element_located(self.from_date))
            element.clear()
            element.send_keys("01-01-2020")

            self.wait.until(EC.element_to_be_clickable(self.sub_category)).click()
            self.wait.until(EC.element_to_be_clickable(self.sub_category)).send_keys(item_name + Keys.ENTER)

            self.wait.until(EC.element_to_be_clickable(self.show_report)).click()

            # Extract result text from the report grid
            result_elements = self.driver.find_elements(By.XPATH,
                                                        "//div[@role='gridcell' and @col-id='SubCategoryName']")
            result_texts = [element.text.strip() for element in result_elements]

            # Check if the item name is in the results
            match_found = item_name.strip() in result_texts

            if match_found:
                print(f"Item '{item_name}' found in the report results.")
                return True
            else:
                print(f"Item '{item_name}' not found in the report results.")
                return False

        except Exception as error:
            print(f"Error creating report section: {error}")
            return False  # Return False in case of an error


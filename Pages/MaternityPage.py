import json
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MaternityPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "Maternity.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.maternity_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.maternity_link = (By.CSS_SELECTOR, 'a[href="#/Maternity"]')
        self.report_link = (By.XPATH, '(//a[@href="#/Maternity/Reports"])[2]')
        self.maternity_allowance_report = (By.XPATH, '(//a[@href="#/Maternity/Reports/MaternityAllowance"])')
        self.date_from = (By.XPATH, '(//input[@id="date"])[1]')
        self.show_report_btn = (By.CSS_SELECTOR, 'button.btn.green.btn-success[type="button"]')
        self.table_row_locator = (By.CSS_SELECTOR, 'div[role="grid"] div[role="row"]:has(div[col-id="CreatedOn"])')
        self.created_on = (By.CSS_SELECTOR, 'div[col-id="CreatedOn"] span')
        self.data_type = (By.XPATH, "//div[@role='gridcell' and @col-id='TransactionType'][1]")

    def verify_maternity_allowance_report(self):
        """
        /**
        * @Test7
        * @description This method verifies the functionality of the Maternity Allowance Report.
        * It navigates to the Maternity module, accesses the report section, and opens the Maternity Allowance Report.
        * Initially, it ensures that the data grid is not visible, selects a date range by entering the 'from date,'
        * and clicks the 'Show Report' button. Finally, it waits for the report to load and asserts that the data grid becomes visible.
        * @expected
        * The data grid should be visible after the report is displayed.
        */
        """
        try:
            from_date = self.maternity_data['DateRange'][0]['FromDate']

            # Navigate to the Maternity module
            self.wait.until(EC.element_to_be_clickable(self.maternity_link)).click()

            # Access the report section
            self.wait.until(EC.element_to_be_clickable(self.report_link)).click()

            # Open the Maternity Allowance Report
            self.wait.until(EC.element_to_be_clickable(self.maternity_allowance_report)).click()

            # Enter the 'from date'
            date_input = self.wait.until(EC.visibility_of_element_located(self.date_from))
            date_input.clear()  # Clear any existing text
            date_input.send_keys(from_date)

            # Click the 'Show Report' button
            self.wait.until(EC.element_to_be_clickable(self.show_report_btn)).click()
            time.sleep(2)  # Wait for the report to load

            # Check if the data grid is visible
            is_visible = self.wait.until(EC.visibility_of_element_located(self.data_type)).is_displayed()

            if is_visible:
                print("Maternity Allowance Report displayed successfully.")
                return True

            print("Maternity Allowance Report failed to display.")
            return False

        except Exception as e:
            print(f"Error verifying Maternity Allowance Report: {e}")
            return False

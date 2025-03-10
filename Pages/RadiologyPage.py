import json
import time
import os
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RadiologyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "Radiology.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.radiology_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.radiology_module = (By.CSS_SELECTOR, 'a[href="#/Radiology"]')
        self.list_request_sub_module = (By.XPATH, '//a[contains(text(),"List Requests")]')
        self.filter_dropdown = (By.XPATH, "//select")
        self.from_date = (By.XPATH, '(//input[@id="date"])[1]')
        self.to_date = (By.XPATH, '(//input[@id="date"])[2]')
        self.ok_button = (By.XPATH, '//button[contains(text(),"OK")]')
        self.add_report_button = (By.XPATH, '(//a[contains(text(),"Add Report")])[1]')
        self.close_modal_button = (By.XPATH, 'a[title="Cancel"]')
        self.date_range_dropdown = (By.XPATH, "//span[@data-toggle='dropdown']")
        self.last_3_months_option = (By.XPATH, "//a[text()= 'Last 3 Months']")
        self.date_cells = (By.XPATH, "//div[@role='gridcell' and @col-id='CreatedOn'][1]")

    def verify_data_within_last_three_months(self):
        """
        /**
        * @Test9
        * @description This method verifies that the data displayed in the radiology list request is within the last three months.
        * It navigates to the Radiology module, selects the "Last 3 Months" option from the date range dropdown, and confirms the filter.
        * @expected
        * All retrieved dates should be within the last three months.
        * @return True if all dates are within range, otherwise False.
        */
        """
        try:
            # Navigate to the Radiology module
            self.wait.until(EC.element_to_be_clickable(self.radiology_module)).click()
            # Click on the List Requests sub-module
            self.wait.until(EC.element_to_be_clickable(self.list_request_sub_module)).click()
            # Select the date range dropdown
            self.wait.until(EC.element_to_be_clickable(self.date_range_dropdown)).click()
            # Select the "Last 3 Months" option
            self.wait.until(EC.element_to_be_clickable(self.last_3_months_option)).click()
            # Click the OK button
            self.wait.until(EC.element_to_be_clickable(self.ok_button)).click()

            # Get the count of date cells
            date_cells = self.driver.find_elements(*self.date_cells)
            debug_elements = len(date_cells)
            print("Number of date cells found:", debug_elements)

            if debug_elements == 0:
                print("No date cells found. Verify the locator or table data.")
                return False

            # Retrieve all dates from the table
            date_texts = [cell.text.strip() for cell in date_cells]
            print("Retrieved dates:", date_texts)

            # Calculate the date range
            today = datetime.now()
            three_months_ago = today - timedelta(days=90)

            for date_text in date_texts:
                try:
                    date_value = datetime.strptime(date_text, "%Y-%m-%d")  # Adjust format as needed
                    if date_value < three_months_ago or date_value > today:
                        print(f"Date out of range: {date_value}")
                        return False  # Return False if any date is invalid
                except ValueError:
                    print(f"Invalid date format: {date_text}")
                    return False  # Return False if a date format is incorrect

            print("All dates are within the last 3 months.")
            return True  # Return True only if all dates pass validation

        except Exception as error:
            print(f'Error verifying "Last 3 Months" data: {error}')
            return False

    def filter_list_requests_by_date_and_type(self):
        """
        /**
        * @Test14
        * @description This method filters the list of radiology requests based on a specified date range and imaging type.
        * It navigates to the Radiology module, applies the selected filter, enters the 'From' and 'To' dates, and confirms the filter action.
        * The method verifies that the filtered results match the specified imaging type.
        * @return True if the filtered results match the specified imaging type, otherwise False.
        */
        """
        try:
            filter_option = self.radiology_data['FilterDropdown'][0]['Filter']
            from_date = self.radiology_data['DateRange'][0]['FromDate']
            to_date = self.radiology_data['DateRange'][1]['ToDate']

            # Navigate to the Radiology module
            self.wait.until(EC.element_to_be_clickable(self.radiology_module)).click()
            self.wait.until(EC.element_to_be_clickable(self.list_request_sub_module)).click()
            time.sleep(2)  # Wait for the page to load

            # Select the filter dropdown
            self.wait.until(EC.element_to_be_clickable(self.filter_dropdown)).click()
            self.driver.find_element(*self.filter_dropdown).send_keys(filter_option + "\n")
            time.sleep(2)  # Wait for the dropdown to update

            # Enter the 'From' and 'To' dates
            from_date_input = self.wait.until(EC.visibility_of_element_located(self.from_date))
            from_date_input.clear()
            from_date_input.send_keys(from_date)

            to_date_input = self.wait.until(EC.visibility_of_element_located(self.to_date))
            to_date_input.clear()
            to_date_input.send_keys(to_date)

            # Click the OK button
            self.wait.until(EC.element_to_be_clickable(self.ok_button)).click()
            time.sleep(3)  # Wait for the results to load

            # Capture and verify the search result
            result_elements = self.driver.find_elements(By.XPATH,
                                                        "//div[@role='gridcell' and @col-id='ImagingTypeName']")
            result_texts = [element.text.strip() for element in result_elements]

            if filter_option.strip() in result_texts:
                print(f"Filter '{filter_option}' successfully applied and found in results.")
                return True
            else:
                print(f"Filter '{filter_option}' not found in results.")
                return False

        except Exception as e:
            print(f"Failed to filter radiology requests: {e}")
            return False  # Return False in case of an error

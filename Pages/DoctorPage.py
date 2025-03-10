import json
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DoctorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "Doctor.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.doctor_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.doctors_link = (By.CSS_SELECTOR, 'a[href="#/Doctors"]')
        self.inpatient_department_tab = (By.XPATH, '(//a[@href="#/Doctors/InPatientDepartment"])[2]')
        self.search_bar = (By.XPATH, "(//input[@placeholder='search'])[3]")
        self.order_dropdown = (By.XPATH, "//select")
        self.imaging_action_button = (By.XPATH, '//a[@danphe-grid-action="imaging"]')
        self.search_order_item = (By.XPATH, '//input[@placeholder="search order items"]')
        self.proceed_button = (By.XPATH, '//button[text()=" Proceed "]')
        self.sign_button = (By.XPATH, '//button[text()="Sign"]')
        self.success_message = (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Imaging and lab order add successfully"]')

    def perform_inpatient_imaging_order(self):
        """
        /**
        * @Test8
        * @description This method verifies the process of placing an imaging order for an inpatient.
        * It navigates to the Inpatient Department, searches for a specific patient, selects an imaging action,
        * chooses an order type, specifies the order item, and completes the process by signing the order.
        * @expected
        * The success message should be visible after the imaging order is placed.
        */
        """
        try:
            patient = self.doctor_data['patientName'][0]['patient']
            option = self.doctor_data['Dropdown'][0]['Option']
            search_order_item = self.doctor_data['Dropdown'][1]['searchOrderItem']

            # Navigate to the Doctors page
            self.wait.until(EC.element_to_be_clickable(self.doctors_link)).click()

            # Click on the Inpatient Department tab
            self.wait.until(EC.element_to_be_clickable(self.inpatient_department_tab)).click()

            time.sleep(2)  # Wait for the page to load

            # Search for the patient
            search_bar = self.wait.until(EC.visibility_of_element_located(self.search_bar))
            search_bar.clear()
            search_bar.send_keys(patient)
            search_bar.send_keys("\n")

            # Click on the Imaging action button
            self.wait.until(EC.element_to_be_clickable(self.imaging_action_button)).click()

            time.sleep(2)  # Wait for the action to complete

            # Select the order type from the dropdown
            order_dropdown = self.wait.until(EC.element_to_be_clickable(self.order_dropdown))
            order_dropdown.click()
            order_dropdown.send_keys(option)
            order_dropdown.send_keys("\n")

            time.sleep(2)  # Wait for the dropdown to update

            # Search for the order item
            search_order_input = self.wait.until(EC.visibility_of_element_located(self.search_order_item))
            search_order_input.clear()
            search_order_input.send_keys(search_order_item)
            search_order_input.send_keys("\n")

            # Click on the Proceed button
            self.wait.until(EC.element_to_be_clickable(self.proceed_button)).click()

            # Click on the Sign button
            self.wait.until(EC.element_to_be_clickable(self.sign_button)).click()

            time.sleep(2)  # Wait for the action to complete

            # Verify the success message is visible
            success_visible = self.wait.until(EC.visibility_of_element_located(self.success_message)).is_displayed()

            if success_visible:
                print("Imaging order placed successfully.")
                return True

            print("Imaging order placement failed.")
            return False

        except Exception as e:
            print(f"Error placing inpatient imaging order: {e}")
            return False

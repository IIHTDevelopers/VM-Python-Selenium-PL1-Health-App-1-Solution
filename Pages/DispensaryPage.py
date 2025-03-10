import os
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DispensaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.download_path = os.path.join(os.getcwd(), "downloads")

        self.dispensary_link = (By.XPATH, '//a[@href="#/Dispensary"]')
        self.reports_tab = (By.XPATH, '//a[contains(text(),"Reports")]')
        self.user_collection_report = (By.XPATH, '//i[text()="User Collection"]')
        self.from_date = (By.XPATH, '(//input[@id="date"])[1]')
        self.show_report_button = (By.XPATH, '//span[text()="Show Report"]')
        self.export_button = (By.XPATH, '//button[@title="Export To Excel"]')

    def verify_export_user_collection_report(self):
        """
        /**
        * @Test10
        * @description This method verifies the export functionality for the User Collection Report.
        * @expected The exported file should download with the name `PharmacyUserwiseCollectionReport_2025`.
        * @return True if the expected file is downloaded, otherwise False.
        */
        """
        try:
            # Get system's default Downloads folder
            download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
            expected_file_keyword = "PharmacyUserwiseCollectionReport_2025"

            # Navigate to Dispensary module
            self.wait.until(EC.element_to_be_clickable(self.dispensary_link)).click()

            # Click Reports tab
            self.wait.until(EC.element_to_be_clickable(self.reports_tab)).click()

            # Select User Collection Report
            self.wait.until(EC.element_to_be_clickable(self.user_collection_report)).click()

            # Enter From Date
            self.wait.until(EC.element_to_be_clickable(self.from_date)).send_keys("01-01-2020")

            # Click Show Report
            self.wait.until(EC.element_to_be_clickable(self.show_report_button)).click()
            time.sleep(2)  # Wait for the report to load

            # Click Export Button
            self.wait.until(EC.element_to_be_clickable(self.export_button)).click()

            # Wait for file download
            timeout = 20  # Max wait time in seconds
            file_downloaded = False

            while timeout > 0:
                downloaded_files = os.listdir(download_folder)
                if any(expected_file_keyword in file for file in downloaded_files):
                    print(f"File downloaded successfully: {expected_file_keyword}")
                    return True  # File found, return True
                time.sleep(1)
                timeout -= 1

            print(f"Expected file containing '{expected_file_keyword}' not found in {download_folder}")
            return False  # Return False if file not found within timeout

        except Exception as error:
            print(f"Error verifying export functionality: {error}")
            return False  # Return False in case of an error




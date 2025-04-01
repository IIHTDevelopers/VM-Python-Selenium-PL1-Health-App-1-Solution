import pathlib
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.PharmacyPage import PharmacyPage
from Pages.MedicalRecordsPage import MedicalRecordsPage
from Pages.SettingsPage import SettingsPage
from Pages.SubStorePage import SubStorePage
from Pages.MaternityPage import MaternityPage
from Pages.DoctorPage import DoctorPage
from Pages.RadiologyPage import RadiologyPage
from Pages.DispensaryPage import DispensaryPage
from tests.TestUtils import TestUtils


# Fixture to set up the WebDriver for each test function
@pytest.fixture(scope="function")
def setup_driver():
    """
    Initializes the WebDriver for Chrome and navigates to the application URL.
    Ensures the driver is properly closed after each test execution.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://healthapp.yaksha.com/')
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()

# Reusable login function to be called before each test
def login_to_application(driver):
    """
    Logs in to the application before each test.

    Args:
        driver (webdriver): Selenium WebDriver instance.
        test_credentials (dict): Dictionary containing username and password.
    """
    login_page = LoginPage(driver)
    login_page.perform_login()
    time.sleep(5)

@pytest.mark.order(1)
def test_verification_module(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        pharmacy_page = PharmacyPage(driver)
        testResult = pharmacy_page.handling_alert_on_radiology()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Pharmacy/Order/GoodsReceiptList")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_verification_module", True, "Functional")
            print("test_verification_module = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_verification_module", False, "Functional")
            print("test_verification_module = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_verification_module", False, "test_verification_module")
        print("test_verification_module = Failed")
    assert passed

@pytest.mark.order(2)
def test_verify_print_receipt(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        pharmacy_page = PharmacyPage(driver)
        testResult = pharmacy_page.verify_print_receipt()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Pharmacy/Order/GoodsReceiptList")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_verify_print_receipt", True, "Functional")
            print("test_verify_print_receipt = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_verify_print_receipt", False, "Functional")
            print("test_verify_print_receipt = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_verify_print_receipt", False, "Functional")
        print("test_verify_print_receipt = Failed")
    assert passed

@pytest.mark.order(3)
def test_keyword_matching(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        medicalRecord_page = MedicalRecordsPage(driver)
        testResult = medicalRecord_page.keyword_matching()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Medical-records/OutpatientList")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_keyword_matching", True, "Functional")
            print("test_keyword_matching = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_keyword_matching", False, "Functional")
            print("test_keyword_matching = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_keyword_matching", False, "Functional")
        print("test_keyword_matching = Failed")
    assert passed

@pytest.mark.order(4)
def test_presence_of_doctor_filter(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        medicalRecord_page = MedicalRecordsPage(driver)
        testResult = medicalRecord_page.presence_of_doctor_filter()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Medical-records/OutpatientList")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_presence_of_doctor_filter", True, "Functional")
            print("test_presence_of_doctor_filter = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_presence_of_doctor_filter", False, "Functional")
            print("test_presence_of_doctor_filter = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_presence_of_doctor_filter", False, "Functional")
        print("test_presence_of_doctor_filter = Failed")
    assert passed

@pytest.mark.order(5)
def test_verify_dynamic_templates(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        settings_page = SettingsPage(driver)
        testResult = settings_page.verify_dynamic_templates()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Settings/DynamicTemplates/Templates")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_verify_dynamic_templates", True, "Functional")
            print("test_verify_dynamic_templates = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_verify_dynamic_templates", False, "Functional")
            print("test_verify_dynamic_template = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_verify_dynamic_templates", False, "Functional")
        print("test_verify_dynamic_templates = Failed")
    assert passed

@pytest.mark.order(6)
def test_create_inventory_requisition(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        substore_page = SubStorePage(driver)
        testResult = substore_page.create_inventory_requisition()
        isTestVerified = verify_user_is_on_correct_url(driver,"/WardSupply/Inventory/InventoryRequisitionItem")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_create_inventory_requisition", True, "Functional")
            print("est_create_inventory_requisition = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_create_inventory_requisition", False, "Functional")
            print("test_create_inventory_requisition = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_create_inventory_requisition", False, "Functional")
        print("test_create_inventory_requisition = Failed")
    assert passed

@pytest.mark.order(7)
def test_verify_maternity_allowance_report(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        maternity_page = MaternityPage(driver)
        testResult = maternity_page.verify_maternity_allowance_report()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Maternity/Reports/MaternityAllowance")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_verify_maternity_allowance_report", True, "Functional")
            print("test_verify_maternity_allowance_report = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_verify_maternity_allowance_report", False, "Functional")
            print("test_verify_maternity_allowance_report= Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_verify_maternity_allowance_report", False, "Functional")
        print("test_verify_maternity_allowance_report= Failed")
    assert passed

@pytest.mark.order(8)
def test_perform_inpatient_imaging_order(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        doctor_page = DoctorPage(driver)
        testResult = doctor_page.perform_inpatient_imaging_order()
        isTestVerified = verify_active_order_is_present(driver)
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_perform_inpatient_imaging_order", True, "Functional")
            print("test_perform_inpatient_imaging_order = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_perform_inpatient_imaging_order", False, "Functional")
            print("test_perform_inpatient_imaging_order = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_perform_inpatient_imaging_order", False, "Functional")
        print("test_perform_inpatient_imaging_order = Failed")
    assert passed

@pytest.mark.order(9)
def test_verify_data_within_last_three_months(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        radiology_page = RadiologyPage(driver)
        testResult = radiology_page.verify_data_within_last_three_months()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Radiology/ImagingRequisitionList")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_verify_data_within_last_three_months", True, "Functional")
            print("test_verify_data_within_last_three_months = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_verify_data_within_last_three_months", False, "Functional")
            print("test_verify_data_within_last_three_months = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_verify_data_within_last_three_months", False, "Functional")
        print("test_verify_data_within_last_three_months = Failed")
    assert passed

@pytest.mark.order(10)
def test_verify_export_user_collection_report(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        dispensary_page = DispensaryPage(driver)
        testResult = dispensary_page.verify_export_user_collection_report()
        isTestVerified = verify_if_records_are_present(driver)
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_verify_export_user_collection_report", True, "Functional")
            print("test_verify_export_user_collection_report = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_verify_export_user_collection_report", False, "Functional")
            print("test_verify_export_user_collection_report = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_verify_export_user_collection_report", False, "Functional")
        print("test_verify_export_user_collection_report = Failed")
    assert passed

@pytest.mark.order(11)
def test_creating_consumption_section(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        substore_page = SubStorePage(driver)
        testResult = substore_page.creating_consumption_section()
        isTestVerified = verify_user_is_on_correct_url(driver,"/WardSupply/Inventory/Consumption/ConsumptionList")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_creating_consumption_section", True, "Functional")
            print("TestValidLogin = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_creating_consumption_section", False, "Functional")
            print("TestValidLogin = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_creating_consumption_section", False, "Functional")
        print("test_creating_consumption_section = Failed")
    assert passed

@pytest.mark.order(12)
def test_creating_report_section(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        substore_page = SubStorePage(driver)
        testResult = substore_page.creating_report_section()
        isTestVerified = verify_user_is_on_correct_url(driver,"/WardSupply/Inventory/Reports/ConsumptionReport")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_creating_report_section", True, "Functional")
            print("TestValidLogin = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_creating_report_section", False, "Functional")
            print("test_creating_report_section = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_creating_report_section", False, "Functional")
        print("test_creating_report_section = Failed")
    assert passed

@pytest.mark.order(13)
def test_verify_presence_of_supplier_name(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        pharmacy_page = PharmacyPage(driver)
        testResult = pharmacy_page.verify_presence_of_supplier_name()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Pharmacy/Order/GoodsReceiptList")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_verify_presence_of_supplier_name", True, "Functional")
            print("test_verify_presence_of_supplier_name = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_verify_presence_of_supplier_name", False, "Functional")
            print("test_verify_presence_of_supplier_name = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_verify_presence_of_supplier_name", False, "Functional")
        print("test_verify_presence_of_supplier_name = Failed")
    assert passed

@pytest.mark.order(14)
def test_filter_list_requests_by_date_and_type(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        radiology_page = RadiologyPage(driver)
        testResult = radiology_page.filter_list_requests_by_date_and_type()
        isTestVerified = verify_user_is_on_correct_url(driver,"/Radiology/ImagingRequisitionList")
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_filter_list_requests_by_date_and_type", True, "Functional")
            print("test_filter_list_requests_by_date_and_type = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("Test14", False, "Functional")
            print("test_filter_list_requests_by_date_and_type = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_filter_list_requests_by_date_and_type", False, "Functional")
        print("test_filter_list_requests_by_date_and_type = Failed")
    assert passed

@pytest.mark.order(15)
def test_perform_login_with_invalid_credentials(setup_driver):
    try:
        driver = setup_driver
        test_obj = TestUtils()
        login_to_application(driver)  # Perform login before test
        login_page = LoginPage(driver)
        testResult = login_page.perform_login_with_invalid_credentials()
        isTestVerified = verify_user_is_not_logged_in(driver)
        if (testResult==True and isTestVerified==True):
            passed = True
            test_obj.yakshaAssert("test_perform_login_with_invalid_credentials", True, "Functional")
            print("test_perform_login_with_invalid_credentials = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("test_perform_login_with_invalid_credentials", False, "Functional")
            print("test_perform_login_with_invalid_credentials = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("test_perform_login_with_invalid_credentials", False, "Functional")
        print("test_perform_login_with_invalid_credentials = Failed")
    assert passed


"""------------------------------------------------- Helper Method------------------------------------------------------------"""

def verify_user_is_on_correct_url(driver, expected_url):
    """
    Verifies that the user is on the expected URL.

    :param driver: Selenium WebDriver instance
    :param expected_url: The expected URL (or a part of it) to verify
    :return: True if the expected URL is found in the current URL, otherwise False.
    """
    try:
        WebDriverWait(driver, 10).until(lambda d: expected_url in d.current_url)
        return expected_url in driver.current_url
    except Exception as e:
        print(f"URL verification failed: {e}")
        return False

def verify_active_order_is_present(driver):
    """
    Verifies if the 'Active Orders' element is visible on the page.

    :param driver: Selenium WebDriver instance
    :return: True if the 'Active Orders' element is visible, otherwise False.
    """
    try:
        wait = WebDriverWait(driver, 10)
        active_order_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()=" Active Orders"]')))
        return active_order_element.is_displayed()
    except Exception as e:
        print(f"Active Orders verification failed: {e}")
        return False

def verify_user_is_not_logged_in(driver):
    """
    Verifies if the 'Invalid credentials!' message is displayed, indicating a failed login attempt.

    :param driver: Selenium WebDriver instance
    :return: True if the 'Invalid credentials!' message is visible, otherwise False.
    """
    try:
        wait = WebDriverWait(driver, 10)
        invalid_credentials_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Invalid credentials !")]')))
        return invalid_credentials_element.is_displayed()
    except Exception as e:
        print(f"User login failure verification failed: {e}")
        return False

def verify_if_records_are_present(driver):
    """
    Checks if more than one record is present in the specified column.

    :param driver: Selenium WebDriver instance
    :return: True if more than one record is found, otherwise False.
    """
    try:
        wait = WebDriverWait(driver, 10)
        records = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[col-id="PatientName"]')))
        return len(records) > 1
    except Exception as e:
        print(f"Record verification failed: {e}")
        return False

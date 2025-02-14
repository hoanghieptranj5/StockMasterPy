from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverManager:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def start_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def quit_driver(self):
        if self.driver:
            self.driver.quit()

    def go_to_page(self, url):
        """
        Navigate the Selenium WebDriver to the specified URL.
        """
        try:
            self.driver.get(url)  # Navigate to the URL
            self.driver.implicitly_wait(10)  # Wait up to 10 seconds for the page to load
        except Exception as e:
            print(f"Error navigating to page: {e}")


    def find_element_by_xpath(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element
        except Exception as e:
            print(f"Error finding element by XPath {xpath}: {str(e)}")
            return None

    def click_element_by_xpath(self, xpath):
        try:
            element = self.find_element_by_xpath(xpath)
            if element:
                element.click()
                print(f"Element clicked successfully: {xpath}")
            else:
                print(f"Element not found for click: {xpath}")
        except Exception as e:
            print(f"Error clicking element by XPath {xpath}: {str(e)}")

    def send_keys_by_xpath(self, xpath, keys):
        try:
            element = self.find_element_by_xpath(xpath)
            if element:
                element.clear()  # Clear the field before sending keys
                element.send_keys(keys)
                print(f"Text '{keys}' sent to element: {xpath}")
            else:
                print(f"Element not found for sending keys: {xpath}")
        except Exception as e:
            print(f"Error sending keys to element by XPath {xpath}: {str(e)}")

    def get_text_by_xpath(self, xpath):
        try:
            element = self.find_element_by_xpath(xpath)
            if element:
                text = element.text
                print(f"Text extracted: {text}")
                return text
            else:
                print(f"Element not found to extract text: {xpath}")
                return None
        except Exception as e:
            print(f"Error extracting text by XPath {xpath}: {str(e)}")
            return None

    def element_exists_by_xpath(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element is not None
        except Exception:
            return False

    def scroll_to_element_by_xpath(self, xpath):
        try:
            element = self.find_element_by_xpath(xpath)
            if element:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                print(f"Scrolled to element: {xpath}")
            else:
                print(f"Element not found to scroll to: {xpath}")
        except Exception as e:
            print(f"Error scrolling to element by XPath {xpath}: {str(e)}")

    def get_attribute_by_xpath(self, xpath, attribute_name):
        try:
            element = self.find_element_by_xpath(xpath)
            if element:
                attribute_value = element.get_attribute(attribute_name)
                print(f"Attribute '{attribute_name}' value: {attribute_value}")
                return attribute_value
            else:
                print(f"Element not found to get attribute: {xpath}")
                return None
        except Exception as e:
            print(f"Error getting attribute by XPath {xpath}: {str(e)}")
            return None

    def select_dropdown_option_by_xpath(self, xpath, option_text):
        try:
            element = self.find_element_by_xpath(xpath)
            if element:
                select = Select(element)
                select.select_by_visible_text(option_text)
                print(f"Option '{option_text}' selected in dropdown: {xpath}")
            else:
                print(f"Dropdown element not found: {xpath}")
        except Exception as e:
            print(f"Error selecting dropdown option by XPath {xpath}: {str(e)}")

    def wait_for_element_visible_by_xpath(self, xpath, timeout=0.1):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ExpectedConditions.visibility_of_element_located((By.XPATH, xpath))
            )
            print(f"Element visible: {xpath}")
            return element
        except Exception as e:
            print(f"Error waiting for element by XPath {xpath}: {str(e)}")
            return None

    def find_elements_by_xpath(self, xpath):
        try:
            elements = self.driver.find_elements(By.XPATH, xpath)
            if elements:
                print(f"Found {len(elements)} elements for XPath: {xpath}")
            else:
                print(f"No elements found for XPath: {xpath}")
            return elements
        except Exception as e:
            print(f"Error finding elements by XPath {xpath}: {str(e)}")
            return []

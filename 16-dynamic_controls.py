import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'.\chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://the-internet.herokuapp.com/dynamic_controls")
	
	def test_dynamic_controls(self):
		driver = self.driver

		checkbox = driver.find_elements_by_css_selector('#checkbox > input[type=checkbox]')
		checkbox.click()
		
		remove_add_button = driver.find_elements_by_css_selector('#checkbox-example > button')
		remove_add_button.click()

		WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
		click.click()

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
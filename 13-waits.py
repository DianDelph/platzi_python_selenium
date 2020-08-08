import unittest
from selenium import webdriver
#by nos ayuda a hacer referencia a un elemento del sitio web
# a través de sus selectores para interactuar con él
from selenium.webdriver.common.by import By
#webdriverwait sirve para usar las expected conditions
#junto con las esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait
#para las esperas explícitas. se importan as EC para no escribir
# su nombre completo cada vez que se usen
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'.\chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")
	
	def test_account_link(self):


		WebDriverWait(self.driver,10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

		account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
		account.click()

	def test_create_new_customer(self):
		self.driver.find_element_by_link_text('ACCOUNT').click()

		#espera a que el elemento sea encontrado
		my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT,'My Account')))
		my_account.click()

		#espera a que el elemento pueda ser clickeable
		create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
		create_account_button.click()

		WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
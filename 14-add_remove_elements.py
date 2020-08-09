import unittest
from selenium import webdriver
from time import sleep

class CompareProducts(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'.\chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
	
	def test_add_remove(self):
		driver = self.driver
		added_elements = int(input('How many elements will you add?: '))
		removed_elements = int (input('How many elements will you remove? :'))
		total_elements = added_elements - removed_elements

		add_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')

		sleep(3)

		for i in range(added_elements):
			add_button.click()
		
		for i in range(removed_elements):
			try:
				delete_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button[1]')
				delete_button.click()
			except:
				('You are trying to delete more elements than available')
				break
		
		if total_elements > 0:
			print(f'There are total {total_elements} elements on screen')
		else:
			print(f'There are 0 elements on screen')
		
		sleep(3)

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
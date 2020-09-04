import unittest
from selenium import webdriver
from time import sleep

class testCaseML(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'.\chromedriver.exe')
		driver = self.driver
		driver.get("http://mercadolibre.com/")
	
	def test_search_ps4(self):
		driver = self.driver
		
		#busca méxico
		country = driver.find_element_by_id("MX")
		#click en méxico
		country.click()
		sleep(3)
		#asigna la barra de búsqueda
		search_field = driver.find_element_by_name('as_word')
		#me ubico en la barra de búsqueda
		search_field.click()
		#la limpio
		search_field.clear()
		#escribo lo que quiero buscar
		search_field.send_keys('ps4')
		#enviar
		search_field.submit()
		
		sleep(3)
		#limito resultados por ubicación
		state = driver.find_element_by_partial_link_text("Veracruz")
		state.click()

		sleep(3)
		#refino por condición = nuevo
		condition = driver.find_element_by_partial_link_text("Nuevo")
		condition.click()

		sleep(3)
		#busco el menú desplegable para ordernar de mayor a menor
		order_menu = driver.find_element_by_class_name('andes-dropdown__trigger ')
		order_menu.click()
		higher_price = driver.find_element_by_xpath('//*[@id="root-app"]/div/div[1]/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[3]/div/div/a')
		higher_price.click()

		sleep(3)
		
		#para guardar los datos
		articles = []
		prices = []
		
		# busco el elemento título de los primeros cinco elementos y extraigo el texto
		for i in range(5):
			article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
			articles.append(article_name)
			
			article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
			prices.append(article_price)

		print(articles, prices)

	def tearDown(self):		
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
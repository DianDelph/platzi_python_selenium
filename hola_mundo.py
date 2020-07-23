import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

	#va a ejecutar todo lo necesario antes de hacer una prueba
	#va a preparar el entorno de la prueba
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'.\chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(10)
	
	#aquí va lo que queremos que la prueba haga
	def test_hello_world(self):
		driver = self.driver
		driver.get('https://platzi.com/')
	
	#cierra el navegador para evitar 
	#fuga de recursos
	def tearDown(self):
		self.driver.quit()



if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))



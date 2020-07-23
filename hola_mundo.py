import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

	#va a ejecutar todo lo necesario antes de hacer una prueba
	#va a preparar el entorno de la prueba
	@classmethod  # para que abra las pestañas en una misma ventana
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = r'.\chromedriver.exe')
		driver = cls.driver
		driver.implicitly_wait(10)
	
	#aquí va lo que queremos que la prueba haga
	def test_hello_world(self):
		driver = self.driver
		driver.get('https://platzi.com/')

	def test_visit_wikipedia(self):
		self.driver.get('https://es.wikipedia.org/')

	#cierra el navegador para evitar 
	#fuga de recursos
	@classmethod #decorador para que no se cierre la ventana después de la primera prueba
	def tearDownClass(cls):
		cls.driver.quit()



if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))



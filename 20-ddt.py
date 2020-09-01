import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

#creamos una clase para consultar nuestro archivo csv
def get_data(file_name):
	#creamos una lista para indicar el número de filas que hay
	rows = []
	#abrimos el archivo en modo lectura (r = read)
	data_file = open(file_name, 'r')
	#indicaremos que la libreria csv leerá el archivo
	reader = csv.reader(data_file)
	#le decimos que pase a la siguiente fila de datos
	#Con "None" omitimos la cabecera
	next(reader, None)

	#con el for, indicamos que la siguiente fila se agrega a nuestra lista
	#de filas
	for row in reader:
		rows.append(row)
	return rows

@ddt
class SearchDDT(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'.\chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("https://demo.onestepcheckout.com/")	

	#decoradores a los que pasamos los datos del archivo csv
	#unpack: para obtener la información del csv
	@data(*get_data('testdata.csv'))
	@unpack
	
	#search value: el valor de la búsqueda
	#expected_count: la cantidad de resultados que esperamos encontrar
	def test_search_ddf(self, search_value, expected_count):
		driver = self.driver
		
		search_field = driver.find_element_by_name('q')
		#como buena práctica limpiamos la barra de búsqueda
		search_field.clear()

		#simularemos la entrada del teclado usando search_value
		search_field.send_keys(search_value)
		search_field.submit()

		#ahora vamos a identificar donde están los productos
		products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')

		#para evitar conflictos, decimos que expected_count es un int
		expected_count = int(expected_count)

		if expected_count > 0:
			self.assertEqual(expected_count, len(products))
		else:
			message = driver.find_element_by_class_name('note-msg')
			self.assertEqual('Your search returns no results.', message)

		print(f'Found {len(products)} products')

		
	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)

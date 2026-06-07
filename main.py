import data

from page import UrbanRoutesPage


# no modificar






class TestUrbanRoutes:

    driver = None

    #@classmethod
    #def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        #from selenium.webdriver import DesiredCapabilities
        #capabilities = DesiredCapabilities.CHROME
        #capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        #cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    #Actualizado el metodo con el que dieron en preguntas de proyecto pues el metodo anterior ya no funciona con la versión de Selenium actual
    @classmethod
    def setup_class(cls):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        cls.driver.get(data.urban_routes_url)

        cls.routes_page = UrbanRoutesPage(cls.driver)

    #Test 1: Configurar la dirección
    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    #Test 2: Seleccionar la tarifa Comfort
    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_call_taxi()
        routes_page.select_comfort_tariff()
        assert routes_page.get_tariff_selected() == "Comfort"

    #Test 3: Agregar número de teléfono.
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        routes_page.set_route(address_from, address_to)
        routes_page.click_call_taxi()
        routes_page.set_phone_number(phone_number)
        assert routes_page.get_phone_number() == phone_number

    #Test 4: Agregar tarjeta a métodos de pago
    def test_add_card_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        card_number, code = data.card_number, data.card_code
        routes_page.set_route(address_from, address_to)
        routes_page.click_call_taxi()
        routes_page.add_card_information(card_number, code)
        assert routes_page.get_payment_methods() == 'Tarjeta'

    #Test 5: Escribir un mensaje para el conductor
    def test_add_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        message = data.message_for_driver
        routes_page.set_route(address_from, address_to)
        routes_page.click_call_taxi()
        routes_page.input_comment_for_driver(message)
        assert routes_page.get_comment_for_driver() == message

    # Test 6: Pedir manta y pañuelos.
    def test_request_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to

        #variable extraída de las propiedades de un botón activado
        activated_color = 'rgba(0, 126, 255, 1)'
        routes_page.set_route(address_from, address_to)
        routes_page.click_call_taxi()
        routes_page.select_comfort_tariff()
        routes_page.request_blanket_and_tissues()
        assert routes_page.get_blanket_and_tissues_toggle_status(activated_color) == activated_color

    # Test 7: Pedir 2 helados
    def test_request_two_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to

        #Variable que marca la cantidad de helados a pedir
        ice_cream_requests = 2
        routes_page.set_route(address_from, address_to)
        routes_page.click_call_taxi()
        routes_page.select_comfort_tariff()
        while ice_cream_requests > 0:
            routes_page.add_ice_cream()
            ice_cream_requests -= 1
        assert routes_page.get_ice_cream_count() == "2"

    # Test 8: Reservar un taxi
    def test_reserve_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        card_number, code = data.card_number, data.card_code
        routes_page.set_route(address_from, address_to)
        routes_page.click_call_taxi()
        routes_page.set_phone_number(phone_number)
        routes_page.add_card_information(card_number, code)
        routes_page.close_payment_methods()
        routes_page.click_reserve_taxi()
        assert routes_page.get_searching_for_taxi_window_status() == True



    #Test 9: Esperar a encontrar un taxi
    def test_wait_to_find_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.clear_webpage_caché()
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        card_number, code = data.card_number, data.card_code
        routes_page.set_route(address_from, address_to)
        routes_page.click_call_taxi()
        routes_page.set_phone_number(phone_number)
        routes_page.add_card_information(card_number, code)
        routes_page.close_payment_methods()
        routes_page.click_reserve_taxi()
        assert routes_page.wait_for_taxi_to_be_found() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

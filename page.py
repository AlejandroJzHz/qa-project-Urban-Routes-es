from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait
import time

import helpers


class UrbanRoutesPage:
    #Variable para encontrar el campo "Desde".
    from_field = (By.ID, 'from')
    # Variable para encontrar el campo "Hasta".
    to_field = (By.ID, 'to')
    # Variable para encontrar el boton "Pedir un taxi".
    taxi_call_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    # Variable para encontrar el botón pata la tarifa de taxi "Comfort".
    comfort_tariff_button = (By.XPATH, "//div[text()='Comfort']")
    # Variable para encontrar la tarifa de taxi seleccionada.
    tariff_selected = (By.XPATH, "//div[@class='tcard active']//div[@class='tcard-title']")
    # Variable para encontrar el apartado "Numero de telefono".
    phone_input = (By.CSS_SELECTOR, ".np-text")
    # Variable para encontrar el campo "Numero de telefono" en la ventana "Introduce tu numero de telefono".
    phone_field = (By.ID, 'phone')
    # Variable para encontrar el boton "Siguiente" en la ventana "Introduce tu numero de telefono".
    phone_button_next = (By.XPATH, "//button[text()='Siguiente']")
    # Variable para encontrar el campo Introduce el codigo" en la ventana "Introduce el código SMS".
    code_sms_field = (By.ID, 'code')
    # Variable para encontrar el boton "Confirmar" en la ventana "Introduce el código SMS".
    code_sms_button_next = (By.XPATH, "//button[text()='Confirmar']")
    # Variable para encontrar el campo "Metodo de pago.
    payment_input = (By.CLASS_NAME, "pp-text")
    # Variable para encontrar el botón para agregar tarjeta en la ventana "Métodos de pago.
    new_card_button = (By.XPATH, "//div[text()='Agregar tarjeta']")
    # Variable para encontrar el campo de número de tarjeta en la ventana "Agregar tarjeta".
    card_number_input = (By.XPATH, "//div[@class='card-number-input']//input[@type='text']")
    # Variable para encontrar el campo de CCV en la ventana "Agregar tarjeta".
    card_code_input =(By.XPATH, "//div[@class='card-code-input']//input[@type='text']")
    # Variable para encontrar el boton "Agregar" en la ventana "Agregar tarjeta".
    new_card_confirm_button = (By.XPATH, "//div[@class='pp-buttons']//button[@type='submit']")
    # Variable para encontrar el texto del campo "Metodo de pago".
    current_payment_method = (By.CLASS_NAME, "pp-value-text")
    # Variable para encontrar el campo para añadir comentario para el conductor.
    comment_for_driver = (By.ID, 'comment')
    # Variable para encontrar el switch para pedir manta y pañuelos.
    blanket_and_tissues_toggle = (By.XPATH, "//div[text()='Manta y pañuelos']//following-sibling::div//span[@class='slider round']")
    # Variable para encontrar el botón para pedir más "Helado" de la sección "Cubeta de helado".
    ice_cream_add = (By.XPATH, "//div[text()='Helado']//following-sibling::div[@class='r-counter']//div[@class='counter-plus']")
    # Variable para encontrar la cantidad de "Helado" pedida de la sección "Cubeta de helado".
    ice_cream_count = (By.XPATH, "//div[text()='Helado']//following-sibling::div[@class='r-counter']//div[@class='counter-value']")
    # Variable para encontrar el botón para reservar taxi.
    taxi_reserve_button = (By.CLASS_NAME, "smart-button-wrapper")
    # Variable para encontrar el boton para cerrar la ventana de Metodos de pago.
    button_close_payment_methods = (By.XPATH, "//div[@class='payment-picker open']//button[@class='close-button section-close']")
    #Variable para encontrar la ventana de "Buscando un taxi"
    window_looking_for_taxi = (By.XPATH, "//div[@class='order shown']")
    #Variable para encontrar el temporizador de la ventana "Buscando un taxi".
    timer_looking_for_taxi = (By.CLASS_NAME, "order-header-time")
    #Variable para encontrar al conductor en la ventana de Espera de taxi.
    driver_information_image = (By.CLASS_NAME, "order-btn-rating")



    blanket_and_tissues_toggle
    def __init__(self, driver):
        self.driver = driver

    #función para escribir la direccion en el apartado "Desde".
    def set_from(self, from_address):
        direccion_desde = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.from_field))
        direccion_desde.send_keys(from_address)

    # función para escribir la direccion en el apartado "Hasta".
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    #Función para recibir lo que está escrito en el apartado "Desde".
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Función para recibir lo que está escrito en el apartado "Desde".
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #Función para escribir la direccion en los apartados "Desde" y "Hasta".
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    #Función para hacer click en el botón "Pedir un taxi".
    def click_call_taxi(self):
        boton_pedir_taxi = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.taxi_call_button))
        boton_pedir_taxi.click()

    # Función para hacer click en la tarifa de taxi "Comfort".
    def select_comfort_tariff(self):
        boton_tarifa_comfort = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.comfort_tariff_button))
        boton_tarifa_comfort.click()

    #fuinción para recibir la tarifa de taxi seleccionada.
    def get_tariff_selected(self):
        tariff_selected = self.driver.find_element(*self.tariff_selected)
        return tariff_selected.text

    #Función para hacer click en el apartado "Número de Teléfono".
    def click_phone_number(self):
        campo_numero_telefonico = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.phone_input))
        campo_numero_telefonico.click()

    #Función para ingresar número telefónico en el campo "número de teléfono".
    def introduce_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    #Función para hacer click en el botón "Siguiente" del formulario de número de teléfono".
    def click_next_phone_number(self):
        self.driver.find_element(*self.phone_button_next).click()

    #Función para introducir código SMS en campo "Introduce el código" en ventana "Introduce el código SMS".
    def introduce_code_sms(self, code):
        codigo_sms = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.code_sms_field))
        codigo_sms.send_keys(code)

    #Función para hacer click en el botón "Confirmar" en ventana "Introduce el código SMS".
    def click_confirm_sms_code(self):
        self.driver.find_element(*self.code_sms_button_next).click()

    #Función para hacer los pasos correctos para agregar número de teléfono con los prerequisitos hechos.
    def set_sms_code(self):
        code = helpers.retrieve_phone_code(self.driver)
        self.introduce_code_sms(code)
        self.click_confirm_sms_code()

    #Función para hacer los pasos correctos para agregar número de teléfono desde hacer click en el campo vacío de numero de teléfono hasta hacer click en el boton para confirmar el códigp SMS.
    def set_phone_number(self, phone_number):
        self.click_phone_number()
        self.introduce_phone_number(phone_number)
        self.click_next_phone_number()
        self.set_sms_code()

    #Función para revisar el valor en el campo "número de teléfono".
    def get_phone_number(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    #Función para hacer click en "Métodos de pago".
    def click_payment_methods(self):
        boton_metodo_de_pago = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.payment_input))
        boton_metodo_de_pago.click()

    # Función para hacer click en "Agregar tarjeta".
    def click_add_card(self):
        boton_agregar_tarjeta = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.new_card_button))
        boton_agregar_tarjeta.click()

    #Función para escribir en apartado "Número de tarjeta".
    def input_card_number(self, card_number):
        codigo_sms = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.card_number_input))
        codigo_sms.send_keys(card_number)

    # Función para escribir en apartado "Código de tarjeta".
    def input_card_code(self, code):
        codigo_sms = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.card_code_input))
        codigo_sms.send_keys(code)

    # Función para hacer click en "Agregar" en la ventana "Agregar tarjeta".
    def click_confirm_card(self):
        self.driver.find_element(*self.new_card_confirm_button).click()

    # Función para cerrar la ventana "Metodos de pago"
    def close_payment_methods(self):
        boton_cerrar_métodos_de_pago = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.button_close_payment_methods))
        boton_cerrar_métodos_de_pago.click()

    #Función para recibir la forma de pago seleccionada
    def get_payment_methods(self):
        metodo_de_pago = self.driver.find_element(*self.current_payment_method)
        return metodo_de_pago.text

    #Función para hacer los pasos para agregar tarjeta de crédito desde seleccionar el metodo de pago hasta hacer click en el botón agregar en la ventana "Agregar tarjeta"
    def add_card_information(self, card_number, code):
        self.click_payment_methods()
        self.click_add_card()
        self.input_card_number(card_number)
        self.input_card_code(code)
        self.click_confirm_card()

    #Función para agregar texto en "Mensaje para el conductor".
    def input_comment_for_driver(self, message):
        codigo_sms = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.comment_for_driver))
        codigo_sms.send_keys(message)

    #Función para recibir el texto en el apartado "Mensaje para el conductor".
    def get_comment_for_driver(self):
        comentario_para_conductor = self.driver.find_element(*self.comment_for_driver)
        return comentario_para_conductor.get_attribute('value')

    #Función para hacer click en la opción para pedir Manta y pañuelos.
    def request_blanket_and_tissues(self):

        boton_agregar_manta_y_pañuelos = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.blanket_and_tissues_toggle))
        boton_agregar_manta_y_pañuelos.click()

    #función para determinar el estado de la opción "pedir Manta y pañuelos".
    def get_blanket_and_tissues_toggle_status(self, activated_color):
        WebDriverWait(self.driver, 4).until(lambda d: d.find_element(*self.blanket_and_tissues_toggle).value_of_css_property("background-color") == activated_color)
        estado_del_switch_manta_y_pañuelos = self.driver.find_element(*self.blanket_and_tissues_toggle)
        return estado_del_switch_manta_y_pañuelos.value_of_css_property('background-color')

    #Función para agregar un "Helado" de la sección "Cubeta de helado".
    def add_ice_cream(self):
        boton_agregar_helado = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.ice_cream_add))
        boton_agregar_helado.click()


    #Función para recibir la cantidad pedida de "Helado" de la sección "Cubeta de helado".
    def get_ice_cream_count(self):
        helados_pedidos = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.ice_cream_count))
        return helados_pedidos.text

    #Función para hacer click en reservar un taxi.
    def click_reserve_taxi(self):
        self.driver.find_element(*self.taxi_reserve_button).click()

    #Función para determinar la existancia de el modal para buscar un taxi.
    def get_searching_for_taxi_window_status(self):
        try:
            self.driver.find_element(*self.window_looking_for_taxi)
        except:
            return False
        return True

    #Función para esperar el tiempo de búsqueda de taxi´y encontrar el modal de espera de taxi.
    def wait_for_taxi_to_be_found(self):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.driver_information_image))

        try:
            self.driver.find_element(*self.driver_information_image)
        except:
            return False
        return True

    #Función para borrar información guardada entre cada prueba consecutiva
    def clear_webpage_caché(self):
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.refresh()

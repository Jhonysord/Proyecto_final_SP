import time  # Importa la librería para manejar tiempos.
import copy  # Importa la librería para copiar objetos.
import pandas as pd  # Importa pandas para trabajar con datos estructurados.

# Importa Selenium y componentes específicos de Selenium.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains  # Librería de interacción con periféricos.

# LOCATOR
from Locators.Locators import MyLocators  # Importa los localizadores definidos en otro archivo.

class TC_1():
    def __init__(self, driver):
        # Inicializa la clase TC_1 con el controlador del navegador y los localizadores.
        self.driver = driver
        self.Linktext_proveedores = MyLocators.Linktext_proveedores  # Establece los localizadores para proveedores.
        # Establece los localizadores para las diferentes categorías.
        self.XPATH_tabla_categorias = MyLocators.XPATH_tabla_categorias
        self.XPATH_tabla_proveedores = MyLocators.XPATH_tabla_proveedores
        self.XPATH_categoria_abrasivos = MyLocators.XPATH_categoria_abrasivos
        self.XPATH_categoria_AceitesyLubricantes =MyLocators.XPATH_categoria_AceitesyLubricantes
        self.XPATH_categoria_AcerosyMetales= MyLocators.XPATH_categoria_AcerosyMetales
        self.XPATH_categoria_acondicionadosyRefris=MyLocators.XPATH_categoria_acondicionadosyRefris
        self.XPATH_categoria_articulosPromoionales = MyLocators.XPATH_categoria_articulosPromoionales
        self.XPATH_categoria_asesoriayConsultoria=MyLocators.XPATH_categoria_asesoriayConsultoria
        self.XPATH_primer_proveedor = MyLocators.XPATH_primer_proveedor

        #self.root_Excel = pd.read_excel(MyLocators.root_Excel, engine="openpyxl")

    def start(self):
        # Inicia la prueba: carga la URL, maximiza la ventana del navegador y espera implícitamente 3 segundos.
        print("Inicio de la prueba")
        self.driver.get(MyLocators.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        # Cierra un elemento emergente en la página.
        self.driver.find_element(By.XPATH, MyLocators.XPATH_cerrar_swalmodal).click()
        try:
            # Espera a que aparezca un elemento específico (botón de proveedores) antes de continuar.
            message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.LINK_TEXT, self.Linktext_proveedores))
            )
            print("Se encontró el botón de proveedores", message)
        except TimeoutException as toe:
            print("Error: ", toe)

        # Hace clic en el enlace de proveedores.
        self.driver.find_element(By.LINK_TEXT, self.Linktext_proveedores).click()

        # Define una lista de categorías para iterar.
        categorias = [self.XPATH_categoria_abrasivos,
                  self.XPATH_categoria_AceitesyLubricantes,
                  self.XPATH_categoria_AcerosyMetales,
                  self.XPATH_categoria_acondicionadosyRefris,
                  self.XPATH_categoria_articulosPromoionales,
                  self.XPATH_categoria_asesoriayConsultoria]
        # Crea un diccionario de proveedores con datos de prueba predefinidos.
        self.proveedores = {
        }

        # Itera sobre las categorías para interactuar con los elementos de la página.
        for i in categorias:
            # Hace clic en una categoría específica.
            self.driver.find_element(By.XPATH, categorias[0]).click()

            # Hace clic en un proveedor específico.
            self.driver.find_element(By.CSS_SELECTOR, ".col-md-8").click()

            # Hace clic en el primer proveedor (posiblemente para ver detalles).
            self.driver.find_element(By.XPATH, self.XPATH_primer_proveedor).click()

            # Obtiene información del proveedor y la asigna al diccionario de proveedores.
            self.proveedores[i]["direccion"] = self.driver.find_element(By.CSS_SELECTOR,
                                                                        ".row:nth-child(1) > .col-md-8:nth-child(2)").text
            self.proveedores[i]["ciudad"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) > .col-md-8").text
            self.proveedores[i]["estado"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > .col-md-8").text
            self.proveedores[i]["pais"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4) > .col-md-8").text
            self.proveedores[i]["telefono"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) > .col-md-8").text
            self.proveedores[i]["correo"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(6) > .col-md-8").text
            self.proveedores[i]["sitioweb"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(7) > .col-md-8").text
            self.proveedores[i]["contacto"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(8) > .col-md-8").text
    

            # Imprime los detalles del proveedor obtenidos.
            print("{}".format(self.proveedores[i]["direccion"]))
            print("{}".format(self.proveedores[i]["ciudad"]))
            print("{}".format(self.proveedores[i]["estado"]))
            print("{}".format(self.proveedores[i]["pais"]))
            print("{}".format(self.proveedores[i]["telefono"]))
            print("{}".format(self.proveedores[i]["correo"]))
            print("{}".format(self.proveedores[i]["sitioweb"]))
            print("{}".format(self.proveedores[i]["contacto"]))
            print("{}".format(self.proveedores[i]["direccion"]))

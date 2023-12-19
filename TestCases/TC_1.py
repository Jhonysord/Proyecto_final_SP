import time
import copy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains #librería de uso de perifericos Mouse teclado etc

# LOCATOR
from Locators.Locators import MyLocators

class TC_1():
  def __init__ (self, driver):
    self.driver = driver
    self.Linktext_proveedores = MyLocators.Linktext_proveedores
    self.XPATH_tabla_categorias = MyLocators.XPATH_tabla_categorias
    self.XPATH_tabla_proveedores = MyLocators.XPATH_tabla_proveedores
    self.XPATH_categoria_abrasivos = MyLocators.XPATH_categoria_abrasivos
    self.XPATH_categoria_AceitesyLubricantes =MyLocators.XPATH_categoria_AceitesyLubricantes
    self.XPATH_categoria_AcerosyMetales= MyLocators.XPATH_categoria_AcerosyMetales
    self.XPATH_categoria_acondicionadosyRefris=MyLocators.XPATH_categoria_acondicionadosyRefris
    self.XPATH_categoria_articulosPromoionales = MyLocators.XPATH_categoria_articulosPromoionales
    self.XPATH_categoria_asesoriayConsultoria=MyLocators.XPATH_categoria_asesoriayConsultoria

    self.root_Excel = pd.read_excel(MyLocators.root_Excel, engine = "openpyxl")

  def start(self):

    self.driver.get(MyLocators.URL)
    self.driver.maximize_window()
    self.driver.implicitly_wait(3)
    try:
      message = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, self.Linktext_proveedores))
        )
      print("Se encontró el boton de proveedores", message)
    except TimeoutException as toe:
      print("Error: ", toe)

    self.driver.find_element(By.LINK_TEXT, self.Linktext_proveedores).click()    
    size_table_categorias = self.driver.find_element(By.XPATH,self.XPATH_tabla_categorias)
    #categorias = len(size_table_categorias)
    categorias = {    self.XPATH_tabla_categorias,
                      self.XPATH_tabla_proveedores ,
                      self.XPATH_categoria_abrasivos,
                      self.XPATH_categoria_AceitesyLubricantes,
                      self.XPATH_categoria_AcerosyMetales,
                      self.XPATH_categoria_acondicionadosyRefris,
                      self.XPATH_categoria_articulosPromoionales,
                      self.XPATH_categoria_asesoriayConsultoria}
    for i in categorias:
      self.driver.find_element(By.CSS_SELECTOR, MyLocators.proveedores[i]).click()
      #size_table_proveedores = self.driver.find_element(By.XPATH,self.XPATH_tabla_proveedores)
      #proveedores= len(size_table_proveedores)
      for i in categorias:
          self.driver.find_element(By.CSS_SELECTOR, ".col-md-8").click()
          self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) > .col-md-10 > p").click()
          self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) > .col-md-8:nth-child(2)").click()
          self.vars["direccion"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) > .col-md-8:nth-child(2)").text
          self.vars["ciudad"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) > .col-md-8").text
          self.vars["estado"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > .col-md-8").text
          self.vars["pais"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4) > .col-md-8").text
          self.vars["telefono"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) > .col-md-8").text
          self.vars["correo"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(6) > .col-md-8").text
          self.vars["sitioweb"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(7) > .col-md-8").text
          self.vars["contacto"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(8) > .col-md-8").text
      else:
        print("Este proveedor")
    
    print("{}".format(self.vars["direccion"]))
    print("{}".format(self.vars["ciudad"]))
    print("{}".format(self.vars["estado"]))
    print("{}".format(self.vars["pais"]))
    print("{}".format(self.vars["telefono"]))
    print("{}".format(self.vars["correo"]))
    print("{}".format(self.vars["sitioweb"]))
    print("{}".format(self.vars["contacto"]))
    print("{}".format(self.vars["direccion"]))
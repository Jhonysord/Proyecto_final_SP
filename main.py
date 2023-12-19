import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

import HtmlTestRunner

#Aquí se importan los Locators
from Locators.Locators import MyLocators
#Aquí se importan los test cases
from TestCases.TC_1 import TC_1

class TestCatalogo(unittest.TestCase):
    
    @classmethod #bandera para un metodo que le da prioridad al metodo de ejecutarse primero
    def setUpClass (cls):
        print("INICIO DE LA PRUEBA")
        miServicio = Service(MyLocators.Driver_Path)
        cls.driver = webdriver.Chrome(service=miServicio)
        
        options=webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])#Here
        cls.driver = webdriver.Chrome(options=options)
        time.sleep(5)
        #miServicio

    def test_Proyecto_final_SP(self):
        driver=self.driver
        tc_1=TC_1(driver)
        tc_1.start()
        #=(driver)
        #.start()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("FIN DE LA PRUEBA")
       
if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner(output=MyLocators.Reporte))
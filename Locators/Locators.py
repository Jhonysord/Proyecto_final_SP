class MyLocators():

    Driver_Path = "C:\\Proyecto_final_SP\\webdriver\\chromedriver.exe" #Casa
    #Driver_Path = "C:\\Users\\Fernando Tester IT\\Documents\\Proyecto_final_SP\\webdriver\\chromedriver.exe"#trabajo
    URL = "https://www.industriamaquiladora.com/"
    root_Excel = "C:\\Proyecto_final_SP\\Data\\Test_Matrix.xlsx"
    #root_Excel = "C:\\Users\\Fernando Tester IT\\Documents\\Proyecto_final_SP\\data\\Test_Matrix.xlsx"
    Reporte = "C:\\Proyecto_final_SP\\evidencias\\Reporte.html"
    #Reporte = "C:\\Users\\Fernando Tester IT\\Documents\\Proyecto_final_SP\\evidencias\\Reporte.html"
    evidenciaExcel = "C:\\Proyecto_final_SP\\evidencias\\Catalogo.xlsx" 

    # Main Page
    Linktext_proveedores="PROVEEDORES"

    # Categorias page
    XPATH_tabla_categorias = "//section[@id='content12-d']/div/div/div"
    XPATH_categoria_abrasivos = "/html/body/section[3]/div/div/div[1]/div[1]/div/div"
    XPATH_categoria_AceitesyLubricantes = "/html/body/section[3]/div/div/div[1]/div[2]/div/div"
    XPATH_categoria_AcerosyMetales = "/html/body/section[3]/div/div/div[1]/div[3]/div/div"
    XPATH_categoria_acondicionadosyRefris="/html/body/section[3]/div/div/div[1]/div[4]/div/div"
    XPATH_categoria_articulosPromoionales ="/html/body/section[3]/div/div/div[1]/div[5]/div/div"
    XPATH_categoria_asesoriayConsultoria = "/html/body/section[3]/div/div/div[1]/div[6]/div/div"
   # Provedores de categoria page
    XPATH_tabla_proveedores = "//section[@id='extClients3-1i']/div[2]/div/div"
  

    # Tabla de Evidencia
    list_Columns = ["Mensaje"]
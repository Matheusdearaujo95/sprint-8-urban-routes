from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

input("Pressione Enter para fechar o navegador...")  # Pausa pra você ver o Chrome aberto
driver.quit()
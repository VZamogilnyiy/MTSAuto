from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://test.payment.ewt.mts.ru")
driver.implicitly_wait(50)

#Ждем кнопку в попапе, проиводим клик.
popup1 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH , "/html/body/div[3]/div/div[2]/div[5]/div/div[1]/button"))).click()

#Вводим номер, ищем кнопку, произвдим клик
login_input = driver.find_element_by_id("phone")
login_input.send_keys("9999999930") 
login_open = driver.find_element_by_css_selector(".sc-bdfBwQ.joyPHQ").click()

#Ищем инпут пасворда, вставляем код из смс
password = driver.find_element_by_css_selector(".sc-cxFLnm.sc-iBaPrD.bfEZWs.gdARiY")
password.send_keys("9999")

#Я не Ашхен
ashen = driver.find_element_by_xpath("/html/body/div/div[1]/main/button[3]").click()

#Я клиент банка
popup2 = driver.find_element_by_xpath("/html/body/aside/div[2]/div/div[3]/button[1]").click()

#Войти в ограниченном режиме
ogran = driver.find_element_by_xpath("/html/body/div/div[1]/main/button").click()

#Асерт на наличие номера
def test_number():
	test = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/section[1]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/a/div[2]")
	assert test is not None, "Номер не совпадает"
	driver.quit()












from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открываем браузер и переходим по ссылке
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")

    # Нажимаем кнопку
    browser.find_element(By.ID, "button")

  

finally:
   
    browser.quit()
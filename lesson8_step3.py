from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Открытие браузера и переход на страницу
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    # Получение значений x и y
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = int(x_element.text)
    y = int(y_element.text)
    result = str(x + y)

    # Выбор результата в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    # Нажатие на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Пауза для визуальной проверки
    time.sleep(10)
    browser.quit()
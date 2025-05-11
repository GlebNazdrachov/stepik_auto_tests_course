from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажимаем на кнопку
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Нажимаем Submit
    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

finally:
    # Ждем 10 секунд чтобы увидеть результат
    time.sleep(10)
    browser.quit()
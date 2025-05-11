from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://example.com")  # можно заменить на любую страницу

# Вызов alert
browser.execute_script("alert('Robots at work');")

# Пауза, чтобы увидеть alert
time.sleep(5)

# Закрытие alert
alert = browser.switch_to.alert
alert.accept()

# Завершение
browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Инициализация браузера
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполнение текстовых полей
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")

    # Получаем путь к файлу file.txt в той же папке, где скрипт
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    # Создаем файл, если его нет
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # создаем пустой файл

    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку "Submit"
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)  # даём время на визуальную проверку
    browser.quit()
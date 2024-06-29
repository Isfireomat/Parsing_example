from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random

# Укажите путь к вашему chromedriver
chrome_driver_path = 'chromedriver.exe'

# Настройки браузера
chrome_options = Options()
# chrome_options.add_argument("--headless")  # запуск без открытия окна браузера
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
# https://www.alib.ru/razdel.php4?n9=0&all=11677&sortby=4&bs=andy111&&findword=tbros
# Инициализация драйвера
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
x=0
while x<11677:
    try:# Открываем сайт
        driver.get(f'https://www.alib.ru/razdel.php4?n9={x}&all=11677&sortby=4&bs=andy111&&findword=tbros')
        x+=60
        time.sleep( random.uniform(3, 7)) 
        
        page_source = driver.page_source

        # Парсим страницу с помощью BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Ищем заголовки новостей
        paragraphs = soup.find_all('p')
        paragraphs = paragraphs[3:-3]

        with open("text.txt","a", encoding='utf-8') as f:
            for index, headline in enumerate(paragraphs, start=1):
                f.write(headline.text.replace('\n', ' ')+"\n")
        
    except: print("Error")
# finally:
#     # Закрываем браузер
#     driver.quit()
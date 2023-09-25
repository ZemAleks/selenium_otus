import time
from selenium.webdriver.common.by import By


# проверка фильтрации поиска по запросу в opencart
def test_search_input(driver, base_url):
    driver.get(base_url)
    driver.find_element(By.NAME, "search").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, "#search button").click()
    driver.find_element(value="content")
    time.sleep(2)


# проверка заголовка на главной странице в opencart
def test_first(driver):
    driver.get("http://10.66.66.7:80")
    assert driver.title == "Your Store"
    time.sleep(2)


# проверка заголовка на главной странице яндекс дзена
def test_second(driver):
    driver.get("https://dzen.ru")
    assert driver.title == "Дзен"

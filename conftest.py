import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FierfoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", choices=["chrome", "firefox", "yandex", "safari", "edge"]
    )
    parser.addoption(
        "--headless", action="store_true",
    )
    parser.addoption(
        "--base_url", required=True
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    service = Service()

    if browser_name == "chrome":
        options = Options()
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
        service = Service(executable_path=os.path.expanduser("E:/drivers/chromedriver.exe"))
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FierfoxOptions()
        if headless:
            options.add_argument("-headless")
        service = Service(executable_path=os.path.expanduser("E:/drivers/geckodriver.exe"))
        browser = webdriver.Firefox(service=service, options=options)
    elif browser_name == "yandex":
        options = Options()
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
        service = Service(executable_path=os.path.expanduser("E:/drivers/yandexdriver.exe"))
        browser = webdriver.Chrome(service=service, options=options)
    else:
        raise NotImplemented()

    yield browser
    browser.close()

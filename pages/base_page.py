from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

base_url = 'https://qa-scooter.praktikum-services.ru/'

class BasePage:

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    @allure.step("Открываем страницу: {base_url}")
    def open(self, base_url):
        self.driver.get(base_url)

    @allure.step("Закрываем баннер cookies")
    def close_cookie_banner(self):
        btn = self.driver.find_element(*self.COOKIE_BUTTON)
        btn.click()

    @allure.step("Кликаем по логотипу Самоката")
    def click_scooter_logo(self):
        self.driver.find_element(*self.LOGO_SCOOTER).click()

    @allure.step("Кликаем по логотипу Яндекс")
    def click_yandex_logo(self):
        self.driver.find_element(*self.LOGO_YANDEX).click()

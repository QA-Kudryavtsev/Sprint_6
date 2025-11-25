from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators
from data.urls import BASE_URL
import allure


class BasePage:

    @allure.step("Инициализируем базовую страницу")
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    @allure.step("Открываем страницу")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Находим элемент: {locator}")
    def find(self, locator):
        return self.wait(EC.visibility_of_element_located(locator))
    
    @allure.step("Находим элементы: {locator}")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)
    
    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        self.wait(EC.element_to_be_clickable(locator)).click()

    @allure.step("Вводим текст '{text}' в элемент: {locator}")
    def type(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    @allure.step('Ожидание')
    def wait(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)
    
    @allure.step('Ожидание видимости')
    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
    
    @allure.step('Ожидание кликабельности')
    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получаем список окон")
    def get_window_handles(self):
        return self.driver.window_handles
    
    @allure.step("Получаем текущее окно")
    def get_current_window(self):
        return self.driver.current_window_handle
    
    @allure.step("Переключаемся на окно: {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Ожидаем открытие нового окна")
    def wait_new_window_opened(self, old_handles):
        self.wait(lambda d: len(d.window_handles) > len(old_handles))
        new = [h for h in self.driver.window_handles if h not in old_handles]
        return new[0]
    
    @allure.step("Ожидаем, что URL будет содержать: {text}")
    def wait_url_contains(self, text):
        self.wait(EC.url_contains(text))
    
    @allure.step("Принимаем куки")
    def accept_cookies(self):
        self.click(HomePageLocators.COOKIE_BUTTON)

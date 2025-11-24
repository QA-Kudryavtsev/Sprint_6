from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import allure


class OrderPage(BasePage):

 
    TOP_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g")
    BOTTOM_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    METRO_OPTION = (By.CSS_SELECTOR, "div.select-search__select ul li")
    INPUT_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    BODY = (By.CSS_SELECTOR, "body")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")

    @allure.step("Нажимаем кнопку Заказать: {entry}")
    def click_order_button(self, entry):
        if entry == "top":
            self.driver.find_element(*self.TOP_ORDER_BUTTON).click()
        elif entry == "bottom":
            self.driver.find_element(*self.BOTTOM_ORDER_BUTTON).click()

    @allure.step("Заполняем шаг 1 формы заказа")
    def fill_first_step(self, name, lastname, address, station, phone):
        self.driver.find_element(*self.INPUT_NAME).send_keys(name)
        self.driver.find_element(*self.INPUT_LASTNAME).send_keys(lastname)
        self.driver.find_element(*self.INPUT_ADDRESS).send_keys(address)
        self.driver.find_element(*self.INPUT_METRO).click()
        elements = self.driver.find_elements(*self.METRO_OPTION)
        for el in elements:
            if station.lower() in el.text.lower():
                el.click()
                break
        self.driver.find_element(*self.INPUT_PHONE).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()
        
    @allure.step("Заполняем шаг 2 формы заказа")
    def fill_second_step(self, date, rent_period_index=1, choose_black=True):
        self.driver.find_element(*self.INPUT_DATE).send_keys(date)
        self.driver.find_element(*self.BODY).click()
        self.driver.find_element(*self.RENT_DROPDOWN).click()
        self.driver.find_elements(*self.RENT_OPTIONS)[rent_period_index].click()
        if choose_black:
            self.driver.find_element(*self.COLOR_BLACK).click()
        else:
            self.driver.find_element(*self.COLOR_GREY).click()
        self.driver.find_elements(*self.ORDER_BUTTON)[1].click()
        self.driver.find_element(*self.YES_BUTTON).click()

    def is_success_modal_visible(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(*self.SUCCESS_MODAL))
    
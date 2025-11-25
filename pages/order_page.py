from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    @allure.step("Нажимаем кнопку Заказать: {entry}")
    def click_order_button(self, entry):
        if entry == "top":
            self.click(OrderPageLocators.TOP_ORDER_BUTTON)
        elif entry == "bottom":
            self.click(OrderPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Заполняем поля Имя")
    def fill_name(self, name):
        self.type(OrderPageLocators.INPUT_NAME, name)

    @allure.step("Заполняем поля Фамилия")
    def fill_lastname(self, lastname):
        self.type(OrderPageLocators.INPUT_LASTNAME, lastname)

    @allure.step("Заполняем поле Адресс")
    def fill_address(self, address):
        self.type(OrderPageLocators.INPUT_ADDRESS, address)
    
    @allure.step("Выбираем станцию метро: {station}")
    def fill_metro(self, station):
        metro_input = self.find(OrderPageLocators.INPUT_METRO)
        self.click(metro_input)
        elements = self.find_all(OrderPageLocators.METRO_OPTION)
        for el in elements:
            if station.lower() in el.text.lower():
                self.click(el)
                break

    @allure.step("Заполняем поле Телефон")
    def fill_phone(self, phone):
        self.type(OrderPageLocators.INPUT_PHONE, phone)

    @allure.step("Обьединяем заполнение полей в 1 шаг")
    def step_one(self, name, lastname, address, station, phone):
        self.fill_name(name)
        self.fill_lastname(lastname)
        self.fill_address(address)
        self.fill_metro(station)
        self.fill_phone(phone)

    @allure.step("Кликаем кнопку Далее")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)
  
    @allure.step('Заполняем дату')
    def fill_date(self, date):
        self.type(OrderPageLocators.INPUT_DATE, date)

    @allure.step('Клик по пустому месту')
    def click_body(self):
        self.click(OrderPageLocators.BODY)

    @allure.step('Заполняем аренду')
    def fill_rent(self, rent_period_index=1, choose_black=True):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        rent_options = self.find_all(OrderPageLocators.RENT_OPTIONS)
        rent_options[rent_period_index].click()                       # Не знаю как заставить тут кликнуть по web элементу, чтобы не изменять метод .click :(
        if choose_black:
            black = self.find(OrderPageLocators.COLOR_BLACK)
            self.click(black)
        else:
            grey = self.find(OrderPageLocators.COLOR_GREY)
            self.click(grey)

    @allure.step('Кликаем по кнопке заказать')
    def click_order_button_next(self):
        btns = self.find_all(OrderPageLocators.ORDER_BUTTON)
        self.wait_clickable(OrderPageLocators.ORDER_BUTTON)
        btns[1].click()                                              # Тоже самое...

    @allure.step('Кликаем по кнопке подтверждения')
    def click_yes(self):
        yes_btn = self.find(OrderPageLocators.YES_BUTTON)
        self.click(yes_btn)

    @allure.step('Обьединяем заполнение полей в шаг 2')
    def step_2(self, date, rent_period_index, choose_black=True):
        self.fill_date(date)
        self.click_body()
        self.fill_rent(rent_period_index, choose_black)

    def is_success_modal_visible(self):
        return self.wait_visible(OrderPageLocators.SUCCESS_MODAL)
    
        

    
import pytest
from pages.order_page import OrderPage
import allure
from data.tests_order_data import Order_Tests_DATA

@allure.feature("Оформление заказа")
class TestOrderFlow:

        @allure.story("Позитивный сценарий")
        @allure.title("Проверка оформления заказа через кнопку '{entry}' — {data[name]} {data[lastname]}")
        @pytest.mark.parametrize("entry", ["top", "bottom"])
        @pytest.mark.parametrize("data", Order_Tests_DATA.ORDER_DATA)
        def test_order_positive_flow(self, driver, entry, data):
            page = OrderPage(driver)
            page.open()
            page.accept_cookies()
            page.click_order_button(entry)
            page.step_one(data['name'], data['lastname'], data['address'], data['station'],data['phone'])
            page.click_next()
            page.step_2(data["date"], rent_period_index=1, choose_black=data["color"])
            page.click_order_button_next()
            page.click_yes()
            assert page.is_success_modal_visible(), "Окно подтверждения успешного заказа не появилось"
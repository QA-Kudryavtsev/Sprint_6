import pytest
from pages.order_page import OrderPage
import allure

ORDER_DATA = [
    {
        'name': 'Иван',
        'lastname': 'Иванов',
        'address': 'ул Пушкина, 10',
        'station': 'Комсомольская',
        'phone': '+79001234567',
        'date': '01.08.2025',
        'color': True
    },
    {
        'name': 'Ольга',
        'lastname': 'Петрова',
        'address': 'ул Ленина, 5',
        'station': 'Тверская',
        'phone': '+79007654321',
        'date': '05.08.2025',
        'color': False
    }
]

@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий")
@allure.title("Проверка оформления заказа через кнопку '{entry}' — {data[name]} {data[lastname]}")
@pytest.mark.parametrize("entry", ["top", "bottom"])
@pytest.mark.parametrize("data", ORDER_DATA)
def test_order_positive_flow(driver, base_url, entry, data):
    page = OrderPage(driver, base_url)
    page.open(base_url)
    page.close_cookie_banner()
    page.click_order_button(entry)
    page.fill_first_step(
        data["name"],
        data["lastname"],
        data["address"],
        data["station"],
        data["phone"]
    )

    page.fill_second_step(
        data["date"],
        rent_period_index=1,
        choose_black=data["color"]
    )
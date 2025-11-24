from pages.base_page import BasePage
import allure

@allure.feature("Хедер")
@allure.story("Переход по логотипу Скутер")
@allure.title("Проверка перехода на главную по клику на логотип 'Самокат'")
def test_logo_scooter_redirects_to_home(driver, base_url):
    driver.get(base_url + "order")
    page = BasePage(driver, base_url)
    page.click_scooter_logo()
    assert driver.current_url == base_url, f"Ожидали переход на главную {base_url}, а получили {driver.current_url}"

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure

@allure.feature("Хедер")
@allure.story("Переход по логотипу Яндекс")
@allure.title("Проверка открытия Яндекс.Дзен в новой вкладке")
def test_logo_yandex_opens_dzen_in_new_tab(driver, base_url):
    page = BasePage(driver, base_url)
    page.open(base_url)
    old_tabs = driver.window_handles
    page.click_yandex_logo()
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > len(old_tabs))
    new_tab = [tab for tab in driver.window_handles if tab not in old_tabs][0]
    driver.switch_to.window(new_tab)
    WebDriverWait(driver, 10).until(
        lambda d: "dzen" in d.current_url.lower())
    assert "dzen" in driver.current_url.lower(), \
        f"Ожидали переход на Дзен, а получили: {driver.current_url}"
import pytest
import allure
from pages.home_page import HomePage
from data.urls import BASE_URL, DZEN_URL


@allure.feature("Проверка логотипов")
class TestLogos:

    @allure.story("Логотип Самоката")
    @allure.title("Проверка перехода на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()
        home_page.click_scooter_logo()
        current_url = home_page.get_current_url()
        assert current_url == BASE_URL, (
            f"Ожидали URL: {BASE_URL}, но получили: {current_url}")

    @allure.story("Логотип Яндекс")
    @allure.title("Проверка перехода на Дзен по логотипу Яндекс")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()
        original_window = home_page.get_current_window()
        home_page.click_yandex_logo()
        home_page.wait_new_window_opened([original_window])
        new_window = [window for window in home_page.get_window_handles() 
                     if window != original_window][0]
        home_page.switch_to_window(new_window)
        home_page.wait_url_contains("dzen.ru")
        current_url = home_page.get_current_url()
        assert "dzen.ru" in current_url, (
            f"Ожидали, что URL содержит 'dzen.ru', но получили: {current_url}")
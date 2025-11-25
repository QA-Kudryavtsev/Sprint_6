import pytest
from pages.home_page import HomePage
import allure
from data.test_data import Tests_Data

@allure.feature("Главная страница")
class TestFAQ:

    @allure.story("FAQ")
    @allure.title("Проверка корректности ответа в FAQ — вопрос №{index}")
    @pytest.mark.parametrize("index", list(range(8)))
    def test_questions_accept_reveals(self, driver, index):
      page = HomePage(driver)
      page.open()
      page.accept_cookies()
      page.click_question_by_index(index)
      actual_answer = page.get_answer_by_index(index)
      expected_answer = Tests_Data.QUESTION_EXPECTED_ANSWERS[index]

      assert expected_answer in actual_answer, (
          f"Ожидали ответ: '{expected_answer}', "f"но получили: '{actual_answer}'")

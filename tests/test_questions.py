import pytest
from pages.home_page import HomePage
import allure

@allure.feature("Главная страница")
@allure.story("FAQ")
@allure.title("Проверка корректности ответа в FAQ — вопрос №{index}")
@pytest.mark.parametrize("index", list(range(8)))
def test_questions_accept_reveals(driver, index, base_url):
  page = HomePage(driver, base_url)
  page.open(base_url)
  page.close_cookie_banner()
  actual_answer = page.open_question_by_index(index)
  expected_answer = page.get_expected_answer(index)

  assert expected_answer in actual_answer, (
      f"Ожидали ответ: '{expected_answer}', "f"но получили: '{actual_answer}'")

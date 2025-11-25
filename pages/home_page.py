from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure

class HomePage(BasePage):

      @allure.step("Кликаем по вопросу с индексом: {index}")
      def click_question_by_index(self, index):
            questions = self.find_all(HomePageLocators.QUESTION_BUTTON)
            q = questions[index]
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",q)
            self.wait(lambda d: q.is_displayed(), timeout=2)
            try:
                  self.click(q)
            except Exception:
                  self.driver.execute_script("arguments[0].click();", q)
            return q.text.strip()
  
      @allure.step("Получаем ответ по индексу FAQ: {index}")
      def get_answer_by_index(self, index):
            answers = self.find_all(HomePageLocators.ANSWER_ITEMS)
            self.wait(EC.visibility_of(answers[index]))
            return answers[index].text.strip()
      
      @allure.step("Кликаем по логотипу Самоката")
      def click_scooter_logo(self):
            self.click(HomePageLocators.LOGO_SCOOTER)

      @allure.step("Кликаем по логотипу Яндекс")
      def click_yandex_logo(self):
            self.click(HomePageLocators.LOGO_YANDEX)
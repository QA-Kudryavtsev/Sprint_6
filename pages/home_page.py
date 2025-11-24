from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import allure

class HomePage(BasePage):
   
      QUESTION_ITEMS = (By.CSS_SELECTOR, 'div[data-accordion-component="AccordionItem"].accordion__item, div.accordion__item')
      QUESTION_BUTTON = (By.CSS_SELECTOR, 'div[data-accordion-component="AccordionItemButton"], div.accordion__button, button.accordion__button')
      QUESTION_EXPECTED_ANSWERS = {
            0: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
            1: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
            2: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
            3: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
            4: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
            5: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
            6: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
            7: "Да, обязательно. Всем самокатов! И Москве, и Московской области."}
  
      @allure.step("Получаем количество вопросов FAQ") 
      def question_count(self):
            items = self.driver.find_elements(*self.QUESTION_ITEMS)
            return len(items)
  
      @allure.step("Открываем FAQ-вопрос с номером {index}")
      def open_question_by_index(self, index):
            items = self.driver.find_elements(*self.QUESTION_ITEMS)
            if index < 0 or index >= len(items):
                  raise IndexError("Question index is out of range")
            item = items[index]
            btn = item.find_element(*self.QUESTION_BUTTON)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((self.QUESTION_BUTTON)))
            aria = btn.get_attribute("aria-controls")
            btn.click()
            panel = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, aria)))
            return panel.text
  
      @allure.step("Получаем ожидаемый текст ответа для вопроса №{index}")
      def get_expected_answer(self, index):
            return self.QUESTION_EXPECTED_ANSWERS[index]
         
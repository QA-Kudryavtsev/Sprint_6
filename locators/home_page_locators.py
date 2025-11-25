from selenium.webdriver.common.by import By

class HomePageLocators:
    QUESTION_ITEMS = (By.CSS_SELECTOR, 'div[data-accordion-component="AccordionItem"].accordion__item, div.accordion__item')
    QUESTION_BUTTON = (By.CSS_SELECTOR, 'div[data-accordion-component="AccordionItemButton"], div.accordion__button, button.accordion__button')
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    ANSWER_ITEMS = (By.CSS_SELECTOR, "div[data-accordion-component='AccordionItemPanel']")
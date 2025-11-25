from selenium.webdriver.common.by import By

class OrderPageLocators:
    
    TOP_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g")
    BOTTOM_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    METRO_OPTION = (By.CSS_SELECTOR, "div.select-search__select ul li")
    INPUT_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    BODY = (By.CSS_SELECTOR, "body")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
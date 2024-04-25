from selenium.webdriver.common.by import By


class OrderListLocators:
    ORDER_LIST_TEXT = By.XPATH, '//h1[contains(text(),"Лента заказов")]'
    ORDER = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    CONSIST_TEXT = By.XPATH, '//p[text()="Cостав"]'


import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.move_to_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_order_list_button(self):
        self.move_to_element_and_click(MainPageLocators.FEED_BUTTON)

    @allure.step('Клик по ингридиенту')
    def click_ingredient_button(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT)

    @allure.step('Клик по кнопке закрытия')
    def click_close_popup_window_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)

    @allure.step('Проверить наличие элемента на экране')
    def check_ingredients_details_on_screen(self):
        return self.find_element(MainPageLocators.INGREDIENT_DETAILS_TEXT).is_displayed()

    @allure.step('Дождаться исчезновения деталей заказа')
    def wait_for_order_details_disappear(self):
        self.wait_element_disappear(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step('Кликнуть по кнопке "Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_BUTTON)

    @allure.step('Добавить ингридиент в констуктор')
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(self.find_element(MainPageLocators.INGREDIENT),
                           self.find_element(MainPageLocators.BURGER_CONSTRUCTOR))




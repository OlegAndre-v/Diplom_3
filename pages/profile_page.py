import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    @allure.step('Клик по кнопке "Личный кабинет')
    def click_lk_button(self):
        self.move_to_element_and_click(MainPageLocators.LK_BUTTON)

    @allure.step('Логин на аккаунт')
    def login(self, data):
        self.send_input(ProfilePageLocators.EMAIL_INPUT, data['email'])
        self.send_input(ProfilePageLocators.PASSWORD_INPUT, data['password'])
        self.move_to_element_and_click(ProfilePageLocators.LOGIN_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_order_history_button(self):
        self.move_to_element_and_click(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_button(self):
        self.move_to_element_and_click(ProfilePageLocators.LOGOUT_BUTTON)


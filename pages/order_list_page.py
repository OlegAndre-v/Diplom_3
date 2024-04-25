import allure

import helpers
from pages.base_page import BasePage
from locators.order_list_page_locators import OrderListLocators
from data import TestData


class OrderList(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль')
    def click_password_recovery_button(self):
        self.move_to_element_and_click()

    @allure.step('Клик по заказу в листе заказов')
    def click_order(self):
        self.click_element(OrderListLocators.ORDER)

    @allure.step('Создаем заказ авторизированным пользоваетелем')
    def create_order(self, user):
        return helpers.create_order(TestData.INGREDIENTS, user['json']['accessToken'])

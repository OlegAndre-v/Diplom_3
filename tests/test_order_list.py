import allure
from data import Url
from pages.order_list_page import OrderList
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from locators.order_list_page_locators import OrderListLocators
from locators.profile_page_locators import ProfilePageLocators
import time


@allure.story('Тесты ленты заказов')
class TestOrderList:
    # @allure.title('Тест всплывающего окна с деталями заказа')
    # def test_order_details_popup(self, driver):
    #     page = OrderList(driver)
    #     page.open(Url.ORDER_LIST_PAGE)
    #     page.click_order()
    #     assert page.get_text(OrderListLocators.CONSIST_TEXT) == 'Cостав'

    @allure.title('Заказы из истории заказов отображаются в ленте заказов')
    def test_user_order_displayed_in_order_list(self, driver, user):
        order_page = OrderList(driver)
        order_page.open(Url.LOGIN_PAGE)
        response = order_page.create_order(user)
        profile_page = ProfilePage(driver)
        profile_page.login(user)
        profile_page.wait_url_change(Url.BASE_PAGE)
        main_page = MainPage(driver)
        main_page.click_order_list_button()

        profile_page.click_lk_button()
        profile_page.wait_url_change(Url.ACCOUNT_PROFILE_PAGE)
        profile_page.click_order_history_button()
        assert str(response.json()['order']['number']) in profile_page.get_text(ProfilePageLocators.ORDER_NUMBER)




        #
        # print(response.json()['order']['number'])



import allure
from data import Url
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators
from locators.order_list_page_locators import OrderListLocators


@allure.story('Тесты основного функционала')
class TestMainFunctionality:
    @allure.title('Тест переход по кнопке "Констуктор"')
    def test_transition_to_constructor(self, driver):
        page = MainPage(driver)
        page.open(Url.ORDER_LIST_PAGE)
        page.click_constructor_button()
        assert (page.get_url() == Url.BASE_PAGE and
                page.get_text(MainPageLocators.LOGIN_BUTTON) == 'Войти в аккаунт')

    @allure.title('Тест переход по кнопке "Лента Заказов"')
    def test_transition_to_order_list(self, driver):
        page = MainPage(driver)
        page.open(Url.BASE_PAGE)
        page.click_order_list_button()
        assert (page.get_url() == Url.ORDER_LIST_PAGE and
                page.get_text(OrderListLocators.ORDER_LIST_TEXT) == 'Лента заказов')

    @allure.title('Тест всплывающего окна ингридиента')
    def test_ingredient_popup(self, driver):
        page = MainPage(driver)
        page.open(Url.BASE_PAGE)
        page.click_ingredient_button()
        assert page.get_text(MainPageLocators.INGREDIENT_DETAILS_TEXT) == 'Детали ингредиента'

    @allure.title('Тест кнопки закрытия всплывающего окна')
    def test_ingredient_popup_close_button(self, driver):
        page = MainPage(driver)
        page.open(Url.BASE_PAGE)
        page.click_ingredient_button()
        page.click_close_popup_window_button()
        page.wait_for_order_details_disappear()
        assert page.check_ingredients_details_on_screen() == False

    @allure.title('Тест счетчика ингридиентов')
    def test_ingredient_counter(self, driver):
        page = MainPage(driver)
        page.open(Url.BASE_PAGE)
        page.add_ingredient_to_constructor()
        assert page.get_text(MainPageLocators.INGREDIENT_COUNTER) == '2'

    @allure.title('Тест оформления заказа авторизованным пользователем')
    def test_successful_order(self,driver, user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open(Url.LOGIN_PAGE)
        profile_page.login(user)
        main_page.wait_url_change(Url.BASE_PAGE)
        main_page.add_ingredient_to_constructor()
        main_page.click_order_button()
        assert main_page.get_text(MainPageLocators.ORDER_TEXT) == 'идентификатор заказа'



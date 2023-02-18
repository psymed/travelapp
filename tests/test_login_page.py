from .pages.login_page import LoginPages
from .locators.login_page_locators import LoginPageLocators


def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://travel.mycwt.com/signon/")
    assert login_page.get_title() == "CWT - Business Travel Management Company"
    login_page.enter_email("testuser@test.com").regesh()
    login_page.enter_password("testpass")
    login_page.click_login_button()
    assert "dashboard" in driver.current_url

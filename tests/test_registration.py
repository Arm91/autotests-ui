import pytest
from playwright.sync_api import Page, expect


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = chromium_page.get_by_role("textbox", name="Email")
    email_input.fill("user.name@gmail.com")

    username_input = chromium_page.get_by_role("textbox", name="Username")
    username_input.fill("username")

    username_input = chromium_page.get_by_role("textbox", name="Password")
    username_input.fill("password")

    login_button = chromium_page.get_by_test_id('registration-page-registration-button')
    login_button.click()

    dashboard_title_text = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title_text).to_be_visible()
    expect(dashboard_title_text).to_have_text("Dashboard")

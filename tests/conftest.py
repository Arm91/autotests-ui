import pytest
from playwright.sync_api import Page, Playwright, expect


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='function')
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_role("textbox", name="Email")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_role("textbox", name="Username")
    username_input.fill("username")

    username_input = page.get_by_role("textbox", name="Password")
    username_input.fill("password")

    login_button = page.get_by_test_id('registration-page-registration-button')
    login_button.click()

    dashboard_title_text = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title_text).to_be_visible()
    expect(dashboard_title_text).to_have_text("Dashboard")

    context.storage_state(path='../browser-state.json')

    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='../browser-state.json')
    page = context.new_page()

    yield page

    browser.close()

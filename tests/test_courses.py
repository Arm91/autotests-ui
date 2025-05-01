import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
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

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page(storage_state='../browser-state.json')

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title_text = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title_text).to_be_visible()
        expect(courses_title_text).to_have_text('Courses')

        courses_empty_folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_empty_folder_icon).to_be_visible()

        courses_no_result_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_no_result_title_text).to_have_text('There is no results')

        course_no_result_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(course_no_result_text).to_have_text('Results from the load test pipeline will be displayed here')

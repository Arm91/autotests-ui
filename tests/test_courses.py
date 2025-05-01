import pytest
from playwright.sync_api import Playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
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

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
              wait_until='networkidle')

    # Error 1
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Error 2
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # Error 3
    page.evaluate("""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        """)

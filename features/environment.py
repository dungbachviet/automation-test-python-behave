from behave.fixture import use_fixture_by_tag
from behave import fixture
from selenium import webdriver


@fixture(name="fixture.browser.firefox")
def browser_firefox(context, *args, **kwargs):
    # -- SETUP-FIXTURE PART:
    context.browser = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        options=webdriver.FirefoxOptions(),
    )
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


fixture_registry = {
    "fixture.browser.firefox": browser_firefox,
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)

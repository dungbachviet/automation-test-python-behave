from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helpers import get_password


@given("I navigate to Foresight")
def step_impl(context):
    context.browser.get("https://foresight.piscada.online/")


@then("I see the login page with the title '{title}'")
def step_impl(context, title):
    context.browser.implicitly_wait(30)
    real_title = context.browser.title
    assert real_title == title, f"expected '{title}' and got '{real_title}'."


@when("I log in as '{username}'")
def step_impl(context, username):
    context.browser.implicitly_wait(30)
    username_field = context.browser.find_element(by=By.ID, value="username")
    username_field.send_keys(username)
    login_button = context.browser.find_element(by=By.ID, value="kc-login")
    login_button.click()
    password = get_password(username, context)
    password_field = context.browser.find_element(by=By.ID, value="password")
    password_field.send_keys(password)
    login_button = context.browser.find_element(by=By.ID, value="kc-login")
    login_button.click()


@then("I see the portal page with the menu button")
def step_impl(context):
    context.browser.implicitly_wait(30)
    menu_button = context.browser.find_element(by=By.CLASS_NAME, value="MuiButtonBase-root")
    menu_button_aria_label = menu_button.get_attribute("aria-label")
    assert menu_button_aria_label == "Menu", f"expected 'Menu' and got '{menu_button_aria_label}'."

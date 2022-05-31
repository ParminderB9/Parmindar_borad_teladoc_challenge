from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


@given(u'I launch Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@when(u'I Open "http://www.way2automation.com/angularjs-protractor/webtables/" page')
def open_webpage(context):
    context.driver.get("http://www.way2automation.com/angularjs-protractor/webtables/")
    context.driver.implicitly_wait(5)


@when(u'Click on Add user button')
def click_add(context):
    context.rows = (len(context.driver.find_elements(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr')))
    # print(">> Before adding new user total users:: " + str(context.rows))
    context.driver.find_element(By.XPATH, "//body[1]/table[1]/thead[1]/tr[2]/td[1]/button[1]").click()


@when(u'Enter user information')
def add_user(context):
    context.driver.find_element(By.NAME, 'FirstName').send_keys("Pam")
    context.driver.find_element(By.NAME, 'LastName').send_keys("B")
    context.driver.find_element(By.NAME, 'UserName').send_keys("Pam")
    context.driver.find_element(By.NAME, 'Password').send_keys("999")
    context.driver.find_element(By.NAME, 'optionsRadios').click()

    ele_role = context.driver.find_element(By.NAME, 'RoleId')
    drp_role = Select(ele_role)
    drp_role.select_by_visible_text('Customer')
    # drp_role.select_by_index(2)
    # drp_role.select_by_value(1)

    context.driver.find_element(By.NAME, 'Email').send_keys("pam.b@abc.com")
    context.driver.find_element(By.NAME, 'Mobilephone').send_keys("999999")
    # sleep(2)


@when(u'Click on Save button')
def save_user(context):
    if context.driver.find_element(By.XPATH, "//body[1]/div[3]/div[3]/button[2]").is_displayed():
        context.driver.find_element(By.XPATH, "//body[1]/div[3]/div[3]/button[2]").click()
        # sleep(5)


@then(u'User must be successfully saved')
def success(context):
    total_rows = (len(context.driver.find_elements(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr')))
    assert context.rows < total_rows

    # print(">> After adding new user total users:: " + str(total_rows))
    # if context.rows < total_rows:
    #     print(">> Pam user is added successfully!")
    sleep(5)
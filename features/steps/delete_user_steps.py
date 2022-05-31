from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from behave import *


@given(u'I launch browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@when(u'I open webpage')
def open_webpage(context):
    context.driver.get("http://www.way2automation.com/angularjs-protractor/webtables/")
    context.driver.implicitly_wait(5)


@when(u"Delete 'novak' user by clicking on 'x' button")
def delete_user(context):
    context.rows = (len(context.driver.find_elements(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr')))

    # print(">> Before delete total users:: " + str(context.rows))
    # columns = (len(context.driver.find_elements(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr/td')))
    # print(columns)

    for row in range(1, context.rows):
        # for column in range(1, 9): print(driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr["+str(
        # row)+"]/td["+str(column)+"]").text)

        username = context.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/table[1]/tbody[1]/tr[" + str(row) + "]/td[3]").text
        print(username.lower())
        if username.lower() == "novak":
            context.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/table[1]/tbody[1]/tr[" + str(
                                            row) + "]/td[11]/button[1]").click()
            # sleep(2)
            if context.driver.find_element(By.XPATH, "//body[1]/div[3]/div[3]/button[2]").is_displayed():
                context.driver.find_element(By.XPATH, "//body[1]/div[3]/div[3]/button[2]").click()
                # sleep(5)


@then(u'Confirm user must be successfully deleted')
def success(context):
    total_rows = (len(context.driver.find_elements(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr')))
    assert context.rows > total_rows

    # print(">> After delete total users:: " + str(total_rows))
    # if context.rows > total_rows:
    #     print(">> Novak user is deleted successfully!")
    sleep(5)

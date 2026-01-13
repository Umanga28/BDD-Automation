from behave import * 
from selenium.webdriver import Chrome
from behave.api.pending_step import StepNotImplementedError
@Given(u'user is on Registration Page')
def step_imp(context):
    context.driver.get('https://www.facebook.com/r.php')
    context.driver.maximize_window()
@When(u'user enters firstname')
def step_imp(context):
    context.driver.find_element('name','firstname').send_keys("Umanga")

@When(u'user enter lastname')
def step_imp(context):
    context.driver.find_element('name','lastname').send_keys("Yogi")

@When(u'user enters birth_month')
def step_imp(context):
    context.driver.find_element('name','birthday_month').send_keys("November")

@When(u'user enters birth_day')
def step_imp(context):
   context.driver.find_element('name','birthday_day').send_keys("28")

@When(u'user enters birth_year')
def step_imp(context):
   context.driver.find_element('name','birthday_year').send_keys("2002")

@When(u'user click gender')
def step_imp(context):
    context.driver.find_element('xpath',"//input[@value='1']").click()

@When(u'user enters phone_number')
def step_imp(context):
    context.driver.find_element('xpath',"//input[@name='reg_email__']").send_keys("9847123456")

@When(u'user enters password')
def step_imp(context):
    context.driver.find_element('xpath',"//input[@aria-label='New password']").send_keys("Arati@1234")

@When(u'user click on Signup button')
def step_imp(context):
    context.driver.find_element('xpath',"//button[@name='websubmit']").click()

@Then(u'User should be registerd successfully')
def step_imp(context):
    print("Registered")

@When(u'User enters duplicate phone_number')
def step_imp(context):
    print("Duplicate phone_number")

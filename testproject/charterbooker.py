import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

# TC1 Űrlap kitöltése

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(2)

    select = Select(driver.find_element_by_name("bf_totalGuests"))
    select.select_by_visible_text('1')

    next_btn1 = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button')
    next_btn1.click()

    bf_date = driver.find_element_by_name('bf_date')
    bf_date.send_keys('2021.08.01')

    select = Select(driver.find_element_by_name("bf_time"))
    select.select_by_visible_text('Morning')

    select = Select(driver.find_element_by_name("bf_hours"))
    select.select_by_visible_text('3')

    next_btn2 = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button')
    next_btn2.click()

    bf_fullname = driver.find_element_by_name('bf_fullname')
    bf_fullname.send_keys('David Sirok')

    bf_email = driver.find_element_by_name('bf_email')
    bf_email.send_keys('sirok.david@gmail.com')

    request_btn = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button')
    request_btn.click()
    time.sleep(3)

    feedback = driver.find_element_by_xpath('//*[@id="booking-form"]/h2')

    assert feedback.text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."

    # TC2 Mail cím validációja
    # Behívom újra a drivert, majd az email cím megadásáig minden ugyanaz, mint a TC1-ben
    # Beírom a helytelen email címet: sirok.davidgmail.com, megnyomom a request_btn gombot
    # Majd ellenőrzöm, hogy jött-e hibaüzenet
    # alert = driver.find_element_by_xpath('//*[@id="bf_email-error"]')
    # assert alert.text == "PLEASE ENTER A VALID EMAIL ADDRESS."

finally:
    pass
    # driver.close()

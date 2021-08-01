import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")
    time.sleep(2)

    number_input = driver.find_elements_by_xpath('/html/body/div/div[2]/input')
    guess_btn = driver.find_element_by_xpath('/html/body/div/div[2]/span/button')
    restart_btn = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/button')
    alert = driver.find_element_by_xpath('/html/body/div/p[5]')
    number_of_guesses = driver.find_element_by_xpath('/html/body/div/div[3]/p/span')
    values = [-19, 255]

    # TC1 Szám kitalálása, 1-től kezdve beküldöm a számokat amíg ki nem írja az üzenetet, hogy eltalálta

    while True:
        for i in range(1, 100):
            number_input.sendkeys(i)
            guess_btn.click()
        if alert.text == "Yes! That is it.":
            break
        continue

    assert number_input.get_attribute('value').strip() == number_of_guesses.text

    # Teszt negatív számmal

    restart_btn.click()
    number_input.sendkeys(values[0])
    guess_btn.click()

    assert alert.text == "Guess higher."

finally:
    pass
    # driver.close()

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")
    time.sleep(2)

    iceman = driver.find_element_by_id('iceman')
    original_btn = driver.find_element_by_xpath('/html/body/div/label[1]')
    factor_btn = driver.find_element_by_xpath('/html/body/div/label[3]')

    # Minden hős azonosítója után ki van írva a data-teams-be hogy hová tartozik: <li id="iceman" data-teams="original factor">
    # Azt lehetne asserttel megnézni, hogy ha megnyomjuk a csapatjának a gombját, előjön-e a hős képe.

finally:
    pass
    # driver.close()
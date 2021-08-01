import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")
    time.sleep(2)

    elements = driver.find_elements_by_xpath('/html/body/div/ul/li/span')

    # Az így kapott lista elemeit kellene átkonvertálni szöveges állománnyá és asserttel összehasonlítani a data.txt tartalmával
    # Data.txt megnyitása olvasásra: with open('data.txt', 'r') as text_file:

finally:
    pass
    # driver.close()

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")
    time.sleep(2)


    def get_all_films():
        return driver.find_elements_by_xpath('/html/body/div[2]/div[3]/a')


    # TC1 Filmek száma a weboldalon

    films = get_all_films()
    assert len(films) == 24

    # TC2 Új film regisztrálása

    register_btn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/button')
    register_btn.click()
    time.sleep(2)

    title = driver.find_element_by_id("nomeFilme")
    release = driver.find_element_by_id("anoLancamentoFilme")
    chrono = driver.find_element_by_id("anoCronologiaFilme")
    trailer = driver.find_element_by_id("linkTrailerFilme")
    image = driver.find_element_by_id("linkImagemFilme")
    summary = driver.find_element_by_id("linkImdbFilme")

    title.send_keys("Black widow")
    release.send_keys("2021")
    chrono.send_keys("2020")
    trailer.send_keys("https://www.youtube.com/watch?v=Fp9pNPdNwjI")
    image.send_keys("https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg")
    summary.send_keys("https://www.imdb.com/title/tt3480822/")

    save_btn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]')
    save_btn.click()

    films = get_all_films()
    assert len(films) == 25

finally:
    pass
    # driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By


def testchrom():
    driver = webdriver.Chrome()
    driver.get("http://www.walla.co.il")


def testmozilla():
    driver_mozilla = webdriver.Firefox()
    driver_mozilla.get("http://www.ynet.co.il")

# ---------------------------------------------------------------------------------


def test_youtube():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    driver.find_element(By.ID, "search").send_keys("guns and roses")
    driver.find_element(By.ID, "search-icon-legacy").click()



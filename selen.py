from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver = webdriver.Chrome(executable_path='D:/Download/chromedriver_win32/chromedriver')
my_driver.get('file:/Users/taras/PycharmProjects/Dev2710/index.html')

my_driver.find_element(By.ID, 'billamt').send_keys('100')
my_driver.find_element(By.XPATH, '//*[@id="serviceQual"]/option[3]').click()
my_driver.find_element(By.XPATH, '//*[@id="peopleamt"]').send_keys('4')
my_driver.find_element(By.ID, 'calculate').click()

tip_results = my_driver.find_element(By.ID, 'tip').text
assert tip_results == "5.00"
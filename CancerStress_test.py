from selenium import webdriver
from selenium.webdriver.common.by import By


def test_bn_why():
    driver = webdriver.Chrome(executable_path='/Users/divyaprabha/PycharmProjects/BlueNote/Drivers/chromedriver')

    driver.get('https://bluenotetherapeutics.com/')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value="/html/body/nav/div[1]/div[1]/a").click()
    title = driver.title

    assert ("Blue Note Therapeutics | Cancer-Related Distress" == title)
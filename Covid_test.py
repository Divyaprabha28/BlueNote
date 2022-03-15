from selenium import webdriver
from selenium.webdriver.common.by import By


def test_cancer_covid_checks():
    driver = webdriver.Chrome(executable_path='/Users/divyaprabha/PycharmProjects/BlueNote/Drivers/chromedriver')

    driver.get('https://bluenotetherapeutics.com/')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[1]/a").click()

    bote = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[3]/button")
    test_one = bote.get_property('disabled')

    assert (test_one == True)

    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[3]/label[1]/span[1]/div").click()

    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[3]/label[2]/span/div").click()
    test_one = bote.get_property('Continue')

    assert (test_one == None)

    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[3]/button").click()

    welcome = driver.find_element(by=By.XPATH, value="//*[@id='app']/main/article/div[1]/div[2]/div")

    assert (welcome.is_displayed())

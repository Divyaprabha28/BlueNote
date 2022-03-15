import driver as driver
from selenium import webdriver
  class HomePageLocators(object):

    cancer_and_Stress = driver.find_element_by_xpath("/html/body/nav/div[1]/div[1]/a")

    try_it_here = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/a")

    driver = webdriver.Chrome(executable_path="/Users/divyaprabha/PycharmProjects/BlueNote/Drivers/chromedriver")

    driver.get('https://bluenotetherapeutics.com/')
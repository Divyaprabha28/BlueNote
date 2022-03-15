from selenium import webdriver
import pytest


def test_blue_note_homepage():

    driver = webdriver.Chrome(executable_path='/Users/divyaprabha/PycharmProjects/BlueNote/Drivers/chromedriver')

    driver.get('https://bluenotetherapeutics.com/')

    driver.maximize_window()

    title = driver.title

    assert("Blue Note Therapeutics | Helping Cancer Patients Live Better" == title), 'Wrong title!'
    driver.close()
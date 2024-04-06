from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from time import sleep


def iniciar_driver():

    chrome_options = Options()

    arguments = ['--lang=pt-BR', '--window-size=1200,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    browser = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(
        browser,
        20,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return browser, wait


browser, wait = iniciar_driver()


# CÓDIGO AQUI


input('digite algo para fechar... ')
browser.quit()

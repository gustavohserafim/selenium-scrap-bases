import os
from datetime import datetime
from selenium import webdriver


options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": os.path.dirname(os.path.abspath(__file__)) # Current path
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
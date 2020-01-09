import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

fp = FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.helperApps.alwaysAsk.force", False)
fp.set_preference("browser.download.dir", os.path.dirname(os.path.abspath(__file__))) # Current path
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-zip-compressed")
fp.set_preference("browser.helperApps.neverAsk.openFile", "application/x-zip-compressed")
fp.set_preference("browser.download.manager.focusWhenStarting", False)
fp.set_preference("browser.download.manager.useWindow", False)
fp.set_preference("browser.download.manager.showAlertOnComplete", False)
fp.set_preference("browser.download.panel.shown", False)

driver = webdriver.Firefox(firefox_profile=fp)
driver.implicitly_wait(5)

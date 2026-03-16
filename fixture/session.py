from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        self.app.wd.find_element(By.NAME, "user").click()
        self.app.wd.find_element(By.NAME, "user").send_keys(username)
        self.app.wd.find_element(By.NAME, "pass").send_keys(password)
        self.app.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.app.wd.find_element(By.LINK_TEXT, "Logout").click()
        self.app.wd.find_element(By.CSS_SELECTOR, "html").click()
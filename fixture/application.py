from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)


    def return_to_groups_page(self):
        self.wd.get("https://localhost/addressbook/group.php")

    def create_group(self, group):
        self.open_groups_page()
        # init group creation
        self.wd.find_element(By.NAME, "new").click()
        # fill group form
        self.wd.find_element(By.NAME, "group_name").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()


    def open_home_page(self):
        self.wd.get("https://localhost/addressbook/")
        self.wd.set_window_size(1006, 892)

    def destroy(self):
        self.wd.quit()


from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        self.app.wd.get("https://localhost/addressbook/group.php")

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.wd.find_element(By.NAME, "new").click()
        # fill group form
        self.app.wd.find_element(By.NAME, "group_name").click()
        self.app.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.app.wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        self.app.wd.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        self.open_groups_page()
        # select first group
        self.app.wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        self.app.wd.find_element(By.NAME, "delete").click()
        self.app.wd.find_element(By.LINK_TEXT, "group page").click()

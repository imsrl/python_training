from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.vars = {}

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()
        self.wd.find_element(By.CSS_SELECTOR, "html").click()

    def return_to_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "group page").click()

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

    def login(self, username, password):
        self.open_home_page()
        self.wd.find_element(By.NAME, "user").click()
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/addressbook/")
        self.wd.set_window_size(1006, 892)

    def destroy(self):
        self.wd.quit()

######
    def back_to_homepage(self):
        self.wd.find_element(By.LINK_TEXT, "home page").click()

    def add_new_contact(self):
        self.wd.find_element(By.LINK_TEXT, "add new").click()

    def fill_contact_info(self, contact):
        self.wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.wd.find_element(By.NAME, "title").send_keys(contact.title)
        self.wd.find_element(By.NAME, "company").send_keys(contact.company)
        self.wd.find_element(By.NAME, "address").send_keys(contact.address)
        self.wd.find_element(By.NAME, "home").send_keys(contact.home)
        self.wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        self.wd.find_element(By.NAME, "work").send_keys(contact.work)
        self.wd.find_element(By.NAME, "email").send_keys(contact.email)
        self.wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        self.wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        self.wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        dropdown = self.wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '24']").click()
        self.wd.find_element(By.CSS_SELECTOR, "select:nth-child(58) > option:nth-child(26)").click()
        dropdown = self.wd.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = 'November']").click()
        self.wd.find_element(By.CSS_SELECTOR, "select:nth-child(59) > option:nth-child(12)").click()
        self.wd.find_element(By.NAME, "byear").send_keys("1991")
        dropdown = self.wd.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, "//option[. = '13']").click()
        self.wd.find_element(By.CSS_SELECTOR, "select:nth-child(63) > option:nth-child(15)").click()
        dropdown = self.wd.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, "//option[. = 'May']").click()
        self.wd.find_element(By.CSS_SELECTOR, "select:nth-child(64) > option:nth-child(6)").click()
        self.wd.find_element(By.NAME, "ayear").send_keys("2021")
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(71)").click()

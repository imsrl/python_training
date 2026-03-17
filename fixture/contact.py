from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def back_to_homepage(self):
        self.app.wd.find_element(By.LINK_TEXT, "home page").click()

    def add_new_contact(self):
        self.app.wd.find_element(By.LINK_TEXT, "add new").click()

    def fill_info(self, contact):
        self.app.wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.app.wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.app.wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.app.wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.app.wd.find_element(By.NAME, "title").send_keys(contact.title)
        self.app.wd.find_element(By.NAME, "company").send_keys(contact.company)
        self.app.wd.find_element(By.NAME, "address").send_keys(contact.address)
        self.app.wd.find_element(By.NAME, "home").send_keys(contact.home)
        self.app.wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        self.app.wd.find_element(By.NAME, "work").send_keys(contact.work)
        self.app.wd.find_element(By.NAME, "email").send_keys(contact.email)
        self.app.wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        self.app.wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        self.app.wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        dropdown = self.app.wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '24']").click()
        self.app.wd.find_element(By.CSS_SELECTOR, "select:nth-child(58) > option:nth-child(26)").click()
        dropdown = self.app.wd.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = 'November']").click()
        self.app.wd.find_element(By.CSS_SELECTOR, "select:nth-child(59) > option:nth-child(12)").click()
        self.app.wd.find_element(By.NAME, "byear").send_keys("1991")
        dropdown = self.app.wd.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, "//option[. = '13']").click()
        self.app.wd.find_element(By.CSS_SELECTOR, "select:nth-child(63) > option:nth-child(15)").click()
        dropdown = self.app.wd.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, "//option[. = 'May']").click()
        self.app.wd.find_element(By.CSS_SELECTOR, "select:nth-child(64) > option:nth-child(6)").click()
        self.app.wd.find_element(By.NAME, "ayear").send_keys("2021")
        self.app.wd.find_element(By.CSS_SELECTOR, "input:nth-child(71)").click()

    def submit(self):
        self.app.wd.find_element(By.NAME, "submit").click()

    def delete_first_contact(self):
        self.app.wd.find_element(By.NAME, "selected[]").click()
        self.app.wd.find_element(By.NAME, "delete").click()

    def edit_first_contact(self):
        self.app.wd.find_element(By.NAME, "Edit").click()

    def update(self):
        self.app.wd.find_element(By.NAME, "update").click()

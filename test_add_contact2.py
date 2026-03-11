from selenium import webdriver
from selenium.webdriver.common.by import By
from contact import ContactInfo


class TestUntitled():
    def setup_method(self, method):
        self.wd = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.wd.quit()

    def test_add_contact(self):
        self.open_home_page()
        self.login(login="admin", password="secret")
        self.add_new_contact()
        self.fill_contact_info(
            ContactInfo(firstname="oleg", middlename="olegovich", lastname="olegovskiy", nickname="LEGO",
                        title="UUUU", company="Roga and Kopyta", address="Planet Earth, Country Russia, City Novosibirsk",
                        home="83842021244", mobile="89039932131", work="83842101011",
                        email="oleg@mail.ru", email2="olego12@mail.ru", email3="internationaloleg@gmail.com",
                        homepage="https://software-testing.ru/"))
        self.back_to_homepage()
        self.logout()

    def back_to_homepage(self):
        self.wd.find_element(By.LINK_TEXT, "home page").click()

    def open_home_page(self):
        self.wd.get("https://localhost/addressbook/")
        self.wd.set_window_size(884, 1034)

    def login(self, login, password):
        self.wd.find_element(By.NAME, "user").send_keys(login)
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

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

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

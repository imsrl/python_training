from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_addressbook(self):
        self.app.wd.get("https://localhost/addressbook/")

    def back_to_homepage(self):
        self.app.wd.find_element(By.LINK_TEXT, "home page").click()


    def add_new_contact(self, new_contact_data):
        self.open_addressbook()
        self.button_add_new()
        # fill contact information
        self.fill_contact(new_contact_data)
        self.fill_dropdown_menu()
        # submit creation
        self.submit()
        self.back_to_homepage()

    def button_add_new(self):
        self.app.wd.find_element(By.LINK_TEXT, "add new").click()

    def fill_dropdown_menu(self):
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

    def submit(self):
        self.app.wd.find_element(By.NAME, "submit").click()

    def delete_first_contact(self):
        self.open_addressbook()
        self.app.wd.find_element(By.NAME, "selected[]").click()
        self.app.wd.find_element(By.NAME, "delete").click()
        self.back_to_homepage()

    def modify_first_contact(self, new_contact_data):
        # self.app.wd.find_element(By.NAME, "Edit").click()
        self.open_addressbook()
        # select first contact
        self.app.wd.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .center:nth-child(8) img").click()
        self.fill_contact(new_contact_data)
        self.update_button()
        self.back_to_homepage()

    def fill_contact(self, contact):
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("middlename", contact.middlename)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.home)
        self.change_contact_field_value("mobile", contact.mobile)
        self.change_contact_field_value("work", contact.work)
        self.change_contact_field_value("email", contact.email)
        self.change_contact_field_value("email2", contact.email2)
        self.change_contact_field_value("email3", contact.email3)
        self.change_contact_field_value("homepage", contact.homepage)

    def change_contact_field_value(self, field_name, text):
        if text is not None:
            self.app.wd.find_element(By.NAME, field_name).click()
            self.app.wd.find_element(By.NAME, field_name).clear()
            self.app.wd.find_element(By.NAME, field_name).send_keys(text)

    def update_button(self):
        self.app.wd.find_element(By.NAME, "update").click()

    def count(self):
        self.open_addressbook()
        return len(self.app.wd.find_elements(By.NAME, "selected[]"))

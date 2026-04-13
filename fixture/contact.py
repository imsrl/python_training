from selenium.webdriver.common.by import By
from model.contact import ContactInfo
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_homepage(self):
        if self.app.wd.current_url.endswith("addressbook/") or self.app.wd.current_url.endswith("/index.php"):
            return
        else:
            # дома поменять обратно
            self.app.wd.get("http://localhost/addressbook/addressbook/")


    def back_to_homepage(self):
        self.app.wd.find_element(By.LINK_TEXT, "home page").click()


    def add_new_contact(self, new_contact_data):
        self.open_homepage()
        self.button_add_new()
        # fill contact information
        self.fill_contact(new_contact_data)
        self.fill_dropdown_menu()
        # submit creation
        self.submit()
        self.back_to_homepage()
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        self.open_homepage()
        self.select_contact_by_index(index)
        self.app.wd.find_element(By.NAME, "delete").click()
        self.back_to_homepage()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        self.app.wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_first_contact(self):
        self.app.wd.find_element(By.NAME, "selected[]").click()

    def modify_contact_by_index(self, index, new_contact_data):
        self.open_homepage()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact(new_contact_data)
        self.update_button()
        self.back_to_homepage()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        self.open_homepage()
        self.app.wd.find_elements(By.XPATH, '//img[@alt="Edit"]')[index].click()

    def fill_contact(self, contact):
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("middlename", contact.middlename)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.homephone)
        self.change_contact_field_value("mobile", contact.mobilephone)
        self.change_contact_field_value("work", contact.workphone)
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
        self.open_homepage()
        return len(self.app.wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.open_homepage()
            self.contact_cache = []
            for element in self.app.wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(ContactInfo(lastname=lastname, firstname=firstname, id=id,
                                                      all_phones_from_home_page = all_phones,
                                                      all_emails_from_home_page=all_emails))
        return list(self.contact_cache)



    def open_contact_view_by_index(self, index):
        self.open_homepage()
        row = self.app.wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        firstname = self.app.wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = self.app.wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = self.app.wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = self.app.wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = self.app.wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = self.app.wd.find_element(By.NAME, "mobile").get_attribute("value")
        email = self.app.wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = self.app.wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = self.app.wd.find_element(By.NAME, "email3").get_attribute("value")
        return ContactInfo(firstname=firstname, lastname=lastname, id=id, homephone=homephone,
                           workphone=workphone, mobilephone=mobilephone,
                           email = email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        self.open_contact_view_by_index(index)
        text = self.app.wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return ContactInfo(homephone=homephone, workphone=workphone, mobilephone=mobilephone)

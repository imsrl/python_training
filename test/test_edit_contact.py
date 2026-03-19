from model.contact import ContactInfo


def test_edit_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact()
    app.contact.fill_contact(ContactInfo(firstname="EDITED", middlename="EDITED", lastname="EDITED", nickname="EDITED",
                                   title="EDITED", company="EDITED", address="EDITED",
                                   home="EDITED", mobile="EDITED", work="EDITED",
                                   email="EDITED", email2="EDITED@mail.ru", email3="EDITED@gmail.com",
                                   homepage="https://EDITED.ru/"))
    app.contact.update_button()
    app.contact.back_to_homepage()
    app.session.logout()

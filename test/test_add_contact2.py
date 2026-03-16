from model.contact import ContactInfo


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.fill_info(
        ContactInfo(firstname="oleg", middlename="olegovich", lastname="olegovskiy", nickname="LEGO",
                    title="UUUU", company="Roga and Kopyta", address="Planet Earth, Country Russia, City Novosibirsk",
                    home="83842021244", mobile="89039932131", work="83842101011",
                    email="oleg@mail.ru", email2="olego12@mail.ru", email3="internationaloleg@gmail.com",
                    homepage="https://software-testing.ru/"))
    app.contact.back_to_homepage()
    app.session.logout()

def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.submit()
    app.contact.back_to_homepage()
    app.session.logout()
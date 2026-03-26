from model.contact import ContactInfo


def test_add_contact(app):
    app.contact.add_new_contact(
        ContactInfo(firstname="oleg", middlename="olegovich", lastname="olegovskiy", nickname="LEGO",
                    title="UUUU", company="Roga and Kopyta", address="Planet Earth, Country Russia, City Novosibirsk",
                    home="83842021244", mobile="89039932131", work="83842101011",
                    email="oleg@mail.ru", email2="olego12@mail.ru", email3="internationaloleg@gmail.com",
                    homepage="https://software-testing.ru/"))


def test_add_empty_contact(app):
    app.contact.button_add_new()
    app.contact.submit()
    app.contact.back_to_homepage()

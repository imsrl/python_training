from contact import ContactInfo
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.add_new_contact()
    app.fill_contact_info(
        ContactInfo(firstname="oleg", middlename="olegovich", lastname="olegovskiy", nickname="LEGO",
                    title="UUUU", company="Roga and Kopyta", address="Planet Earth, Country Russia, City Novosibirsk",
                    home="83842021244", mobile="89039932131", work="83842101011",
                    email="oleg@mail.ru", email2="olego12@mail.ru", email3="internationaloleg@gmail.com",
                    homepage="https://software-testing.ru/"))
    app.back_to_homepage()
    app.logout()

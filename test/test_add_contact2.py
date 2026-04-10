from model.contact import ContactInfo
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [ContactInfo(firstname="", lastname="")] + [
    ContactInfo(firstname=random_string("name", 10), middlename=random_string("middlename", 10),
                lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                title=random_string("title", 15), company=random_string("company", 15),
                address=random_string("address", 20), homephone=random_string("homephone", 15),
                mobilephone=random_string("mobilephone", 15), workphone=random_string("workphone", 15),
                email=random_string("email", 15), email2=random_string("email2", 15),
                email3=random_string("email3", 15), homepage=random_string("homepage", 15))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

# def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = ContactInfo(firstname="", lastname="")
#    app.contact.button_add_new()
#    app.contact.fill_contact(contact)
#    app.contact.submit()
#    app.contact.back_to_homepage()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

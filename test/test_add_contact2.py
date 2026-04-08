from model.contact import ContactInfo


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactInfo(firstname="oleg", middlename="olegovich", lastname="olegovskiy", nickname="LEGO",
                          title="UUUU", company="Roga and Kopyta", address="Planet Earth, Country Russia, City Novosibirsk",
                          homephone="83842021244", mobilephone="89039932131", workphone="83842101011",
                          email="oleg@mail.ru", email2="olego12@mail.ru", email3="internationaloleg@gmail.com",
                          homepage="https://software-testing.ru/")
    app.contact.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)


#def test_add_empty_contact(app):
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

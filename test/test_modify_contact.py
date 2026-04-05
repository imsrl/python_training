from model.contact import ContactInfo
from random import randrange


def test_edit_some_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = ContactInfo(firstname="NAME WAS EDITED")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)


#def test_edit_first_contact_middlename(app):
#   if app.contact.count() == 0:
#        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
#    old_contacts = app.contact.get_contact_list()
#    contact = ContactInfo(middlename="MIDDLENAME WAS EDITED")
#    contact.id = old_contacts[0].id
#    #добавил еще и с firstname так как тест на имзенение middlename
#    contact.firstname = old_contacts[0].firstname
#    contact.lastname = old_contacts[0].lastname
#    app.contact.modify_first_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)


#def test_edit_first_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
#    old_contacts = app.contact.get_contact_list()
#    contact = ContactInfo(lastname="LASTNAME WAS EDITED")
#    contact.id = old_contacts[0].id
#    contact.firstname = old_contacts[0].firstname
#    app.contact.modify_first_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

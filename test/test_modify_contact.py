from model.contact import ContactInfo
import random


def test_edit_some_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id,
                                     ContactInfo(firstname="NAME WAS EDITED", lastname="LASTNAME WAS EDITED"))
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    modified_contact = ContactInfo(id=contact.id, firstname="NAME WAS EDITED", lastname="LASTNAME WAS EDITED")
    # изменение old_contacts, так как были внесены изменения
    expected_contacts = [
        modified_contact if c.id == contact.id else c
        for c in old_contacts
    ]
    assert sorted(expected_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactInfo.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=ContactInfo.id_or_max)

# def test_edit_first_contact_middlename(app):
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


# def test_edit_first_contact_lastname(app):
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

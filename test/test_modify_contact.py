from model.contact import ContactInfo


def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(ContactInfo(firstname="NAME WAS EDITED"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(ContactInfo(middlename="MIDDLENAME WAS EDITED"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(ContactInfo(lastname="LASTNAME WAS EDITED"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
from model.contact import ContactInfo


def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    app.contact.modify_first_contact(ContactInfo(firstname="NAME WAS EDITED"))


def test_edit_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    app.contact.modify_first_contact(ContactInfo(middlename="MIDDLENAME WAS EDITED"))


def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    app.contact.modify_first_contact(ContactInfo(lastname="LASTNAME WAS EDITED"))

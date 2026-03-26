from model.contact import ContactInfo


def test_edit_first_contact_name(app):
    app.contact.modify_first_contact(ContactInfo(firstname="NAME WAS EDITED"))


def test_edit_first_contact_middlename(app):
    app.contact.modify_first_contact(ContactInfo(middlename="MIDDLENAME WAS EDITED"))


def test_edit_first_contact_lastname(app):
    app.contact.modify_first_contact(ContactInfo(lastname="LASTNAME WAS EDITED"))

from model.contact import ContactInfo
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    app.contact.delete_first_contact()

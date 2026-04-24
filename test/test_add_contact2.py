from model.contact import ContactInfo


def test_add_contact(app, json_contacts):
    contact = json_contacts
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

from model.contact import ContactInfo
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(ContactInfo(firstname="for delete"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
   # index = randrange(len(old_contacts))
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=ContactInfo.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=ContactInfo.id_or_max)
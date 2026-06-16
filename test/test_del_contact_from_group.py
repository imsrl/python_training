from random import choice
from model.contact import ContactInfo
from model.group import Group


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="22testdel group"))
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(ContactInfo(firstname="22testdel contact"))
    group = choice(db.get_group_list())
    contacts_in_group = orm.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        contacts_not_in_group = orm.get_contacts_not_in_group(group)
        if len(contacts_not_in_group) == 0:
            app.contact.add_new_contact(ContactInfo(firstname="contactdel from group"))
            contacts_not_in_group = orm.get_contacts_not_in_group(group)
        contact = choice(contacts_not_in_group)
        app.contact.add_contact_to_group(contact.id, group.id)
        contacts_in_group = orm.get_contacts_in_group(group)
    contact = choice(contacts_in_group)
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.delete_contact_from_group(contact.id, group.id)
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts = [
        c for c in old_contacts
        if c.id != contact.id
    ]
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts,key=ContactInfo.id_or_max)

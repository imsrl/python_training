import re
from random import randrange
from model.contact import ContactInfo

def test_data_from_home_page_and_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    contacts_from_home_page_sorted = sorted(contacts_from_home_page, key=ContactInfo.id_or_max)
    contacts_from_db_sorted = sorted(contacts_from_db, key=ContactInfo.id_or_max)
    for i in range(len(contacts_from_home_page_sorted)):
        contact_from_home_page = contacts_from_home_page_sorted[i]
        contact_from_db = contacts_from_db_sorted[i]
        assert clear_text(contact_from_home_page.firstname) == clear_text(contact_from_db.firstname)
        assert clear_text(contact_from_home_page.lastname) == clear_text(contact_from_db.lastname)
        assert clear_text(contact_from_home_page.address) == clear_text(contact_from_db.address)
        #assert contact_from_home_page.address == contact_from_db.address
        merged_phones = merge_phones_like_on_home_page(contact_from_db)
        merged_emails = merge_emails_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merged_phones
        assert contact_from_home_page.all_emails_from_home_page == merged_emails

#def normalize_text(s):
#    if s is None:
#        return ""
#    return re.sub(r"[ \t]+", " ", s.replace("\r\n", "\n").replace("\r", "\n")).strip()

#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone

#def test_all_data_from_contact_home_page(app):
#    contacts = app.contact.get_contact_list()
#    index = randrange(len(contacts))
#    contact_from_home_page = contacts[index]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert contact_from_home_page.address == contact_from_edit_page.address
#    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_all_contacts_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(ContactInfo(firstname="newcontact"))
    ui_list = app.contact.get_contact_list()
    db_list = db.get_home_page_contacts()
    assert len(ui_list) == len(db_list)
    assert sorted(ui_list, key=ContactInfo.id_or_max) == sorted(db_list, key=ContactInfo.id_or_max)




def clear(s):
    if s is None:
        return ""
    return re.sub("[() ./-]", "", s)
#def clear1(s):
#    return re.sub("[() -]", "", s)

def clear_email(s):
    if s is None:
        return ""
    return re.sub(" +", " ", s.strip())

def clear_text(s):
    if s is None:
        return ""
    return re.sub(" +", " ", "\n".join(s.splitlines()).strip())

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))


#def merge_emails_like_on_home_page(contact):
#    return "\n".join(filter(lambda x: x != "",
#                                filter(lambda x: x is not None,
#                                    [contact.email, contact.email2, contact.email3])))
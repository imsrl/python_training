import pymysql.cursors
from model.group import Group
from model.contact import ContactInfo


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, "
                "work, email, email2, email3, homepage from addressbook where deprecated is Null")
            #0000-00-00 00:00:00
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile,
                 work, email, email2, email3, homepage) = row
                list.append(ContactInfo(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                        nickname=nickname, company=company, title=title, address=address, homephone=home,
                                        mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3,
                                        homepage=homepage))
        finally:
            cursor.close()
        return list

    def get_home_page_contacts(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, email, email2, email3 "
                "from addressbook where deprecated is Null"
            )

            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row

                phone_list = [home, mobile, work]
                email_list = [email, email2, email3]

                all_phones = "\n".join([phone for phone in phone_list if phone])
                all_emails = "\n".join([mail for mail in email_list if mail])

                contacts.append(ContactInfo(
                    id=str(id),
                    firstname=firstname.strip() if firstname else "",
                    lastname=lastname.strip() if lastname else "",
                    address=address,
                    all_phones_from_home_page=all_phones,
                    all_emails_from_home_page=all_emails
                ))
        finally:
            cursor.close()

        return contacts

    def destroy(self):
        self.connection.close()

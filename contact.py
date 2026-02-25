class ContactInfo:
    def __init__(self, firstname, middlename , lastname , nickname , title):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title

class CompanyInfo:
    def __init__(self, company, address):
        self.company = company
        self.address = address

class PhoneInfo:
    def __init__(self, home, mobile, work):
        self.home = home
        self.mobile = mobile
        self.work = work

class EmailAndSiteInfo:
    def __init__(self, email, email2, email3,homepage):
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage

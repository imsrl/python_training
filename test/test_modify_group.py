from model.group import Group

def test_modify_group_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="changed group name1"))
    app.group.return_to_groups_page()
    app.session.logout()

def test_modify_group_header(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="changed group header"))
    app.group.return_to_groups_page()
    app.session.logout()
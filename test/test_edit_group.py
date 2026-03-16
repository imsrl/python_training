from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="changed group name1", header="changed group header", footer="changed group footer"))
    app.group.return_to_groups_page()
    app.session.logout()
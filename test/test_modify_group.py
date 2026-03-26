from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.modify_first_group(Group(name="changed group name1"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.modify_first_group(Group(header="changed group header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.modify_first_group(Group(footer="changed group footer"))
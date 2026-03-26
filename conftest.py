from fixture.application import Application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    print("app fixture called, fixture =", fixture)
    if fixture is None:
        print("creating Application because fixture is None")
        fixture = Application()
    else:
        print("checking is_valid")
        if not fixture.is_valid():
            print("creating Application because is_valid() is False")
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
